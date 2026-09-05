---
name: fdtdx
description: Build, debug, and validate FDTDX Python/JAX simulations and inverse design when selected by the user or project dependencies, including installed API and backend compatibility.
---

# FDTDX

Use the campaign's selected interpreter and installed source with matching
tests/docs. Never silently upgrade or mix upstream and installed APIs. Record
interpreter, module path, version/pins/commit when available; version alone may
misidentify an editable or shadowing module. Resolve official upstream separately
for upgrades/latest features/unresolved compatibility, or before choosing APIs
for a new project without a runtime. Disclose unavailable verification.

## Query the API before loading tutorials

Paths are relative to this skill; run with the project Python.

```text
python scripts/fdtdx_docs.py api <Symbol> --source installed --max-doc-lines 20
python scripts/fdtdx_docs.py api <Symbol> --member <method> --source installed --max-doc-lines 20
```

Installed mode imports but does not construct/solve; import/missing-symbol errors
never fall back. Default `api` mode is **snapshot**, reading bundled JSON regardless
of interpreter. Use `--source snapshot` explicitly for offline lookup; tutorials
contain legacy constructors and stale dispersion claims. Increase output/read
source when the bounded result does not establish the full contract.

| Need | Read/run only the matching route |
| --- | --- |
| Missing/changed environment evidence | `scripts/fdtdx_doctor.py --project <project>` |
| Version mismatch or capability limits | `references/capabilities-and-versioning.md` |
| Build/placement/run pattern | Relevant section of `references/workflows.md` |
| Specific source/material/detector/geometry | Matching row in `references/navigation.md`, then selected source/test |
| JIT, memory, sharding, gradients | `references/jax-performance.md` |
| Scientific/gradient acceptance | `references/convergence-validation.md` |
| Failure diagnosis | `references/troubleshooting.md` |
| Snapshot provenance/refresh | `references/corpus-manifest.md` |

Use `scripts/fdtdx_docs.py search "<symbol>" --max-results 8` to locate snapshot
source when needed. Prefer matching tests for correctness, examples for architecture;
do not load all routing files or a whole tutorial to answer one signature question.

## Preserve lifecycle and physics

Define SI units, axes/polarization, material/spectrum/boundaries, metric and tolerance.
Audit affected symbols, never infer them from another solver. The following API
details describe the snapshot: verify changed behavior against the selected runtime.

- Place outside JIT; keep resolved `config` from `place_objects` (fifth return is
  placement info, not a key). Inspect realized grid/slices, PML clearance, planes,
  dtype, devices, time step/steps and memory before compiling/solving.
- Keep both `arrays` and `objects` from `apply_params`; split PRNG keys for
  `run_fdtd`. Use fresh field/detector state; never reuse donated arrays.
- TreeClass fields are generally immutable/keyword-only: use `.aset`/`.at`.
  `= null` means required, not a default. `key=None` can hide accidental reuse.
- Fields: `(3,Nx,Ny,Nz)`; detectors add latent time. Anchors: `-1/0/+1`, offsets:
  `margins`/`grid_margins`. Cell rounding resolves to `RectilinearGrid`; inspect it.
- Negative epsilon needs stable dispersion. Nonzero Bloch vectors: rad/m and
  complex fields; `PeriodicBoundary` is zero Bloch. Symmetry `0/-1/+1` means
  none/PEC/PMC; unfold for full-domain comparisons.
- Field/phasor reduction is a weighted mean, energy a volume integral, flux an
  oriented face-area integral. Check finite/nonzero signals, keys, shapes, signs,
  units and reference normalization before interpreting metrics.
- Reversible gradients need `Recorder`; checkpointed mode needs `num_checkpoints`.
  Custom stopping is incompatible with gradient mode. Verify device placement,
  divisibility, numerical parity and measured scaling before GPU/multi-device claims.

## Validate within authorization

Reuse unchanged evidence for local edits. Follow workspace contracts before solves,
optimization or expensive extraction; checklists authorize no additional runs.
Establish/reuse physical references and grid/runtime/PML/placement convergence
within the approved budget. Report pending checks instead of extending it silently.
Record runtime/API provenance, backend/devices/dtype, seeds/grid, timing,
normalization, convergence and limitations. Import/placement checks or plausible
plots alone do not validate scientific results.
