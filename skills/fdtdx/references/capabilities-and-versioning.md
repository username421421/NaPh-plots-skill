# FDTDX Capabilities and Versioning

## Contents

- [Source-of-truth order](#source-of-truth-order)
- [Offline snapshot capability matrix](#offline-snapshot-capability-matrix)
- [Known limits and snapshot documentation drift](#known-limits-and-snapshot-documentation-drift)
- [Version-mismatch policy](#version-mismatch-policy)

## Source-of-truth order

For new work, use this order when sources disagree:

1. The latest official FDTDX release/source resolved at task time.
2. The user's installed FDTDX version and project source, which determine what can actually run.
3. The bundled API index and package source snapshot under `doc/api-index.json` and `doc/package-src/`, as an offline fallback.
4. Bundled tests under `doc/tests/`; they encode supported behavior and physics checks for the snapshot.
5. Bundled examples and documentation snapshots under `doc/examples/`, `doc/readthedocs/`, and `doc/notebooks/`.

The bundled corpus is a historical offline snapshot of FDTDX current main at commit `b93f90412db852527393c4a95a448c25aed1f6a8`, which reported package version 0.6.2. It is not authoritative for the latest upstream API; resolve the latest release/source from official upstream at task time. Read `references/corpus-manifest.md` for provenance.

## Offline snapshot capability matrix

| Area | Supported surface |
| --- | --- |
| Solver | Explicit 3D Yee-grid FDTD through `place_objects -> apply_params -> run_fdtd` |
| Grids | `UniformGrid`, `QuasiUniformGrid`, realized `RectilinearGrid`; CFL uses the smallest axis spacing |
| Materials | Isotropic, diagonal anisotropic, full tensor material properties, conductivity, per-axis dispersive poles subject to restrictions |
| Dispersion | `LorentzPole`, `DrudePole`, `CCPRPole`, `DispersionModel`; spectral/coefficient helpers and source correction |
| Geometry | Simulation volume, uniform material objects, cylinders, spheres, extruded polygons, GDS layer stacks, parameterized `Device` objects |
| Placement | Relative/absolute positions, grid coordinates, same/relative sizes, face placement, extension to objects or domain boundaries |
| Boundaries | PML, Bloch, zero-vector periodic alias, PEC, PMC, and domain-reducing mirror symmetry |
| Sources | Uniform/Gaussian plane, guided mode plane, point dipole, temporal profiles, TFSF source region |
| Detectors | Field, energy, phasor, Poynting flux, closed-surface flux, mode overlap, angular/cartesian/k-space field projection |
| Analysis | Energy/power/flux metrics, normalization, modes, S-parameters, plotting, videos, logging |
| Differentiation | Reversible and checkpointed gradients; recorder modules and parameter transformations for inverse design |
| Scaling | JAX JIT, device sharding helpers, CPU/GPU/TPU/Metal backend selection |
| I/O | JSON setup serialization, STL export, uniform-grid VTI, rectilinear-grid VTR, array snapshots, GDS import helpers |
| Symmetry | PEC/PMC mirror reduction plus unfold helpers for fields, detectors, and modes |

Use `python scripts/fdtdx_docs.py api <symbol>` for exact fields, signatures, methods, and docstrings.

## Known limits and snapshot documentation drift

- The current solver is 3D. “2D” means a thin periodic extrusion, not a separate true-2D solver. Use the validated pattern in `doc/tests/simulation/physics/test_mie_scattering.py`.
- The notebook `02_basic_materials` says dispersion is not implemented; that statement is stale. Version 0.6.2 includes dispersive poles and validated examples/tests.
- Older notebooks and tagged/PyPI `v0.6.2` construct `SimulationConfig(resolution=...)`. The bundled current-main snapshot uses `SimulationConfig(grid=UniformGrid(spacing=...), time=...)`. Prefer the installed signature, then current examples, tests, API index, and source.
- Full off-diagonal anisotropy together with dispersion is not implemented. Off-diagonal conductivity together with dispersion is rejected. Per-axis dispersive poles are supported.
- A static nonpositive permittivity is numerically unsafe; represent metals/negative epsilon with a stable dispersive model and validate its spectrum.
- `Material` stores forward relative tensors; inverse material arrays are created for the solver. Material/device index order is sorted by electromagnetic properties, not input-dictionary order.
- Device parameter transforms execute in the order supplied. On nonuniform grids, physical-unit design voxels are not implemented; use `partial_voxel_grid_shape` after auditing the realized mesh.
- `DiffractiveDetector` and stopping-condition subclasses exist internally but are not root-public exports in this snapshot. Do not advertise or import them from `fdtdx` without checking the installed source.
- The rendered API text describes `UniformMaterialObject` as abstract, but current source, examples, and tests instantiate it directly. Follow installed source/tests for this inconsistency.
- The repository has sharding unit tests but no end-to-end real multi-GPU physics/scaling benchmark. Do not claim multi-GPU correctness or scaling without testing the target machine.
- Native Windows normally receives CPU-only official JAX wheels. Use Linux/WSL for official NVIDIA CUDA wheels.
- Some public examples are intentionally large or analysis-specific. Prefer tests as minimal validated patterns; use the examples as architecture.

## Version-mismatch policy

Before writing or modifying FDTDX code:

1. Resolve the latest official release/source from PyPI and the official GitHub repository; record its version and commit.
2. Run `python scripts/fdtdx_doctor.py --project <project>` with the project's intended interpreter.
3. Compare the installed source commit, public exports, and key signatures with the latest target; package version alone is not sufficient.
4. If they differ, inspect the installed signature/source (`inspect.signature`, `inspect.getsourcefile`) and the project's lock file. Upgrade the project before implementation when the task includes an upgrade; otherwise do not mix APIs.
5. Use the bundled API index/source only as a fallback and label any snapshot-specific behavior.
6. When live docs or source are consulted, record the target and installed version/commit in implementation notes.
