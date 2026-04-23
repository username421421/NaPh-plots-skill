# Style foundation for Nature Photonics-style scientific figures

Load this file before substantial plotting edits. Then load only the relevant figure-family file or files.

## Core design rules

- Clarity first. Every style choice must make the data easier to read.
- Design at final size, not notebook size.
- Use color semantically, not decoratively.
- Keep text, axes, line art, panel labels, arrows, and scale bars editable whenever possible.
- Use deterministic, reusable Matplotlib code.
- Do not change scientific processing unless the user asks or the existing code is clearly wrong.

## Default rcParams

Prefer this block unless the repository already has a stricter local standard.

```python
import matplotlib as mpl
from cycler import cycler

NATURE_PHOTONICS_COLORS = [
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
    "figure.figsize": (3.5, 2.4),
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
    "font.size": 6,
    "axes.labelsize": 7,
    "axes.titlesize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,
    "mathtext.fontset": "dejavusans",
    "mathtext.default": "regular",
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
    "legend.frameon": False,
    "legend.handlelength": 1.6,
    "legend.handletextpad": 0.4,
    "legend.borderaxespad": 0.3,
    "legend.labelspacing": 0.25,
    "legend.columnspacing": 0.8,
    "image.cmap": "viridis",
    "image.interpolation": "none",
    "axes.prop_cycle": cycler(color=NATURE_PHOTONICS_COLORS),
})
```

## Figure sizes

Use inches internally.

```python
FIG_SIZES = {
    "single": (3.5, 2.4),
    "one_half": (5.2, 3.2),
    "double": (7.2, 4.6),
    "square_single": (3.5, 3.5),
    "tall_single": (3.5, 4.2),
    "wide_double": (7.2, 3.2),
}
```

- `single`: simple line plots, small statistical plots, one heat map
- `one_half`: two related panels with compact labels or a shared colorbar
- `double`: multi-panel figures, mixed plot+image figures, or long labels
- Keep height compact. Avoid creating a large figure and shrinking it later.

## Color rules

- Do not use `jet`, `rainbow`, or arbitrary rainbow gradients for scalar scientific data.
- Do not encode the main comparison using red-vs-green alone.
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
cbar.ax.tick_params(width=0.6, size=2.2, labelsize=6)
cbar.outline.set_linewidth(0.6)
```

## Export policy

- Prefer PDF or SVG for line art and mixed vector figures.
- Export PNG or TIFF at 600 dpi for raster-heavy figures.
- Keep text editable with `pdf.fonttype=42` and `svg.fonttype="none"`.
- Rasterize only dense artists, never labels, panel letters, legends, arrows, or scale bars.
- For microscopy/image figures, keep scale bars, ROI boxes, arrows, and labels as vector overlays over the raster image.

```python
fig.savefig("figure.pdf")
fig.savefig("figure.svg")
fig.savefig("figure.png", dpi=600)
```

## Code-editing policy

When rewriting user code:

1. Preserve variable names and scientific calculations unless clearly broken.
2. Isolate style changes into a style block or helper function when practical.
3. Do not add new dependencies unless requested or already present in the repository.
4. Keep the solution Matplotlib-native unless the project already requires another plotting stack.
5. Add missing labels, units, colorbars, panel labels, scale bars, and export commands.
6. Avoid optimizing for one monitor or notebook display at the expense of print readability.
