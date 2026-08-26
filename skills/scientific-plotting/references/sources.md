# Sources and rationale

This skill is a pragmatic Matplotlib style and code-generation runbook for Nature Communications-style figures. It is not an official Nature Communications template.

## Primary references consulted

1. OpenAI Codex Agent Skills documentation
   - Skills are directories containing a required `SKILL.md` file with `name` and `description` front matter, plus optional `scripts/`, `references/`, `assets/`, and `agents/` folders.
   - Source: https://developers.openai.com/codex/skills

2. SciencePlots by garrettj403
   - A widely used Matplotlib style package for scientific papers, presentations, and theses.
   - Important usage note: recent SciencePlots versions require `import scienceplots` before `plt.style.use(...)`.
   - Includes `science`, `nature`, `no-latex`, journal styles, and colorblind-aware cycles.
   - Source: https://github.com/garrettj403/SciencePlots
   - Gallery: https://github.com/garrettj403/SciencePlots/wiki/Gallery

3. Brief guide for submission to Nature Communications, revised May 3, 2019
   - Images should be RGB and 300 dpi or higher.
   - All figure text should use the same typeface, Arial or Helvetica; use Symbol for Greek letters.
   - Use distinct colors with comparable visibility, avoid red and green for contrast, and avoid rainbow color scales.
   - Figures are best prepared at expected print size; optimum font size at final size is 5-8 pt.
   - Editable vector or layered files are preferred where possible.
   - Source: local copy of the Nature Communications submission guide (PDF).

4. Nature Communications online guide to authors, pasted by user on 2026-04-29
   - Figures should be one- or two-column display items.
   - Figure lettering should use a clear sans-serif typeface such as Helvetica, with approximately the same size across figures.
   - Display items should have a white background and avoid excessive boxing, unnecessary color, decorative effects, highly pixelated drawings, and 3D histogram effects.
   - Thinnest final lines should be no smaller than 1 pt.
   - Multipart figures use lower-case bold panel letters in the same type size as the rest of the figure.
   - Units should use SI style with a space between number and unit; scale bars are preferred over magnification factors and their lengths should be defined in the legend.
   - Use colorblind-aware palettes and recolor arbitrary green/red heat maps, graphs, and schematics.
   - Final production widths are 88 mm single column and 180 mm double column.
   - Line art, graphs, charts, and schematics should be vector; if not vector, use 1,200 dpi.
   - Photographic and bitmapped images should be RGB TIFF at 300 dpi or higher, with minimum widths of 1,040 px single-column and 2,080 px double-column.
   - Nature Communications will not publish or review manuscripts using the image Lena.
   - Source: user-provided text from Nature Communications "How to submit" author guidance.

5. Nature Research Figure Guide
   - Use standard fonts such as Arial or Helvetica.
   - Retain editing capabilities and do not outline text.
   - Embed fonts as TrueType 2 or 42.
   - For Python/Matplotlib, use `Matplotlib.rcParams['pdf.fonttype'] = 42`.
   - PDF/EPS preferred for vector material; RGB color space; minimum image resolution guidance.
   - Source: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/

6. Matplotlib colormap and normalization documentation
   - Colormap mapping uses normalization from data to [0, 1] and then maps to colormap values.
   - `LogNorm` is useful for data spanning disparate scales.
   - `TwoSlopeNorm` centers a map at a conceptual midpoint such as zero.
   - `BoundaryNorm` maps discrete intervals to integer color indices.
   - Sources:
     - https://matplotlib.org/stable/users/explain/colors/colormapnorms.html
     - https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html
     - https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html

## Design assumptions

- The target is a compact, clean scientific figure suitable for Nature Communications.
- Exact journal production requirements may change and can vary at final acceptance. Always check the specific journal's current production instructions before submission.
- This skill intentionally avoids making SciencePlots mandatory, because many reproducible workflows should not require LaTeX or additional plotting packages.
- If SciencePlots is available, it is used as a base style and then overridden with stricter Nature Communications defaults.
- This skill favors Matplotlib-native code and optional NumPy-only helpers for maximum portability.
