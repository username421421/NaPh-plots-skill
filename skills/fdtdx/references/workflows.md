# FDTDX Workflows

## Contents

- [Current simulation lifecycle](#current-simulation-lifecycle)
- [Build and inspect a scene](#build-and-inspect-a-scene)
- [Choose source and detector timing](#choose-source-and-detector-timing)
- [Extract modes and S-parameters](#extract-modes-and-s-parameters)
- [Model dispersion and anisotropy](#model-dispersion-and-anisotropy)
- [Build a quasi-2D simulation](#build-a-quasi-2d-simulation)
- [Sweep Bloch bands](#sweep-bloch-bands)
- [Run inverse design](#run-inverse-design)
- [Use symmetry, GDS, and exports](#use-symmetry-gds-and-exports)

## Current simulation lifecycle

Use this lifecycle for the bundled current-main snapshot. It deliberately keeps placement outside JIT and retains every returned object that may have been resolved or updated.

```python
import fdtdx
import jax
import jax.numpy as jnp

root_key = jax.random.key(0)
placement_key, transform_key, simulation_key = jax.random.split(root_key, 3)

config = fdtdx.SimulationConfig(
    time=120e-15,
    grid=fdtdx.UniformGrid(spacing=50e-9),
    backend="cpu",  # choose only after checking jax.devices()
    dtype=jnp.float32,
)
volume = fdtdx.SimulationVolume(partial_real_shape=(2e-6, 2e-6, 4e-6))

boundary_config = fdtdx.BoundaryConfig.from_uniform_bound(thickness=10)
boundaries, boundary_constraints = fdtdx.boundary_objects_from_config(
    boundary_config,
    volume,
)

object_list = [volume, *boundaries.values()]  # add geometry, sources, detectors
constraints = [*boundary_constraints]         # add their placement constraints

objects, arrays, params, config, placement_info = fdtdx.place_objects(
    object_list=object_list,
    constraints=constraints,
    config=config,
    key=placement_key,
)

arrays, objects, transform_info = fdtdx.apply_params(
    arrays=arrays,
    objects=objects,
    params=params,
    key=transform_key,
)

time_step, arrays_out = fdtdx.run_fdtd(
    arrays=arrays,
    objects=objects,
    config=config,
    key=simulation_key,
    show_progress=False,
)
```

Contracts that prevent subtle failures:

- Keep the `config` returned by `place_objects`; it contains the realized grid and any symmetry reduction.
- Treat the fifth `place_objects` return as an information dictionary, never as a PRNG key.
- Keep both `arrays` and `objects` returned by `apply_params`; device and source transformations can update both.
- Read detector data from `arrays_out.detector_states[name][state_key]` after checking the placed detector and its state shape.
- A new `run_fdtd` call resets dynamic fields and detector states. It is a fresh run, not a continuation.
- Some bundled application examples reuse one PRNG key across lifecycle stages; split placement, transformation, and simulation keys when adapting them.
- Tagged/PyPI `v0.6.2` used `SimulationConfig(resolution=...)`; current main uses `grid=UniformGrid(spacing=...)`. Inspect the installed signature before adapting either form.

## Build and inspect a scene

1. Express all lengths in SI units and state the axes, propagation direction, polarization, and material reference frequency.
2. Create the volume, materials, geometry, sources, detectors, and boundary objects.
3. Add explicit constraints. Position anchors are numeric `-1`, `0`, and `+1`; current offset keywords are `margins` and `grid_margins`.
4. Resolve with `place_objects` outside JIT.
5. Inspect the returned `config.resolved_grid`, object slices, rounded dimensions, and placement information.
6. Call `fdtdx.plot_setup(...)` before an expensive solve and check source/detector/PML overlap.
7. Estimate memory from cells, six field components, dtype, PML/dispersion state, detectors, and gradient recording.

For a small, validated plane-wave scene, adapt `doc/tests/simulation/physics/test_plane_wave.py`. It uses periodic transverse boundaries, PML along propagation, a one-cell `UniformPlaneSource`, and reduced phasor detectors. Preserve its nonzero-signal, phase-velocity, and impedance checks.

Object trees are immutable. Use functional updates such as `obj.aset("field", value)` or `.at[...]`; do not assign attributes. Higher `placement_order` overwrites lower material placement order.

## Choose source and detector timing

Use `WaveCharacter` with exactly one of `wavelength`, `frequency`, or `period`.

- For steady monochromatic fields, use `SingleFrequencyProfile`, allow startup/ringdown, and record an integer number of periods.
- For broadband spectra, S-parameters, and pulse clearing, use `GaussianPulseProfile(center_wave=..., spectral_width=...)` and verify the source spectrum covers every reported frequency.
- Use `OnOffSwitch` to define sampling rather than silently accepting all time steps.
- Use a phasor detector for complex amplitude/phase, Poynting detectors for oriented area-integrated flux, energy detectors for volume-integrated energy, and field detectors for field samples.
- Detector states include a leading latent-time dimension. Never guess axis order or reduction semantics; inspect the test/source for that detector.

Route to `doc/tests/simulation/physics/sources/` for source timing and to `doc/tests/unit/objects/detectors/` for detector state semantics. Validate pulse-versus-CW consistency, whole-period phasor windows, and finite nonzero reference signals.

## Extract modes and S-parameters

Prefer the public workflow in `doc/tests/simulation/physics/test_sparams.py` and `doc/package-src/fdtdx/utils/sparams.py`:

1. Inject a pulsed `ModePlaneSource` at the input port.
2. Add a same-mode `ModeOverlapDetector` beside the source for input normalization.
3. Add output `ModeOverlapDetector` objects with `scaling_mode="pulse"`.
4. Resolve placement, then call `extend_material_to_pml` when a waveguide enters PML.
5. Call `calculate_sparam` for one active input or `calculate_sparams` across inputs.
6. Interpret keys as `(detector_name, source_name)` and verify the expected vector shape/frequency order.
7. Check power conservation, reciprocity where applicable, detector-position stability, and a straight/reference device.

The current helper divides by the input-mode overlap without a near-zero threshold. Reject nonfinite or implausibly large ratios and verify the normalization detector's returned state is finite and nonzero. In `test_sparams.py`, trust the executable assertion (over 99% for its lossless straight guide) rather than the stale prose that says 90%.

`setup_sparams_simulation(...)` is a convenience helper for polygon/GDS-derived layouts. Its own argument is named `resolution`; that does not mean current `SimulationConfig` accepts `resolution`. In this snapshot the helper's mode detectors retain the default `scaling_mode="continuous"`, while the validated broadband manual pattern uses `"pulse"`; audit the returned setup or prefer the manual workflow. `PortSpec.center` is measured from the core-region origin, excluding PML padding.

The mode source/detector relies on Tidy3D. Confirm optional configuration, cross-section materials, mode index, polarization filter, and propagation direction. In restricted environments, point `TIDY3D_BASE_DIR` at a persistent writable directory before importing FDTDX. Do not default to the private/manual analysis in `width_sweep_analysis.py`.

`extend_material_to_pml` rewrites every PML face from its adjacent interior plane. Its warning only says the PML already contained non-volume-default material, so it can be benign when the rewritten values are exactly the intended continuation. Compare the affected pre/post material slices; treat the warning as an error if heterogeneous geometry, dispersion, or an unintended material would be erased.

## Model dispersion and anisotropy

1. Build metals or negative-epsilon media with positive `eps_inf` plus `LorentzPole`, `DrudePole`, or `CCPRPole`; do not use a nonpositive static diagonal permittivity.
2. Check the continuous model first with `DispersionModel.permittivity(omega, eps_inf)` or `permittivity_axes(...)` over the full source band.
3. After placement produces ADE coefficient arrays and a resolved `dt`, use `compute_eps_spectrum_from_coefficients` to audit the realized discrete spectrum where needed.
4. Check the pole/time-step stability restrictions in `doc/package-src/fdtdx/dispersion.py` and the dispersion tests.
5. Compare propagation, attenuation, or reflection to an analytic/nondispersive reference and repeat at a refined grid and time step.

Use `doc/examples/dispersive_gaussian_pulse.py` and `hyperbolic_dispersive_slab.py`; split lifecycle PRNG keys when adapting the latter. For anisotropy, start from the two anisotropic examples and `test_birefringence.py`. Full off-diagonal tensors combined with dispersion are not supported; off-diagonal conductivity with dispersion is rejected.

## Build a quasi-2D simulation

FDTDX remains a 3D solver. Use a thin periodic extrusion only when the physics is invariant along one axis:

- Use a small uniform-grid thickness, commonly two cells, along the invariant axis.
- Use periodic boundaries on both faces of that axis and PML on open in-plane faces.
- Span geometry, sources, and detectors through the invariant axis.
- For scattering, use `TFSFPlaneSourceRegion` plus inner/outer closed-surface flux contours restricted to the two in-plane axes.
- Run a blank/reference scene to determine incident irradiance before normalizing scattering power.

Adapt `doc/tests/simulation/physics/test_mie_scattering.py`, not the older notebook blindly. `QuasiUniformGrid` requires even cell counts on every axis and is not suitable for a one-cell invariant axis.

## Sweep Bloch bands

Adapt `doc/examples/bloch_band_structure.py`:

1. Model exactly one unit cell.
2. Use zero-vector periodic boundaries transversely and paired Bloch boundaries along the swept axis.
3. Supply the Bloch vector in rad/m; nonzero components require complex fields.
4. Excite multiple locations/parities with reproducible broadband sources to avoid missing modal nodes.
5. Record complex fields, window the time trace, FFT, and compare peaks to an analytic transfer-matrix or other reference.
6. Avoid or separately handle the exact Gamma point if the implementation changes real/complex field structure there.

The example recompiles for each static Bloch vector. Treat compile time separately and redesign only after numerical parity checks.

## Run inverse design

Use `doc/examples/optimize_ceviche_corner.py` as the architecture:

1. Create a `Device` with explicit materials, voxelization, and ordered `param_transforms`.
2. Configure reversible differentiation with a `Recorder`, or checkpointed differentiation with `num_checkpoints`. Bare `GradientConfig()` is invalid.
3. Run `place_objects` once outside differentiation.
4. Put `apply_params`, `run_fdtd`, and a scalar objective inside `jax.value_and_grad`; split independent transform/simulation keys even if an older example reuses one.
5. Guard every normalized objective against near-zero denominators.
6. Compile after placement with `.lower(...).compile()`; donate arrays only if they will never be reused.
7. Assert finite loss and gradients, spot-check centered finite differences, and compare reversible/checkpointed gradients for difficult media or long runs.
8. Re-evaluate the final design in a forward-only converged simulation.

Parameter transforms execute in the order supplied. Pass `beta=...` to every `apply_params` call when using `SubpixelSmoothedProjection`, including initialization/evaluation. Subpixel smoothing uses a diagonal approximation unless `subpixel_full_tensor=True`; audit the current source before relying on full-tensor behavior. Material index order follows the library's electromagnetic-property sort, not dictionary insertion order.

`full_backward` is only for explicit reverse-field propagation/inspection; ordinary JAX gradient computation does not require calling it manually.

## Use symmetry, GDS, and exports

- Symmetry tuple entries are `0` (none), `-1` (PEC parity), and `+1` (PMC parity). Placement may reduce the grid; use the appropriate `unfold_*` helper before comparing full-domain fields, detectors, or modes.
- For GDS, inspect layer/port axes and units, then use the public layer-stack, port-source, and port-detector helpers. Confirm optional dependencies from the project lock file.
- Use JSON for supported setup trees, VTI for uniform grids, VTR for nonuniform rectilinear grids, and STL for suitable 3D binary voxel data.
- Record the FDTDX version/commit with serialized artifacts and validate round trips using `doc/tests/integration/conversion/`.
