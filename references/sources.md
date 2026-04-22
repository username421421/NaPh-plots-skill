# Sources and rationale

This skill is a pragmatic Matplotlib style and code-generation runbook for Nature Photonics-style figures. It is not an official Nature Photonics template.

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

3. Nature Research Figure Guide
   - Use standard fonts such as Arial or Helvetica.
   - Retain editing capabilities and do not outline text.
   - Embed fonts as TrueType 2 or 42.
   - For Python/Matplotlib, use `Matplotlib.rcParams['pdf.fonttype'] = 42`.
   - PDF/EPS preferred for vector material; RGB color space; minimum image resolution guidance.
   - Source: https://research-figure-guide.nature.com/figures/preparing-figures-our-specifications/

4. Matplotlib colormap and normalization documentation
   - Colormap mapping uses normalization from data to [0, 1] and then maps to colormap values.
   - `LogNorm` is useful for data spanning disparate scales.
   - `TwoSlopeNorm` centers a map at a conceptual midpoint such as zero.
   - `BoundaryNorm` maps discrete intervals to integer color indices.
   - Sources:
     - https://matplotlib.org/stable/users/explain/colors/colormapnorms.html
     - https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.TwoSlopeNorm.html
     - https://matplotlib.org/stable/api/_as_gen/matplotlib.colors.BoundaryNorm.html

## Design assumptions

- The target is a compact, clean scientific figure suitable for a Nature-family photonics paper.
- Exact journal production requirements may change and can vary at final acceptance. Always check the specific journal's current production instructions before submission.
- This skill intentionally avoids making SciencePlots mandatory, because many reproducible workflows should not require LaTeX or additional plotting packages.
- If SciencePlots is available, it is used as a base style and then overridden with stricter Nature Photonics defaults.
- This skill favors Matplotlib-native code and optional NumPy-only helpers for maximum portability.
