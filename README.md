# Nature Photonics plotting skill for Codex

This folder is an OpenAI/Codex agent skill for generating and editing Nature Photonics-style scientific Matplotlib figures.

## Contents

- `SKILL.md` — required skill manifest and main instructions.
- `references/plot_type_recipes.md` — detailed plot recipes for spectra, PSF maps, heat maps, histograms, box plots, violin plots, bar charts, image panels, vector fields, polar plots, and multi-panel figures.
- `references/review_checklist.md` — QA checklist and anti-patterns.
- `references/sources.md` — source references and rationale.
- `assets/nature_photonics.mplstyle` — Matplotlib stylesheet.
- `scripts/np_plot_style.py` — reusable helper functions.
- `scripts/style_qa.py` — static checks for common style mistakes.

## How to use

Place the `nature-photonics-plotting` directory wherever your Codex skill installation expects skills, or keep it in your repository and explicitly tell Codex to use this skill. In Codex, invoke the skill when asking for figure work, for example:

```text
Use the nature-photonics-plotting skill to refactor scripts/plot_psf.py into publication-grade Nature Photonics-style Matplotlib code.
```

## Optional Python usage

You may also copy the helper script into your plotting code:

```python
from scripts.np_plot_style import apply_nature_style, figure_size, add_panel_label, add_colorbar, save_publication_figure

apply_nature_style(use_scienceplots=False)
fig, ax = plt.subplots(figsize=figure_size("single"))
# ... plotting code ...
save_publication_figure(fig, "figure1")
```

To use the stylesheet directly:

```python
import matplotlib.pyplot as plt
plt.style.use("assets/nature_photonics.mplstyle")
```

## Optional QA check

```bash
python scripts/style_qa.py path/to/plot_script.py
```
