# Multi-panel layouts

Use this file for any figure with more than one panel, shared colorbars, inset axes, mixed plot+image layouts, panel labels, or complex GridSpec/subplot_mosaic arrangements.

Assume `style-foundation.md` is already loaded.

## Core layout rule

A multi-panel figure must read as one coherent scientific figure, not several separate plots pasted together.

Nature Communications expects figures to be one- or two-column display items. Do not make a multipart figure unless the parts are logically connected, and size each panel so the whole figure can be reduced by the same amount while preserving essential details.

Prioritize:

- compact, space-efficient arrangement
- consistent typography
- consistent stroke widths
- consistent tick sizes
- consistent colorbar style
- aligned axes, labels, and image boundaries
- logical reading order

Avoid:

- random panel sizes
- inconsistent spacing
- oversized gaps
- repeated redundant legends or colorbars
- per-panel titles when panel labels and caption are sufficient
- unrelated panels grouped only to save figure count
- decorative panel boxes or heavy outer frames

## Panel labels

Use lower-case bold panel labels and keep placement consistent. Use 8 pt panel
labels after matching the generated figure width to the intended LaTeX display
width. Only apply generated-width / display-width compensation when an existing
script cannot be resized to its LaTeX display width.

```python
from np_plot_style import panel_label_fontsize

panel_fs = panel_label_fontsize(total_width_in=fig_width)
for label, ax in zip("abc", axes.flat):
    ax.text(
        -0.16, 1.06, label,
        transform=ax.transAxes,
        fontsize=panel_fs,
        fontweight="bold",
        va="top",
        ha="left",
    )
```

Prefer placement just outside the upper-left of each panel. If a label must go inside an image, put it in unused high-contrast space.

## Figure widths for multi-panel work

- Nature Communications single-column final width: 88 mm = 3.4646 in
- Nature Communications double-column final width: 180 mm = 7.0866 in
- intermediate widths should be used only when matching a review/manuscript LaTeX insertion size
- keep total height under about 6.69 in when possible

## LaTeX-matched width for multi-panel figures

Generate the multi-panel figure at the exact width it will occupy in LaTeX so all panels have the same displayed font size in the compiled PDF.

- Use the full figure width in `figsize`, not the width of one panel.
- Unless the user explicitly says otherwise, assume the figure is inserted as `\textwidth` and use a 6.5 in text width if the actual manuscript text width is unknown.
- If the user says the whole multi-panel figure will be inserted smaller than full text width, compute the generated figure width from that insertion fraction; for example, `0.8\textwidth` means `fig_width = 0.8 * page_width_in`.
- With matched widths, use unchanged 8 pt base/title/legend, 7 pt axis/tick/colorbar, and 8 pt panel labels.
- Keep all panels on one typography scale; do not let each subplot choose independent font sizes.

```python
from np_plot_style import apply_nature_style, matched_figure_width

fig_width = matched_figure_width(page_width_in=6.5)
apply_nature_style()
fig, axes = plt.subplots(2, 3, figsize=(fig_width, 4.6), constrained_layout=True)
```

If the figure will be inserted as `0.8\textwidth`, generate it at that width:

```python
fig_width = matched_figure_width(page_width_in=6.5, latex_width_fraction=0.8)
apply_nature_style()
fig, axes = plt.subplots(2, 3, figsize=(fig_width, 3.2), constrained_layout=True)
```

## Shared axes and shared colorbars

- Share axes when direct comparison benefits from identical scales.
- Share colorbars only when the underlying normalization is intentionally identical.
- Keep colorbars aligned and compact.

## Layout patterns

Simple side-by-side panels:

```python
fig, axes = plt.subplots(1, 2, figsize=(7.0866, 2.8), constrained_layout=True)
```

Complex layout with `GridSpec`:

```python
fig = plt.figure(figsize=(7.0866, 4.54), constrained_layout=True)
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.05], height_ratios=[1, 1])
ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])
ax_c = fig.add_subplot(gs[0, 2])
ax_d = fig.add_subplot(gs[1, :2])
ax_e = fig.add_subplot(gs[1, 2])
```

Use `subplot_mosaic` when named layout readability matters more than manual ratio tuning.

## Insets and zoom panels

Use inset axes when a local zoom is genuinely clearer than a separate panel.

```python
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

axins = inset_axes(ax, width="38%", height="38%", loc="upper right", borderpad=0.6)
axins.plot(x, y, lw=1.0, color="#1B3B6F")
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.tick_params(labelsize=5, width=0.5, length=2)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.4", lw=1.0)
```

Rules:

- Keep inset tick labels readable.
- Use inset connectors only when they improve clarity.
- Avoid more than one inset per panel unless the science demands it.

## Stacked zoom rows for profile panels

For multi-column profile comparisons where an inset would obscure data or make
curves too small, prefer a dedicated stacked zoom row above the full profile row.
This is better for PSF line cuts, spectra with weak side lobes, tails,
low-intensity shoulders, or any distribution where the main peak hides the
secondary structure.

Use this pattern:

- Put the zoomed axis directly above the corresponding full-range axis.
- Keep each zoom axis the same width and horizontal position as its full axis.
- Use the same x limits for the zoom and full axes in each column.
- Hide x tick labels and x-axis labels on the zoom row; put the coordinate label only on the full row below.
- Give the zoom row its own y limits and y tick labels. Per-column y caps are acceptable when the detail scale differs.
- Omit the zoom-row vertical axis label unless it is necessary. If used, keep it short.
- Use the same curve colors, line styles, and stroke widths as the full plot.
- Use one shared legend for the full profile family, not one legend per zoom panel.
- Increase the figure height rather than squeezing the heat maps, colorbar, or full profile axes.

Example structure:

```python
mosaic = [
    ["map_a", "map_b", "map_c"],
    ["cbar", "cbar", "cbar"],
    ["zoom_a", "zoom_b", "zoom_c"],
    ["profile_a", "profile_b", "profile_c"],
    ["legend", "legend", "legend"],
]
fig, axes = plt.subplot_mosaic(
    mosaic,
    figsize=(fig_width, taller_height),
    gridspec_kw={"height_ratios": [1.0, 0.08, 0.34, 0.62, 0.16]},
)

for zoom_ax, profile_ax, xlim, zoom_ylim in profile_pairs:
    zoom_ax.plot(x, y1, color=color1, ls="-")
    zoom_ax.plot(x, y2, color=color2, ls="--")
    profile_ax.plot(x, y1, color=color1, ls="-")
    profile_ax.plot(x, y2, color=color2, ls="--")
    zoom_ax.set_xlim(xlim)
    profile_ax.set_xlim(xlim)
    zoom_ax.set_ylim(zoom_ylim)
    profile_ax.set_ylim(full_ylim)
    zoom_ax.tick_params(labelbottom=False)
```

## Legends, direct labels, and annotation

- Prefer direct labels for two or three curves if they do not clutter the panel.
- Keep legends short and unboxed unless a box is genuinely needed for readability.
- Keep arrows and callouts thin and sparse.

Minimal legend:

```python
ax.legend(
    loc="best",
    frameon=False,
    handlelength=1.5,
    handletextpad=0.4,
    borderaxespad=0.3,
    labelspacing=0.25,
)
```

## Family checklist

- Panel labels are lower-case bold and aligned.
- Panel spacing is consistent and compact.
- Shared axes and colorbars are used only when scientifically appropriate.
- Insets are justified and clearly tied to the parent panel.
- Mixed plot+image panels use one coherent visual language.
