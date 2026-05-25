---
name: scientific-plotting
description: >-
  Use when generating, editing, or reviewing publication-grade scientific figures or figure layouts in Python/Matplotlib, with Nature Communications-style defaults when a journal aesthetic is useful:
  spectra, PSF/intensity maps, heat maps, microscopy/SEM/TEM/AFM panels,
  statistical plots, multi-panel layouts, mixed plot+image figures, and export
  workflows. Do not use for decorative business graphics unless the user
  explicitly asks for a journal-style scientific figure.
---

# Scientific plotting skill

## Purpose

Produce compact, technically correct, publication-ready scientific figures and figure layouts with a Nature Communications / Nature Portfolio aesthetic. Preserve the scientific content while improving readability, normalization, color choice, layout, annotation, and export.

This is a general plotting guideline, not a repository- or paper-specific workflow. Do not assume project-specific paths, manuscript geometry, datasets, or local conventions unless the user provides them.

Keep this file lean. Use it as a router. Load only the reference files needed for the active figure family instead of pulling every recipe into context.

## Non-negotiable global rules

- Preserve scientific meaning. Do not silently change processing, normalization semantics, statistics, or units.
- Design at final journal size, not notebook size.
- Use the same typeface across all figures. Prefer Arial or Helvetica, with Symbol/mathtext used for Greek letters and symbols when needed.
- Keep typography sans-serif and compact at final display size. Nature Communications states that the optimum final-size font is 5-8 pt. Use base/title/legend 8 pt, axis/tick/colorbar 7 pt, panel labels 8 pt, and SEM/image annotation text 7 pt unless the user specifies otherwise.
- For final Nature Communications production files, use one- or two-column figure widths: 88 mm single column or 180 mm double column. For manuscript/LaTeX review files, first determine the LaTeX display width for the whole figure and make the generated figure width match it. If no LaTeX file or production target is available, assume a 6.5 in text width. Use the full figure width, not one subplot width.
- Use lower-case bold panel labels: `a`, `b`, `c`, ... Use 8 pt labels when the generated width matches the LaTeX display width. Only scale panel labels as a fallback when an existing script cannot generate at the LaTeX display width.
- Keep text, axes, scale bars, arrows, and boxes editable whenever possible.
- Use a white background for all display items.
- Keep the thinnest final line art at least 1 pt wide. Avoid excessive boxing and decorative outer frames.
- Use semantically correct colormaps and normalization.
- Use distinct colors with comparable visibility. Avoid red-vs-green contrast and avoid rainbow colormaps for scalar data.
- Provide photographic/bitmapped images as TIFF in RGB color at 300 dpi or higher resolution, close to final page size. Single-column bitmap panels should be at least 1,040 px wide; double-column bitmap figures should be at least 2,080 px wide, excluding peripheral whitespace.
- Supply line art, graphs, charts, and schematics as vector files such as PDF/EPS/AI when possible. If line art cannot be supplied as vector, export it at 1,200 dpi.
- Prefer editable vector or layered files when possible.
- Avoid decorative effects, heavy grids, and thick borders.
- For microscopy/image panels, keep scale bars and annotations as vector overlays over the raster image. Use scale bars rather than magnification factors; by default define the scale-bar length in the figure legend, not as text on the bar.
- For SEM publication-finalizer requests, generate one standalone Python script with a top-level `CONFIG` dictionary; do not create YAML, JSON, TOML, or other external config files unless explicitly requested.
- Prefer PDF/SVG for vector or mixed figures and PNG/TIFF at 300 dpi or higher; use 600 dpi for raster-heavy output when practical.

## Routing workflow

1. Classify the figure family first.
2. Read `references/style-foundation.md`.
3. Read only the relevant family file or files from the routing table below.
4. For mixed figures, combine only the needed family files plus `references/multi-panel-layouts.md`.
5. Before returning code or review guidance, read `references/review_checklist.md`.

## Figure-family routing

- Line, spectrum, response curve, error bars, scatter, parity, residual, calibration, log-scale line plot:
  Read `references/curves-and-scatter.md`
- Histogram, ECDF, box plot, violin plot, bar chart, grouped categorical comparison:
  Read `references/statistical-and-categorical.md`
- Heat map, pcolormesh, PSF, intensity map, phase map, residual map, contour plot, correlation matrix, confusion matrix:
  Read `references/scalar-fields-and-maps.md`
- Vector field, quiver, streamplot, polar plot, spectrogram, waterfall, dispersion, band structure:
  Read `references/specialized-plots.md`
- Microscopy, SEM, FESEM, STEM, TEM, AFM-like, optical micrograph, overview+zoom, annotated image panel:
  Read `references/microscopy-and-sem-panels.md`
- Multi-panel figure, mixed plot+image figure, shared colorbars, panel letters, GridSpec/subplot_mosaic layouts, inset axes, stacked zoom rows:
  Read `references/multi-panel-layouts.md`

If the task spans several families, load the smallest useful combination. Typical combinations:

- Spectrum + heat map + panel layout:
  Read `references/style-foundation.md`, `references/curves-and-scatter.md`, `references/scalar-fields-and-maps.md`, `references/multi-panel-layouts.md`
- SEM + plot + layout:
  Read `references/style-foundation.md`, `references/microscopy-and-sem-panels.md`, the relevant plot-family file, and `references/multi-panel-layouts.md`
- Box plot + scatter overlay:
  Read `references/style-foundation.md`, `references/statistical-and-categorical.md`, and `references/multi-panel-layouts.md` only if it is part of a larger figure

## Quick classification checklist

Before editing user code or giving figure guidance, identify:

- Is the primary object a 1D curve, a point cloud, a distribution, a 2D field, a microscopy image, or a mixed panel figure?
- Does the figure need shared axes, shared colorbars, inset panels, or panel labels?
- Are there hidden physical axes that require a scale bar?
- Is the data positive, signed, logarithmic, cyclic, or discrete?
- Is the task about generating code, reviewing a figure, or correcting style in existing code?

Then load only the matching references.

## Shared defaults to apply everywhere

- Base the visual language on `references/style-foundation.md`.
- Use `references/plot_type_recipes.md` only as a legacy index if you need a quick map of the available families.
- Prefer existing helpers in `scripts/np_plot_style.py` when they fit the task.
- Use `references/review_checklist.md` as the final QA pass.

## Files in this skill

- `assets/nature_communications.mplstyle`: reusable Matplotlib style sheet.
- `assets/nature_photonics.mplstyle`: legacy filename kept for compatibility; content follows Nature Communications defaults.
- `scripts/np_plot_style.py`: helper functions for style, sizing, panel labels, robust limits, colorbars, and scale bars.
- `scripts/style_qa.py`: static lint-style checks for plotting mistakes.
- `references/style-foundation.md`: core rcParams, sizing, color, normalization, export, and editing policy.
- `references/curves-and-scatter.md`: line/scatter/error-bar recipes.
- `references/statistical-and-categorical.md`: histogram/ECDF/box/violin/bar recipes.
- `references/scalar-fields-and-maps.md`: heat map, PSF, phase, contour, and matrix recipes.
- `references/specialized-plots.md`: vector-field, polar, spectrogram, waterfall, and dispersion recipes.
- `references/microscopy-and-sem-panels.md`: microscopy and SEM panel guidance.
- `references/multi-panel-layouts.md`: panel layout, inset, and label guidance.
- `references/plot_type_recipes.md`: legacy index that points to the split family files.
- `references/review_checklist.md`: final QA checklist and anti-patterns.
- `references/sources.md`: source references and rationale.
