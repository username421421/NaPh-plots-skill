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
- scale-bar values printed on the bar when they can instead be defined in the figure legend
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

## SEM publication figure finalizer workflow

When the user asks for a finalized annotated SEM figure, SEM comparison panel, overview plus close-up, ROI-box figure, scale-bar SEM figure, or clean Nature Communications-compatible SEM layout, generate a standalone Python script that assembles the figure.

Required behavior:

- Generate a single self-contained Python script unless the user explicitly requests modularization.
- Put all editable settings in a top-level Python dictionary named `CONFIG`.
- Do not generate YAML, JSON, TOML, or any external config file unless the user explicitly asks for one.
- Make the script ready for the user to edit and run.
- Export PDF, SVG, PNG, and optionally TIFF.
- Use `numpy`, `matplotlib`, and `Pillow`; avoid extra dependencies unless there is a clear need.

Expected script structure:

- imports
- top-level `CONFIG` dictionary
- image loading helpers
- global normalization helpers
- scale-bar helper
- annotation helper
- panel rendering logic
- figure assembly logic
- export logic
- `main()` function

Use a configuration pattern like:

```python
CONFIG = {
    "output_basename": "final_sem_figure",
    "dpi": 600,
    "figure_width_mm": 180,
    "formats": ["pdf", "svg", "png", "tiff"],
    "font_family": "Arial",
    "font_size_pt": 7,
    "panel_label_size_pt": 8,
    "page_width_in": 6.5,
    "latex_width_fraction": 1.0,
    "processing": {
        "contrast_percentiles": None,
        "invert": False,
    },
    "panels": [
        {
            "id": "a",
            "image_path": "sem_overview.tif",
            "pixel_size_nm": 4.8,
            "crop_px": None,
            "scale_bar_um": 2,
            "title": None,
            "annotations": [
                {"type": "box", "xywh_px": [700, 500, 300, 220]},
            ],
        },
        {
            "id": "b",
            "image_path": "sem_closeup.tif",
            "pixel_size_nm": 0.85,
            "crop_px": None,
            "scale_bar_nm": 200,
            "title": None,
            "annotations": [
                {
                    "type": "arrow",
                    "start_px": [540, 390],
                    "end_px": [470, 330],
                    "text": "nanogap",
                },
            ],
        },
    ],
}
```

Figure requirements:

- Load one or more SEM images.
- Convert to grayscale for display.
- Optionally crop panels.
- Optionally create overview plus zoom or separate higher-magnification close-up panels.
- Add lower-case bold panel labels: `a`, `b`, `c`, ...
- Add calibrated scale bars.
- Add optional ROI rectangles, arrows, and short text labels.
- Arrange panels in a clean publication layout with consistent gutters and alignment.
- Keep all annotations minimal, high-contrast, and scientifically necessary.
- Match the generated SEM figure width to the intended LaTeX display width, as
  with plots. With matched widths, use the configured annotation and panel-label
  font sizes unchanged unless the user explicitly asks for smaller SEM-only
  annotation text.
- For final Nature Communications production files, use 88 mm or 180 mm figure
  width and export bitmap-heavy panels as RGB TIFF at 300 dpi or higher.

## Scale bars

- Use scale bars instead of magnification factors.
- Scale bars must come from direct calibration, preferably `pixel_size_nm`, or another explicit pixel-to-length calibration.
- Do not infer scale from magnification text alone.
- If calibration is missing, raise an error or clearly state that scale-bar generation cannot proceed.
- Nature Communications asks that the scale-bar length be defined in the figure legend rather than on the bar itself. Omit in-panel scale-bar text by default; add it only if the user explicitly requests an in-panel label or the figure will be used outside the manuscript legend.
- Keep scale bars crisp, simple, and visually secondary.
- Prefer white bars with subtle black outline or path effect for contrast.
- Place scale bars near lower-right or lower-left unless the image content requires otherwise.
- Use the same font, line thickness, and placement logic across the figure.
- Any panel with a distinct pixel scale should normally have its own scale bar.
- If the user does not specify a scale-bar length, choose a visually reasonable length from the calibrated field of view.

Basic panel:

```python
fig, ax = plt.subplots(figsize=(3.4646, 3.0), constrained_layout=True)
ax.imshow(img, cmap="gray", interpolation="none")
ax.set_axis_off()
```

Anchored scale bar:

```python
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm

fontprops = fm.FontProperties(size=7)
scalebar = AnchoredSizeBar(
    ax.transData,
    length_px,
    "",
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
- Allowed processing is limited to grayscale loading/conversion, global brightness adjustment, global contrast normalization, optional percentile normalization, cropping, layout composition, and annotation overlays.
- Apply brightness and contrast changes only to the whole image, not to local regions.
- Apply comparable tonal treatment across control or comparison images when appropriate.
- If juxtaposing different images is essential, keep them clearly separate and say so in the legend.
- Do not fabricate scale bars without direct calibration input.

## Caption expectations

For microscopy and SEM figures, the legend should:

- identify each panel in order
- state what each panel shows
- specify what region is enlarged if a zoom is included
- state scale-bar values for relevant panels
- define scale-bar values in the legend rather than relying on in-panel scale-bar text
- disclose if panels came from different samples, devices, or acquisitions when that matters
- disclose any rotation, mirroring, montage, or special image processing when relevant

## Family checklist

- Every panel that needs one has a scale bar.
- Text and scale bars remain editable overlays.
- Annotation is minimal and high contrast.
- Comparative panels use consistent orientation and tonal treatment.
- Zoom regions are explicit.
- No local retouching or content removal is implied.
