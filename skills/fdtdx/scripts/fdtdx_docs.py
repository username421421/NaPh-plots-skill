#!/usr/bin/env python3
"""Query the bundled FDTDX docs, notebooks, examples, tests, source, and API index."""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SKILL_ROOT = Path(__file__).resolve().parents[1]
DOC_ROOT = SKILL_ROOT / "doc"
API_INDEX = DOC_ROOT / "api-index.json"
TEXT_SUFFIXES = {".md", ".rst", ".py", ".toml", ".txt"}
HEADING_RE = re.compile(r"^(#{1,6})\s*(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*([A-Za-z0-9_+.-]*)?.*$")


@dataclass
class Heading:
    line: int
    level: int
    text: str


@dataclass
class CodeBlock:
    start: int
    end: int
    language: str
    heading_path: str


def fail(message: str) -> "None":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def relative(path: Path) -> str:
    return path.relative_to(SKILL_ROOT).as_posix()


def category(path: Path) -> str:
    rel = relative(path)
    if rel.startswith("doc/notebooks/"):
        return "notebooks"
    if rel.startswith("doc/examples/"):
        return "examples"
    if rel.startswith("doc/package-src/"):
        return "source"
    if rel.startswith("doc/tests/"):
        return "tests"
    if rel.startswith("doc/readthedocs/"):
        return "docs"
    return "metadata"


def iter_text_files(kind: str = "all") -> list[Path]:
    files = []
    for path in DOC_ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        # The clean Markdown is the searchable representation of the HTML site.
        if "doc/readthedocs/site/" in relative(path):
            continue
        if kind != "all" and category(path) != kind:
            continue
        files.append(path)
    return sorted(files, key=lambda p: relative(p).lower())


def resolve_page(query: str, kind: str = "all") -> Path:
    direct_candidates = [SKILL_ROOT / query, DOC_ROOT / query]
    for direct in direct_candidates:
        if direct.exists() and direct.is_file():
            return direct.resolve()
    lowered = query.replace("\\", "/").lower()
    name = Path(query).name.lower()
    stem = Path(query).stem.lower()
    matches = []
    for path in iter_text_files(kind):
        rel = relative(path).lower()
        if rel == lowered or rel.endswith("/" + lowered):
            matches.append(path)
        elif path.name.lower() == name or path.stem.lower() in {stem, lowered}:
            matches.append(path)
    unique = sorted(set(matches), key=lambda p: relative(p).lower())
    if len(unique) == 1:
        return unique[0]
    if not unique:
        fail(f"page not found: {query}")
    options = ", ".join(relative(path) for path in unique[:12])
    fail(f"ambiguous page '{query}'; use a relative path. Matches: {options}")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def normalize_heading(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.rstrip("#").strip()


def markdown_headings(lines: list[str]) -> list[Heading]:
    headings = []
    in_fence = False
    marker = ""
    for index, line in enumerate(lines):
        fence = FENCE_RE.match(line)
        if fence:
            current = fence.group(1)[0]
            if not in_fence:
                in_fence, marker = True, current
            elif current == marker:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append(Heading(index, len(match.group(1)), normalize_heading(match.group(2))))
    return headings


def rst_headings(lines: list[str]) -> list[Heading]:
    underline_order = {"=": 1, "-": 2, "~": 3, "^": 4, '"': 5}
    found: list[tuple[int, str, str]] = []
    for index in range(len(lines) - 1):
        title = lines[index].strip()
        underline = lines[index + 1].strip()
        if not title or len(underline) < 3 or len(set(underline)) != 1:
            continue
        char = underline[0]
        if char in underline_order:
            found.append((index, title, char))
    seen_chars: list[str] = []
    headings = []
    for line, text, char in found:
        if char not in seen_chars:
            seen_chars.append(char)
        headings.append(Heading(line, seen_chars.index(char) + 1, normalize_heading(text)))
    return headings


def python_headings(path: Path, lines: list[str]) -> list[Heading]:
    try:
        tree = ast.parse("\n".join(lines), filename=str(path))
    except SyntaxError:
        return []
    headings = []
    for node in tree.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            prefix = "class" if isinstance(node, ast.ClassDef) else "def"
            headings.append(Heading(node.lineno - 1, 1, f"{prefix} {node.name}"))
            if isinstance(node, ast.ClassDef):
                for member in node.body:
                    if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef)) and not member.name.startswith("_"):
                        headings.append(Heading(member.lineno - 1, 2, f"def {node.name}.{member.name}"))
    return sorted(headings, key=lambda h: h.line)


def headings_for(path: Path, lines: list[str]) -> list[Heading]:
    if path.suffix.lower() == ".md":
        return markdown_headings(lines)
    if path.suffix.lower() == ".rst":
        return rst_headings(lines)
    if path.suffix.lower() == ".py":
        return python_headings(path, lines)
    return []


