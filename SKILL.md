---
name: nature-photonics-plotting
description: >-
  Use when generating, editing, or reviewing publication-grade Nature
  Photonics-style scientific figures or figure layouts in Python/Matplotlib:
  spectra, PSF/intensity maps, heat maps, microscopy/SEM/TEM/AFM panels,
  statistical plots, multi-panel layouts, mixed plot+image figures, and export
  workflows. Do not use for decorative business graphics unless the user
  explicitly asks for a journal-style scientific figure.
---

# Nature Photonics-style scientific figure skill

## Purpose

Produce compact, technically correct, publication-ready scientific figures and figure layouts with a Nature Photonics / Nature Portfolio aesthetic. Preserve the scientific content while improving readability, normalization, color choice, layout, annotation, and export.

Keep this file lean. Use it as a router. Load only the reference files needed for the active figure family instead of pulling every recipe into context.

## Non-negotiable global rules

- Preserve scientific meaning. Do not silently change processing, normalization semantics, statistics, or units.
- Design at final journal size, not notebook size.
- Keep typography sans-serif and compact: typically 5-7 pt at final size.
- Use lower-case bold panel labels: `a`, `b`, `c`, ...
- Keep text, axes, scale bars, arrows, and boxes editable whenever possible.
- Use semantically correct colormaps and normalization.
- Avoid decorative effects, heavy grids, thick borders, and rainbow colormaps for scalar data.
- For microscopy/image panels, keep scale bars and annotations as vector overlays over the raster image.
- Prefer PDF/SVG for vector or mixed figures and PNG/TIFF at 600 dpi for raster-heavy output.

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
- Multi-panel figure, mixed plot+image figure, shared colorbars, panel letters, GridSpec/subplot_mosaic layouts, inset axes:
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

- `assets/nature_photonics.mplstyle`: reusable Matplotlib style sheet.
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
