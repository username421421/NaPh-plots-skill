---
name: nature-photonics-plotting
description: >-
  Use this skill whenever generating, editing, or reviewing Python/Matplotlib
  code for publication-grade Nature Photonics-style scientific figures:
  photonics plots, spectra, PSF/intensity maps, heat maps, phase maps,
  histograms, box/violin plots, bar charts, scatter/density plots, image
  panels, contour plots, vector fields, polar plots, multi-panel figures, and
  export workflows. Do not use for decorative business graphics unless the user
  explicitly asks for journal-style scientific plotting.
---

# Nature Photonics-style Matplotlib plotting skill

## Purpose

Produce restrained, compact, technically correct scientific figures with a Nature Photonics / Nature Portfolio aesthetic. Preserve the scientific content. Improve presentation, readability, normalization, color choices, layout, labels, and export settings.

This skill should be applied to any plotting task involving photonics, optics, nanophotonics, microscopy, spectroscopy, simulation outputs, experimental data, statistical comparisons, or paper-ready scientific visualization.

When the user asks for “Nature”, “Nature Photonics”, “publication quality”, “journal figure”, “paper figure”, “scientific plot”, “PSF”, “heat map”, “spectra”, “far field”, “near field”, “phase”, “mode profile”, “histogram”, “box plot”, “violin plot”, or “multi-panel figure”, use this skill automatically.

## Core design principles

1. **Clarity first.** Every styling decision must make the data easier to read.
2. **Compact final-size design.** Assume the figure will be read at journal column width, not full-screen notebook width.
3. **Restrained color.** Use color to encode meaning, not decoration.
4. **Vector-first export.** Keep text, axes, line art, and annotations editable whenever possible.
5. **Perceptual correctness.** Use perceptually ordered colormaps and appropriate normalization.
6. **Reproducibility.** Generate deterministic, reusable Matplotlib code.
7. **No scientific mutation.** Do not change data processing, statistics, normalization semantics, or units unless the user asks or the original code is clearly wrong.

## Required first actions when editing user code

Before changing code, infer the plot category:

- 1D data: line, spectrum, response curve, error bars, uncertainty band, fitted curve.
- Point data: scatter, parity plot, calibration curve, residual plot.
- Statistical distribution: histogram, ECDF, KDE/density, box plot, violin plot, beeswarm/jitter plot.
- Categorical summary: bar, grouped bar, stacked bar, point estimate with CI.
- 2D scalar field: heat map, PSF, near-field intensity, far-field pattern, mode profile, phase, residual map.
- 2D coordinates: pcolormesh, contourf, contour, tricontour, irregular mesh.
- Imaging: microscopy, SEM/TEM/AFM/optical micrograph, annotated image, scale bar.
- Vector/tensor field: quiver, streamplot, polarization ellipse, orientation map.
- Spectral/time-frequency: spectrogram, waterfall, dispersion, band diagram.
- Geometric/angular: polar/radar, angular emission pattern, radiation lobe.
- 3D: surface, wireframe, volumetric projection. Avoid 3D unless scientifically necessary.
- Multi-panel: combined figure with panel labels and consistent visual language.

Then apply the relevant recipe from `references/plot_type_recipes.md`.

## Default Nature Photonics style

Prefer this rcParams block unless the repository already has a stricter local standard. Keep the skill dependency-light and Matplotlib-native; do not route through SciencePlots for this skill.

```python
import matplotlib as mpl
from cycler import cycler

NATURE_PHOTONICS_COLORS = [
    "#1B3B6F",  # deep blue
    "#D55E00",  # orange
    "#007C73",  # teal
    "#B2479A",  # magenta
    "#C99A00",  # gold
    "#4D4D4D",  # dark gray
    "#56B4E9",  # sky blue
    "#000000",  # black
]

mpl.rcParams.update({
    # Figure geometry
    "figure.figsize": (3.5, 2.4),        # ~89 mm single column
    "figure.dpi": 150,                   # notebook display only
    "figure.constrained_layout.use": True,

    # Export
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
    "savefig.transparent": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",

    # Typography
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 6,
    "axes.labelsize": 7,
    "axes.titlesize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",

    # Axes, ticks, and lines
    "axes.linewidth": 0.6,
    "axes.labelpad": 2.0,
    "lines.linewidth": 1.2,
    "lines.markersize": 3.5,
    "lines.markeredgewidth": 0.6,
    "patch.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.minor.width": 0.45,
    "ytick.minor.width": 0.45,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "xtick.minor.size": 1.5,
    "ytick.minor.size": 1.5,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.top": False,
    "ytick.right": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,

    # Legends
    "legend.frameon": False,
    "legend.handlelength": 1.6,
    "legend.handletextpad": 0.4,
    "legend.borderaxespad": 0.3,
    "legend.labelspacing": 0.25,
    "legend.columnspacing": 0.8,

    # Images and colors
    "image.cmap": "viridis",
    "image.interpolation": "none",
    "axes.prop_cycle": cycler(color=NATURE_PHOTONICS_COLORS),
})
```

