#!/usr/bin/env python3
"""Static QA checks for Nature Communications-style Matplotlib scripts.

Usage:
    python style_qa.py path/to/script.py [another.py ...]

The checker is heuristic. It flags common figure-style problems but does not replace visual review.
"""

from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path
from typing import Iterable

BANNED_CMAPS = {"jet", "rainbow", "hsv", "gist_rainbow", "nipy_spectral"}
WARN_CMAPS = {"turbo"}
REQUIRED_EXPORT_HINTS = {"pdf.fonttype", "svg.fonttype", "savefig.dpi"}
NCOMMS_SINGLE_COLUMN_WIDTH_IN = 88 / 25.4
NCOMMS_DOUBLE_COLUMN_WIDTH_IN = 180 / 25.4


class PlotStyleVisitor(ast.NodeVisitor):
    def __init__(self, source: str, path: Path):
        self.source = source
        self.path = path
        self.issues: list[tuple[int, str, str]] = []

    def warn(self, node: ast.AST, code: str, msg: str) -> None:
        line = getattr(node, "lineno", 0)
        self.issues.append((line, code, msg))

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        func_name = self._func_name(node.func)

        # cmap='jet' or plt.get_cmap('jet')
        for kw in node.keywords:
            if kw.arg == "cmap":
                val = self._literal_str(kw.value)
                if val in BANNED_CMAPS:
                    self.warn(node, "BANNED_CMAP", f"Replace cmap='{val}' with semantic cmap: viridis/cividis, magma/inferno, RdBu_r, or twilight.")
                elif val in WARN_CMAPS:
                    self.warn(node, "WARN_CMAP", f"Avoid cmap='{val}' for publication scalar data unless specifically justified.")

        if func_name.endswith("get_cmap") and node.args:
            val = self._literal_str(node.args[0])
            if val in BANNED_CMAPS:
                self.warn(node, "BANNED_CMAP", f"Replace get_cmap('{val}') with a perceptually appropriate map.")

        # figure size too large for publication script
        if func_name.endswith("figure") or func_name.endswith("subplots"):
            for kw in node.keywords:
                if kw.arg == "figsize":
                    size = self._tuple_numbers(kw.value)
                    if size and (size[0] > 7.5 or size[1] > 6):
                        self.warn(node, "LARGE_FIGSIZE", f"figsize={size} is likely presentation-sized; use 88 mm single-column or 180 mm double-column width.")

        # linewidth too large
        for kw in node.keywords:
            if kw.arg in {"linewidth", "linewidths", "lw"}:
                num = self._number(kw.value)
                if num is not None and num >= 3:
                    self.warn(node, "THICK_LINE", f"{kw.arg}={num:g} is heavy for journal plots; prefer 1.0 for axes/contours or 1.2-1.5 for curves.")
                if num is not None and 0 < num < 1:
                    self.warn(node, "THIN_LINE", f"{kw.arg}={num:g} is below Nature Communications' 1 pt minimum final line weight.")
            if kw.arg in {"markersize", "ms"}:
                num = self._number(kw.value)
                if num is not None and num > 7:
                    self.warn(node, "LARGE_MARKER", f"{kw.arg}={num:g} is large for final-size paper figures; prefer 3–4.")
            if kw.arg == "s":
                num = self._number(kw.value)
                if num is not None and num > 80:
                    self.warn(node, "LARGE_SCATTER", f"scatter s={num:g} is large for compact figures; prefer 12–20 unless highlighting.")

        # imshow without origin/aspect/cmap/norm hints
        if func_name.endswith("imshow"):
            kw_names = {kw.arg for kw in node.keywords if kw.arg}
            if "origin" not in kw_names:
                self.warn(node, "IMSHOW_ORIGIN", "Set origin='lower' for scientific coordinate maps unless image convention requires upper origin.")
            if "aspect" not in kw_names:
                self.warn(node, "IMSHOW_ASPECT", "Set aspect='equal' for spatial maps or aspect='auto' for parameter sweeps.")
            if "cmap" not in kw_names:
                self.warn(node, "IMSHOW_CMAP", "Choose cmap by data semantics instead of relying on defaults.")

        # savefig low-dpi raster or no extension
        if func_name.endswith("savefig"):
            first = self._literal_str(node.args[0]) if node.args else ""
            if first and not Path(first).suffix:
                self.warn(node, "SAVEFIG_EXT", "Use an explicit publication extension such as .pdf, .svg, .eps, or .tif.")
            if first and first.lower().endswith((".jpg", ".jpeg")):
                self.warn(node, "JPEG_EXPORT", "Avoid JPEG for final Nature Communications figure files; use vector PDF/EPS/AI for line art or RGB TIFF for bitmap images.")
            if first and first.lower().endswith((".png", ".jpg", ".jpeg", ".tif", ".tiff")):
                dpi = None
                for kw in node.keywords:
                    if kw.arg == "dpi":
                        dpi = self._number(kw.value)
                if dpi is not None and dpi < 300:
                    self.warn(node, "LOW_DPI", f"Raster export dpi={dpi:g} is low; use at least 300 dpi for Nature Communications.")

        self.generic_visit(node)

    @staticmethod
    def _func_name(node: ast.AST) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            return PlotStyleVisitor._func_name(node.value) + "." + node.attr
        return ""

    @staticmethod
    def _literal_str(node: ast.AST) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        return None

    @staticmethod
    def _number(node: ast.AST) -> float | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        return None

    @staticmethod
    def _tuple_numbers(node: ast.AST) -> tuple[float, ...] | None:
        if isinstance(node, (ast.Tuple, ast.List)):
            out = []
            for elt in node.elts:
                val = PlotStyleVisitor._number(elt)
                if val is None:
                    return None
                out.append(val)
            return tuple(out)
        return None


