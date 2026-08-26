# Meep Troubleshooting Guide

## 1) Fields Diverge Or Blow Up

Primary docs:

- `doc/docs/FAQ.md` ("Why are the fields blowing up in my simulation?")
- `doc/docs/Materials.md` (numerical stability and material models)
- `doc/docs/Perfectly_Matched_Layer.md`

Common causes and fixes:

- PML overlapping dispersive media with backward-wave behavior.
  - Try `mp.Absorber(...)` instead of `mp.PML(...)`.
- Lorentz resonance too high for current timestep.
  - Increase `resolution` and/or reduce `Courant`.
- Frequency-independent negative epsilon model used directly.
  - Replace with fitted Drude-Lorentz model.
- A voxel contains multiple dielectric interfaces with subpixel smoothing.
  - Disable subpixel averaging for that run and test higher resolution.
- Refractive index less than 1 with default Courant.
  - Lower `Courant`.

## 2) Reflectance/Transmittance Is Invalid (negative or >1 unexpectedly)

Primary docs:

- `doc/docs/FAQ.md` (reflectance/transmittance question)
- `doc/docs/Python_Tutorials/Basics.md`

Checks:

- Normalization and scattering runs are geometrically identical except for scatterer.
- Runtime is long enough for DFT convergence.
- Frequency points are not too far into low source-spectrum tails.
- Source and monitors are not too close to structures causing LDOS contamination.
- Reflection monitor in normalization run is not too close to source.

## 3) PML Is Not Absorbing Well

Primary docs:

- `doc/docs/Perfectly_Matched_Layer.md`
- `doc/docs/FAQ.md` (PML absorption behavior)

Checks:

- Increase PML thickness (often around half the largest wavelength, then test larger).
- For glancing-angle or inhomogeneous boundary-normal media, use `Absorber`.
- Keep analysis regions outside PML (fields in PML are not physical).
- If planewave source spans PML, set source `is_integrated=True`.

## 4) Harminv Finds Nothing Or Wrong Modes

Primary docs:

- `doc/docs/FAQ.md` (Harminv question)
- `doc/docs/Python_User_Interface.md` (Harminv section)

Checks:

- Wrap Harminv in `mp.after_sources(...)`.
- Increase run time.
- Move monitor off nodal lines/planes.
- Narrow source bandwidth around target resonance.
- Check for hidden field instability first.

## 5) Slow Parallel Scaling

Primary docs:

- `doc/docs/Parallel_Meep.md`
- `doc/docs/FAQ.md` (parallel speedup and DTFT costs)

Checks:

- Problem size large enough per MPI rank.
- Try `split_chunks_evenly=False` for better cost-based partitioning.
- Reduce unnecessary frequency points in DFT monitors.
- Use parallel HDF5 build for heavy I/O workloads.
- Avoid calling collective Meep operations only on master rank.

## 6) Wrong Physics Due To Unit/Convention Mistakes

Primary docs:

- `doc/docs/Introduction.md` (units)
- `doc/docs/FAQ.md` (2*pi convention)
- `doc/docs/Units_and_Nonlinearity.md`

Checks:

- Use frequency `f` (not angular `omega`) in API calls.
- Be explicit about chosen length unit and wavelength/frequency conversion.
- For nonlinear runs, verify coefficient conversions and power scaling assumptions.

## 7) Step Functions Not Executing As Expected

Primary docs:

- `doc/docs/The_Run_Function_Is_Not_A_Loop.md`
- `doc/docs/Python_User_Interface.md` (run and step functions)

Fix:

- Pass function objects to `sim.run(...)`, not immediate function-call results.
- Use wrappers like `mp.at_every`, `mp.at_beginning`, `mp.after_sources`.

## 8) Convergence Is Unclear

Primary docs:

- `doc/docs/FAQ.md` ("Checking convergence")

Minimum convergence protocol:

1. Double `resolution`.
2. Increase runtime / reduce `decay_by`.
3. Increase PML thickness.
4. Compare target metrics between runs.

Do not finalize quantitative claims until sensitivity checks are stable.
