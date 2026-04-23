# Plot-type recipe index

Use this file as a lightweight map of the available figure-family references. Do not load every reference by default.

## Recommended loading order

1. Read `style-foundation.md`
2. Read only the matching family file or files below
3. Read `review_checklist.md` before returning code or figure feedback

## Routing table

- Line, spectrum, response curve, error bars, scatter, parity, residual, calibration, log-scale line plot:
  `curves-and-scatter.md`
- Histogram, ECDF, box plot, violin plot, bar chart, grouped categorical comparison:
  `statistical-and-categorical.md`
- Heat map, pcolormesh, PSF, intensity map, phase map, residual map, contour plot, correlation matrix, confusion matrix:
  `scalar-fields-and-maps.md`
- Vector field, quiver, streamplot, polar plot, spectrogram, waterfall, dispersion, band structure:
  `specialized-plots.md`
- Microscopy, SEM, FESEM, STEM, TEM, AFM-like, optical micrograph, overview+zoom, annotated image panel:
  `microscopy-and-sem-panels.md`
- Multi-panel figure, mixed plot+image figure, shared colorbars, panel letters, GridSpec/subplot_mosaic layouts, inset axes:
  `multi-panel-layouts.md`

## Common mixed-figure combinations

- Spectrum + heat map:
  `style-foundation.md` + `curves-and-scatter.md` + `scalar-fields-and-maps.md`
- SEM + quantitative plots:
  `style-foundation.md` + `microscopy-and-sem-panels.md` + relevant plot-family file + `multi-panel-layouts.md`
- Box plot + scatter or box plot + simulation marker:
  `style-foundation.md` + `statistical-and-categorical.md`
- Any figure with more than one panel:
  Add `multi-panel-layouts.md`

## Notes

- `style-foundation.md` contains the shared rcParams block, figure sizes, color rules, normalization rules, export policy, and code-editing policy.
- `review_checklist.md` is the final QA pass.
- Family files are intentionally grouped by plot family rather than by every individual chart subtype to keep routing simple while still saving context.
