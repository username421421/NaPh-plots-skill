---
name: fdtdx
description: Use when creating, reviewing, debugging, optimizing, or validating FDTDX electromagnetic simulations in Python/JAX, including grids, materials and dispersion, placement, PML/Bloch/periodic/PEC/PMC boundaries, plane/mode/dipole/TFSF sources, detectors/phasors/flux/S-parameters/far fields, quasi-2D, symmetry, GDS/I/O, JIT/multi-device execution, and reversible or checkpointed inverse design. Also use for FDTDX installation/backend problems or exact API guidance from bundled current docs, source, tests, notebooks, and examples.
---

# FDTDX

Build source-grounded FDTDX simulations and validate their numerical and physical correctness. Target the newest official upstream FDTDX source available at task time. Treat the bundled corpus as a versioned offline fallback, not as the latest API or as interchangeable snippets.

## Start with the latest upstream API and installed runtime

Resolve the latest official FDTDX release/source at task time from PyPI and the official GitHub repository. Prefer the newest published release for executable and production work; use the development branch only when it is explicitly requested or is the only source containing the required fix. Record the target release and source commit. Never infer “latest” from the bundled corpus or from a package version string alone.

1. Run the environment check from this skill directory with the project's intended interpreter, not an unrelated system Python:

   ```powershell
   & "<project-directory>\.venv\Scripts\python.exe" scripts\fdtdx_doctor.py --project "<project-directory>"
   ```

   On POSIX use `<project-directory>/.venv/bin/python`; with uv, `uv run --project <project-directory> python scripts/fdtdx_doctor.py ...` is also suitable.

2. Inspect the exact symbol in the installed runtime before writing code:

   ```powershell
   & "<project-python>" scripts\fdtdx_docs.py api SimulationConfig
   & "<project-python>" scripts\fdtdx_docs.py api SimulationObject --member place_relative_to
   ```

3. Compare the installed runtime with the latest upstream target. If they differ, inspect the installed source and project lock file. Upgrade the project environment before implementation when the task includes an upgrade; otherwise report the mismatch and do not mix latest documentation with an older runtime. Never silently upgrade or mix APIs.

The bundled corpus contains historical API examples and may differ from both the latest upstream source and the installed runtime. Read `references/capabilities-and-versioning.md` whenever compatibility matters.

## Use the source hierarchy

For the target API, trust sources in this order:

1. Latest official FDTDX release/source resolved at task time.
2. User's installed package and project source for runtime compatibility.
3. `doc/api-index.json` and `doc/package-src/` as an offline fallback.
4. `doc/tests/` for supported behavior and validated physics.
5. `doc/examples/` for complete application architecture.
6. `doc/readthedocs/` and `doc/notebooks/` for concepts and tutorials.

The rendered tutorials contain legacy constructors and a stale claim that dispersion is unavailable. Never copy a notebook block without checking the API index and current tests.

Use the local query tool before browsing:

```powershell
python scripts/fdtdx_docs.py manifest
python scripts/fdtdx_docs.py search "ModeOverlapDetector|calculate_sparam" --max-results 40
python scripts/fdtdx_docs.py toc doc/notebooks/markdown/04_basic_simulation.md
python scripts/fdtdx_docs.py section doc/package-src/fdtdx/config.py "class SimulationConfig"
python scripts/fdtdx_docs.py examples
```

Use live official primary sources to resolve the latest upstream version and API at each FDTDX task. If live verification is unavailable, say so explicitly and do not claim that the bundled corpus is current. State the target version/commit and the installed runtime version/commit used.

## Follow the implementation workflow