## Figure size rules

Use inches internally.

```python
FIG_SIZES = {
    "single": (3.5, 2.4),      # 89 mm wide
    "one_half": (5.2, 3.2),    # ~132 mm wide
    "double": (7.2, 4.6),      # 183 mm wide
    "square_single": (3.5, 3.5),
    "tall_single": (3.5, 4.2),
    "wide_double": (7.2, 3.2),
}
```

- Use `single` for simple line plots, small statistical plots, and one heat map.
- Use `one_half` for two panels side by side with a shared colorbar.
- Use `double` for multi-panel figures, spectra + image panels, or plots with long labels.
- Keep height compact. Avoid empty vertical space.
- Design at final size; do not create huge plots and shrink later.

## Color rules

### Non-negotiable restrictions

- Do not use `jet`, `rainbow`, `hsv`, `turbo`, or arbitrary rainbow gradients for scalar scientific data.
- Do not encode primary comparisons using red-vs-green alone.
- Do not use pastel colors for thin lines unless the data are background references.
- Do not use heavy gray grids or colored backgrounds.

### Recommended categorical line colors

```python
NATURE_PHOTONICS_COLORS = [
    "#1B3B6F",  # deep blue
    "#D55E00",  # orange
    "#007C73",  # teal
    "#B2479A",  # magenta
    "#C99A00",  # gold
    "#4D4D4D",  # dark gray
    "#56B4E9",  # sky blue
    "#000000",  # black
]
```

### Colormap selection

Use colormaps by data semantics:

- Positive scalar magnitude: `viridis`, `cividis`.
- Optical intensity / PSF / near-field magnitude: `magma`, `inferno`.
- Log-scale positive intensity: `magma` or `inferno` with `LogNorm`.
- Signed residual / difference / error: `RdBu_r`, `coolwarm`, `seismic` only if center is exact zero.
- Phase on a cyclic domain: `twilight`, `twilight_shifted`, or `hsv` only for true cyclic phase, never for magnitude.
- Discrete class/bin map: `ListedColormap` + `BoundaryNorm`.
- Binary mask: `gray`, `Greys`, or a two-color `ListedColormap`.

## Normalization rules

Choose normalization based on physical interpretation, not aesthetics.

```python
from matplotlib.colors import Normalize, LogNorm, PowerNorm, SymLogNorm, TwoSlopeNorm, BoundaryNorm
```

- `Normalize`: linear values with moderate range.
- `LogNorm`: positive values over orders of magnitude, especially PSF/intensity fields.
- `PowerNorm(gamma=...)`: positive maps where gamma correction is explicitly useful; avoid unless justified.
- `TwoSlopeNorm(vcenter=0)`: signed data where zero is meaningful but magnitudes are asymmetric.
- `SymLogNorm(linthresh=...)`: signed values spanning orders of magnitude around zero.
- `BoundaryNorm`: discrete bins, classification, thresholded regimes.

For robust limits, use percentiles only when outliers visually dominate and are not the scientific focus:

```python
import numpy as np
vmin, vmax = np.nanpercentile(data, [1, 99])
```

For PSF-like data:

```python
positive = np.asarray(psf, float)
floor = max(np.nanmax(positive) * 1e-4, np.nanmin(positive[positive > 0]))
norm = LogNorm(vmin=floor, vmax=np.nanmax(positive))
```

Never apply percentile clipping silently if the extrema are scientifically important.

## Plot-type recipes

Read `references/plot_type_recipes.md` for full recipes. Key defaults:

### Line / spectrum / response curve

