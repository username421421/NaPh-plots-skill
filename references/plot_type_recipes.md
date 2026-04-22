# Plot-type recipes for Nature Photonics-style scientific figures

Use these recipes when generating or editing Matplotlib code. The common visual language is: compact figure, white background, sans-serif labels, thin axes, restrained line widths, small markers, semantically correct colors, no decorative grid, vector-first export.

## 1. Shared utility patterns

### Imports

```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LogNorm, PowerNorm, SymLogNorm, TwoSlopeNorm, BoundaryNorm, ListedColormap
from matplotlib.ticker import MaxNLocator, AutoMinorLocator, ScalarFormatter, LogLocator, LogFormatterMathtext
```

### Figure creation

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
```

Use these sizes:

```python
FIG_SIZES = {
    "single": (3.5, 2.4),
    "single_square": (3.5, 3.5),
    "single_tall": (3.5, 4.2),
    "one_half": (5.2, 3.2),
    "double": (7.2, 4.6),
    "double_wide": (7.2, 3.2),
}
```

### Axis finishing helper

```python
def polish_axis(ax, xlabel=None, ylabel=None, xlim=None, ylim=None, minor=True):
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if xlim is not None:
        ax.set_xlim(*xlim)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.tick_params(direction="out", width=0.6, length=2.5)
    if minor:
        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.tick_params(which="minor", direction="out", width=0.45, length=1.5)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=5, prune=None))
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5, prune=None))
    return ax
```

Use this only when it does not break log-scale axes. For log axes, use log locators instead.

## 2. Line plots, spectra, response curves

Use for wavelength spectra, transmission/reflection/absorption, power sweeps, time traces, S-parameters, efficiency curves, mode index vs wavelength, quality factor vs parameter.

Defaults:

- `lw=1.2–1.5`
- no markers for dense data
- markers only for sparse experimental points
- use `zorder=3` for main data
- axis labels with units
- legend only when direct annotation is not cleaner

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.plot(wavelength_nm, transmission, lw=1.3, color="#1B3B6F", label="Measured")
ax.plot(wavelength_nm, simulation, lw=1.1, color="#D55E00", ls="--", label="Simulated")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Transmission")
ax.legend(loc="best")
ax.tick_params(direction="out")
fig.savefig("spectrum.pdf")
```

For measured points plus fitted curve:

```python
ax.plot(xfit, yfit, lw=1.3, color="#1B3B6F", label="Fit")
ax.plot(x, y, "o", ms=3.2, mfc="white", mec="#1B3B6F", mew=0.6, label="Data")
```

Anti-patterns:

- Do not use `linewidth > 2` at single-column width.
- Do not use markers on every point of dense spectra.
- Do not include a panel title repeating the y-axis label.
- Do not use random colors from default state if traces have meaning.

## 3. Error bars and confidence intervals

Use when showing replicate measurements, fitted parameter uncertainty, calibration data, or binned means.

Defaults:

```python
ax.errorbar(
    x, y, yerr=yerr, xerr=None,
    fmt="o", ms=3.2, mfc="white", mec="#1B3B6F", mew=0.6,
    ecolor="#1B3B6F", elinewidth=0.8, capsize=2.0, capthick=0.8,
    lw=0, zorder=3, label="Experiment"
)
```

For confidence bands:

```python
ax.plot(x, mean, lw=1.3, color="#1B3B6F", label="Mean")
ax.fill_between(x, lower, upper, color="#1B3B6F", alpha=0.18, linewidth=0, label="95% CI")
```

Rules:

- Use CI/SD/SEM accurately in the label or caption.
- For small n, show individual points in addition to summary statistics.
- Use `alpha` in uncertainty bands but keep the central line fully opaque.

## 4. Scatter, parity, residual, and calibration plots

Use for measured vs predicted, simulation vs experiment, parameter correlations, fabrication variation, and calibration.

Defaults:

- `s=12–20`
- `alpha=0.75–0.9`
- `linewidths=0.3–0.5`
- avoid edge outlines for very dense scatter
- use rasterization for >20k points in PDF