def scan_text(source: str, path: Path) -> list[tuple[int, str, str]]:
    issues: list[tuple[int, str, str]] = []
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [(exc.lineno or 0, "SYNTAX", f"Could not parse Python file: {exc.msg}")]

    visitor = PlotStyleVisitor(source, path)
    visitor.visit(tree)
    issues.extend(visitor.issues)

    # Whole-file checks.
    if "matplotlib" in source or "plt." in source:
        for hint in REQUIRED_EXPORT_HINTS:
            if hint not in source:
                issues.append((0, "MISSING_RCPARAM", f"Consider setting rcParams['{hint}'] for editable/high-resolution export."))
        if re.search(r"plt\.grid\(\s*True", source) or re.search(r"ax\.grid\(\s*True", source):
            issues.append((0, "GRID", "Use no grid or very subtle grid lines for compact Nature Communications-style plots."))
        if "legend(" in source and "frameon=False" not in source and "legend.frameon" not in source:
            issues.append((0, "LEGEND_FRAME", "Use frameon=False for minimal legends unless a frame is needed."))
        if re.search(r"\blena\b", f"{path} {source}", re.IGNORECASE):
            issues.append((0, "LENA_IMAGE", "Nature Communications will not publish or peer review manuscripts using the image Lena."))
        if re.search(r"\bmsec\b", source):
            issues.append((0, "UNIT_MSEC", "Use SI-style unit 'ms' instead of 'msec'."))
        if "transparent=True" in source or '"savefig.transparent": True' in source or "'savefig.transparent': True" in source:
            issues.append((0, "TRANSPARENT_BG", "Nature Communications display items should be on a white background, not transparent."))

    return sorted(issues, key=lambda item: item[0])


def scan_file(path: Path) -> list[tuple[int, str, str]]:
    return scan_text(path.read_text(encoding="utf-8"), path)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path, help="Python files to scan")
    args = parser.parse_args(argv)

    total = 0
    for path in args.paths:
        if not path.exists():
            print(f"{path}: ERROR file does not exist")
            total += 1
            continue
        issues = scan_file(path)
        if not issues:
            print(f"{path}: OK")
            continue
        for line, code, msg in issues:
            loc = f"{path}:{line}" if line else str(path)
            print(f"{loc}: {code}: {msg}")
        total += len(issues)
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
