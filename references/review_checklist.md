# Nature Photonics-style figure review checklist

Use this checklist before returning Matplotlib code or reviewing user figures.

## 1. Scientific integrity

- The plotted data arrays are unchanged unless the user requested processing.
- Any smoothing, clipping, normalization, averaging, interpolation, or log transform is explicit.
- Axis units match the data.
- Labels are not misleading.
- Error bars are identified as SD, SEM, CI, fit uncertainty, or measurement uncertainty where code/caption permits.
- Color limits are comparable across panels when panels are compared.
- Outliers are not hidden unless the reason is clear and stated.

## 2. Journal-scale readability

- Final figure width is chosen intentionally: single ~3.5 in, one-half ~5.2 in, double ~7.2 in.
- Tick labels remain readable at final size.
- Figure is compact with minimal unused whitespace.
- Fonts are consistent, sans-serif, and approximately 5–7 pt at final size.
- Axes linewidth is approximately 0.6 pt.
- Main line widths are approximately 1.2–1.5 pt.
- Markers are approximately 3–4 pt, not oversized.
- Error bars use thin caps and lines.

## 3. Axes and labels

- Axis labels are concise.
- Units are in parentheses: `Wavelength (nm)`, `Position (µm)`, `Intensity (a.u.)`.
- Major ticks are sparse: usually 4–6 per axis.
- Minor ticks are used only when useful.
- Top and right spines are hidden unless a boxed axis is needed.
- Ticks point outward.
- Log axes use appropriate log tick locators and labels.
- No unnecessary subplot titles; panel labels and caption should carry structure.

## 4. Color and accessibility

- No `jet`, `rainbow`, or non-monotonic colormaps for scalar data.
- No red-green-only primary comparison.
- Color cycle is colorblind-aware and restrained.
- Black/gray is used for axes and text.
- Background is white.
- Grid lines are absent or very light.
- Categorical colors do not compete with scalar colormaps in the same panel.

## 5. Colormap and normalization

- Positive magnitude uses sequential map: `viridis`, `cividis`, `magma`, or `inferno`.
- PSF/intensity uses `magma` or `inferno`; log scale considered for high dynamic range.
- Signed residual/difference uses diverging map and centered norm.
- Wrapped phase uses cyclic map and phase ticks.
- Discrete classes use `ListedColormap` + `BoundaryNorm`.
- `vmin`/`vmax` are intentional.
- Percentile clipping is marked with `extend` on colorbar when relevant.
- Shared colorbars use shared `norm`.

## 6. Plot-specific checks

### Line plots

- Dense traces do not use markers.
- Simulated vs measured curves are visually distinguishable by line style and/or markers.
- Fits do not obscure data points.
- Legends are short and unobtrusive.

### Scatter

- Marker size is not too large.
- Dense scatter is rasterized or converted to density plot.
- Parity plots include y=x reference and equal aspect.
- Residual plots include a zero reference line.

### Histograms

- Binning is deliberate.
- Comparisons use shared bins.
- Density vs count is correctly labeled.
- Overlapping histograms use outlines or transparency without muddy color.

### Box/violin plots

- Small-n data show individual points.
- Medians are visible.
- Outlier policy is explicit.
- Category labels are readable.

### Bar charts

- Y-axis starts at zero unless there is a clear reason not to.
- Error bars or individual points are included where relevant.
- Bars are not used to hide distributions.

### Heat maps / PSF / images

- `origin`, `extent`, `aspect`, `norm`, `cmap`, and colorbar label are set deliberately.
- Physical axes or scale bar are present.
- Interpolation is off unless smoothing is intentional.
- Image evidence is not contrast-manipulated silently.

### Multi-panel figures

- Panel labels are lower-case bold.
- Panels are aligned.
- Comparable panels share scales and norms.
- Colorbars are consistent.
- Whitespace is balanced.

## 7. Export checks

- PDF/SVG output is available for vector/mixed figures.
- Raster output is 600 dpi when needed.
- `pdf.fonttype=42`, `ps.fonttype=42`, `svg.fonttype='none'` are set.
- Text is editable in vector outputs.
- Dense raster artists are rasterized but labels remain vector.
- `bbox_inches='tight'` and small padding are used.

## 8. Anti-patterns to fix automatically

Replace or fix these when editing code:

- `cmap='jet'`, `cmap='rainbow'`, `cmap='hsv'` for scalar magnitude.
- `plt.figure(figsize=(12, 8))` for publication plots.
- Fonts larger than 10 pt in a single-column scientific figure.
- `linewidth >= 3` for standard data curves.
- Oversized markers (`s > 80`, `markersize > 8`) unless user explicitly wants a presentation slide.
- Missing axis labels.
- Missing colorbar labels.
- Legends with frames unless a frame is necessary for readability.
- Heavy default grids.
- Relying on default `imshow` origin/aspect for physical maps.
- Saving only low-resolution PNG.
- Converting text to outlines in vector export.

## 9. Response style for Codex

When the user asks for code, return code. Include only a compact note if important choices need justification.

When the user asks for a review, use this structure:

1. Key issues found.
2. Corrected code.
3. Short checklist of changes.

When ambiguity exists, make the most conservative journal-style choice and leave a clear comment in the code.
