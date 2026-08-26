# Style foundation for Nature Communications-style scientific figures

Load this file before substantial plotting edits. Then load only the relevant figure-family file or files.

## Core design rules

- Clarity first. Every style choice must make the data easier to read.
- Treat this as a general Scientific Plotting guideline. Do not assume repository-specific paths, page geometry, or manuscript conventions unless the user provides them.
- Design at final size, not notebook size.
- Size each generated figure to its intended LaTeX display width so the final displayed LaTeX PDF has consistent font sizes. Use the total figure width, not the width of one subplot.
- Use color semantically, not decoratively.
- Keep text, axes, line art, panel labels, arrows, and scale bars editable whenever possible.
- Use deterministic, reusable Matplotlib code.
- Use simple, consistent quantitative axes. Do not add decorative outer boxes or heavy frames.
- Do not change scientific processing unless the user asks or the existing code is clearly wrong.

## Default rcParams

Prefer this block unless the user, journal template, or target manuscript explicitly specifies a stricter standard.

```python
import matplotlib as mpl
from cycler import cycler

NCOMMS_SINGLE_COLUMN_WIDTH_IN = 88 / 25.4
NCOMMS_DOUBLE_COLUMN_WIDTH_IN = 180 / 25.4

NATURE_COMMUNICATIONS_COLORS = [
    "#1B3B6F",
    "#D55E00",
    "#007C73",
    "#B2479A",
    "#C99A00",
    "#4D4D4D",
    "#56B4E9",
    "#000000",
]

mpl.rcParams.update({
    "figure.figsize": (3.4646, 2.4945),
    "figure.dpi": 150,
    "figure.constrained_layout.use": True,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
    "savefig.transparent": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 8,
    "axes.labelsize": 7,
    "axes.titlesize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 8,
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",
    "axes.linewidth": 1.0,
    "axes.labelpad": 2.0,
    "lines.linewidth": 1.2,
    "lines.markersize": 3.5,
    "lines.markeredgewidth": 1.0,
    "patch.linewidth": 1.0,
    "xtick.major.width": 1.0,
    "ytick.major.width": 1.0,
    "xtick.minor.width": 1.0,
    "ytick.minor.width": 1.0,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "xtick.minor.size": 1.5,
    "ytick.minor.size": 1.5,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.top": False,
    "ytick.right": False,
    "axes.spines.top": True,
    "axes.spines.right": True,
    "axes.grid": False,
    "legend.frameon": False,
    "legend.handlelength": 1.6,
    "legend.handletextpad": 0.4,
    "legend.borderaxespad": 0.3,
    "legend.labelspacing": 0.25,
    "legend.columnspacing": 0.8,
    "image.cmap": "viridis",
    "image.interpolation": "none",
    "axes.prop_cycle": cycler(color=NATURE_COMMUNICATIONS_COLORS),
})
```

## Typography and LaTeX-matched figure width

Use these as target final displayed font sizes unless the user specifies otherwise:

- base/title/legend: 8 pt
- axis-label/tick-label/colorbar: 7 pt
- panel label: 8 pt
- SEM/image annotation and optional in-panel scale-bar text: 7 pt
- inset, contour, and dense secondary labels: 5-6 pt

The preferred workflow is to remove LaTeX width rescaling by generating each figure at the exact width it will occupy in LaTeX.

- First determine the manuscript `\textwidth` in inches. Prefer the LaTeX log or the source. If no LaTeX file or log is available, use the default `page_width_in = 6.5` in.
- If the figure is inserted as `width=\textwidth`, set the generated figure width to `page_width_in`.
- If the figure is inserted as `width=0.7\textwidth`, set the generated figure width to `0.7 * page_width_in`.
- If the figure is inside a minipage and included as `width=\linewidth`, use the minipage width as the generated figure width.
- If the user gives an absolute final display width, use that width directly.
- For multi-panel figures, this width is the full generated figure width. Do not calculate sizing from the width of one subplot.
- Keep these 5-8 pt final-size font targets across all generated figures after their widths have been matched.

Preferred formula:

```python
generated_total_width_in = page_width_in * latex_width_fraction
rc_font_size = target_font_size
```

Fallback formula only when an existing script must keep a generated width that differs from the LaTeX display width:

```python
final_display_width_in = page_width_in * latex_width_fraction
font_scale = generated_total_width_in / final_display_width_in
rc_font_size = target_font_size * font_scale
```

Examples:

```python
from np_plot_style import apply_nature_style, matched_figure_width

# Full-width figure generated at the same width as LaTeX \textwidth.
fig_width = matched_figure_width(page_width_in=6.5)
apply_nature_style()
fig, ax = plt.subplots(figsize=(fig_width, 4.2), constrained_layout=True)
```

```python
# Full-width multi-panel figure. Width is matched for the whole figure,
# not for each subplot.
fig_width = matched_figure_width(page_width_in=6.5)
apply_nature_style()
fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4.6), constrained_layout=True)
```

```python
# Figure generated at 0.49\textwidth and inserted into a matching minipage.
# The generated width matches the LaTeX display width, so fonts stay unchanged.
fig_width = matched_figure_width(page_width_in=6.5, latex_width_fraction=0.49)
apply_nature_style()
fig, ax = plt.subplots(figsize=(fig_width, 3.2), constrained_layout=True)
```

Use `page_width_in=...` when the manuscript text width is known. Use `final_width_in=...` when the final display width is known directly. For subfigures placed side by side in LaTeX minipages, pass the minipage or includegraphics fraction as `latex_width_fraction`.

