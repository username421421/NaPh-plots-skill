# Curves and scatter plots

Use this file for line plots, spectra, response curves, error bars, scatter plots, parity plots, residual plots, calibration plots, dense point clouds, and log-scale line plots.

Assume `style-foundation.md` is already loaded.

## Line, spectrum, and response curves

Defaults:

- `lw=1.2-1.5`
- no markers unless individual sample points matter
- 4-6 major ticks per axis
- no title unless the panel is standalone
- use concise axis labels with units

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.plot(wavelength_nm, transmission, lw=1.3, color="#1B3B6F", label="Measured")
ax.plot(wavelength_nm, simulation, lw=1.1, color="#D55E00", ls="--", label="Simulated")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Transmission")
```

For measured points plus a fit:

```python
ax.plot(xfit, yfit, lw=1.3, color="#1B3B6F", label="Fit")
ax.plot(x, y, "o", ms=3.2, mfc="white", mec="#1B3B6F", mew=0.6, label="Data")
```

Avoid:

- `linewidth > 2` at single-column width
- markers on every point of a dense spectrum
- random default colors when trace identity matters

## Error bars and confidence bands

```python
ax.errorbar(
    x, y, yerr=yerr,
    fmt="o", ms=3.2, mfc="white", mec="#1B3B6F", mew=0.6,
    ecolor="#1B3B6F", elinewidth=0.8, capsize=2.0, capthick=0.8,
    lw=0, zorder=3,
)
```

```python
ax.plot(x, mean, lw=1.3, color="#1B3B6F")
ax.fill_between(x, lower, upper, color="#1B3B6F", alpha=0.18, linewidth=0)
```

Rules:

- Identify SD, SEM, CI, or fit uncertainty correctly in labels or caption.
- For small `n`, show individual points when possible.
- Keep uncertainty bands light and secondary to the main curve.

## Scatter, parity, residual, and calibration plots

Defaults:

- `s=12-20`
- `alpha=0.75-0.9`
- `linewidths=0.3-0.5`
- rasterize for very dense scatter in vector output

```python
fig, ax = plt.subplots(figsize=(3.0, 3.0), constrained_layout=True)
ax.scatter(x, y, s=16, color="#1B3B6F", alpha=0.82, linewidths=0,
           rasterized=(len(x) > 20000))
ax.set_xlabel("Measured Q")
ax.set_ylabel("Predicted Q")
```

Parity plot:

```python
lims = [min(np.nanmin(x), np.nanmin(y)), max(np.nanmax(x), np.nanmax(y))]
ax.plot(lims, lims, color="0.25", lw=0.8, ls="--", zorder=1)
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_aspect("equal", adjustable="box")
```

Residual plot:

```python
ax.axhline(0, color="0.25", lw=0.8, ls="--", zorder=1)
ax.scatter(x, residual, s=14, color="#4D4D4D", alpha=0.85, linewidths=0)
```

## Dense clouds: 2D histogram and hexbin

Use these when raw scatter overplots.

```python
h = ax.hist2d(x, y, bins=80, cmap="viridis", norm=LogNorm())
cbar = fig.colorbar(h[3], ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Counts")
```

```python
hb = ax.hexbin(x, y, gridsize=45, bins="log", cmap="viridis", mincnt=1)
cbar = fig.colorbar(hb, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Counts")
```

## Log-scale line plots

Use when the plotted quantity spans orders of magnitude.

```python
ax.semilogy(x, y, lw=1.3, color="#1B3B6F")
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=5))
ax.yaxis.set_major_formatter(LogFormatterMathtext(base=10))
```

Rules:

- Do not pass nonpositive values to log axes without handling them explicitly.
- Keep log ticks sparse.
- Label the physical quantity, not `log(quantity)`, unless the values were transformed before plotting.

## Family checklist

- Main curves are readable at final size.
- Markers are used only when they add meaning.
- Error bars are thin and correctly described.
- Dense scatter is rasterized or converted to a density view.
- Parity plots include a `y=x` reference and equal aspect.
- Residual plots include a zero reference line.
