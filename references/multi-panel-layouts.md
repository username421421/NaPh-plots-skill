# Multi-panel layouts

Use this file for any figure with more than one panel, shared colorbars, inset axes, mixed plot+image layouts, panel labels, or complex GridSpec/subplot_mosaic arrangements.

Assume `style-foundation.md` is already loaded.

## Core layout rule

A multi-panel figure must read as one coherent scientific figure, not several separate plots pasted together.

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

## Panel labels

Use lower-case bold panel labels and keep placement consistent.

```python
for label, ax in zip("abc", axes.flat):
    ax.text(
        -0.16, 1.06, label,
        transform=ax.transAxes,
        fontsize=8,
        fontweight="bold",
        va="top",
        ha="left",
    )
```

Prefer placement just outside the upper-left of each panel. If a label must go inside an image, put it in unused high-contrast space.

## Figure widths for multi-panel work

- single-column: 3.50 in
- one-and-a-half-column: 4.72-5.35 in
- double-column: 7.20 in
- keep total height under about 6.69 in when possible

## Shared axes and shared colorbars

- Share axes when direct comparison benefits from identical scales.
- Share colorbars only when the underlying normalization is intentionally identical.
- Keep colorbars aligned and compact.

## Layout patterns

Simple side-by-side panels:

```python
fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), constrained_layout=True)
```

Complex layout with `GridSpec`:

```python
fig = plt.figure(figsize=(7.2, 4.6), constrained_layout=True)
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
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.4", lw=0.5)
```

Rules:

- Keep inset tick labels readable.
- Use inset connectors only when they improve clarity.
- Avoid more than one inset per panel unless the science demands it.

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
