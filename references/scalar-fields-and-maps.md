# Scalar fields and maps

Use this file for heat maps, `imshow`, `pcolormesh`, PSF or intensity maps, phase maps, contour plots, and matrix-style visualizations such as correlation or confusion matrices.

Assume `style-foundation.md` is already loaded.

## Heat maps with `imshow`

Use for regular 2D arrays such as PSFs, near-field maps, correlation matrices, or parameter sweeps on a regular grid.

```python
fig, ax = plt.subplots(figsize=(3.5, 3.0), constrained_layout=True)
im = ax.imshow(
    Z,
    origin="lower",
    aspect="auto",
    cmap="viridis",
    extent=[x.min(), x.max(), y.min(), y.max()],
    norm=Normalize(vmin=vmin, vmax=vmax),
    interpolation="none",
)
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Signal (a.u.)")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Position (um)")
```

Rules:

- Use `aspect="equal"` when x and y share the same physical units.
- Use `extent` whenever the axes have physical coordinates.
- Keep interpolation off unless smoothing is intentional and stated.

## `pcolormesh` for explicit or nonuniform grids

```python
pcm = ax.pcolormesh(
    X, Y, Z,
    cmap="viridis",
    norm=Normalize(vmin, vmax),
    shading="auto",
    rasterized=True,
)
cbar = fig.colorbar(pcm, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Field enhancement")
```

Use `pcolormesh` when the coordinate grid is explicit or nonuniform. Do not use it for simple image arrays when `imshow` is clearer.

## PSF, mode-profile, and intensity maps

Use for Airy PSFs, simulated focal spots, near-field intensity, mode intensity, or energy density.

Linear view:

```python
im = ax.imshow(
    I,
    origin="lower",
    aspect="equal",
    cmap="magma",
    extent=[xmin, xmax, ymin, ymax],
    interpolation="none",
    norm=Normalize(vmin=0, vmax=np.nanmax(I)),
)
```

Log view:

```python
I = np.asarray(I, float)
Imax = np.nanmax(I)
positive_min = np.nanmin(I[I > 0]) if np.any(I > 0) else Imax * 1e-6
floor = max(Imax * 1e-4, positive_min)
im = ax.imshow(
    I,
    origin="lower",
    aspect="equal",
    cmap="magma",
    extent=[xmin, xmax, ymin, ymax],
    interpolation="none",
    norm=LogNorm(vmin=floor, vmax=Imax),
)
```

Rules:

- Use `magma` or `inferno`.
- Decide explicitly between linear and log scale.
- Use shared normalization when comparing fields directly.
- Add a scale bar if axes are hidden but the panel is spatial.

## Phase maps and signed residual maps

Wrapped phase:

```python
im = ax.imshow(
    phase,
    origin="lower",
    aspect="equal",
    cmap="twilight",
    extent=[xmin, xmax, ymin, ymax],
    vmin=-np.pi,
    vmax=np.pi,
    interpolation="none",
)
```

Signed residual:

```python
v = np.nanpercentile(np.abs(residual), 99)
im = ax.imshow(
    residual,
    origin="lower",
    aspect="equal",
    cmap="RdBu_r",
    norm=TwoSlopeNorm(vmin=-v, vcenter=0, vmax=v),
    interpolation="none",
)
```

Rules:

- Use cyclic maps only for cyclic variables.
- Use diverging maps for signed differences and center them on the meaningful reference value.

## Contour and contourf plots

Use when level sets have physical meaning.

```python
levels = np.linspace(vmin, vmax, 9)
cf = ax.contourf(X, Y, Z, levels=levels, cmap="viridis", extend="both")
cs = ax.contour(X, Y, Z, levels=levels[::2], colors="0.15", linewidths=0.45)
ax.clabel(cs, fmt="%.2g", fontsize=5, inline=True)
```

Rules:

- Use roughly 6-10 levels for compact figures unless the science needs more.
- Label contours sparsely.
- Do not imply false precision with excessive contour density.

## Correlation and confusion matrices

Correlation matrix:

```python
im = ax.imshow(
    C,
    cmap="RdBu_r",
    norm=TwoSlopeNorm(vmin=-1, vcenter=0, vmax=1),
    interpolation="none",
)
ax.set_xticks(np.arange(len(names)), names, rotation=45, ha="right")
ax.set_yticks(np.arange(len(names)), names)
```

Confusion matrix:

```python
im = ax.imshow(cm, cmap="Blues", interpolation="none")
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        val = cm[i, j]
        ax.text(j, i, f"{val:g}", ha="center", va="center", fontsize=5,
                color="white" if val > 0.6 * np.nanmax(cm) else "black")
```

Rules:

- Use diverging color for signed correlations.
- Use sequential color for counts or probabilities.
- Annotate values only when the matrix is small enough to remain legible.

## Family checklist

- `origin`, `extent`, `aspect`, `norm`, and `cmap` are chosen deliberately.
- Colorbars are compact and labeled.
- Shared fields use shared normalization where comparison matters.
- Spatial panels keep equal aspect unless there is a good reason not to.
- Contour and matrix annotations remain readable at final size.
