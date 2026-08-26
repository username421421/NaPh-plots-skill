# Personal scientific-computing skills

This repository is a portable bundle of personal Codex skills for computational photonics and scientific figures. Each skill is self-contained under `skills/` so the repository can be cloned, pulled, or copied into a local skill directory.

## Included skills

| Skill | Focus |
| --- | --- |
| [`lumerical-fdtd`](skills/lumerical-fdtd/SKILL.md) | Ansys Lumerical FDTD, `lumapi`/PyLumerical automation, solver setup, sources, monitors, boundaries, and convergence. |
| [`fdtdx`](skills/fdtdx/SKILL.md) | FDTDX electromagnetic simulations in Python/JAX, placement, detectors, JIT execution, inverse design, and validation. |
| [`meep`](skills/meep/SKILL.md) | Meep/PyMeep FDTD simulations, spectra, resonances, mode decomposition, near-to-far fields, and adjoint workflows. |
| [`scientific-plotting`](skills/scientific-plotting/SKILL.md) | Publication-grade Matplotlib figures, scientific visualizations, microscopy panels, layouts, and export QA. |

The simulation skills include their bundled reference corpora, local query scripts, examples, notebooks, and tests where present. The plotting skill includes its Matplotlib styles, helper library, references, and QA script.

## Clone and keep it updated

```bash
git clone https://github.com/username421421/NaPh-plots-skill.git
cd NaPh-plots-skill
git pull --ff-only
```

The repository name is intentionally not part of the skill names, so it can be renamed later without changing the packages inside it.

## Install all skills locally

For a Codex installation, copy the four directories under `skills/` into the skill directory used by your setup. For example, in PowerShell:

```powershell
$bundleRoot = (Get-Location).Path
$codexSkills = Join-Path $env:USERPROFILE ".codex\skills"
New-Item -ItemType Directory -Path $codexSkills -Force | Out-Null
Copy-Item -Path (Join-Path $bundleRoot "skills\*") -Destination $codexSkills -Recurse -Force
```

On systems using an `.agents/skills` directory, copy the same four directories there instead. To update an installed copy, pull this repository and repeat the copy, or point your skill search path directly at each directory under `skills/`.

## Use one skill without installing everything

The package paths are independent. A tool can use only one of these directories, for example:

```text
NaPh-plots-skill/skills/meep
NaPh-plots-skill/skills/fdtdx
```

Keep each `SKILL.md` beside its `references/`, `scripts/`, `doc/`, `assets/`, and `agents/` directories. The instructions intentionally use relative paths into those directories.

## Maintenance notes

- The FDTDX skill distinguishes the latest upstream API from its bundled offline corpus; check its versioning instructions before relying on an API example.
- The Lumerical FDTD skill uses its local Ansys reference corpus before live lookup.
- The Meep skill treats its bundled Python API documentation as the local source of truth and requires convergence checks for numerical conclusions.
- The scientific-plotting skill is a style and QA workflow; it does not install Matplotlib or other Python packages.
- Do not commit private simulation data, credentials, local virtual environments, or generated result files to this repository.

## Adding another personal skill

Add a new self-contained directory at `skills/<skill-name>/` with a `SKILL.md` and any references or scripts it uses. Keep paths relative to that skill directory so the package remains portable.