- `lw=1.2–1.5`
- no markers unless sample points matter
- 4–6 major ticks per axis
- no title unless the panel is standalone
- use SI units in labels

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4))
ax.plot(x, y, lw=1.3, color="#1B3B6F")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Transmission")
```

### Error bars / uncertainty bands

- error bars: `elinewidth=0.8`, `capsize=2`, `capthick=0.8`
- uncertainty band: `alpha=0.16–0.25`, no edge

```python
ax.errorbar(x, y, yerr=err, fmt="o", ms=3.2, lw=0,
            elinewidth=0.8, capsize=2, capthick=0.8)
ax.plot(x, yfit, lw=1.3)
```

### Scatter / parity / calibration

- `s=12–20`, `linewidths=0.3–0.5`, `alpha=0.75–0.9`
- use an equal aspect and reference line for parity plots
- avoid huge markers

### Histograms

- use a neutral filled histogram with thin edge
- choose binning deliberately (`bins="fd"`, explicit bins, or domain-specific bin width)
- overlay density/fit only if meaningful

```python
ax.hist(values, bins="fd", density=False, color="#4D4D4D",
        alpha=0.82, edgecolor="white", linewidth=0.35)
```

### Box plots / violin plots

- prefer box/violin for distributions, not bar plots of means
- show median and data points when sample size is small
- use muted fills and black/gray outlines
- avoid decorative gradients
- for experiment-vs-simulation box plots, use the dedicated recipe in `references/plot_type_recipes.md`

### Bar charts

- use only for categorical summaries, not continuous distributions
- show error bars or individual data points when reporting experimental replicates
- keep bars narrow with neutral edges

### Heat maps / 2D fields

- regular grids: `imshow`
- explicit rectangular grids: `pcolormesh`
- irregular grids: `tricontourf` / `tripcolor`
- meaningful contours: `contour` or `contourf`
- colorbar must be compact and labeled

### PSF/intensity maps

- `cmap="magma"` or `"inferno"`
- `origin="lower"`, `aspect="equal"`
- `LogNorm` for high dynamic range
- label colorbar `Intensity (a.u.)`, `|E|² (a.u.)`, or the physical quantity
- add scale bar if physical axis units are not explicit

### Phase maps

- wrapped phase: cyclic colormap, ticks at `-π, 0, π`
- signed unwrapped phase/residual: diverging colormap centered at zero
- never use sequential maps for signed phase residuals

### Contour plots

- use thin contour lines `linewidths=0.5–0.7`
- use 6–10 levels unless more are scientifically needed
- label only important contours

### Polar plots

- use for angular emission, radiation patterns, polarization response
- reduce grid visibility
- annotate units and angular convention
- keep radial ticks sparse

### 3D plots

- avoid if 2D color map or contour plot communicates the result better
- if used, remove pane fill, reduce grid, use orthographic projection when available, and export at high DPI

## Multi-panel figures

Use consistent panel labels and shared style.

```python
for label, ax in zip("abc", axes.flat):
    ax.text(-0.16, 1.06, label, transform=ax.transAxes,
            fontsize=8, fontweight="bold", va="top", ha="left")
