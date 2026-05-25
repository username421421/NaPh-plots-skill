# Nature Communications-style figure review checklist

Use this checklist after reading the relevant family file or files.

## Scientific integrity

- Data meaning is unchanged unless the user explicitly requested processing changes.
- Any smoothing, clipping, interpolation, averaging, normalization, or log scaling is explicit.
- Axis labels and units match the plotted quantity.
- Comparable panels use comparable axes, limits, and normalization when the comparison depends on it.
- Outliers are not hidden without a clear reason.

## Journal-scale readability

- Final production width is intentional: Nature Communications single column is 88 mm / 3.4646 in and double column is 180 mm / 7.0866 in. Review/manuscript figures may instead match the actual LaTeX display width.
- Generated figure width matches the intended LaTeX display width, so LaTeX does not resize the typography. Unless the user explicitly specifies another insertion size, assume `width=\textwidth`; for fractional widths, generate at that fraction of `\textwidth`; for multi-panel figures, use the full figure width, not one panel.
- Figure height is compact and whitespace is controlled.
- Fonts are Arial/Helvetica-style sans-serif, use one typeface family across the figure, and remain within the 5-8 pt final-size range unless the user specified otherwise.
- Multi-panel figure width is matched from the total figure width, not one panel width.
- Axes, ticks, lines, markers, legends, and colorbars are compact rather than presentation-sized.
- The thinnest final line art is at least 1 pt wide.
- Display items have a white background and no excessive boxing or decorative frames.

## Labels and structure

- Labels are concise and include units where needed.
- Panel labels are lower-case bold and consistently placed.
- Figure lettering is lower-case except the first letter of text labels where grammar requires capitalization.
- Numbers and SI units have one space between them, unusual abbreviations are defined, and thousands use commas.
- Titles are omitted unless they add information beyond the caption and panel labels.
- Legends are short and unobtrusive, or replaced with direct labels when cleaner.

## Color and normalization

- No `jet`, `rainbow`, or other non-monotonic scalar colormaps.
- No red-vs-green-only primary comparison.
- Sequential, diverging, cyclic, or discrete colormaps match the data semantics.
- Normalization is deliberate: linear, log, centered, cyclic, or discrete as appropriate.
- Shared colorbars use shared `norm`, `vmin`, and `vmax`.

## Image and microscopy panels

- Image panels use scale bars when physical axes are hidden.
- Scale-bar values are defined in the figure legend by default, not printed on the bar unless explicitly requested.
- Scale bars and annotations are editable overlays, not flattened into the raster image.
- No local retouching, content removal, or invented features are implied.
- Overview+zoom panels mark the zoom source clearly.

## Multi-panel layout

- Panels align cleanly.
- Gaps are consistent.
- Shared axes and shared colorbars are used when scientifically appropriate.
- Mixed plot+image figures look coherent rather than pasted together.

## Export

- Vector or mixed figures export to PDF or SVG with editable text.
- Line art, graphs, charts, and schematics are vector PDF/EPS/AI where possible; if forced to raster, they are 1,200 dpi.
- Photographic/bitmapped output is RGB TIFF and at least 300 dpi; raster-heavy output uses 600 dpi when practical.
- Single-column bitmap width is at least 1,040 px and double-column bitmap width is at least 2,080 px, excluding peripheral whitespace.
- Dense artists may be rasterized, but labels, legends, scale bars, and annotations remain vector.
- Output includes the formats the user needs, not just a low-resolution preview PNG.

## Fix automatically when editing code

- Replace `jet`, `rainbow`, or decorative colormaps for scalar magnitude data.
- Replace oversized figures, fonts, lines, and markers intended for slides rather than journals.
- Add missing axis labels, units, colorbar labels, panel labels, scale bars, or export commands.
- Remove heavy grids, thick borders, legend frames, and decorative effects unless they are required for clarity.
- Remove the image Lena from any submitted figure workflow.
