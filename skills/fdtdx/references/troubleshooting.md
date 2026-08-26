# FDTDX Troubleshooting

## Contents

- [Import or backend failures](#import-or-backend-failures)
- [Placement failures](#placement-failures)
- [Divergence or nonfinite fields](#divergence-or-nonfinite-fields)
- [Zero or wrong detector results](#zero-or-wrong-detector-results)
- [Mode and S-parameter problems](#mode-and-s-parameter-problems)
- [Dispersion failures](#dispersion-failures)
- [JIT, memory, and sharding failures](#jit-memory-and-sharding-failures)
- [Serialization and export failures](#serialization-and-export-failures)

## Import or backend failures

1. Run `python scripts/fdtdx_doctor.py --project <project>`.
2. Confirm the active interpreter/venv and editable project path.
3. Check Python is `>=3.11,<3.15`.
4. Inspect `jax.devices()` before setting `backend="gpu"` or `"tpu"`.
5. On native Windows, expect CPU unless using an unofficial stack; use WSL/Linux for official CUDA JAX.
6. If Tidy3D configuration initialization blocks in a restricted environment, set `TIDY3D_BASE_DIR` to a writable directory for that process.

## Placement failures

Search the exact exception in `doc/tests/integration/placement/` and inspect the current `SimulationObject` member through the API script.

Common causes:

- A `None` size expanded to the domain but another constraint tries to reposition/resize it.
- Conflicting position, size, extension, grid-coordinate, or real-coordinate constraints.
- Duplicate object names.
- An extension target/direction is inconsistent or unresolved.
- Grid and real sizes round to incompatible cells.
- Symmetry requires an even cell count on each reduced axis.

Call `plot_setup` and inspect placed slices immediately after `place_objects`.

## Divergence or nonfinite fields

- Reduce the Courant factor and verify the realized grid's minimum spacing.
- Refine under-resolved geometry/material wavelengths.
- Check material tensor positive-definiteness where required.
- Replace static negative epsilon with Drude/Lorentz/CCPR dispersion.
- Check dispersive stability (`gamma*dt`, `omega0*dt`, CCPR divisor) against source/tests.
- Increase PML thickness/distance and ensure incompatible structures do not enter PML.
- Test a vacuum/background-only scene and one source at a time.

## Zero or wrong detector results

- Confirm the detector switch is on after fields arrive and covers enough periods/ringdown.
- Check source polarization, propagation axis/direction, detector normal, and requested components.
- Verify the detector is outside PML and not on a field node.
- Inspect detector state keys and shapes; do not assume component order.
- Use whole-period steady-state windows for phasors.
- Check `reduce_volume`, `aggregate`, and `as_slices` semantics.
- Assert finite and nonzero reference signals before normalization.

## Mode and S-parameter problems

- Verify source/detector cross section, material extension, mode index, polarization filter, and propagation direction.
- Extend waveguide material into PML where the validated S-parameter workflow requires it.
- Use a pulsed `ModePlaneSource`, source-normalization `ModeOverlapDetector`, output overlaps, and the public `calculate_sparam(s)` helpers.
- Keep `(detector_name, source_name)` result keys explicit.
- Move mode planes away from discontinuities and confirm the computed mode profile.
- Do not use the manual/private mode-analysis path from `width_sweep_analysis.py` as the default API.

## Dispersion failures

- Validate the intended epsilon spectrum with `compute_eps_spectrum_from_coefficients` before simulation.
- Use `eps_inf >= 1` unless current source/tests explicitly justify another value.
- Enforce time-step stability restrictions from `doc/package-src/fdtdx/dispersion.py` and dispersion tests.
- Full off-diagonal anisotropy plus dispersion is not implemented.
- Off-diagonal conductivity plus dispersion is rejected.
- Compare to a nondispersive/vacuum reference and analytic propagation/attenuation.

## JIT, memory, and sharding failures

- Recompile after any static structure/shape/dtype/boundary change.
- Do not mutate Python state or perform plotting/file I/O inside JIT.
- Do not reuse donated buffers.
- Ensure PRNG keys and arrays live on devices compatible with the configured backend/sharding.
- Ensure the sharded dimension is divisible by device count.
- Reduce detector recording, domain size, dtype, gradient checkpoints, or design complexity before changing physics.

## Serialization and export failures

- JSON embeds an FDTDX version; treat version drift explicitly.
- VTI is for uniform grids; use VTR for nonuniform rectilinear grids.
- Validate array shape, dtype, offsets, and slices before snapshot export.
- STL expects a suitable binary 3D voxel representation.
- GDS helpers may need optional dependencies and valid layer/cell/port axis metadata.
- Use the matching tests under `doc/tests/unit/conversion/` and `doc/tests/integration/conversion/`.