```

Rules:

- lower-case bold panel labels: `a`, `b`, `c`, ...
- align labels and axes
- match axis limits where comparison matters
- use shared colorbars for comparable heat maps
- avoid per-panel titles if captions/panel labels suffice
- keep whitespace minimal but not crowded
- use `GridSpec` for complex layouts

## Multi-panel figures and subplot labelling — Nature Photonics style

Use this section whenever generating, editing, or reviewing figures with more than one panel, subplot, image, heat map, schematic, microscopy panel, PSF panel, spectrum, boxplot, or mixed experimental/simulation layout.

### Core multi-panel design rule

A multi-panel figure must look like one coherent scientific figure, not several independent plots pasted together.

Prioritize:
- compact, space-efficient arrangement
- consistent typography
- consistent stroke widths
- consistent tick sizes
- consistent colorbar style
- consistent panel-label placement
- logical left-to-right, top-to-bottom reading order
- minimal white space
- aligned axes, labels, and image boundaries
- shared axes and shared colorbars where scientifically appropriate

Avoid:
- random panel sizes
- inconsistent subplot spacing
- oversized panel gaps
- misaligned image panels
- repeated redundant legends
- repeated redundant colorbars
- per-panel titles when panel labels and captions are sufficient
- uppercase panel labels unless the user explicitly requests them
- placing labels directly over data or images when avoidable
- exporting each subplot separately for final manuscript use

### Figure dimensions

Generate figures at the intended final print size.

Recommended final widths:
- single-column: 89 mm = 3.50 in
- one-and-a-half-column: 120-136 mm = 4.72-5.35 in
- double-column: 183 mm = 7.20 in

Recommended maximum final height:
- keep under 170 mm = 6.69 in when possible

Default sizes:
```python
SINGLE_COL = 3.50
ONE_HALF_COL = 5.20
DOUBLE_COL = 7.20
MAX_HEIGHT = 6.69
```

## Colorbar rules

- Every colorbar must have a label with units where applicable.
- Use compact padding: `pad=0.02–0.04`.
- Use small tick labels matching axes.
- Avoid oversized colorbars.
- Use `extend="min"`, `"max"`, or `"both"` when data are clipped.
- For comparable panels, use identical `norm`, `vmin`, and `vmax`.

```python
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Intensity (a.u.)")
cbar.ax.tick_params(width=0.6, size=2.2, labelsize=6)
cbar.outline.set_linewidth(0.6)
```

## Export policy

Always include export commands in generated final scripts unless the user asks for interactive-only code.

```python
fig.savefig("figure.pdf")              # preferred for vector/mixed figures
fig.savefig("figure.svg")              # editable vector, useful for layout tools
fig.savefig("figure.png", dpi=600)     # raster fallback
```

Rules:

- PDF/SVG for line art and mixed vector figures.
- PNG/TIFF at 600 dpi for raster-heavy plots.
- Keep text editable: `pdf.fonttype=42`, `svg.fonttype="none"`.
- Use `bbox_inches="tight"`, `pad_inches=0.02` if not set globally.
- Rasterize only heavy artists, not text or axes.

Example:

```python
mesh = ax.pcolormesh(X, Y, Z, cmap="viridis", shading="auto", rasterized=True)
fig.savefig("field_map.pdf")
```

## Code-editing policy

When rewriting user code:

1. Preserve variable names and scientific calculations unless clearly broken.
2. Isolate style changes into helper functions or a style block.
3. Do not add new dependencies unless the user requested them or they already exist.
4. Use Matplotlib and NumPy as the default stack. Avoid seaborn unless the project already uses it and the user wants it.
5. Keep the solution Matplotlib-native unless the user explicitly requires a different plotting dependency that is already part of the repository.
6. Replace poor colormaps and weak normalization choices.
7. Add missing labels, units, colorbars, panel labels, and export commands.
8. Avoid overfitting to a single monitor/notebook display.
9. If data ranges are unknown, choose semantically safe defaults and leave comments where the user should set physical limits.
10. For publication scripts, prefer explicit `fig, ax = plt.subplots(...)` over stateful pyplot.

## Review checklist before final answer

Before returning code, check:

- [ ] Does figure size match single/one-half/double-column needs?
- [ ] Are fonts 5–7 pt scale at final size, with sans-serif family?
- [ ] Are axes, lines, markers, ticks, and legends compact?
- [ ] Are labels concise and units included?
- [ ] Are colormaps semantically correct and not rainbow/jet?
- [ ] Is normalization appropriate for positive, signed, logarithmic, or discrete data?
- [ ] Are colorbar labels and ticks present and compact?
- [ ] Are panel labels lower-case bold and aligned?
- [ ] Are export settings vector-first with editable text?
- [ ] Is no scientific data transformation changed accidentally?

## Files in this skill

- `assets/nature_photonics.mplstyle`: a reusable Matplotlib style sheet.
- `scripts/np_plot_style.py`: helper functions for applying style, sizing figures, box-plot presets, adding panel labels, robust limits, colorbars, and scale bars.
- `scripts/style_qa.py`: static lint-style checks for common plotting mistakes.
- `references/plot_type_recipes.md`: detailed recipes for scientific plot families.
- `references/review_checklist.md`: stricter QA checklist and anti-patterns.
- `references/sources.md`: source references and rationale.

When the task is complex or asks for “all scientific plots”, read `references/plot_type_recipes.md` first. For box plots, grouped distributions, or experiment-vs-simulation overlays, use the dedicated box-plot recipe there rather than a generic statistical-plot recipe.