## Nature Communications production widths

For final accepted Nature Communications production files, use the journal column widths directly unless the editor or acceptance letter specifies otherwise:

- single-column figure: 88 mm = 3.4646 in
- double-column figure: 180 mm = 7.0866 in
- final PDF page target: 210 x 276 mm
- single-column bitmap minimum: 1,040 px wide, excluding peripheral whitespace
- double-column bitmap minimum: 2,080 px wide, excluding peripheral whitespace

For first submission or review manuscripts where the figure is embedded in a LaTeX document, match the actual LaTeX display width instead. For final production export, regenerate at 88 mm or 180 mm rather than relying on LaTeX scaling.

## Figure sizes

Use inches internally.

```python
FIG_SIZES = {
    "single": (3.4646, 2.49),
    "one_half": (5.2, 3.2),
    "double": (7.0866, 4.54),
    "square_single": (3.4646, 3.4646),
    "tall_single": (3.4646, 4.16),
    "wide_double": (7.0866, 3.15),
}
```

- `single`: simple line plots and profile overlays; default aspect is 0.72
- `one_half`: two related panels with compact labels or a shared colorbar
- `double`: multi-panel figures, mixed plot+image figures, or long labels
- Keep height compact. Avoid creating a large figure and shrinking it later.

## Color rules

- Do not use `jet`, `rainbow`, or arbitrary rainbow gradients for scalar scientific data.
- Do not encode the main comparison using red-vs-green alone.
- Prefer colorblind-accessible arbitrary-color pairs such as green/magenta, turquoise/red, or yellow/blue when false-color or categorical contrast is needed.
- Do not use pastel colors for thin lines unless they are clearly background references.
- Do not use heavy gray grids or colored backgrounds.

Use colormaps by data semantics:

- Positive scalar magnitude: `viridis`, `cividis`
- Optical intensity / PSF / near-field magnitude: `magma`, `inferno`
- Log-scale positive intensity: `magma` or `inferno` with `LogNorm`
- Signed residual / difference / error: `RdBu_r`, `coolwarm`, or similar centered diverging map
- Wrapped phase: `twilight` or `twilight_shifted`
- Discrete class/bin map: `ListedColormap` with `BoundaryNorm`
- Binary mask: `gray`, `Greys`, or a two-color discrete map

## Normalization rules

Choose normalization from the physical meaning of the data, not from visual taste.

```python
from matplotlib.colors import Normalize, LogNorm, PowerNorm, SymLogNorm, TwoSlopeNorm, BoundaryNorm
```

- `Normalize`: linear values with moderate range
- `LogNorm`: positive values spanning orders of magnitude
- `PowerNorm`: use sparingly and only when gamma correction is justified
- `TwoSlopeNorm(vcenter=0)`: signed data where zero is meaningful
- `SymLogNorm`: signed values spanning orders of magnitude around zero
- `BoundaryNorm`: discrete bins or classes

Robust limits are acceptable only when outliers are not the scientific focus:

```python
import numpy as np
vmin, vmax = np.nanpercentile(data, [1, 99])
```

Do not clip silently if extrema matter scientifically.

## Colorbars

- Every colorbar needs a label with units where applicable.
- Keep colorbars compact.
- Use shared normalization and shared colorbars for truly comparable panels.
- Use `extend="min"`, `"max"`, or `"both"` when the plotted range is clipped.

```python
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Intensity (a.u.)")
cbar.ax.tick_params(width=1.0, size=2.2, labelsize=6)
cbar.outline.set_linewidth(1.0)
```

## Export policy

- Supply line art, graphs, charts, and schematics as vector files such as PDF/EPS/AI when possible. Do not flatten vector line art into bitmap images.
- If line art cannot be supplied as vector, export it at 1,200 dpi and at final page size.
- Supply photographic and bitmapped image panels as TIFF at 300 dpi or higher, close to final page size.
- Use 600 dpi for raster-heavy scientific figures when practical, but never below 300 dpi for final bitmap output.
- Provide bitmap images in RGB color. If the journal upload system rejects alpha-channel PNG/TIFF files, convert them to RGB after export.
- Keep text editable with `pdf.fonttype=42` and `svg.fonttype="none"`.
- Rasterize only dense artists, never labels, panel letters, legends, arrows, or scale bars.
- For microscopy/image figures, keep scale bars, ROI boxes, arrows, and labels as vector overlays over the raster image.
- Keep the thinnest final line art at least 1 pt wide.

```python
fig.savefig("figure.pdf")
fig.savefig("figure.svg")
fig.savefig("figure.tif", dpi=600)
```

## Lettering, units, and legends

- Keep figure lettering lower-case except the first letter of labels where grammar requires capitalization.
- Use SI units and leave one space between numbers and units.
- Use `ms`, not `msec`; spell out unusual units or abbreviations in the legend.
- Use comma separators for thousands, for example `1,000`.
- Prefer visual cues in legends over prose such as "open red triangles"; make line style, marker shape, and color identifiable.
- Figure legends should begin with a brief title sentence, describe what is shown in each panel, define symbols and scale-bar lengths, and stay under 350 words.

## Code-editing policy

When rewriting user code:

1. Preserve variable names and scientific calculations unless clearly broken.
2. Isolate style changes into a style block or helper function when practical.
3. Do not add new dependencies unless requested or already available in the working environment.
4. Keep the solution Matplotlib-native unless the project already requires another plotting stack.
5. Add missing labels, units, colorbars, panel labels, scale bars, and export commands.
6. Avoid optimizing for one monitor or notebook display at the expense of print readability.
