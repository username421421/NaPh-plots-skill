# Meep Documentation Navigation

## Start Here

Use this order for new requests:

1. `doc/docs/index.md`
2. `doc/docs/Introduction.md`
3. `doc/docs/Python_Tutorials/Basics.md`
4. `doc/docs/Python_User_Interface.md`
5. `doc/docs/FAQ.md`

If the task is implementation-heavy, skip directly to `doc/docs/Python_User_Interface.md` plus the matching tutorial page.
For code reuse, also open `references/examples.md` and pull a section-level snippet with `scripts/meep_docs.py compose`.

## Task To Document Map

| Task | Open First | Then Open |
|---|---|---|
| Install or environment setup | `doc/docs/Installation.md` | `doc/docs/Build_From_Source.md`, `doc/docs/Parallel_Meep.md` |
| Core Python API usage | `doc/docs/Python_User_Interface.md` | `doc/docs/Python_Tutorials/Basics.md` |
| Geometry, objects, materials in scripts | `doc/docs/Python_User_Interface.md` (Medium, GeometricObject, Simulation) | `doc/docs/Materials.md`, `doc/docs/Subpixel_Smoothing.md` |
| Source design and excitation | `doc/docs/Python_User_Interface.md` (Source, SourceTime, EigenModeSource) | `doc/docs/Python_Tutorials/Eigenmode_Source.md`, `doc/docs/Perfectly_Matched_Layer.md` |
| Flux, spectra, normalization runs | `doc/docs/Python_User_Interface.md` (Flux Spectra) | `doc/docs/Python_Tutorials/Basics.md`, `doc/docs/FAQ.md` |
| Resonant modes and Q extraction | `doc/docs/Python_User_Interface.md` (Harminv) | `doc/docs/Python_Tutorials/Resonant_Modes_and_Transmission_in_a_Waveguide_Cavity.md`, `doc/docs/FAQ.md` |
| S-parameters and mode decomposition | `doc/docs/Mode_Decomposition.md` | `doc/docs/Python_Tutorials/Mode_Decomposition.md`, `doc/docs/Python_User_Interface.md` |
| Near-to-far field transforms | `doc/docs/Python_Tutorials/Near_to_Far_Field_Spectra.md` | `doc/docs/Python_User_Interface.md` (Near-to-Far-Field Spectra) |
| Cylindrical coordinates | `doc/docs/Exploiting_Symmetry.md` | `doc/docs/Python_Tutorials/Cylindrical_Coordinates.md`, `doc/docs/FAQ.md` |
| Symmetry setup and parity | `doc/docs/Exploiting_Symmetry.md` | `doc/docs/Python_User_Interface.md` (Symmetry, Mirror, Rotate2, Rotate4) |
| Frequency-domain solver | `doc/docs/Python_User_Interface.md` (Frequency-Domain Solver, Eigensolver) | `doc/docs/Python_Tutorials/Frequency_Domain_Solver.md`, `doc/docs/FAQ.md` |
| Dispersive, lossy, nonlinear, gyrotropic media | `doc/docs/Materials.md` | `doc/docs/Units_and_Nonlinearity.md`, `doc/docs/Python_Tutorials/Material_Dispersion.md`, `doc/docs/Python_Tutorials/Gyrotropic_Media.md` |
| Inverse design / adjoint | `doc/docs/Python_Tutorials/Adjoint_Solver.md` | `doc/docs/Python_User_Interface.md` (MaterialGrid) |
| Parallel runtime and scaling | `doc/docs/Parallel_Meep.md` | `doc/docs/Chunks_and_Symmetry.md`, `doc/docs/FAQ.md` |
| Divergence, unstable runs, odd outputs | `doc/docs/FAQ.md` | `doc/docs/Perfectly_Matched_Layer.md`, `doc/docs/Materials.md`, `doc/docs/The_Run_Function_Is_Not_A_Loop.md` |

## Example Navigation

For concrete script patterns from the tutorials:

- Open `references/examples.md` for request-to-example mapping.
- Use `python scripts/meep_docs.py examples --max-results 200` for a global example index.
- Use `python scripts/meep_docs.py compose <page> --title \"<section>\" --lang py` to get a merged section code snippet.

## High-Value API Sections In Python_User_Interface

Look up these sections by heading:

- `Simulation`
- `Flux Spectra`
- `Mode Decomposition`
- `Near-to-Far-Field Spectra`
- `Run and Step Functions`
- `Predefined Step Functions`
- `Step-Function Modifiers`
- `Medium` and susceptibility classes
- `PML` and `Absorber`
- `Source`, `ContinuousSource`, `GaussianSource`, `EigenModeSource`
- `Harminv`
- `Frequency-Domain Solver`
- `Frequency-Domain Eigensolver`
- `MaterialGrid`

## Fast Local Search

Use the script:

```bash
python scripts/meep_docs.py search "stop_when_fields_decayed"
python scripts/meep_docs.py section Python_User_Interface.md "Flux Spectra"
```

Or use ripgrep directly:

```bash
rg -n "add_flux|get_fluxes|get_flux_freqs|load_minus_flux_data" doc/docs/Python_User_Interface.md
rg -n "Harminv|after_sources|run_k_points" doc/docs/Python_User_Interface.md
rg -n "Why are the fields blowing up|Checking convergence" doc/docs/FAQ.md
```
