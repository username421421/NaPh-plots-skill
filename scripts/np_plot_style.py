"""Nature Photonics-style Matplotlib helpers.

This module is intentionally dependency-light: NumPy + Matplotlib only.
Import it from plotting scripts or copy selected helpers into a paper repository.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Literal, Sequence

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.colors import Normalize, LogNorm, PowerNorm, SymLogNorm, TwoSlopeNorm, BoundaryNorm, ListedColormap
from matplotlib.ticker import AutoMinorLocator, MaxNLocator

try:
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
    import matplotlib.font_manager as fm
except Exception:  # pragma: no cover - optional Matplotlib toolkit availability
    AnchoredSizeBar = None
    fm = None

NatureColumn = Literal["single", "one_half", "double", "square_single", "tall_single", "wide_double"]
NormKind = Literal["linear", "log", "power", "symlog", "twoslope", "boundary", "auto"]

NATURE_PHOTONICS_COLORS: list[str] = [
    "#1B3B6F",  # deep blue
    "#D55E00",  # orange
    "#007C73",  # teal
    "#B2479A",  # magenta
    "#C99A00",  # gold
    "#4D4D4D",  # dark gray
    "#56B4E9",  # sky blue
    "#000000",  # black
]

FIG_SIZES: dict[str, tuple[float, float]] = {
    "single": (3.5, 2.4),
    "one_half": (5.2, 3.2),
    "double": (7.2, 4.6),
    "square_single": (3.5, 3.5),
    "tall_single": (3.5, 4.2),
    "wide_double": (7.2, 3.2),
}


def nature_rcparams() -> dict[str, object]:
    """Return rcParams for compact Nature Photonics-style figures."""
    return {
        "figure.figsize": FIG_SIZES["single"],
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
    }


def boxplot_rcparams() -> dict[str, object]:
    """Return a compact rcParams override for box-plot figures."""
    return {
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
    }


def apply_nature_style() -> None:
    """Apply Nature Photonics-style Matplotlib settings."""
    mpl.rcParams.update(nature_rcparams())


def apply_boxplot_style() -> None:
    """Apply box-plot-specific Nature Photonics rcParams."""
    mpl.rcParams.update(nature_rcparams())
    mpl.rcParams.update(boxplot_rcparams())


def figure_size(column: NatureColumn = "single", aspect: float | None = None) -> tuple[float, float]:
    """Return a journal-sized Matplotlib figure size in inches."""
    width, height = FIG_SIZES[column]
    if aspect is not None:
        height = width * float(aspect)
    return width, height


def robust_limits(data: np.ndarray, percentiles: tuple[float, float] = (1, 99), symmetric: bool = False) -> tuple[float, float]:
    """Return finite percentile limits, optionally symmetric around zero."""
    arr = np.asarray(data, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        raise ValueError("Cannot compute limits: data contain no finite values.")
    lo, hi = np.nanpercentile(finite, percentiles)
    if symmetric:
        v = max(abs(lo), abs(hi))
        return -v, v
    if lo == hi:
        eps = abs(lo) * 1e-9 + 1e-12
        return lo - eps, hi + eps
    return float(lo), float(hi)


def positive_floor(data: np.ndarray, fraction: float = 1e-4) -> float:
    """Return a positive lower limit for LogNorm based on data max and minimum positive value."""
    arr = np.asarray(data, dtype=float)
    finite = arr[np.isfinite(arr)]
    finite = finite[finite > 0]
    if finite.size == 0:
        raise ValueError("LogNorm requires at least one positive finite value.")
    vmax = float(np.nanmax(finite))
    return max(vmax * fraction, float(np.nanmin(finite)))


def make_norm(
    data: np.ndarray,
    kind: NormKind = "auto",
    *,
    vmin: float | None = None,
    vmax: float | None = None,
    center: float | None = None,
    robust: bool = False,
    percentiles: tuple[float, float] = (1, 99),
    log_floor_fraction: float = 1e-4,
    gamma: float = 0.5,
    linthresh: float | None = None,
    boundaries: Sequence[float] | None = None,
    ncolors: int | None = None,
) -> Normalize:
    """Create a Matplotlib normalization object from data semantics.

    `kind='auto'` chooses:
    - `TwoSlopeNorm` if center is supplied or data span negative and positive values.
    - `LogNorm` if all finite values are positive and max/min positive > 1e3.
    - `Normalize` otherwise.
    """
    arr = np.asarray(data, dtype=float)
    finite = arr[np.isfinite(arr)]
    if finite.size == 0:
        raise ValueError("Cannot normalize data with no finite values.")

    if robust and kind not in {"log", "boundary"}:
        rvmin, rvmax = robust_limits(finite, percentiles, symmetric=(center is not None))
        vmin = rvmin if vmin is None else vmin
        vmax = rvmax if vmax is None else vmax
    else:
        vmin = float(np.nanmin(finite)) if vmin is None else vmin
        vmax = float(np.nanmax(finite)) if vmax is None else vmax

    if kind == "auto":
        finite_pos = finite[finite > 0]
        if center is not None or (np.nanmin(finite) < 0 < np.nanmax(finite)):
            kind = "twoslope"
            center = 0.0 if center is None else center
        elif finite_pos.size and np.nanmin(finite_pos) > 0 and (np.nanmax(finite_pos) / np.nanmin(finite_pos) > 1e3):
            kind = "log"
        else:
            kind = "linear"

    if kind == "linear":
        return Normalize(vmin=vmin, vmax=vmax)
    if kind == "log":
        floor = positive_floor(finite, fraction=log_floor_fraction) if vmin is None or vmin <= 0 else vmin
        upper = float(np.nanmax(finite[finite > 0])) if vmax is None else vmax
        return LogNorm(vmin=floor, vmax=upper)
    if kind == "power":
        return PowerNorm(gamma=gamma, vmin=vmin, vmax=vmax)
    if kind == "symlog":
        if linthresh is None:
            linthresh = max(np.nanpercentile(np.abs(finite), 5), 1e-12)
        return SymLogNorm(linthresh=linthresh, vmin=vmin, vmax=vmax)
    if kind == "twoslope":
        if center is None:
            center = 0.0
        if not (vmin < center < vmax):
            delta = max(abs(vmin - center), abs(vmax - center), 1e-12)
            vmin, vmax = center - delta, center + delta
        return TwoSlopeNorm(vmin=vmin, vcenter=center, vmax=vmax)
    if kind == "boundary":
        if boundaries is None:
            raise ValueError("BoundaryNorm requires boundaries.")
        if ncolors is None:
            ncolors = len(boundaries) - 1
        return BoundaryNorm(boundaries, ncolors=ncolors)
    raise ValueError(f"Unknown norm kind: {kind}")


def add_colorbar(im, ax, label: str = "", *, fig=None, pad: float = 0.02, fraction: float = 0.05, **kwargs):
    """Add a compact, journal-style colorbar."""
    if fig is None:
        fig = ax.figure
    cbar = fig.colorbar(im, ax=ax, pad=pad, fraction=fraction, **kwargs)
    if label:
        cbar.set_label(label)
    cbar.ax.tick_params(width=0.6, size=2.2, labelsize=6, direction="out")
    cbar.outline.set_linewidth(0.6)
    return cbar


def add_panel_label(ax, label: str, *, x: float = -0.16, y: float = 1.06, fontsize: float = 8, **kwargs):
    """Add bold lower-case panel label using axes coordinates."""
    defaults = dict(transform=ax.transAxes, fontsize=fontsize, fontweight="bold", va="top", ha="left")
    defaults.update(kwargs)
    return ax.text(x, y, label, **defaults)


def polish_axis(
    ax,
    *,
    xlabel: str | None = None,
    ylabel: str | None = None,
    xlim: tuple[float, float] | None = None,
    ylim: tuple[float, float] | None = None,
    minor: bool = True,
    max_major_ticks: int = 5,
):
    """Apply compact Nature-style axis labels and ticks."""
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if xlim is not None:
        ax.set_xlim(*xlim)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.tick_params(which="major", direction="out", width=0.6, length=2.5)
    ax.tick_params(which="minor", direction="out", width=0.45, length=1.5)
    if minor and ax.get_xscale() == "linear":
        ax.xaxis.set_minor_locator(AutoMinorLocator())
    if minor and ax.get_yscale() == "linear":
        ax.yaxis.set_minor_locator(AutoMinorLocator())
    if ax.get_xscale() == "linear":
        ax.xaxis.set_major_locator(MaxNLocator(nbins=max_major_ticks))
    if ax.get_yscale() == "linear":
        ax.yaxis.set_major_locator(MaxNLocator(nbins=max_major_ticks))
    return ax


def add_scalebar(
    ax,
    length_data: float,
    label: str,
    *,
    loc: str = "lower right",
    color: str = "white",
    size_vertical: float | None = None,
    pad: float = 0.25,
    frameon: bool = False,
):
    """Add a scale bar to an image axis.

    length_data is in the axis data units. For pixel images, pass the bar length in pixels.
    """
    if AnchoredSizeBar is None or fm is None:
        raise RuntimeError("AnchoredSizeBar is unavailable in this Matplotlib installation.")
    if size_vertical is None:
        size_vertical = max(length_data * 0.04, 1e-12)
    fontprops = fm.FontProperties(size=6)
    bar = AnchoredSizeBar(
        ax.transData,
        length_data,
        label,
        loc,
        pad=pad,
        color=color,
        frameon=frameon,
        size_vertical=size_vertical,
        fontproperties=fontprops,
    )
    ax.add_artist(bar)
    return bar


def save_publication_figure(
    fig,
    stem: str | Path,
    *,
    formats: Iterable[str] = ("pdf", "svg", "png"),
    dpi: int = 600,
    bbox_inches: str = "tight",
    pad_inches: float = 0.02,
) -> list[Path]:
    """Save a figure in publication-friendly formats and return output paths."""
    stem = Path(stem)
    outputs: list[Path] = []
    for fmt in formats:
        fmt = fmt.lower().lstrip(".")
        path = stem.with_suffix(f".{fmt}")
        if fmt in {"png", "tif", "tiff", "jpg", "jpeg"}:
            fig.savefig(path, dpi=dpi, bbox_inches=bbox_inches, pad_inches=pad_inches)
        else:
            fig.savefig(path, bbox_inches=bbox_inches, pad_inches=pad_inches)
        outputs.append(path)
    return outputs


@dataclass(frozen=True)
class PlotSemantic:
    """Recommended colormap/norm semantics for common scientific map types."""

    cmap: str
    norm_kind: NormKind
    center: float | None = None


SEMANTICS: dict[str, PlotSemantic] = {
    "magnitude": PlotSemantic("viridis", "linear"),
    "positive": PlotSemantic("viridis", "linear"),
    "intensity": PlotSemantic("magma", "auto"),
    "psf": PlotSemantic("magma", "log"),
    "field_intensity": PlotSemantic("inferno", "auto"),
    "phase": PlotSemantic("twilight", "linear"),
    "residual": PlotSemantic("RdBu_r", "twoslope", center=0.0),
    "difference": PlotSemantic("RdBu_r", "twoslope", center=0.0),
    "correlation": PlotSemantic("RdBu_r", "twoslope", center=0.0),
    "mask": PlotSemantic("gray", "boundary"),
}


def semantic_cmap_norm(data: np.ndarray, semantic: str, **norm_kwargs):
    """Return `(cmap, norm)` for a named scientific semantic."""
    spec = SEMANTICS.get(semantic, SEMANTICS["magnitude"])
    kwargs = dict(norm_kwargs)
    if spec.center is not None and "center" not in kwargs:
        kwargs["center"] = spec.center
    norm = make_norm(data, spec.norm_kind, **kwargs)
    return spec.cmap, norm
