# FDTDX Task Navigation

## Contents

- [Fast local lookup](#fast-local-lookup)
- [Task-to-source map](#task-to-source-map)
- [Public API categories](#public-api-categories)
- [Choosing examples versus tests](#choosing-examples-versus-tests)

## Fast local lookup

Run commands from the skill root:

```powershell
python scripts/fdtdx_docs.py manifest
python scripts/fdtdx_docs.py search "BlochBoundary|bloch_vector" --max-results 40
python scripts/fdtdx_docs.py search "place_objects(" --literal --max-results 40
python scripts/fdtdx_docs.py api SimulationConfig
python scripts/fdtdx_docs.py api SimulationObject --member place_relative_to
python scripts/fdtdx_docs.py toc fdtdx.Material --kind docs
python scripts/fdtdx_docs.py toc doc/notebooks/markdown/04_basic_simulation.md
python scripts/fdtdx_docs.py compose doc/notebooks/markdown/02_mode_source_detector.md --title "Simulation Scene"
python scripts/fdtdx_docs.py examples
```

Use `rg` directly for cross-file audits:

```powershell
rg -n "SimulationConfig|UniformGrid|place_objects|apply_params|run_fdtd" doc/examples doc/tests
rg -n "LorentzPole|DrudePole|CCPRPole|dispersion" doc/package-src doc/tests doc/examples
rg -n "ModeOverlapDetector|calculate_sparam|PortSpec" doc/package-src doc/tests
```

## Task-to-source map

| Task | Open first | Then inspect |
| --- | --- | --- |
| Install/backend diagnosis | `references/jax-performance.md` | `scripts/fdtdx_doctor.py`, bundled `doc/pyproject.toml` |
| JAX/TreeClass fundamentals | `doc/notebooks/markdown/01_jax_introduction.md` | `doc/package-src/fdtdx/core/jax/`, `references/jax-performance.md` |
| Minimal current simulation | `references/workflows.md` | `doc/tests/simulation/physics/test_plane_wave.py` |
| Materials and objects | `doc/notebooks/markdown/02_basic_materials.md` | `doc/package-src/fdtdx/materials.py`, `doc/tests/unit/test_materials.py` |
| Object placement and sizing | `doc/notebooks/markdown/03_object_placement_guide.md` | `doc/tests/integration/placement/test_constraint_placement.py` |
| Uniform/Gaussian source | `doc/tests/simulation/physics/sources/test_plane_source.py` | `test_gaussian_source.py`, `test_temporal_profiles.py` |
| Mode source/detector | `doc/notebooks/markdown/02_mode_source_detector.md` | `doc/tests/simulation/physics/sources/test_mode_source.py` |
| Dipole/TFSF sources | `doc/tests/simulation/physics/sources/test_dipole_radiation.py` | `test_tfsf_region.py`, `test_tfsf_grid_normalization.py` |
| PML/periodic/Bloch/PEC/PMC | `doc/tests/simulation/physics/boundaries/` | `doc/package-src/fdtdx/objects/boundaries/` |
| Mirror symmetry/reduction | `doc/tests/simulation/physics/boundaries/test_simulation_symmetry.py` | `doc/tests/integration/fdtd/test_symmetry_reduction.py` |
| Nonuniform grid | `doc/tests/simulation/physics/test_nonuniform_grid.py` | `doc/tests/unit/core/test_grid.py` |
| Quasi-2D simulation | `doc/tests/simulation/physics/test_mie_scattering.py` | `doc/notebooks/markdown/01_2d_simulation.md` (older pattern) |
| Phasors/steady state | `doc/tests/simulation/physics/test_phasor_poynting_flux.py` | `doc/tests/unit/objects/detectors/test_phasor.py` |
| Flux, energy, normalization | `doc/tests/simulation/physics/test_fresnel.py` | `doc/tests/unit/objects/detectors/` |
| Modes/S-parameters | `doc/tests/simulation/physics/test_sparams.py` | `doc/package-src/fdtdx/utils/sparams.py` |
| Field projection/far field | `doc/tests/unit/objects/detectors/test_field_projection.py` | `doc/package-src/fdtdx/objects/detectors/field_projection.py` |
| Dispersion | `doc/examples/dispersive_gaussian_pulse.py` | `hyperbolic_dispersive_slab.py`, dispersion tests |
| Anisotropy | `doc/examples/simulate_gaussian_source_anisotropic.py` | `simulate_gaussian_source_fully_anisotropic.py`, `test_birefringence.py` |
| Bloch band structure | `doc/examples/bloch_band_structure.py` | `test_bloch_oblique.py`, `test_bloch_zero_vector.py` |
| Inverse design/adjoint | `doc/examples/optimize_ceviche_corner.py` | `doc/tests/simulation/fdtd/test_fdtd.py`, `test_time_reversal.py`, Device tests, `references/jax-performance.md` |
| Stopping conditions | `doc/tests/unit/fdtd/test_stop_conditions.py` | `doc/tests/integration/fdtd/test_stop_conditions.py` |
| GDS | `doc/package-src/fdtdx/objects/static_material/gds_layer_stack.py` | GDS layer-stack tests |
| JSON/STL/VTK | `doc/tests/integration/conversion/` | `doc/package-src/fdtdx/conversion/` |
| Plotting/video/logging | current public examples | `doc/package-src/fdtdx/utils/`, detector plotting tests |
| Multi-device/sharding | `doc/tests/unit/core/jax/test_sharding.py` | `references/jax-performance.md` |
| Contributing/internal changes | `doc/readthedocs/source/05_contributing.rst` | mirrored source and tests |

## Public API categories

- Lifecycle/config: `SimulationConfig`, `GradientConfig`, grids, containers, `place_objects`, `apply_params`, `run_fdtd`, `full_backward`.
- Materials/dispersion: `Material`, pole classes, `DispersionModel`, coefficient/spectrum helpers.
- Geometry/placement: `SimulationObject`, constraints, volume, primitives, polygons, GDS helpers.
- Boundaries/symmetry: `BoundaryConfig`, PML/Bloch/Periodic/PEC/PMC, unfold helpers.
- Sources/profiles: plane, Gaussian, mode, dipole, TFSF, `WaveCharacter`, temporal profiles, `OnOffSwitch`.
- Detectors/metrics: field, energy, phasor, flux, mode overlap, field projections, normalization functions.
- Inverse design: `Device`, transformations, projections, smoothing, discretization, symmetry and morphology modules.
- I/O/utilities: JSON/STL/VTI/VTR, plotting, logger, S-parameters, PML extension.

Use the API query script instead of relying on this category list for arguments.

## Choosing examples versus tests

- Start from a current test when correctness and a minimal setup matter.
- Start from an example when the task needs a complete application architecture, visualization, optimization loop, or analysis pipeline.
- Preserve the physical validation from the test when adapting an example.
- Do not copy private attributes or internal functions from `width_sweep_analysis.py` without auditing the source; its manual mode analysis is not the preferred public S-parameter workflow.
- Do not use older notebook constructors without checking `doc/api-index.json`.
- Use `doc/readthedocs/api-markdown/fdtdx.<Symbol>.md` when the exact official rendered API page matters; use the API query command for faster signature/member lookup.
