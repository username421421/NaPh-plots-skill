# FDTDX Capabilities and Versioning

## Contents

- [Source-of-truth order](#source-of-truth-order)
- [Offline snapshot capability matrix](#offline-snapshot-capability-matrix)
- [Known limits and snapshot documentation drift](#known-limits-and-snapshot-documentation-drift)
- [Version-mismatch policy](#version-mismatch-policy)

## Source-of-truth order

For executable behavior, trust the campaign's selected installed source and
version-matched tests/docs. Record interpreter, module path, package version,
source commit when available, and lock metadata. Resolve official upstream for
requested upgrades, latest-capability questions, or unresolved compatibility;
keep its target release/commit separate from the installed runtime. For a new
project without a runtime, select an official release before coding.

The bundled corpus is an offline snapshot at commit
`b93f90412db852527393c4a95a448c25aed1f6a8`, reporting version 0.6.2. Its API index,
source, tests, examples, and tutorials describe that snapshot, not necessarily the
installed or latest API. Read `references/corpus-manifest.md` for provenance.

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

Use `python scripts/fdtdx_docs.py api <symbol> --source snapshot` for indexed snapshot fields and docs. Use the project interpreter with `--source installed` for the actual runtime signature and requested member. The default remains snapshot and is labeled in output.

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

For changed FDTDX API behavior:

1. Identify the selected interpreter and dependency/source pins.
2. Run `fdtdx_doctor.py --project <project>` with that interpreter when environment evidence is missing or changed.
3. Inspect affected symbols with `fdtdx_docs.py api <symbol> --source installed`; this imports the package but does not solve.
4. Compare with matching source/tests. Consult official upstream when the task requires a newer target or evidence is unresolved; never silently upgrade.
5. Label snapshot-specific examples. Missing installed imports/symbols are failures, not permission to fall back to the snapshot.
6. Record inspected versions/commits and reuse verified evidence for unchanged behavior. Documentation-only edits do not require a fresh backend check.
