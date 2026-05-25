# Scientific Plotting skill for Codex

This folder is an OpenAI/Codex agent skill for generating, editing, and reviewing publication-grade scientific Matplotlib figures.

## Contents

- `SKILL.md` - required skill manifest and main instructions.
- `references/plot_type_recipes.md` - detailed plot recipes for spectra, PSF maps, heat maps, histograms, box plots, violin plots, bar charts, image panels, vector fields, polar plots, and multi-panel figures.
- `references/review_checklist.md` - QA checklist and anti-patterns.
- `references/sources.md` - source references and rationale.
- `assets/nature_communications.mplstyle` - Matplotlib stylesheet.
- `assets/nature_photonics.mplstyle` - legacy stylesheet filename kept for compatibility.
- `scripts/np_plot_style.py` - reusable helper functions.
- `scripts/style_qa.py` - static checks for common style mistakes.

## How to use

Place the skill directory wherever your Codex skill installation expects skills, or explicitly tell Codex to use this skill from its current location. This is a general plotting skill and does not depend on a specific repository or paper. In Codex, invoke the skill when asking for figure work, for example:

```text
Use the scientific-plotting skill to refactor scripts/plot_psf.py into publication-grade scientific Matplotlib code.
```

## Optional Python usage

You may also copy the helper script into your plotting code:

```python
from scripts.np_plot_style import apply_nature_style, figure_size, add_panel_label, add_colorbar, save_publication_figure

apply_nature_style()
fig, ax = plt.subplots(figsize=figure_size("single"))
# ... plotting code ...
save_publication_figure(fig, "figure1")
```

To use the stylesheet directly:

```python
import matplotlib.pyplot as plt
plt.style.use("assets/nature_communications.mplstyle")
```

## Optional QA check

```bash
python scripts/style_qa.py path/to/plot_script.py
```
