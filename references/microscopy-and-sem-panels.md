# Microscopy and SEM panels

Use this file for microscopy image panels, SEM, FESEM, STEM, TEM, AFM-like panels, optical micrographs, overview+zoom figures, and mixed image+plot figures that include microscopy imagery.

Assume `style-foundation.md` is already loaded.

## Core intent

Microscopy panels must look clean, honest, compact, and editorially polished.

Prioritize:

- clear image provenance
- minimal but legible annotation
- scale-aware presentation
- consistent panel styling
- editable text and vector overlays
- high image integrity

Avoid:

- decorative effects
- thick borders
- colored labels
- magnification text instead of scale bars
- flattened text or flattened scale bars
- cluttered annotation
- ambiguous zoom regions
- screenshot-like layouts

## Global image-panel rules

- Use grayscale by default unless false color is scientifically necessary.
- Remove x/y axes and ticks unless coordinates are scientifically necessary.
- Use only black or white annotation text depending on local contrast.
- Keep orientation consistent across comparable panels when possible.
- Do not rotate, mirror, or flip one comparative panel relative to another unless scientifically necessary and disclosed.
- Do not overcrop; preserve enough context for interpretation.

## Scale bars

- Use scale bars instead of magnification factors.
- Put the scale-bar value directly with the bar or immediately adjacent to it.
- Keep scale bars crisp, simple, and visually secondary.
- Use the same font, line thickness, and placement logic across the figure.
- Any panel with a distinct pixel scale should normally have its own scale bar.

Basic panel:

```python
fig, ax = plt.subplots(figsize=(3.5, 3.0), constrained_layout=True)
ax.imshow(img, cmap="gray", interpolation="none")
ax.set_axis_off()
```

Anchored scale bar:

```python
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm

fontprops = fm.FontProperties(size=6)
scalebar = AnchoredSizeBar(
    ax.transData,
    length_px,
    "2 um",
    "lower right",
    pad=0.25,
    color="white",
    frameon=False,
    size_vertical=max(1, int(length_px * 0.04)),
    fontproperties=fontprops,
)
ax.add_artist(scalebar)
```

## Single-panel microscopy or SEM figures

- Keep the panel simple: image, scale bar, panel label if needed, and only essential feature labels.
- Do not add ROI boxes or connector lines unless a zoom or comparison panel exists.
- Keep local contrast generous but avoid clipped highlights and crushed shadows.

## Multiple microscopy or SEM panels

- Align outer edges and keep inter-panel gaps consistent.
- Use equal-sized panels when they carry equal conceptual weight.
- Keep font, panel-label style, scale-bar style, and annotation style consistent.
- Do not make separate acquisitions look like one continuous image.
- If panels come from different samples, devices, fields of view, or acquisition sessions, keep them clearly separate and make that clear in the legend when needed.

## Overview + zoom / inset figures

- Mark the zoom source on the overview image with a thin ROI box or inset frame.
- Use connector lines only when they clarify the relationship.
- Keep overview and zoom at the same orientation when possible.
- Give the zoomed panel its own scale bar unless the scale is otherwise fully explicit.
- Do not draw ROI boxes when no zoom panel exists.

## Mixed image + non-image figures

When microscopy panels appear beside plots, heat maps, or schematics:

- keep typography identical across all panels
- keep panel-label positions visually consistent
- avoid oversized image annotations that overpower quantitative panels
- use `GridSpec` or `subplot_mosaic` when panel sizes differ

## Image integrity rules

- Do not use healing, cloning, content-aware, remove, or generative tools on image data.
- Do not obscure, invent, or erase image features.
- Apply brightness and contrast changes only to the whole image, not to local regions.
- Apply comparable tonal treatment across control or comparison images when appropriate.
- If juxtaposing different images is essential, keep them clearly separate and say so in the legend.

## Caption expectations

For microscopy and SEM figures, the legend should:

- identify each panel in order
- state what each panel shows
- specify what region is enlarged if a zoom is included
- state scale-bar values for relevant panels
- disclose if panels came from different samples, devices, or acquisitions when that matters
- disclose any rotation, mirroring, montage, or special image processing when relevant

## Family checklist

- Every panel that needs one has a scale bar.
- Text and scale bars remain editable overlays.
- Annotation is minimal and high contrast.
- Comparative panels use consistent orientation and tonal treatment.
- Zoom regions are explicit.
- No local retouching or content removal is implied.
