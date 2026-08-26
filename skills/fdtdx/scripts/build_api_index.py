#!/usr/bin/env python3
"""Build a static index of the public FDTDX API for offline agent lookup."""

from __future__ import annotations

import argparse
import importlib
import importlib.metadata
import inspect
import json
import os
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def safe_signature(obj: Any) -> str:
    target = obj.__init__ if inspect.isclass(obj) else obj
    try:
        return str(inspect.signature(target))
    except (TypeError, ValueError):
        return ""


def safe_source(obj: Any, source_root: Path | None) -> tuple[str, int | None]:
    try:
        path = Path(inspect.getsourcefile(obj) or inspect.getfile(obj)).resolve()
    except (TypeError, OSError):
        return "", None
    try:
        line = inspect.getsourcelines(obj)[1]
    except (TypeError, OSError):
        line = None
    if source_root is not None:
        try:
            path_text = path.relative_to(source_root.resolve()).as_posix()
        except ValueError:
            path_text = path.as_posix()
    else:
        path_text = path.as_posix()
    return path_text, line


def kind_of(obj: Any) -> str:
    if inspect.isclass(obj):
        return "class"
    if inspect.iscoroutinefunction(obj):
        return "async-function"
    if inspect.isfunction(obj) or inspect.ismethod(obj) or inspect.isbuiltin(obj):
        return "function"
    if isinstance(obj, type(None)):
        return "none"
    return "alias" if getattr(obj, "__module__", "").startswith("fdtdx") else "value"


def class_fields(cls: type) -> list[dict[str, str]]:
    fields: dict[str, dict[str, str]] = {}
    for base in reversed(cls.__mro__):
        for name, annotation in getattr(base, "__annotations__", {}).items():
            if name.startswith("_"):
                continue
            default = ""
            try:
                value = inspect.getattr_static(cls, name)
                try:
                    default = repr(value)
                except (RecursionError, RuntimeError, ValueError):
                    default = f"<{type(value).__module__}.{type(value).__qualname__}>"
            except AttributeError:
                pass
            fields[name] = {
                "name": name,
                "annotation": inspect.formatannotation(annotation),
                "default": default,
                "defined_in": f"{base.__module__}.{base.__qualname__}",
            }
    return list(fields.values())


def public_members(cls: type, source_root: Path | None) -> list[dict[str, Any]]:
    members: list[dict[str, Any]] = []
    for name in sorted(dir(cls), key=str.lower):
        if name.startswith("_") or name in {"at"}:
            continue
        try:
            raw = inspect.getattr_static(cls, name)
            value = getattr(cls, name)
        except Exception:
            continue
        if isinstance(raw, property):
            target = raw.fget
            member_kind = "property"
        elif isinstance(raw, (classmethod, staticmethod)):
            target = raw.__func__
            member_kind = "class-method" if isinstance(raw, classmethod) else "static-method"
        elif callable(value):
            target = value
            member_kind = "method"
        else:
            continue
        source, line = safe_source(target, source_root)
        members.append(
            {
                "name": name,
                "kind": member_kind,
                "signature": safe_signature(value),
                "doc": inspect.getdoc(value) or "",
                "module": getattr(target, "__module__", ""),
                "qualname": getattr(target, "__qualname__", name),
                "source": source,
                "line": line,
            }
        )
    return members


def build_index(
    package_name: str,
    source_root: Path | None,
    source_label: str,
    source_commit: str,
) -> dict[str, Any]:
    temp_base = tempfile.mkdtemp(prefix="fdtdx-skill-api-")
    os.environ.setdefault("TIDY3D_BASE_DIR", temp_base)
    package = importlib.import_module(package_name)
    exports = list(getattr(package, "__all__", []))
    entries: list[dict[str, Any]] = []
    for name in sorted(exports, key=str.lower):
        obj = getattr(package, name)
        source, line = safe_source(obj, source_root)
        entry: dict[str, Any] = {
            "name": name,
            "qualified_name": f"{package_name}.{name}",
            "kind": kind_of(obj),
            "signature": safe_signature(obj),
            "doc": inspect.getdoc(obj) or "",
            "module": getattr(obj, "__module__", ""),
            "qualname": getattr(obj, "__qualname__", name),
            "source": source,
            "line": line,
        }
        if inspect.isclass(obj):
            entry["fields"] = class_fields(obj)
            entry["members"] = public_members(obj, source_root)
        entries.append(entry)

    try:
        version = importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        version = "unknown"
    return {
        "metadata": {
            "package": package_name,
            "version": version,
            "generated_utc": datetime.now(UTC).isoformat(),
            "export_count": len(entries),
            "source_root": source_label,
            "source_commit": source_commit,
        },
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", default="fdtdx")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--source-label", default="doc/package-src")
    parser.add_argument("--source-commit", default="")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    index = build_index(args.package, args.source_root, args.source_label, args.source_commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {index['metadata']['export_count']} API entries to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
