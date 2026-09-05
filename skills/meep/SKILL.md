---
name: meep
description: Build, debug, and validate Meep/PyMeep simulations and adjoint workflows when the user selects Meep or project imports identify it. Generic FDTD requests alone do not select Meep.
---

# Meep

Prefer Python (`import meep as mp`) unless another interface is requested.
Preserve the campaign's interpreter, environment, and structure. For changed
APIs, verify installed signatures/source and record interpreter, module path,
version, pins/commit when available. Bundled `doc/docs` is a snapshot; disclose
unknown provenance. Use matching official sources when local evidence is missing
or incompatible; never silently upgrade. Reuse verified unchanged evidence.

## Find only what the task needs

Paths below are relative to this skill. Use the selected project Python. Start
with the affected symbol or one matching reference; expand only if unresolved.
Do not load whole manuals, all routing files, or global example inventories.

```text
python scripts/meep_docs.py search "<symbol>" --max-results 8
python scripts/meep_docs.py section Python_User_Interface.md "<heading>" --max-lines 100
python scripts/meep_docs.py compose <relative-page> --title "<section>" --lang py --max-lines 100
```

Use full relative page paths if names are ambiguous. A truncated result is a
locator, not a complete API contract: retrieve the rest of the relevant section
before implementing unresolved arguments or return semantics.

| Need | Read the relevant section |
| --- | --- |
| Constructor/method/step function | `doc/docs/Python_User_Interface.md` |
| New setup, flux normalization, modes, far field, adjoint, convergence | `references/workflows.md` |
| A complete official example | `references/examples.md`, then the selected tutorial section |
| Installation, materials, cylindrical/symmetry, Harminv, MPI or other topic | Matching row in `references/navigation.md` |
| Divergence or suspicious results | `references/troubleshooting.md` |

## Implement correctly

For a new setup: define units, cell, geometry/materials, sources, PML, resolution,
then `mp.Simulation`; add monitors and stopping logic before execution. Audit
changed calls against the selected runtime, not a tutorial from another version.

- Meep frequency is `f`, not angular frequency `2*pi*f`; state length units.
- `sim.run` accepts step-function callables, not arbitrary loop bodies. Factories
  such as `mp.at_every(...)` return callables; do not execute a callback prematurely.
- Prefer pulsed sources for spectra/LDOS/near-to-far; for a single steady frequency,
  consider the frequency-domain solver or smoothly turned-on CW with sufficient runtime.
- PML lies inside the cell: keep monitors out. Plane-wave sources extending into
  PML need `is_integrated=True`. Symmetry must hold for geometry and excitation.
- Match normalization/scattering source and monitor geometry; inspect flux signs
  and reference signals before interpreting ratios or S-parameters.
- Set a decay probe that samples the relevant field, plus a maximum simulation
  time or launcher timeout. Record stop reason; a ceiling hit is unconverged.

## Validate within scope

Follow workspace authorization before solves, normalization, optimization, or
convergence sweeps. Documentation/logging/path edits need no new simulation.
Before scientific claims, establish or reuse applicable resolution, runtime/decay,
PML, and symmetry evidence for the named metric and tolerance. Budget refinements;
doubling resolution is optional. Report units, boundaries, normalization, checks
performed/reused/pending, and limitations. A plausible plot is not convergence.