1. **Define the physics.** State SI units, axes, propagation/polarization, material model, spectrum, boundary assumptions, reported metric, and tolerance.
2. **Select a validated pattern.** Route through `references/navigation.md`; begin with a current test for correctness or an example for application structure.
3. **Audit every symbol.** Query constructors and methods with `fdtdx_docs.py api`; do not infer arguments from Meep, Lumerical, Tidy3D, or old FDTDX code.
4. **Construct and place.** Build objects and constraints, then run `place_objects` outside JIT. Keep its returned resolved `config`; its fifth return is placement information, not a PRNG key.
5. **Inspect before solving.** Check realized grid/dimensions, object slices, PML clearance, source/detector planes, field dtype, backend/devices, time step, total steps, and memory estimate. Plot the setup when useful.
6. **Transform and run.** Keep both `arrays` and `objects` returned by `apply_params`; run `run_fdtd` with an explicit split key. Treat every run as a fresh field/detector state.
7. **Validate.** Assert finite/nonzero signals, correct detector keys/shapes/sign/units, and a physical reference. Sweep grid, runtime/ringdown, PML, and placement until the reported metric converges.
8. **Report reproducibly.** Record both the latest upstream target release/commit and the installed package commit/API shape, plus JAX/backend/devices, dtype, seeds, realized grid, timing, normalization, convergence data, and limitations.

Read `references/workflows.md` for the canonical lifecycle and task procedures. Read `references/convergence-validation.md` before accepting scientific results.

## Apply these guardrails

- Use SI units. Field arrays use `(3, Nx, Ny, Nz)`; detector states add a leading latent-time dimension.
- Use keyword arguments. Most public TreeClass fields are keyword-only and immutable; update with `.aset(...)` or `.at[...]`.
- In introspected signatures, `= null` is TreeClass's required-field sentinel, not a usable default; supply the field.
- Split PRNG keys explicitly. `key=None` is deterministic but can conceal accidental reuse.
- Position anchors are numeric `-1`, `0`, `+1`. Current offset names are `margins` and `grid_margins`.
- Real dimensions round to cells. Placement resolves grid policies to a concrete `RectilinearGrid`; inspect rather than assume dimensions.
- Model negative epsilon with stable dispersion, not a nonpositive static diagonal permittivity. Validate spectra and time-step stability.
- Nonzero Bloch vectors are in rad/m and require complex fields. `PeriodicBoundary` is the zero-vector Bloch alias.
- Symmetry entries are `0` none, `-1` PEC, `+1` PMC; unfold reduced outputs before full-domain comparison.
- Match detector semantics: field/phasor reduction is a weighted mean, energy is a volume integral, and Poynting flux is an oriented face-area integral.
- A reversible `GradientConfig` needs a `Recorder`; checkpointed mode needs `num_checkpoints`. Custom stopping conditions cannot be combined with gradient mode.
- Keep placement outside JIT. Compile only after shapes are resolved; never reuse donated arrays.
- Do not claim GPU or multi-device execution from configuration alone. Verify `jax.devices()`, buffer placement, divisibility, numerical parity, and target-machine scaling.

## Route references deliberately

- Task and file routing: `references/navigation.md`
- End-to-end patterns: `references/workflows.md`
- Supported surface, limits, version drift: `references/capabilities-and-versioning.md`
- Numerical, physics, detector, and gradient checks: `references/convergence-validation.md`
- JIT, memory, backends, sharding, autodiff: `references/jax-performance.md`
- Failure diagnosis: `references/troubleshooting.md`
- Corpus provenance and refresh procedure: `references/corpus-manifest.md`

The corpus includes the official Read the Docs HTML archive plus all 141 standalone API pages, searchable Markdown for both, Sphinx source, nine official notebook sources and Markdown conversions, all eight examples, all 108 package Python files, all 173 test Python files, lock metadata, and a 141-export introspected API index.

## Finish with evidence

For code changes, run the smallest relevant bundled-equivalent test or analytic check first, then the requested workflow. Do not present a plausible plot or a single-resolution number as validated. If a full solve is too expensive, still verify import/API shape, placement, compiled structure where feasible, and provide the exact convergence/physics checks that remain.
