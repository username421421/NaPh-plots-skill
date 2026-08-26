# Meep Implementation Workflows

Before using a workflow, pull the closest tutorial code from `references/examples.md` via `scripts/meep_docs.py compose` and adapt it instead of writing from scratch.

## Workflow 1: Minimal Valid Simulation

Use this for any new setup before adding complexity.

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
boundary_layers = [mp.PML(1.0)]

sim = mp.Simulation(
    cell_size=cell,
    geometry=geometry,
    sources=sources,
    boundary_layers=boundary_layers,
    resolution=20,
)

sim.run(until_after_sources=mp.stop_when_fields_decayed(
    dt=50, c=mp.Ez, pt=mp.Vector3(), decay_by=1e-8
))
```

Then add one feature at a time (monitors, symmetry, custom materials, MPI).

## Workflow 2: Reflectance / Transmittance Spectrum

Use a two-run normalization workflow.

1. Run normalization with background geometry only.
2. Save incident monitor data via `sim.get_flux_data(...)`.
3. Reset and run the scattering case.
4. Load incident fields with `sim.load_minus_flux_data(...)`.
5. Compute `R` and `T` from flux ratios.

```python
# Normalization run
refl = sim.add_flux(fcen, df, nfreq, mp.FluxRegion(center=refl_pt, size=refl_size))
tran = sim.add_flux(fcen, df, nfreq, mp.FluxRegion(center=tran_pt, size=tran_size))
sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ez, probe_pt, 1e-8))

inc_flux = mp.get_fluxes(tran)
refl_data = sim.get_flux_data(refl)
sim.reset_meep()

# Scattering run (new simulation with structure)
refl = sim.add_flux(fcen, df, nfreq, mp.FluxRegion(center=refl_pt, size=refl_size))
tran = sim.add_flux(fcen, df, nfreq, mp.FluxRegion(center=tran_pt, size=tran_size))
sim.load_minus_flux_data(refl, refl_data)
sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ez, probe_pt, 1e-8))

refl_flux = mp.get_fluxes(refl)
tran_flux = mp.get_fluxes(tran)
R = [-r / i for r, i in zip(refl_flux, inc_flux)]
T = [ t / i for t, i in zip(tran_flux, inc_flux)]
```

Notes:

- For Fourier spectra, prefer pulsed sources (`GaussianSource`) and enough runtime for decay.
- Keep monitor/source placements identical between normalization and scattering runs.

## Workflow 3: Resonance Extraction With Harminv

Use this for cavity mode frequencies and Q.

```python
h = mp.Harminv(mp.Ez, mp.Vector3(), fcen, df)
sim.run(mp.after_sources(h), until_after_sources=200)
for mode in h.modes:
    print(mode.freq, mode.Q)
```

Rules:

- Wrap Harminv with `mp.after_sources(...)`.
- Place probe point away from expected nodal planes.
- If no modes found, extend runtime and narrow source bandwidth.

## Workflow 4: Near-To-Far Field

Use this when user needs radiation patterns or far-field metrics.

```python
n2f = sim.add_near2far(
    fcen, df, nfreq,
    mp.Near2FarRegion(center=..., size=..., weight=+1),
    mp.Near2FarRegion(center=..., size=..., weight=-1),
)

sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ez, probe_pt, 1e-8))
far = sim.get_farfields(n2f, resolution=..., where=mp.Volume(center=..., size=...))
```

Rules:

- Ensure near-field box encloses all radiating/scattering content.
- Keep near-field monitors away from PML.
- Validate against a larger near-field box if results are sensitive.

## Workflow 5: Mode Decomposition / S-Parameters

Use when user asks for mode amplitudes, coupling, or S-parameters.

```python
mon = sim.add_mode_monitor(
    fcen, df, nfreq,
    mp.ModeRegion(center=mode_plane_center, size=mode_plane_size)
)

sim.run(until_after_sources=mp.stop_when_fields_decayed(50, mp.Ez, probe_pt, 1e-8))
res = sim.get_eigenmode_coefficients(mon, [1], eig_parity=mp.NO_PARITY)
```

Rules:

- Choose correct monitor orientation and region for guided mode basis.
- Use `eig_parity` consistent with symmetry assumptions.
- Validate that mode order/band index matches the intended physical mode.

## Workflow 6: Frequency-Domain Solver

Use when user wants a single-frequency steady-state response and time stepping is too slow.

```python
sim = mp.Simulation(..., force_complex_fields=True)
sim.init_sim()
sim.solve_cw(tol=1e-8, maxiters=10000, L=2)
```

Rules:

- Requires `ContinuousSource`.
- Requires `force_complex_fields=True`.
- Not for Lorentz-Drude dispersive media in the built-in frequency-domain solver.

## Workflow 7: Adjoint Optimization

Use for gradient-based inverse design with `meep.adjoint`.

Minimum process:

1. Define design region with `MaterialGrid`.
2. Run forward solve for objective.
3. Run adjoint solve for gradient.
4. Update design variables via optimizer.
5. Repeat with feature-size and binarization strategy.

Read first:

- `doc/docs/Python_Tutorials/Adjoint_Solver.md`
- `doc/docs/Python_User_Interface.md` (MaterialGrid)

## Workflow 8: Convergence And Validation

Always run these checks before final claims:

1. Double `resolution`.
2. Increase PML thickness (often 2x).
3. Increase runtime or tighten `decay_by`.
4. Confirm key scalar outputs change less than tolerance.
5. Re-check with and without optional symmetry assumptions when feasible.
