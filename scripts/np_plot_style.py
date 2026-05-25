"""Nature Communications-style Matplotlib helpers.

This module is intentionally dependency-light: NumPy + Matplotlib only.
Import it from plotting scripts or copy selected helpers into any plotting project.
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

MM_PER_IN = 25.4
NCOMMS_PAGE_WIDTH_MM = 210.0
NCOMMS_PAGE_HEIGHT_MM = 276.0
NCOMMS_SINGLE_COLUMN_WIDTH_MM = 88.0
NCOMMS_DOUBLE_COLUMN_WIDTH_MM = 180.0
NCOMMS_SINGLE_COLUMN_WIDTH_IN = NCOMMS_SINGLE_COLUMN_WIDTH_MM / MM_PER_IN
NCOMMS_DOUBLE_COLUMN_WIDTH_IN = NCOMMS_DOUBLE_COLUMN_WIDTH_MM / MM_PER_IN
NCOMMS_SINGLE_COLUMN_MIN_BITMAP_PX = 1040
NCOMMS_DOUBLE_COLUMN_MIN_BITMAP_PX = 2080
LINE_ART_RASTER_DPI = 1200
MIN_FINAL_LINEWIDTH_PT = 1.0

NATURE_COMMUNICATIONS_COLORS: list[str] = [
    "#1B3B6F",  # deep blue
    "#D55E00",  # orange
    "#007C73",  # teal
    "#B2479A",  # magenta
    "#C99A00",  # gold
    "#4D4D4D",  # dark gray
    "#56B4E9",  # sky blue
    "#000000",  # black
]

# Backward-compatible alias for scripts written before the skill was retargeted.
NATURE_PHOTONICS_COLORS = NATURE_COMMUNICATIONS_COLORS

FIG_SIZES: dict[str, tuple[float, float]] = {
    "single": (NCOMMS_SINGLE_COLUMN_WIDTH_IN, NCOMMS_SINGLE_COLUMN_WIDTH_IN * 0.72),
    "one_half": (5.2, 3.2),
    "double": (NCOMMS_DOUBLE_COLUMN_WIDTH_IN, NCOMMS_DOUBLE_COLUMN_WIDTH_IN * 0.64),
    "square_single": (NCOMMS_SINGLE_COLUMN_WIDTH_IN, NCOMMS_SINGLE_COLUMN_WIDTH_IN),
    "tall_single": (NCOMMS_SINGLE_COLUMN_WIDTH_IN, NCOMMS_SINGLE_COLUMN_WIDTH_IN * 1.2),
    "wide_double": (NCOMMS_DOUBLE_COLUMN_WIDTH_IN, NCOMMS_DOUBLE_COLUMN_WIDTH_IN * 0.445),
}

# Single-plot reference geometry.
SINGLE_PLOT_REFERENCE_WIDTH_IN = FIG_SIZES["single"][0]
SINGLE_PLOT_REFERENCE_ASPECT = FIG_SIZES["single"][1] / FIG_SIZES["single"][0]

# Generic default for full LaTeX text width. Override `page_width_in`
# when the target journal/template text width is known.
LATEX_TEXT_WIDTH_IN = 6.5
# Backward-compatible alias. This value means LaTeX text width, not physical
# paper width.
LATEX_PAGE_WIDTH_IN = LATEX_TEXT_WIDTH_IN

# Nature Communications recommends 5-8 pt type at final figure size. The
# preferred workflow is to make the generated figure width equal to the intended
# LaTeX display width, so these values can be used unchanged and LaTeX performs
# no width rescaling.
BASE_TYPOGRAPHY_RCPARAMS: dict[str, float] = {
    "font.size": 8.0,
    "axes.labelsize": 7.0,
    "axes.titlesize": 8.0,
    "xtick.labelsize": 7.0,
    "ytick.labelsize": 7.0,
    "legend.fontsize": 8.0,
}

PANEL_LABEL_BASE_FONTSIZE_PT = 8.0
IMAGE_ANNOTATION_FONTSIZE_PT = 7.0
RASTER_MIN_DPI = 300
RASTER_PREFERRED_DPI = 600


def nature_communications_column_width(column: Literal["single", "double"]) -> float:
    """Return the Nature Communications production column width in inches."""
    if column == "single":
        return NCOMMS_SINGLE_COLUMN_WIDTH_IN
    if column == "double":
        return NCOMMS_DOUBLE_COLUMN_WIDTH_IN
    raise ValueError("column must be 'single' or 'double'.")


def target_typography_rcparams() -> dict[str, float]:
    """Return the fixed target final displayed rcParam font sizes."""
    return dict(BASE_TYPOGRAPHY_RCPARAMS)


def latex_display_width(
    *,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
) -> float:
    """Return the intended final display width in LaTeX, in inches.

    Unless the caller supplies a different fraction or explicit final width,
    assume the figure is inserted at full text width.
    """
    if final_width_in is not None:
        width = float(final_width_in)
    else:
        width = float(page_width_in) * float(latex_width_fraction)
    if width <= 0:
        raise ValueError("Final LaTeX display width must be positive.")
    return width


def matched_figure_width(
    *,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
) -> float:
    """Return the recommended generated figure width.

    Use this width in `figsize` so the exported image already matches its
    intended LaTeX display width and LaTeX does not resize the typography.
    """
    return latex_display_width(
        latex_width_fraction=latex_width_fraction,
        page_width_in=page_width_in,
        final_width_in=final_width_in,
    )


def matched_figure_size(
    *,
    aspect: float,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
) -> tuple[float, float]:
    """Return `(width, height)` matched to the intended LaTeX display width."""
    width = matched_figure_width(
        latex_width_fraction=latex_width_fraction,
        page_width_in=page_width_in,
        final_width_in=final_width_in,
    )
    return width, width * float(aspect)


def latex_typography_scale(
    total_width_in: float,
    *,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> float:
    """Return the fallback rcParam scale for unmatched generated widths.

    `total_width_in` is the full generated figure width, not a single panel
    width. The final display width is either `final_width_in` or
    `page_width_in * latex_width_fraction`. Matplotlib font sizes are specified
    in generated-figure coordinates, so the scale is:

        generated_width / final_display_width

    Preferred workflow: set `total_width_in == final_display_width`, making this
    scale 1.0 and leaving the fixed 8/7/8 pt typography unchanged. Use this
    compensation only when an existing script must keep a generated width that
    differs from the LaTeX display width. `reference_width_in` is accepted only
    for backward compatibility and is intentionally ignored.
    """
    width = float(total_width_in)
    if width <= 0:
        raise ValueError("Generated figure width must be positive.")
    display_width = latex_display_width(
        latex_width_fraction=latex_width_fraction,
        page_width_in=page_width_in,
        final_width_in=final_width_in,
    )
    return width / display_width


def scaled_typography_rcparams(
    total_width_in: float,
    *,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> dict[str, float]:
    """Return fallback font-size rcParams for unmatched generated widths.

    If possible, make the generated figure width equal the intended LaTeX
    display width and omit this scaling. This helper keeps final typography at
    the fixed 8/7/8 pt targets when matching the generated width is not
    practical.
    """
    target_typography = target_typography_rcparams()
    scale = latex_typography_scale(
        total_width_in,
        latex_width_fraction=latex_width_fraction,
        page_width_in=page_width_in,
        final_width_in=final_width_in,
        reference_width_in=reference_width_in,
    )
    return {key: value * scale for key, value in target_typography.items()}


def nature_rcparams(
    *,
    total_width_in: float | None = None,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> dict[str, object]:
    """Return rcParams for compact Nature Communications-style figures."""
    typography = target_typography_rcparams()
    if total_width_in is not None:
        typography.update(
            scaled_typography_rcparams(
                total_width_in,
                latex_width_fraction=latex_width_fraction,
                page_width_in=page_width_in,
                final_width_in=final_width_in,
                reference_width_in=reference_width_in,
            )
        )

    return {
        "figure.figsize": FIG_SIZES["single"],
        "figure.dpi": 150,
        "figure.constrained_layout.use": True,
        "savefig.dpi": RASTER_PREFERRED_DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "savefig.transparent": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        **typography,
        "mathtext.fontset": "dejavusans",
        "mathtext.default": "regular",
        "axes.linewidth": MIN_FINAL_LINEWIDTH_PT,
        "axes.labelpad": 2.0,
        "lines.linewidth": 1.2,
        "lines.markersize": 3.5,
        "lines.markeredgewidth": MIN_FINAL_LINEWIDTH_PT,
        "patch.linewidth": MIN_FINAL_LINEWIDTH_PT,
        "xtick.major.width": MIN_FINAL_LINEWIDTH_PT,
        "ytick.major.width": MIN_FINAL_LINEWIDTH_PT,
        "xtick.minor.width": MIN_FINAL_LINEWIDTH_PT,
        "ytick.minor.width": MIN_FINAL_LINEWIDTH_PT,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "xtick.minor.size": 1.5,
        "ytick.minor.size": 1.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.top": False,
        "ytick.right": False,
        "axes.spines.top": True,
        "axes.spines.right": True,
        "axes.grid": False,
        "legend.frameon": False,
        "legend.handlelength": 1.6,
        "legend.handletextpad": 0.4,
        "legend.borderaxespad": 0.3,
        "legend.labelspacing": 0.25,
        "legend.columnspacing": 0.8,
        "image.cmap": "viridis",
        "image.interpolation": "none",
        "axes.prop_cycle": cycler(color=NATURE_COMMUNICATIONS_COLORS),
    }


def boxplot_rcparams(
    *,
    total_width_in: float | None = None,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> dict[str, object]:
    """Return a compact rcParams override for box-plot figures."""
    typography = target_typography_rcparams()
    if total_width_in is not None:
        typography.update(
            scaled_typography_rcparams(
                total_width_in,
                latex_width_fraction=latex_width_fraction,
                page_width_in=page_width_in,
                final_width_in=final_width_in,
                reference_width_in=reference_width_in,
            )
        )

    return {
        "figure.figsize": (NCOMMS_SINGLE_COLUMN_WIDTH_IN, NCOMMS_SINGLE_COLUMN_WIDTH_IN * 0.68),
        "figure.dpi": 150,
        "savefig.dpi": RASTER_PREFERRED_DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        **typography,
        "axes.linewidth": MIN_FINAL_LINEWIDTH_PT,
        "xtick.major.width": MIN_FINAL_LINEWIDTH_PT,
        "ytick.major.width": MIN_FINAL_LINEWIDTH_PT,
        "xtick.major.size": 2.5,
        "ytick.major.size": 2.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "axes.spines.top": True,
        "axes.spines.right": True,
        "axes.grid": False,
        "legend.frameon": False,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
    }


def lineplot_rcparams() -> dict[str, object]:
    """Return rcParams for compact line plots with visible top/right spines."""
    return {
        "axes.spines.top": True,
        "axes.spines.right": True,
    }


def apply_nature_style(
    *,
    total_width_in: float | None = None,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> None:
    """Apply Nature Communications-style Matplotlib settings."""
    mpl.rcParams.update(
        nature_rcparams(
            total_width_in=total_width_in,
            latex_width_fraction=latex_width_fraction,
            page_width_in=page_width_in,
            final_width_in=final_width_in,
            reference_width_in=reference_width_in,
        )
    )


def apply_lineplot_style(
    *,
    total_width_in: float | None = None,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> None:
    """Apply Nature Communications-style settings for line plots."""
    mpl.rcParams.update(
        nature_rcparams(
            total_width_in=total_width_in,
            latex_width_fraction=latex_width_fraction,
            page_width_in=page_width_in,
            final_width_in=final_width_in,
            reference_width_in=reference_width_in,
        )
    )
    mpl.rcParams.update(lineplot_rcparams())


def apply_boxplot_style(
    *,
    total_width_in: float | None = None,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> None:
    """Apply box-plot-specific Nature Communications rcParams."""
    mpl.rcParams.update(
        nature_rcparams(
            total_width_in=total_width_in,
            latex_width_fraction=latex_width_fraction,
            page_width_in=page_width_in,
            final_width_in=final_width_in,
            reference_width_in=reference_width_in,
        )
    )
    mpl.rcParams.update(
        boxplot_rcparams(
            total_width_in=total_width_in,
            latex_width_fraction=latex_width_fraction,
            page_width_in=page_width_in,
            final_width_in=final_width_in,
            reference_width_in=reference_width_in,
        )
    )


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
    cbar.ax.tick_params(
        width=MIN_FINAL_LINEWIDTH_PT,
        size=2.2,
        labelsize=mpl.rcParams.get("ytick.labelsize", BASE_TYPOGRAPHY_RCPARAMS["ytick.labelsize"]),
        direction="out",
    )
    cbar.outline.set_linewidth(MIN_FINAL_LINEWIDTH_PT)
    return cbar


def target_panel_label_fontsize(*, page_width_in: float = LATEX_PAGE_WIDTH_IN) -> float:
    """Return the fixed target final panel-label size."""
    return PANEL_LABEL_BASE_FONTSIZE_PT


def panel_label_fontsize(
    total_width_in: float | None = None,
    *,
    latex_width_fraction: float = 1.0,
    page_width_in: float = LATEX_PAGE_WIDTH_IN,
    final_width_in: float | None = None,
    reference_width_in: float | None = None,
) -> float:
    """Return panel-label font size.

    The target final panel label is 8 pt. Prefer generating the figure at the
    intended LaTeX display width so this value is used unchanged. When a total
    figure width is provided and it differs from the display width, scale by the
    same fallback generated-width / display-width factor used for the rest of
    the typography.
    """
    if total_width_in is not None:
        return target_panel_label_fontsize(
            page_width_in=page_width_in
        ) * latex_typography_scale(
            total_width_in,
            latex_width_fraction=latex_width_fraction,
            page_width_in=page_width_in,
            final_width_in=final_width_in,
            reference_width_in=reference_width_in,
        )

    base_font = BASE_TYPOGRAPHY_RCPARAMS["font.size"]
    current_font = float(mpl.rcParams.get("font.size", base_font))
    return PANEL_LABEL_BASE_FONTSIZE_PT * current_font / base_font


def add_panel_label(ax, label: str, *, x: float = -0.16, y: float = 1.06, fontsize: float | None = None, **kwargs):
    """Add bold lower-case panel label using axes coordinates.

    The default is an 8 pt label. If using fallback typography compensation,
    call `apply_nature_style(total_width_in=...)` first, or pass `fontsize`
    explicitly using `panel_label_fontsize(total_width_in=...)`.
    """
    if fontsize is None:
        fontsize = panel_label_fontsize()
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
    """Apply compact Nature Communications-style axis labels and ticks."""
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if xlim is not None:
        ax.set_xlim(*xlim)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.tick_params(which="major", direction="out", width=MIN_FINAL_LINEWIDTH_PT, length=2.5)
    ax.tick_params(which="minor", direction="out", width=MIN_FINAL_LINEWIDTH_PT, length=1.5)
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
    label: str = "",
    *,
    loc: str = "lower right",
    color: str = "white",
    size_vertical: float | None = None,
    fontsize: float | None = None,
    pad: float = 0.25,
    frameon: bool = False,
):
    """Add a scale bar to an image axis.

    length_data is in the axis data units. For pixel images, pass the bar
    length in pixels. Nature Communications prefers scale-bar lengths defined
    in the legend rather than printed on the bar, so the default label is empty.
    """
    if AnchoredSizeBar is None or fm is None:
        raise RuntimeError("AnchoredSizeBar is unavailable in this Matplotlib installation.")
    if size_vertical is None:
        size_vertical = max(length_data * 0.04, 1e-12)
    if fontsize is None:
        try:
            fontsize = float(mpl.rcParams.get("axes.labelsize", IMAGE_ANNOTATION_FONTSIZE_PT))
        except (TypeError, ValueError):
            fontsize = IMAGE_ANNOTATION_FONTSIZE_PT
    fontprops = fm.FontProperties(size=fontsize)
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
    dpi: int = RASTER_PREFERRED_DPI,
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
