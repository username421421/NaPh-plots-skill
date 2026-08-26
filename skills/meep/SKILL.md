---
name: meep
description: Use when creating, debugging, or optimizing Meep/PyMeep electromagnetic simulations, including FDTD setup, materials, sources, boundary conditions, monitors, spectra, resonances, mode decomposition, near-to-far fields, and adjoint/inverse design workflows. Trigger on requests mentioning Meep, PyMeep, FDTD, photonics simulation, Maxwell simulation, import meep as mp, or when a task needs guidance from the bundled Meep documentation in doc/docs.
---

# Meep (PyMeep)

## Overview

Use this skill to produce correct Meep code from the local Meep documentation snapshot bundled in this skill (`doc/docs`). Prefer the Python interface unless the user explicitly requests Scheme or C++.

## Source Of Truth

- Primary docs root: `doc/docs`
- API reference: `doc/docs/Python_User_Interface.md`
- First-pass orientation: `doc/docs/index.md`, `doc/docs/Introduction.md`, `doc/docs/Python_Tutorials/Basics.md`, `doc/docs/FAQ.md`
- Use task maps in `references/navigation.md`
- Use example maps/snippets in `references/examples.md`
- Use implementation playbooks in `references/workflows.md`
- Use failure diagnosis in `references/troubleshooting.md`

Before writing code, verify API names and signatures in `doc/docs/Python_User_Interface.md`. Do not rely on memory for Meep API details.

## Local Doc Query Script

Use `scripts/meep_docs.py` to inspect local docs quickly:

```bash
python scripts/meep_docs.py list --limit 40
python scripts/meep_docs.py search "stop_when_fields_decayed"
python scripts/meep_docs.py toc Python_User_Interface.md --max 50
python scripts/meep_docs.py section Perfectly_Matched_Layer.md "Planewave Sources Extending into PML"
python scripts/meep_docs.py examples --max-results 80
python scripts/meep_docs.py snippets Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py
python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py
```

If the page name is ambiguous (for example, `Basics.md`), pass the full relative path such as `Python_Tutorials/Basics.md`.

## Workflow

1. Classify the request.
- Categories: setup/install, field visualization, flux spectra, resonances/Harminv, mode decomposition/S-parameters, near-to-far, dispersive/nonlinear materials, cylindrical coordinates, adjoint optimization, MPI scaling.
2. Load only the relevant docs.
- Start with `references/navigation.md` and `references/examples.md`, then open only mapped pages.
3. Build a minimal valid simulation first.
- Define `cell_size`, `geometry`, `sources`, `boundary_layers`, `resolution`, then instantiate `mp.Simulation(...)`.
4. Add measurements and stopping logic.
- Use DFT monitors/step functions intentionally, then choose `until` or `until_after_sources`.
5. Validate convergence before final conclusions.
- At minimum test sensitivity to resolution, runtime/decay thresholds, and PML thickness.
6. Report assumptions and limitations.
- State unit choices, boundary conditions, symmetry assumptions, and convergence checks that were run.

## Implementation Rules

- Prefer Python interface (`import meep as mp`) for new work.
- Treat `doc/docs/Python_User_Interface.md` as authoritative for function/class behavior.
- Keep run-step semantics correct: `sim.run(...)` accepts step functions; it is not a generic loop body.
- For Fourier-domain outputs (flux, LDOS, near-to-far), prefer pulsed sources and ensure sufficient runtime for decay.
- Keep physical quantities and units explicit. Meep frequencies are `f`, not `omega = 2*pi*f`.
- Respect symmetry constraints: symmetries must hold for both geometry and sources.
- Keep PML logic explicit: PML sits inside the cell; monitor placement must avoid non-physical PML regions.

## Base Script Template (Python)

Use this as the minimal starting structure before task-specific refinement:

```python
import meep as mp

cell = mp.Vector3(16, 8, 0)
geometry = []
sources = [
    mp.Source(
        src=mp.GaussianSource(frequency=0.15, fwidth=0.1),
        component=mp.Ez,
        center=mp.Vector3(-6, 0, 0),
    )
]
boundary_layers = [mp.PML(thickness=1.0)]
resolution = 20

sim = mp.Simulation(
    cell_size=cell,
    geometry=geometry,
    sources=sources,
    boundary_layers=boundary_layers,
    resolution=resolution,
)

sim.run(until_after_sources=mp.stop_when_fields_decayed(
    dt=50, c=mp.Ez, pt=mp.Vector3(), decay_by=1e-8
))
```

Then layer in task-specific monitors and post-processing (flux, eigenmodes, near-to-far, etc.) using `references/workflows.md`.

## Critical Pitfalls To Prevent

Always check these before trusting results:

- `sim.run(...)` misuse: pass functions, not the result of calling them.
- Incomplete convergence: not enough resolution/runtime/PML thickness.
- Wrong source type for the task:
  - Broadband spectra: use pulsed source.
  - Steady single frequency: consider frequency-domain solver or long CW run with smooth turn-on.
- Planewave source extending into PML without `is_integrated=True`.
- Incorrect S-parameter normalization setup (mismatched source/monitor geometry between normalization and scatter runs).
- Misplaced confidence in symmetry when source/geometry do not actually satisfy symmetry constraints.
- Unphysical material setup causing divergence (see `references/troubleshooting.md`).

## Convergence Checklist (Minimum)

- Double `resolution` and compare target outputs.
- Increase runtime (or tighten decay threshold) and verify stable spectra/mode quantities.
- Increase PML thickness (often by factor of two) and verify metrics change below tolerance.
- Confirm monitor/source positions are unchanged between normalization and comparison runs.
- Confirm key conclusions are stable to these checks before presenting as final.

## References To Load

- Task mapping: `references/navigation.md`
- Example routing/snippets: `references/examples.md`
- Implementation playbooks: `references/workflows.md`
- Debug/failure map: `references/troubleshooting.md`
- Full API and class docs: `doc/docs/Python_User_Interface.md`