```python
fig, ax = plt.subplots(figsize=(3.0, 3.0), constrained_layout=True)
ax.scatter(x, y, s=16, color="#1B3B6F", alpha=0.82, linewidths=0, rasterized=(len(x) > 20000))
ax.set_xlabel("Measured $Q$")
ax.set_ylabel("Predicted $Q$")
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

## 5. Density scatter and 2D histograms

Use for very dense point clouds where raw scatter overplots.

2D histogram:

```python
fig, ax = plt.subplots(figsize=(3.5, 2.8), constrained_layout=True)
h = ax.hist2d(x, y, bins=80, cmap="viridis", norm=LogNorm())
cbar = fig.colorbar(h[3], ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Counts")
```

Hexbin:

```python
hb = ax.hexbin(x, y, gridsize=45, bins="log", cmap="viridis", mincnt=1)
cbar = fig.colorbar(hb, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Counts")
```

Rules:

- Use log count scale for broad-density distributions.
- Do not use opaque scatter for dense clouds.
- Preserve outlier visibility when outliers matter.

## 6. Histograms

Use for distributions of linewidth, resonance wavelength, Q factor, residuals, fabrication errors, particle size, intensity values, or measurement noise.

Defaults:

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.hist(values, bins="fd", color="#4D4D4D", alpha=0.82,
        edgecolor="white", linewidth=0.35)
ax.set_xlabel("Resonance shift (nm)")
ax.set_ylabel("Count")
```

Density histogram:

```python
ax.hist(values, bins="fd", density=True, color="#1B3B6F", alpha=0.75,
        edgecolor="white", linewidth=0.35)
ax.set_ylabel("Probability density")
```

Multiple histograms:

```python
bins = np.histogram_bin_edges(np.r_[a, b], bins="fd")
ax.hist(a, bins=bins, density=True, histtype="step", lw=1.2, color="#1B3B6F", label="A")
ax.hist(b, bins=bins, density=True, histtype="step", lw=1.2, color="#D55E00", label="B")
```

Rules:

- Prefer shared bin edges for comparing groups.
- Use `histtype="step"` for overlapping distributions.
- Use filled histograms for single distributions.
- Label count vs probability density accurately.
- Avoid too many bins; use domain knowledge when available.

## 7. ECDF and cumulative distributions

Often cleaner than histograms for comparing distributions.

```python
def ecdf(v):
    v = np.sort(np.asarray(v)[np.isfinite(v)])
    p = np.arange(1, len(v) + 1) / len(v)
    return v, p

for arr, label, color in [(a, "A", "#1B3B6F"), (b, "B", "#D55E00")]:
    xv, pv = ecdf(arr)
    ax.step(xv, pv, where="post", lw=1.2, color=color, label=label)
ax.set_ylabel("Cumulative probability")
```

Use ECDF when sample sizes differ or binning would be arbitrary.

## 8. Box plots

Use for comparing distributions across categorical groups. Prefer box plots over bar charts when distributions matter.

### Box plot / grouped distribution plots — Nature Photonics-style parameters

Use this recipe for small-N experimental distributions, box plots, grouped comparisons, and experiment-vs-simulation overlays.

#### Design intent

Box plots should look compact, restrained, and statistical rather than decorative. The box should communicate the experimental distribution; individual measured points should remain visible when sample size is small; simulation or theory values should be visually distinct but not dominant.

Avoid:

- oversized fonts
- large legends
- thick box outlines
- full boxed axes
- top/right ticks
- saturated box fills
- large simulation markers
- inconsistent box colors when the legend says they represent the same quantity

#### Global style for boxplot figures

Use these values unless the user specifies a larger multi-panel figure:

```python
mpl.rcParams.update({
    "figure.figsize": (3.35, 2.35),
    "figure.dpi": 150,
    "savefig.dpi": 600,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,

    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 6,
    "axes.labelsize": 7,
    "xtick.labelsize": 6,
    "ytick.labelsize": 6,
    "legend.fontsize": 6,

    "axes.linewidth": 0.6,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "xtick.major.size": 2.5,
    "ytick.major.size": 2.5,
    "xtick.direction": "out",
    "ytick.direction": "out",

    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": False,
    "legend.frameon": False,

    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
})
```

#### Recommended implementation pattern

Use one restrained fill color for all experimental boxes when the legend labels them as the same quantity. Keep the simulation/theory marker small and distinct, and avoid text annotations inside the plotting area unless the user explicitly requests them.

```python
fig, ax = plt.subplots(figsize=(3.35, 2.35), constrained_layout=True)
bp = ax.boxplot(
    data_groups,
    labels=labels,
    widths=0.52,
    patch_artist=True,
    showfliers=False,
    medianprops={"color": "black", "linewidth": 0.9},
    boxprops={"linewidth": 0.7, "color": "0.25"},
    whiskerprops={"linewidth": 0.7, "color": "0.25"},
    capprops={"linewidth": 0.7, "color": "0.25"},
)
for patch in bp["boxes"]:
    patch.set_facecolor("#BFD2E6")
    patch.set_alpha(0.65)

rng = np.random.default_rng(0)
for i, vals in enumerate(data_groups, start=1):
    vals = np.asarray(vals)
    xj = i + rng.normal(0, 0.035, size=len(vals))
    ax.plot(xj, vals, "o", ms=2.4, color="0.2", alpha=0.55, mew=0)

ax.plot(
    np.arange(1, len(sim_values) + 1),
    sim_values,
    linestyle="none",
    marker="D",
    ms=4.0,
    mfc="#D55E00",
    mec="white",
    mew=0.35,
    zorder=4,
)
```

Rules:

- `showfliers=False` is acceptable only if individual points or caption clarify outliers; otherwise show fliers with small markers.
- Use the same fill for all experimental boxes when the legend says `Experiment` or `Measured`.
- Keep simulation markers small enough that the distribution remains dominant.
- Do not place text callouts, quartile labels, or value annotations on the plot area unless explicitly requested.
- Do not imply normality with box plots.
- Use category labels sparingly; rotate only if necessary.

## 9. Violin plots

Use when distribution shape is important and sample size is adequate.

```python
vp = ax.violinplot(data_groups, positions=np.arange(1, len(data_groups)+1),
                   widths=0.7, showmeans=False, showmedians=False, showextrema=False)
for body, color in zip(vp["bodies"], ["#1B3B6F", "#D55E00", "#007C73"]):
    body.set_facecolor(color)
    body.set_edgecolor("0.2")
    body.set_linewidth(0.6)
    body.set_alpha(0.45)

# Add median and IQR manually
for i, vals in enumerate(data_groups, start=1):
    q1, med, q3 = np.nanpercentile(vals, [25, 50, 75])
    ax.vlines(i, q1, q3, color="0.15", lw=1.0)
    ax.plot(i, med, "o", ms=3, color="0.15")
ax.set_xticks(np.arange(1, len(labels)+1), labels)
```

Rules:

- Use violins only for enough data to estimate a density.
- Pair with median/IQR markers.
- Use jittered points for small samples instead.

## 10. Bar charts and categorical summaries

Use only for categorical totals or summary values. Avoid for distributions when raw replicates should be shown.

```python
x = np.arange(len(labels))
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.bar(x, mean, yerr=err, width=0.62,
       color="#A8BBD8", edgecolor="0.2", linewidth=0.6,
       error_kw={"elinewidth": 0.8, "capsize": 2, "capthick": 0.8})
ax.set_xticks(x, labels)
ax.set_ylabel("Efficiency (%)")
```

Grouped bars:

```python
width = 0.34
ax.bar(x - width/2, y1, width, color="#1B3B6F", alpha=0.82, label="A")
ax.bar(x + width/2, y2, width, color="#D55E00", alpha=0.82, label="B")
```

Rules:

- Start y-axis at zero for ordinary bar magnitudes.
- Show individual points when bars summarize small-n measurements.
- Avoid 3D bars, gradients, and thick outlines.

## 11. Heat maps with imshow

Use for regular 2D arrays: PSF, near-field maps, spectral maps, correlation matrices, parameter sweeps on a regular grid.

```python
fig, ax = plt.subplots(figsize=(3.5, 3.0), constrained_layout=True)
im = ax.imshow(Z, origin="lower", aspect="auto", cmap="viridis",
               extent=[x.min(), x.max(), y.min(), y.max()],
               norm=Normalize(vmin=vmin, vmax=vmax), interpolation="none")
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Signal (a.u.)")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Position (µm)")
```

Rules:

- Use `aspect="equal"` for physical x/y dimensions with the same units.
- Use `aspect="auto"` for parameter sweeps with different axis units.
- Provide `extent` whenever axes have physical coordinates.
- Use `origin="lower"` for scientific coordinate plots unless image convention dictates otherwise.
- Keep interpolation off unless smoothing is a deliberate visual aid.

## 12. pcolormesh for explicit or nonuniform grids

Use for nonuniform coordinate grids, finite-element/finite-difference parameter grids, spectrograms with explicit bin edges.

```python
fig, ax = plt.subplots(figsize=(3.5, 2.8), constrained_layout=True)
pcm = ax.pcolormesh(X, Y, Z, cmap="viridis", norm=Normalize(vmin, vmax),
                    shading="auto", rasterized=True)
cbar = fig.colorbar(pcm, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Field enhancement")
```

Rules:

- Use `shading="auto"` unless a specific grid convention is required.
- Rasterize dense meshes in vector output.
- Do not use `pcolormesh` for image arrays when `imshow` is simpler and accurate.

## 13. PSF, mode-profile, and optical-intensity maps

Use for Airy PSF, simulated focal spot, near-field/far-field intensity, mode intensity, electromagnetic energy density.

Linear view for modest range:

```python
im = ax.imshow(I, origin="lower", aspect="equal", cmap="magma",
               extent=[xmin, xmax, ymin, ymax], interpolation="none",
               norm=Normalize(vmin=0, vmax=np.nanmax(I)))
```

Log view for high dynamic range:

```python
I = np.asarray(I, float)
Imax = np.nanmax(I)
positive_min = np.nanmin(I[I > 0]) if np.any(I > 0) else Imax * 1e-6
floor = max(Imax * 1e-4, positive_min)
im = ax.imshow(I, origin="lower", aspect="equal", cmap="magma",
               extent=[xmin, xmax, ymin, ymax], interpolation="none",
               norm=LogNorm(vmin=floor, vmax=Imax))
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Intensity (a.u.)")
```

Rules:

- Use `magma` or `inferno`; avoid `jet`.
- Decide if linear or log scale best communicates the result.
- State in the colorbar label or caption if the map is log-scaled.
- Preserve equal spatial aspect unless plotting non-spatial axes.
- Use shared normalization when comparing PSFs.
- Add a scale bar when axes are hidden.
- Keep PSF centered only if the centering operation is already part of the analysis or is explicitly requested.

## 14. Phase maps and signed residual maps

Wrapped phase:

```python
im = ax.imshow(phase, origin="lower", aspect="equal", cmap="twilight",
               extent=[xmin, xmax, ymin, ymax], vmin=-np.pi, vmax=np.pi,
               interpolation="none")
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05, ticks=[-np.pi, 0, np.pi])
cbar.ax.set_yticklabels([r"$-\pi$", "0", r"$\pi$"])
cbar.set_label("Phase (rad)")
```

Signed residual:

```python
v = np.nanpercentile(np.abs(residual), 99)
im = ax.imshow(residual, origin="lower", aspect="equal", cmap="RdBu_r",
               norm=TwoSlopeNorm(vmin=-v, vcenter=0, vmax=v), interpolation="none")
cbar.set_label("Residual (a.u.)")
```

Rules:

- Use cyclic maps only for cyclic variables.
- Use diverging maps for signed residuals or differences.
- Center diverging maps on the physically meaningful reference value, usually zero.

## 15. Contour and contourf plots

Use when level sets have meaning: mode boundaries, phase fronts, intensity thresholds, dispersion contours, iso-frequency curves.

```python
levels = np.linspace(vmin, vmax, 9)
cf = ax.contourf(X, Y, Z, levels=levels, cmap="viridis", extend="both")
cs = ax.contour(X, Y, Z, levels=levels[::2], colors="0.15", linewidths=0.45)
ax.clabel(cs, fmt="%.2g", fontsize=5, inline=True)
cbar = fig.colorbar(cf, ax=ax, pad=0.02, fraction=0.05)
```

Rules:

- Use 6–10 filled contour levels for compact figures.
- Contour labels should be sparse and legible.
- Do not create a false impression of precision with too many contours.

## 16. Image panels: microscopy, SEM/TEM, AFM, camera images

Use for experimental images. Preserve image data. Do not apply aesthetic contrast changes silently if images are evidence.

```python
fig, ax = plt.subplots(figsize=(3.5, 3.0), constrained_layout=True)
ax.imshow(img, cmap="gray", interpolation="none")
ax.set_axis_off()
```

Scale bar using helper:

```python
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
fontprops = fm.FontProperties(size=6)
scalebar = AnchoredSizeBar(ax.transData, length_px, "2 µm", "lower right",
                           pad=0.25, color="white", frameon=False,
                           size_vertical=max(1, length_px * 0.04), fontproperties=fontprops)
ax.add_artist(scalebar)
```

Rules:

- Use grayscale for single-channel morphology images.
- Use physically meaningful contrast limits if needed.
- Include scale bars for micrographs unless physical axes are shown.
- Avoid false-color maps unless they encode measured scalar values.
- Use white scale bars/text on dark images, black on light images.

## 17. Correlation matrices and confusion matrices

Use for model diagnostics, cross-correlation of variables, classification outcomes.

Correlation matrix:

```python
v = 1
im = ax.imshow(C, cmap="RdBu_r", norm=TwoSlopeNorm(vmin=-v, vcenter=0, vmax=v), interpolation="none")
ax.set_xticks(np.arange(len(names)), names, rotation=45, ha="right")
ax.set_yticks(np.arange(len(names)), names)
cbar = fig.colorbar(im, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("Correlation")
```

Confusion matrix:

```python
im = ax.imshow(cm, cmap="Blues", interpolation="none")
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        val = cm[i, j]
        ax.text(j, i, f"{val:g}", ha="center", va="center", fontsize=5,
                color="white" if val > 0.6*np.nanmax(cm) else "black")
```

Rules:

- Use diverging color for correlations.
- Use sequential color for counts or probabilities.
- Use annotation only if matrix is small enough.

## 18. Vector fields: quiver and streamplot

Use for Poynting vector, electric-field direction, polarization, flow, gradients.

```python
fig, ax = plt.subplots(figsize=(3.5, 3.0), constrained_layout=True)
mag = np.hypot(U, V)
im = ax.imshow(mag, origin="lower", extent=[xmin, xmax, ymin, ymax], cmap="viridis", alpha=0.9)
step = 4
q = ax.quiver(X[::step, ::step], Y[::step, ::step], U[::step, ::step], V[::step, ::step],
              color="white", linewidth=0.4, width=0.003, scale=quiver_scale)
```

Rules:

- Subsample arrows aggressively.
- Use a scalar background only if it adds information.
- Include a quiver key when arrow magnitude matters.
- Keep arrows thin and readable.

## 19. Polar plots and angular radiation patterns

Use for angular scattering, far-field emission, antenna/radiation lobes, polarization dependence.

```python
fig, ax = plt.subplots(figsize=(3.2, 3.2), subplot_kw={"projection": "polar"}, constrained_layout=True)
ax.plot(theta, intensity, lw=1.3, color="#1B3B6F")
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.grid(True, color="0.85", lw=0.5)
ax.tick_params(labelsize=6, width=0.6, length=2.5)
```

Rules:

- State angular convention in label/caption.
- Use sparse radial ticks.
- Avoid filled radar-chart aesthetics unless area is physically meaningful.

## 20. Spectrograms and wavelength/time maps

Use for time-resolved spectra, angle-resolved spectra, pump-probe maps, wavelength-position scans.

```python
pcm = ax.pcolormesh(time_ps, wavelength_nm, signal, shading="auto",
                    cmap="viridis", norm=Normalize(vmin, vmax), rasterized=True)
ax.set_xlabel("Delay (ps)")
ax.set_ylabel("Wavelength (nm)")
cbar = fig.colorbar(pcm, ax=ax, pad=0.02, fraction=0.05)
cbar.set_label("ΔT/T")
```

Rules:

- Use diverging colormap centered at zero for differential signals.
- Use sequential colormap for intensity.
- Keep color limits consistent across experimental conditions.

## 21. Waterfall plots and stacked spectra

Use for families of spectra across temperature, power, angle, device index, or time.

```python
offset = 0.0
for i, y in enumerate(spectra):
    ax.plot(wavelength_nm, y + offset*i, lw=0.9, color="#1B3B6F")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Intensity + offset")
```

Rules:

- Make offsets explicit in labels or caption.
- If absolute amplitudes matter, use heat map instead.
- Do not use too many colors for many stacked traces; use one color plus annotation or a gradient only if ordering matters.

## 22. Dispersion and band-structure plots

Use for photonic bands, frequency vs wavevector, angle-resolved dispersion.

```python
for band in bands:
    ax.plot(k, band, lw=1.0, color="#1B3B6F")
for xpos in high_symmetry_positions:
    ax.axvline(xpos, color="0.75", lw=0.5, zorder=0)
ax.set_xticks(high_symmetry_positions, high_symmetry_labels)
ax.set_ylabel("Frequency (THz)")
```

Rules:

- Use subtle vertical guides for high-symmetry points.
- Keep x tick labels compact, e.g. Γ, X, M.
- Use line color sparingly; separate bands by family only if needed.

## 23. Log-scale plots

Use for intensity over dynamic range, noise floors, decay curves, Q distributions.

```python
ax.semilogy(x, y, lw=1.3, color="#1B3B6F")
ax.yaxis.set_major_locator(LogLocator(base=10, numticks=5))
ax.yaxis.set_major_formatter(LogFormatterMathtext(base=10))
ax.tick_params(which="both", direction="out")
```

Rules:

- Do not plot nonpositive values on log axes without handling them explicitly.
- Use log ticks sparingly.
- Label the physical quantity, not “log(quantity)” unless values were transformed before plotting.

## 24. Inset axes and zoom panels

Use to show a resonance, local structure, fabrication image, or detailed region.

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

- Inset tick labels can be smaller, but not unreadable.
- Use mark_inset only if it clarifies the zoomed region.
- Avoid more than one inset per panel unless necessary.

## 25. Broken axes

Use rarely. Prefer transformations, insets, or separate panels. If necessary, make the break visually obvious and do not hide data trends.

Rules:

- Use only when there is a strong outlier or gap.
- Indicate the break clearly.
- Avoid broken axes for statistical comparisons unless unavoidable.

## 26. Multi-panel layout recipes

### Simple 1×2 or 2×1

```python
fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), constrained_layout=True)
for label, ax in zip("ab", axes):
    ax.text(-0.16, 1.06, label, transform=ax.transAxes,
            fontsize=8, fontweight="bold", va="top", ha="left")
```

### Complex layout with GridSpec

```python
fig = plt.figure(figsize=(7.2, 4.6), constrained_layout=True)
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.05], height_ratios=[1, 1])
ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])
ax_c = fig.add_subplot(gs[0, 2])
ax_d = fig.add_subplot(gs[1, :2])
ax_e = fig.add_subplot(gs[1, 2])
```

Rules:

- Use consistent axis label style.
- Align colorbar widths and padding.
- Use shared axes for comparable panels.
- Do not mix multiple unrelated color cycles in one figure.
- Keep panel letters outside/upper-left unless panel content requires inside placement.

## 27. Legends and direct labels

Minimal legend:

```python
ax.legend(loc="best", frameon=False, handlelength=1.5, handletextpad=0.4,
          borderaxespad=0.3, labelspacing=0.25)
```

Direct labels:

```python
ax.text(x[-1], y[-1], "Sample A", color="#1B3B6F", fontsize=6,
        ha="left", va="center")
```

Rules:

- Direct labels are preferred for 2–3 curves if they do not clutter.
- Keep legend labels short.
- Do not place legend over key data.

## 28. Annotation arrows and callouts

```python
ax.annotate("Resonance", xy=(x0, y0), xytext=(x0 + dx, y0 + dy),
            arrowprops={"arrowstyle": "->", "lw": 0.6, "color": "0.2"},
            fontsize=6, color="0.2")
```

Rules:

- Use only a few annotations.
- Arrows should be thin.
- Text should not obscure data.
- Prefer caption for lengthy explanations.

## 29. Rasterization policy

Use rasterization for dense artists in vector files:

```python
ax.scatter(x, y, s=4, alpha=0.4, rasterized=True)
mesh = ax.pcolormesh(X, Y, Z, rasterized=True)
```

Do not rasterize:

- axis labels
- tick labels
- legends
- panel labels
- text annotations
- scale bars
- vector outlines

## 30. Export commands

At the end of a publication script:

```python
fig.savefig("figure.pdf")
fig.savefig("figure.svg")
fig.savefig("figure.png", dpi=600)
```

For only image-heavy single panels, PNG/TIFF can be sufficient, but keep a PDF/SVG version when labels and vector overlays matter.
