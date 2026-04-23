# Nature Photonics-style figure review checklist

Use this checklist after reading the relevant family file or files.

## Scientific integrity

- Data meaning is unchanged unless the user explicitly requested processing changes.
- Any smoothing, clipping, interpolation, averaging, normalization, or log scaling is explicit.
- Axis labels and units match the plotted quantity.
- Comparable panels use comparable axes, limits, and normalization when the comparison depends on it.
- Outliers are not hidden without a clear reason.

## Journal-scale readability

- Final width is intentional: single ~3.5 in, one-half ~5.2 in, or double ~7.2 in.
- Figure height is compact and whitespace is controlled.
- Fonts are sans-serif and roughly 5-7 pt at final size.
- Axes, ticks, lines, markers, legends, and colorbars are compact rather than presentation-sized.

## Labels and structure

- Labels are concise and include units where needed.
- Panel labels are lower-case bold and consistently placed.
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
- Raster-heavy output uses high resolution, typically 600 dpi.
- Dense artists may be rasterized, but labels, legends, scale bars, and annotations remain vector.
- Output includes the formats the user needs, not just a low-resolution preview PNG.

## Fix automatically when editing code

- Replace `jet`, `rainbow`, or decorative colormaps for scalar magnitude data.
- Replace oversized figures, fonts, lines, and markers intended for slides rather than journals.
- Add missing axis labels, units, colorbar labels, panel labels, scale bars, or export commands.
- Remove heavy grids, thick borders, legend frames, and decorative effects unless they are required for clarity.