def section_bounds(headings: list[Heading], selected: Heading, count: int) -> tuple[int, int]:
    end = count
    for heading in headings:
        if heading.line > selected.line and heading.level <= selected.level:
            end = heading.line
            break
    return selected.line, end


def match_heading(headings: list[Heading], query: str) -> Heading:
    needle = normalize_heading(query).lower()
    exact = [h for h in headings if h.text.lower() == needle]
    matches = exact or [h for h in headings if needle in h.text.lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        fail(f"section not found: {query}")
    fail("ambiguous section; matches: " + ", ".join(h.text for h in matches[:12]))


def heading_path(headings: list[Heading], line: int) -> str:
    stack: list[Heading] = []
    for heading in headings:
        if heading.line > line:
            break
        while stack and stack[-1].level >= heading.level:
            stack.pop()
        stack.append(heading)
    return " > ".join(item.text for item in stack)


def code_blocks(path: Path, lines: list[str], title: str = "", language: str = "") -> list[CodeBlock]:
    if path.suffix.lower() != ".md":
        return []
    headings = markdown_headings(lines)
    scope_start, scope_end = 0, len(lines)
    if title:
        selected = match_heading(headings, title)
        scope_start, scope_end = section_bounds(headings, selected, len(lines))
    blocks = []
    index = 0
    while index < len(lines):
        match = FENCE_RE.match(lines[index])
        if not match:
            index += 1
            continue
        marker = match.group(1)
        lang = (match.group(2) or "").lower()
        start = index
        index += 1
        while index < len(lines) and not lines[index].lstrip().startswith(marker[0] * len(marker)):
            index += 1
        end = min(index + 1, len(lines))
        if scope_start <= start < scope_end and (not language or lang in {language.lower(), "py" if language == "python" else language.lower()}):
            blocks.append(CodeBlock(start, end, lang, heading_path(headings, start)))
        index = end
    return blocks


def load_api() -> dict:
    if not API_INDEX.exists():
        fail(f"API index missing: {API_INDEX}")
    return json.loads(API_INDEX.read_text(encoding="utf-8"))


def print_limited(lines: Iterable[str], limit: int) -> None:
    for index, line in enumerate(lines):
        if limit > 0 and index >= limit:
            break
        print(line)


def command_list(kind: str, limit: int) -> None:
    print_limited((f"{category(path):9} {relative(path)}" for path in iter_text_files(kind)), limit)


def command_search(pattern: str, kind: str, case_sensitive: bool, literal: bool, max_results: int) -> None:
    if literal:
        pattern = re.escape(pattern)
    try:
        regex = re.compile(pattern, 0 if case_sensitive else re.IGNORECASE)
    except re.error as exc:
        fail(f"invalid regex: {exc}")
    count = 0
    for path in iter_text_files(kind):
        for line_number, line in enumerate(read_lines(path), start=1):
            if regex.search(line):
                print(f"{relative(path)}:{line_number}: {line}")
                count += 1
                if max_results > 0 and count >= max_results:
                    return


def command_toc(page: str, kind: str, limit: int) -> None:
    path = resolve_page(page, kind)
    headings = headings_for(path, read_lines(path))
    print(f"# {relative(path)}")
    print_limited((f"{heading.line + 1:6}  {'  ' * (heading.level - 1)}{heading.text}" for heading in headings), limit)


def command_section(page: str, title: str, kind: str, max_lines: int) -> None:
    path = resolve_page(page, kind)
    lines = read_lines(path)
    headings = headings_for(path, lines)
    selected = match_heading(headings, title)
    start, end = section_bounds(headings, selected, len(lines))
    print_limited(lines[start:end], max_lines)


def command_snippets(page: str, title: str, language: str, max_results: int, compose: bool) -> None:
    path = resolve_page(page)
    lines = read_lines(path)
    blocks = code_blocks(path, lines, title, language)
    if not blocks:
        fail(f"no matching fenced code blocks in {relative(path)}")
    if max_results > 0:
        blocks = blocks[:max_results]
    if compose:
        for index, block in enumerate(blocks):
            if index:
                print()
            print("\n".join(lines[block.start + 1 : block.end - 1]))
        return
    for index, block in enumerate(blocks, start=1):
        print(f"{index:3}: lines {block.start + 2}-{block.end - 1} | lang={block.language or 'text'} | {block.heading_path}")


def command_api(query: str, member: str, max_results: int, max_doc_lines: int) -> None:
    data = load_api()
    needle = query.lower().removeprefix("fdtdx.")
    entries = data["entries"]
    exact = [entry for entry in entries if entry["name"].lower() == needle]
    matches = exact or [
        entry
        for entry in entries
        if needle in entry["name"].lower()
        or needle in entry.get("doc", "").lower()
        or any(needle in item["name"].lower() for item in entry.get("members", []))
    ]
    if max_results > 0:
        matches = matches[:max_results]
    if not matches:
        fail(f"API symbol not found: {query}")
    for entry_index, entry in enumerate(matches):
        if entry_index:
            print("\n" + "-" * 80)
        print(f"{entry['qualified_name']}{entry.get('signature', '')} [{entry['kind']}]")
        if "= null" in entry.get("signature", ""):
            print("note: `null` is TreeClass's required-field sentinel, not a usable default")
        if entry.get("source"):
            line = f":{entry['line']}" if entry.get("line") else ""
            source = entry["source"]
            if not Path(source).is_absolute():
                source = f"doc/package-src/{source}"
            print(f"source: {source}{line}")
        selected_members = entry.get("members", [])
        if member:
            selected_members = [item for item in selected_members if member.lower() in item["name"].lower()]
            if not selected_members:
                fail(f"member '{member}' not found on {entry['name']}")
        if member:
            for item in selected_members:
                print(f"\n{entry['name']}.{item['name']}{item.get('signature', '')} [{item['kind']}]")
                print_limited(item.get("doc", "").splitlines(), max_doc_lines)
        else:
            print_limited(entry.get("doc", "").splitlines(), max_doc_lines)
            fields = entry.get("fields", [])
            if fields:
                print("\nfields: " + ", ".join(f"{field['name']}: {field['annotation']}" for field in fields))
            if selected_members:
                print("members: " + ", ".join(item["name"] for item in selected_members))


def command_examples(limit: int) -> None:
    paths = iter_text_files("examples") + [
        path for path in iter_text_files("notebooks") if "/markdown/" in relative(path)
    ]
    for path in paths[: limit or None]:
        lines = read_lines(path)
        headings = headings_for(path, lines)
        title = headings[0].text if headings else ""
        blocks = code_blocks(path, lines) if path.suffix == ".md" else []
        print(f"{relative(path)} | {title} | snippets={len(blocks)}")


def command_manifest() -> None:
    data = load_api()
    counts: dict[str, int] = {}
    for path in iter_text_files():
        counts[category(path)] = counts.get(category(path), 0) + 1
    print(json.dumps({"api": data["metadata"], "text_files": counts}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    kinds = ("all", "docs", "notebooks", "examples", "source", "tests", "metadata")

    cmd = sub.add_parser("list", help="List searchable corpus files.")
    cmd.add_argument("--kind", choices=kinds, default="all")
    cmd.add_argument("--limit", type=int, default=0)

    cmd = sub.add_parser("search", help="Regex-search the complete text corpus; use --literal for plain text.")
    cmd.add_argument("pattern")
    cmd.add_argument("--kind", choices=kinds, default="all")
    cmd.add_argument("--case-sensitive", action="store_true")
    cmd.add_argument("--literal", action="store_true", help="Treat the pattern as literal text instead of a regular expression.")
    cmd.add_argument("--max-results", type=int, default=80)

    cmd = sub.add_parser("toc", help="Show headings or Python symbols in one file.")
    cmd.add_argument("page")
    cmd.add_argument("--kind", choices=kinds, default="all")
    cmd.add_argument("--limit", type=int, default=100)

    cmd = sub.add_parser("section", help="Print one Markdown/RST/Python section.")
    cmd.add_argument("page")
    cmd.add_argument("title")
    cmd.add_argument("--kind", choices=kinds, default="all")
    cmd.add_argument("--max-lines", type=int, default=250)

    for name, help_text in (("snippets", "List code blocks in a Markdown page."), ("compose", "Print matching code blocks.")):
        cmd = sub.add_parser(name, help=help_text)
        cmd.add_argument("page")
        cmd.add_argument("--title", default="")
        cmd.add_argument("--lang", default="python")
        cmd.add_argument("--max-results", type=int, default=0)

    cmd = sub.add_parser("api", help="Inspect a public FDTDX symbol or class member.")
    cmd.add_argument("query")
    cmd.add_argument("--member", default="")
    cmd.add_argument("--max-results", type=int, default=12)
    cmd.add_argument("--max-doc-lines", type=int, default=80)

    cmd = sub.add_parser("examples", help="List official examples and rendered notebooks.")
    cmd.add_argument("--limit", type=int, default=100)
    sub.add_parser("manifest", help="Show corpus and API-index metadata.")
    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args()
    if args.command == "list":
        command_list(args.kind, args.limit)
    elif args.command == "search":
        command_search(args.pattern, args.kind, args.case_sensitive, args.literal, args.max_results)
    elif args.command == "toc":
        command_toc(args.page, args.kind, args.limit)
    elif args.command == "section":
        command_section(args.page, args.title, args.kind, args.max_lines)
    elif args.command in {"snippets", "compose"}:
        command_snippets(args.page, args.title, args.lang, args.max_results, args.command == "compose")
    elif args.command == "api":
        command_api(args.query, args.member, args.max_results, args.max_doc_lines)
    elif args.command == "examples":
        command_examples(args.limit)
    elif args.command == "manifest":
        command_manifest()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
