# Statistical and categorical plots

Use this file for histograms, ECDFs, box plots, violin plots, bar charts, and grouped categorical comparisons.

Assume `style-foundation.md` is already loaded.

## Histograms

Use for distributions of linewidth, resonance wavelength, Q factor, residuals, fabrication error, particle size, intensity values, or noise.

```python
fig, ax = plt.subplots(figsize=(3.5, 2.4), constrained_layout=True)
ax.hist(values, bins="fd", color="#4D4D4D", alpha=0.82,
        edgecolor="white", linewidth=0.35)
ax.set_xlabel("Resonance shift (nm)")
ax.set_ylabel("Count")
```

For group comparison:

```python
bins = np.histogram_bin_edges(np.r_[a, b], bins="fd")
ax.hist(a, bins=bins, density=True, histtype="step", lw=1.2, color="#1B3B6F", label="A")
ax.hist(b, bins=bins, density=True, histtype="step", lw=1.2, color="#D55E00", label="B")
```

Rules:

- Use deliberate binning.
- Use shared bins for direct comparison.
- Label count vs density correctly.
- Prefer outlined or lightly transparent overlap, not muddy filled overlap.

## ECDFs

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

## Box plots

Use when distributions matter and a bar chart would hide them.

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
```

Add measured points for small samples:

```python
rng = np.random.default_rng(0)
for i, vals in enumerate(data_groups, start=1):
    vals = np.asarray(vals)
    xj = i + rng.normal(0, 0.035, size=len(vals))
    ax.plot(xj, vals, "o", ms=2.4, color="0.2", alpha=0.55, mew=0)
```

Rules:

- Show individual points when sample size is small.
- Keep fills muted and outlines thin.
- Do not overload the plot with quartile labels or callouts unless explicitly requested.
- If simulation or theory markers are added, keep them visually secondary to the measured distribution.

## Violin plots

Use only when sample size is large enough that distribution shape is meaningful.

```python
vp = ax.violinplot(data_groups, positions=np.arange(1, len(data_groups) + 1),
                   widths=0.7, showmeans=False, showmedians=False, showextrema=False)
for body, color in zip(vp["bodies"], ["#1B3B6F", "#D55E00", "#007C73"]):
    body.set_facecolor(color)
    body.set_edgecolor("0.2")
    body.set_linewidth(0.6)
    body.set_alpha(0.45)
```

Pair violins with median or IQR markers. Use jittered points instead when `n` is small.

## Bar charts

Use only for categorical totals or summary values. Do not use bars when the underlying distribution is the important result.

```python
x = np.arange(len(labels))
ax.bar(
    x, mean, yerr=err, width=0.62,
    color="#A8BBD8", edgecolor="0.2", linewidth=0.6,
    error_kw={"elinewidth": 0.8, "capsize": 2, "capthick": 0.8},
)
ax.set_xticks(x, labels)
ax.set_ylabel("Efficiency (%)")
```

Rules:

- Start the y-axis at zero for ordinary bar magnitudes.
- Add error bars or raw points when summarizing replicates.
- Avoid gradients, 3D bars, or thick outlines.

## Family checklist

- Histograms use deliberate bins and correct normalization labels.
- ECDF is preferred when binning would be arbitrary.
- Box and violin plots do not hide small-sample structure.
- Bar charts are used only for genuine categorical summaries.
- Statistical summary graphics do not replace raw data visibility when raw data matter.
