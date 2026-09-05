# FDTDX Convergence and Validation

## Contents

- [Required validation plan](#required-validation-plan)
- [Numerical convergence](#numerical-convergence)
- [Physics references](#physics-references)
- [Detector semantics](#detector-semantics)
- [Gradient validation](#gradient-validation)
- [Result acceptance checklist](#result-acceptance-checklist)

## Required validation plan

For scientific acceptance, establish or reuse applicable evidence. This checklist does not authorize a solve or sweep. Follow the workspace execution contract; documentation-only edits need no numerical rerun. Report performed, reused, and pending checks.

Define before running:

1. The reported scalar/vector metric and acceptable tolerance.
2. The analytic, conservation, reciprocity, symmetry, or blank/reference result used for comparison.
3. The resolution, runtime/ringdown, PML, source, and detector sweeps.
4. The expected sign, units, normalization, shape, and dtype.
5. Runtime/memory limits and whether JIT compilation time is separated from execution time.

Do not treat a plausible field plot as validation. Stop at the approved runtime/memory or sweep budget and report incomplete convergence; do not expand the campaign automatically.

## Numerical convergence

Sweep one control at a time while keeping the physical geometry fixed:

- Refine grid spacing; include the smallest wavelength inside the highest-index material and the smallest geometry feature.
- Increase simulation duration or tighten the stopping condition; verify pulse clearing or steady-state/ringdown convergence.
- Increase PML thickness and source/structure/PML separation.
- Move detectors and sources modestly to expose near-field or injection artifacts.
- Increase the phasor/FFT window and frequency resolution for narrow features or high-Q structures.
- For nonuniform grids, refine the critical region and remember that the global time step follows the minimum spacing.
- Compare with and without optional symmetry reduction.

Record metric change, runtime, compiled shapes, and memory for every point.

## Physics references

Use the bundled tests as executable acceptance patterns:

- Phase velocity and normalized impedance: `doc/tests/simulation/physics/test_plane_wave.py`.
- Fresnel reflection/transmission and conservation: `test_fresnel.py`.
- Loss and skin depth: `test_skin_depth.py`.
- Mie scattering/quasi-2D/reference irradiance: `test_mie_scattering.py`.
- Bloch/oblique propagation: `boundaries/test_bloch_oblique.py`.
- PEC/PMC reflection and parity: boundary tests.
- Source temporal/spectral behavior: `sources/test_temporal_profiles.py`.
- Pulsed versus CW agreement: `fdtd/test_pulsed_vs_cw.py`.
- Time-domain versus phasor flux: `test_phasor_poynting_flux.py`.
- Dispersion/anisotropy: `test_dispersion.py`, `test_anisotropic_dispersion.py`, `test_birefringence.py`.
- S-parameters: `test_sparams.py`.

For normalized ratios, reject zero, near-zero, or nonfinite reference signals before division.

## Detector semantics

- Reduced `FieldDetector` and `PhasorDetector` values are weighted means.
- `EnergyDetector` reduction is a volume integral.
- `PoyntingFluxDetector` is a face-area integral; orientation/direction controls sign.
- Plane flux/mode detectors require an unambiguous singleton normal axis.
- Phasors require complex-compatible dtype/state and a physically adequate sampling window.
- `EnergyDetector(as_slices=True, reduce_volume=True)` is invalid.
- Whole-period CW windows prevent phase/window bias; use the same window when comparing time and frequency domain results.
- Verify detector state keys and array axes from the API/source rather than assuming a shape.

## Gradient validation

For inverse design:

1. Assert finite loss and finite, nonzero gradients.
2. Spot-check selected parameters with centered finite differences.
3. Compare reversible and checkpointed differentiation for lossy/dispersive or long simulations.
4. Increase `num_checkpoints_reversible` if reverse reconstruction drifts.
5. Keep projection/filter continuation schedules explicit and log their values.
6. Validate the final design with a forward-only run at converged physics settings.
7. Guard objectives against near-zero denominators.

Do not reuse arrays after passing them through a JIT function with donated buffers.

## Result acceptance checklist

- All arrays and metrics are finite.
- Expected sources and detectors receive nonzero signal.
- Signs, units, normalization, component order, and propagation direction are explicit.
- Geometry, sources, detectors, and PML do not overlap unintentionally.
- The result is stable to grid, runtime, PML, and placement sweeps within tolerance.
- A physical reference or invariant passes.
- Symmetry/Bloch/periodicity assumptions are independently checked.
- The exact FDTDX/JAX versions, backend, dtype, grid, seed, and solver settings are recorded.
- Plot/table generation is reproducible from saved raw data.
