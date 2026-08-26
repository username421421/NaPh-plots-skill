# Specialized plots

Use this file for vector fields, quiver or stream plots, polar plots, spectrograms, waterfall plots, and dispersion or band-structure plots.

Assume `style-foundation.md` is already loaded.

## Vector fields

Use for Poynting vectors, electric-field direction, polarization, flow, or gradients.

```python
fig, ax = plt.subplots(figsize=(3.4646, 3.0), constrained_layout=True)
mag = np.hypot(U, V)
im = ax.imshow(mag, origin="lower", extent=[xmin, xmax, ymin, ymax],
               cmap="viridis", alpha=0.9)
step = 4
ax.quiver(
    X[::step, ::step], Y[::step, ::step],
    U[::step, ::step], V[::step, ::step],
    color="white", linewidth=1.0, width=0.003, scale=quiver_scale,
)
```

Rules:

- Subsample arrows aggressively.
- Add a scalar background only if it adds meaning.
- Include a quiver key when vector magnitude matters.

## Polar plots

Use for angular emission, scattering, radiation patterns, or polarization dependence.

```python
fig, ax = plt.subplots(
    figsize=(3.2, 3.2),
    subplot_kw={"projection": "polar"},
    constrained_layout=True,
)
ax.plot(theta, intensity, lw=1.3, color="#1B3B6F")
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.grid(True, color="0.85", lw=1.0)
```

Rules:

- State the angular convention in the figure or caption.
- Keep radial ticks sparse.
- Avoid radar-chart styling unless filled area is physically meaningful.

## Spectrograms and wavelength-time maps

Use for time-resolved spectra, angle-resolved spectra, pump-probe maps, or wavelength-position scans.

```python
pcm = ax.pcolormesh(
    time_ps, wavelength_nm, signal,
    shading="auto",
    cmap="viridis",
    norm=Normalize(vmin, vmax),
    rasterized=True,
)
ax.set_xlabel("Delay (ps)")
ax.set_ylabel("Wavelength (nm)")
```

Rules:

- Use a diverging colormap centered at zero for differential signals.
- Use a sequential colormap for intensity-only maps.
- Keep color limits consistent across comparable conditions.

## Waterfall plots and stacked spectra

Use for families of spectra across temperature, power, angle, device index, or time.

```python
offset = 0.0
for i, y in enumerate(spectra):
    ax.plot(wavelength_nm, y + offset * i, lw=1.0, color="#1B3B6F")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Intensity + offset")
```

Rules:

- Make offsets explicit in labels or caption.
- If absolute amplitudes matter more than relative shape, prefer a heat map.
- Avoid overly colorful trace-by-trace palettes.

## Dispersion and band structure

Use for photonic bands, frequency vs wavevector, or angle-resolved dispersion.

```python
for band in bands:
    ax.plot(k, band, lw=1.0, color="#1B3B6F")
for xpos in high_symmetry_positions:
    ax.axvline(xpos, color="0.75", lw=1.0, zorder=0)
ax.set_xticks(high_symmetry_positions, high_symmetry_labels)
ax.set_ylabel("Frequency (THz)")
```

Rules:

- Use subtle vertical guides for high-symmetry points.
- Keep high-symmetry labels compact.
- Do not use multiple strong colors unless band families need explicit differentiation.

## Family checklist

- Specialized geometry or coordinate conventions are explicit.
- Arrow density, radial ticks, offsets, and color limits are controlled.
- The plot type genuinely communicates the science better than a simpler alternative.
