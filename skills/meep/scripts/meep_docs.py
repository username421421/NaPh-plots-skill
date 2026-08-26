#!/usr/bin/env python3
"""
Query helper for the bundled Meep markdown documentation.

Examples:
  python scripts/meep_docs.py list --limit 30
  python scripts/meep_docs.py search "stop_when_fields_decayed"
  python scripts/meep_docs.py toc Python_User_Interface.md --max 40
  python scripts/meep_docs.py section Perfectly_Matched_Layer.md "Planewave Sources Extending into PML"
  python scripts/meep_docs.py examples --max-results 40
  python scripts/meep_docs.py snippets Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py
  python scripts/meep_docs.py snippet Python_Tutorials/Basics.md 1 --title "Transmittance Spectrum of a Waveguide Bend" --lang py
  python scripts/meep_docs.py snippet Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py --pick longest
  python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "A Straight Waveguide" --lang py
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_DOC_ROOT = Path(__file__).resolve().parents[1] / "doc" / "docs"
HEADING_RE = re.compile(r"^(#{1,6})\s*(.*?)\s*#*\s*$")
SETEXT_RE = re.compile(r"^(=+|-+)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*([A-Za-z0-9_+.\-]*)?.*$")
STDOUT_ENCODING = sys.stdout.encoding or "utf-8"
STDERR_ENCODING = sys.stderr.encoding or "utf-8"


@dataclass
class Heading:
    line_index: int
    level: int
    text: str
    span_lines: int


@dataclass
class CodeBlock:
    start_line_index: int
    end_line_index: int
    lang: str
    closed: bool


@dataclass
class ParsedDoc:
    headings: list[Heading]
    code_blocks: list[CodeBlock]


def die(msg: str) -> "None":
    sys.stderr.buffer.write(f"error: {msg}\n".encode(STDERR_ENCODING, errors="replace"))
    raise SystemExit(1)


def write_out(text: str) -> None:
    sys.stdout.buffer.write(f"{text}\n".encode(STDOUT_ENCODING, errors="replace"))


def iter_pages(root: Path) -> list[Path]:
    return sorted(
        root.rglob("*.md"),
        key=lambda p: p.relative_to(root).as_posix().lower(),
    )


def relpath(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def normalize_heading(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^#+\s*", "", text)
    text = re.sub(r"\s*#+\s*$", "", text)
    return re.sub(r"\s+", " ", text).strip()


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def parse_markdown(lines: list[str]) -> ParsedDoc:
    headings: list[Heading] = []
    code_blocks: list[CodeBlock] = []

    in_code = False
    fence_char = ""
    fence_len = 0
    fence_start = -1
    fence_lang = ""
    i = 0
    while i < len(lines):
        line = lines[i]

        if in_code:
            stripped = line.lstrip()
            if stripped.startswith(fence_char * fence_len):
                code_blocks.append(
                    CodeBlock(
                        start_line_index=fence_start,
                        end_line_index=i + 1,
                        lang=fence_lang,
                        closed=True,
                    )
                )
                in_code = False
            i += 1
            continue

        m_fence = FENCE_RE.match(line)
        if m_fence:
            marker = m_fence.group(1)
            fence_char = marker[0]
            fence_len = len(marker)
            fence_start = i
            fence_lang = (m_fence.group(2) or "").strip().lower()
            in_code = True
            i += 1
            continue

        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text = normalize_heading(m.group(2))
            if text:
                headings.append(Heading(i, level, text, 1))
            i += 1
            continue

        if i + 1 < len(lines):
            nxt = lines[i + 1]
            m2 = SETEXT_RE.match(nxt)
            if m2 and line.strip():
                level = 1 if nxt.strip().startswith("=") else 2
                text = normalize_heading(line)
                if text:
                    headings.append(Heading(i, level, text, 2))
                i += 2
                continue

        i += 1

    if in_code:
        code_blocks.append(
            CodeBlock(
                start_line_index=fence_start,
                end_line_index=len(lines),
                lang=fence_lang,
                closed=False,
            )
        )

    return ParsedDoc(headings=headings, code_blocks=code_blocks)


def build_headings(lines: list[str]) -> list[Heading]:
    return parse_markdown(lines).headings


def resolve_page(root: Path, page: str) -> Path:
    direct = (root / page).resolve()
    if direct.exists() and direct.is_file():
        return direct

    page_obj = Path(page)
    page_name = page_obj.name
    page_stem = page_obj.stem
    page_name_md = page_name if page_name.lower().endswith(".md") else f"{page_name}.md"

    candidates: list[Path] = []
    for p in iter_pages(root):
        rel = relpath(p, root).lower()
        if rel == page.lower() or rel == page_name_md.lower():
            candidates.append(p)
            continue
        if p.name.lower() == page_name.lower() or p.name.lower() == page_name_md.lower():
            candidates.append(p)
            continue
        if p.stem.lower() == page_stem.lower():
            candidates.append(p)

    unique = sorted(set(candidates))
    if len(unique) == 1:
        return unique[0]
    if not unique:
        die(f"page not found: {page}")

    opts = ", ".join(relpath(p, root) for p in unique[:8])
    tail = " ..." if len(unique) > 8 else ""
    die(f"ambiguous page '{page}'. Use full relative path. Matches: {opts}{tail}")


def command_list(root: Path, limit: int) -> int:
    pages = iter_pages(root)
    if limit > 0:
        pages = pages[:limit]
    for p in pages:
        write_out(relpath(p, root))
    return 0


def command_search(root: Path, pattern: str, case_sensitive: bool, max_results: int) -> int:
    flags = 0 if case_sensitive else re.IGNORECASE
    try:
        rx = re.compile(pattern, flags)
    except re.error as exc:
        die(f"invalid regex: {exc}")

    count = 0
    for page in iter_pages(root):
        lines = read_lines(page)
        rel = relpath(page, root)
        for i, line in enumerate(lines, start=1):
            if rx.search(line):
                write_out(f"{rel}:{i}: {line}")
                count += 1
                if max_results > 0 and count >= max_results:
                    return 0
    return 0


def command_toc(root: Path, page: str, max_items: int) -> int:
    target = resolve_page(root, page)
    lines = read_lines(target)
    headings = parse_markdown(lines).headings

    if max_items > 0:
        headings = headings[:max_items]

    for h in headings:
        indent = "  " * (h.level - 1)
        write_out(f"{h.line_index + 1:5}: {indent}{h.text}")
    return 0


def match_headings(headings: list[Heading], title: str) -> list[Heading]:
    norm_title = normalize_heading(title).lower()
    exact = [h for h in headings if h.text.lower() == norm_title]
    if exact:
        return exact
    return [h for h in headings if norm_title in h.text.lower()]


def section_bounds(headings: list[Heading], section: Heading, line_count: int) -> tuple[int, int]:
    start = section.line_index
    end = line_count
    for nxt in headings:
        if nxt.line_index <= section.line_index:
            continue
        if nxt.level <= section.level:
            end = nxt.line_index
            break
    return start, end


def command_section(root: Path, page: str, title: str, max_lines: int) -> int:
    target = resolve_page(root, page)
    lines = read_lines(target)
    parsed = parse_markdown(lines)
    headings = parsed.headings
    hits = match_headings(headings, title)

    if not hits:
        die(f"section not found: '{title}' in {relpath(target, root)}")
    if len(hits) > 1:
        options = ", ".join(f"'{h.text}'" for h in hits[:8])
        tail = " ..." if len(hits) > 8 else ""
        die(f"section title is ambiguous. Matches: {options}{tail}")

    h = hits[0]
    start, end = section_bounds(headings, h, len(lines))

    out = lines[start:end]
    if max_lines > 0:
        out = out[:max_lines]
    for line in out:
        write_out(line)
    return 0


def normalize_lang(lang: str) -> str:
    base = lang.strip().lower()
    if base in ("py", "python3"):
        return "python"
    if base in ("bash", "sh", "zsh", "shell"):
        return "shell"
    return base


def lang_matches(block_lang: str, query_lang: str) -> bool:
    q = normalize_lang(query_lang)
    b = normalize_lang(block_lang)
    if not q:
        return True
    if q == "python":
        return b in ("python", "py", "python3")
    if q == "shell":
        return b in ("shell", "bash", "sh", "zsh")
    return b == q


def heading_path_for_line(headings: list[Heading], line_index: int) -> str:
    stack: list[Heading] = []
    for h in headings:
        if h.line_index > line_index:
            break
        while stack and stack[-1].level >= h.level:
            stack.pop()
        stack.append(h)
    if not stack:
        return ""
    return " > ".join(h.text for h in stack)


def select_code_blocks(
    lines: list[str],
    parsed: ParsedDoc,
    title: str,
    lang: str,
) -> list[CodeBlock]:
    start = 0
    end = len(lines)

    if title:
        hits = match_headings(parsed.headings, title)
        if not hits:
            die(f"section not found: '{title}'")
        if len(hits) > 1:
            options = ", ".join(f"'{h.text}'" for h in hits[:8])
            tail = " ..." if len(hits) > 8 else ""
            die(f"section title is ambiguous. Matches: {options}{tail}")
        start, end = section_bounds(parsed.headings, hits[0], len(lines))

    selected: list[CodeBlock] = []
    for block in parsed.code_blocks:
        if block.start_line_index < start or block.start_line_index >= end:
            continue
        if lang and not lang_matches(block.lang, lang):
            continue
        selected.append(block)
    return selected


def code_block_body_bounds(block: CodeBlock) -> tuple[int, int]:
    start = block.start_line_index + 1
    end = block.end_line_index - 1 if block.closed else block.end_line_index
    if end < start:
        end = start
    return start, end


def command_examples(root: Path, include_all_pages: bool, max_results: int) -> int:
    pages = iter_pages(root)
    if not include_all_pages:
        pages = [p for p in pages if relpath(p, root).startswith("Python_Tutorials/")]

    printed = 0
    for page in pages:
        lines = read_lines(page)
        parsed = parse_markdown(lines)
        if not parsed.code_blocks:
            continue

        by_section: dict[str, int] = {}
        for block in parsed.code_blocks:
            section = heading_path_for_line(parsed.headings, block.start_line_index) or "(no heading)"
            by_section[section] = by_section.get(section, 0) + 1

        rel = relpath(page, root)
        for section, count in by_section.items():
            write_out(f"{rel} | {section} | snippets={count}")
            printed += 1
            if max_results > 0 and printed >= max_results:
                return 0

    return 0


def command_snippets(root: Path, page: str, title: str, lang: str, max_results: int) -> int:
    target = resolve_page(root, page)
    lines = read_lines(target)
    parsed = parse_markdown(lines)
    selected = select_code_blocks(lines, parsed, title, lang)

    if not selected:
        die(f"no code snippets matched in {relpath(target, root)}")

    if max_results > 0:
        selected = selected[:max_results]

    for i, block in enumerate(selected, start=1):
        body_start, body_end = code_block_body_bounds(block)
        language = block.lang or "text"
        section = heading_path_for_line(parsed.headings, block.start_line_index) or "(no heading)"
        write_out(
            f"{i:3}: lines {body_start + 1}-{body_end} | lang={language} | section={section}"
        )
    return 0


def command_snippet(
    root: Path,
    page: str,
    index: int,
    pick: str,
    title: str,
    lang: str,
    no_fence: bool,
    max_lines: int,
) -> int:
    target = resolve_page(root, page)
    lines = read_lines(target)
    parsed = parse_markdown(lines)
    selected = select_code_blocks(lines, parsed, title, lang)

    if not selected:
        die(f"no code snippets matched in {relpath(target, root)}")

    if pick:
        if pick == "first":
            block = selected[0]
        elif pick == "longest":
            block = max(
                selected,
                key=lambda b: code_block_body_bounds(b)[1] - code_block_body_bounds(b)[0],
            )
        else:
            die(f"unknown pick mode: {pick}")
    else:
        if index < 1 or index > len(selected):
            die(f"snippet index out of range: {index} (available: 1..{len(selected)})")
        block = selected[index - 1]

    body_start, body_end = code_block_body_bounds(block)
    body = lines[body_start:body_end]
    if max_lines > 0:
        body = body[:max_lines]

    if not no_fence:
        lang_tag = block.lang
        write_out(f"```{lang_tag}" if lang_tag else "```")
    for line in body:
        write_out(line)
    if not no_fence:
        write_out("```")
    return 0


def command_compose(
    root: Path,
    page: str,
    title: str,
    lang: str,
    no_fence: bool,
    max_lines: int,
    max_blocks: int,
) -> int:
    target = resolve_page(root, page)
    lines = read_lines(target)
    parsed = parse_markdown(lines)
    selected = select_code_blocks(lines, parsed, title, lang)

    if not selected:
        die(f"no code snippets matched in {relpath(target, root)}")
    if max_blocks > 0:
        selected = selected[:max_blocks]

    combined: list[str] = []
    for i, block in enumerate(selected):
        body_start, body_end = code_block_body_bounds(block)
        body = lines[body_start:body_end]
        if not body:
            continue
        if combined:
            combined.append("")
        combined.extend(body)

    if max_lines > 0:
        combined = combined[:max_lines]

    if not no_fence:
        if lang:
            lang_tag = lang
        elif selected:
            lang_tag = selected[0].lang
        else:
            lang_tag = ""
        write_out(f"```{lang_tag}" if lang_tag else "```")
    for line in combined:
        write_out(line)
    if not no_fence:
        write_out("```")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local query helper for bundled Meep docs.")
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=DEFAULT_DOC_ROOT,
        help=f"Path to docs root (default: {DEFAULT_DOC_ROOT})",
    )

    sub = parser.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list", help="List markdown pages.")
    p_list.add_argument("--limit", type=int, default=0, help="Show only first N pages.")

    p_search = sub.add_parser("search", help="Regex search across docs.")
    p_search.add_argument("pattern", help="Regex pattern.")
    p_search.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Use case-sensitive regex matching.",
    )
    p_search.add_argument(
        "--max-results",
        type=int,
        default=0,
        help="Stop after printing this many matches.",
    )

    p_toc = sub.add_parser("toc", help="Show headings for one page.")
    p_toc.add_argument("page", help="Page path or name.")
    p_toc.add_argument("--max", type=int, default=0, help="Show only first N headings.")

    p_section = sub.add_parser("section", help="Print one section by heading title.")
    p_section.add_argument("page", help="Page path or name.")
    p_section.add_argument("title", help="Section heading title (exact or substring).")
    p_section.add_argument(
        "--max-lines",
        type=int,
        default=0,
        help="Show only first N lines of the section.",
    )

    p_examples = sub.add_parser(
        "examples",
        help="List example-rich sections and snippet counts (default: Python tutorials only).",
    )
    p_examples.add_argument(
        "--all-pages",
        action="store_true",
        help="Include all markdown pages (not only Python_Tutorials).",
    )
    p_examples.add_argument(
        "--max-results",
        type=int,
        default=0,
        help="Stop after printing this many rows.",
    )

    p_snippets = sub.add_parser(
        "snippets",
        help="List code snippets in one page, optionally filtered by section title/language.",
    )
    p_snippets.add_argument("page", help="Page path or name.")
    p_snippets.add_argument(
        "--title",
        default="",
        help="Section heading title (exact or substring).",
    )
    p_snippets.add_argument(
        "--lang",
        default="",
        help="Filter by language tag (e.g. py, python, sh, bash).",
    )
    p_snippets.add_argument(
        "--max-results",
        type=int,
        default=0,
        help="Stop after printing this many snippets.",
    )

    p_snippet = sub.add_parser(
        "snippet",
        help="Print one code snippet by 1-based index from the filtered snippet list.",
    )
    p_snippet.add_argument("page", help="Page path or name.")
    p_snippet.add_argument(
        "index",
        nargs="?",
        type=int,
        default=1,
        help="1-based snippet index after filters (default: 1).",
    )
    p_snippet.add_argument(
        "--pick",
        choices=["first", "longest"],
        default="",
        help="Auto-select snippet by strategy (ignores index).",
    )
    p_snippet.add_argument(
        "--title",
        default="",
        help="Section heading title (exact or substring).",
    )
    p_snippet.add_argument(
        "--lang",
        default="",
        help="Filter by language tag (e.g. py, python, sh, bash).",
    )
    p_snippet.add_argument(
        "--no-fence",
        action="store_true",
        help="Print snippet body only (without Markdown fences).",
    )
    p_snippet.add_argument(
        "--max-lines",
        type=int,
        default=0,
        help="Show only first N lines of the snippet body.",
    )

    p_compose = sub.add_parser(
        "compose",
        help="Concatenate all filtered code snippets in order into one composite snippet.",
    )
    p_compose.add_argument("page", help="Page path or name.")
    p_compose.add_argument(
        "--title",
        default="",
        help="Section heading title (exact or substring).",
    )
    p_compose.add_argument(
        "--lang",
        default="",
        help="Filter by language tag (e.g. py, python, sh, bash).",
    )
    p_compose.add_argument(
        "--no-fence",
        action="store_true",
        help="Print composed body only (without Markdown fences).",
    )
    p_compose.add_argument(
        "--max-lines",
        type=int,
        default=0,
        help="Show only first N lines of the composed snippet.",
    )
    p_compose.add_argument(
        "--max-blocks",
        type=int,
        default=0,
        help="Use only first N filtered code blocks.",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    root: Path = args.docs_root

    if not root.exists() or not root.is_dir():
        die(f"docs root does not exist: {root}")

    if args.cmd == "list":
        return command_list(root, args.limit)
    if args.cmd == "search":
        return command_search(root, args.pattern, args.case_sensitive, args.max_results)
    if args.cmd == "toc":
        return command_toc(root, args.page, args.max)
    if args.cmd == "section":
        return command_section(root, args.page, args.title, args.max_lines)
    if args.cmd == "examples":
        return command_examples(root, args.all_pages, args.max_results)
    if args.cmd == "snippets":
        return command_snippets(root, args.page, args.title, args.lang, args.max_results)
    if args.cmd == "snippet":
        return command_snippet(
            root,
            args.page,
            args.index,
            args.pick,
            args.title,
            args.lang,
            args.no_fence,
            args.max_lines,
        )
    if args.cmd == "compose":
        return command_compose(
            root,
            args.page,
            args.title,
            args.lang,
            args.no_fence,
            args.max_lines,
            args.max_blocks,
        )

    die(f"unknown command: {args.cmd}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
