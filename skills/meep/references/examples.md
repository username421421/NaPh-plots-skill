# Meep Example Navigation and Snippet Retrieval

## How To Use This Reference

1. Match the user request to a row in **Task To Example Map**.
2. Pull the example code from the mapped section using `compose` (default) or `snippets` + `snippet`.
3. Keep the extracted example as the starting point, then adapt geometry/source/monitor parameters.
4. Verify every API call against `doc/docs/Python_User_Interface.md` before final output.

## Snippet Commands

Use these commands from the skill root (`meep/`):

```bash
python scripts/meep_docs.py examples --max-results 300
python scripts/meep_docs.py snippets Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py
python scripts/meep_docs.py snippet Python_Tutorials/Basics.md 1 --title "Transmittance Spectrum of a Waveguide Bend" --lang py
python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py
```

`compose` is usually best because it merges all code blocks in a section into one coherent snippet.

## Task To Example Map

| Request Pattern | Tutorial Section | Pull Code Snippet |
|---|---|---|
| Minimal waveguide propagation setup | `Python_Tutorials/Basics.md` -> `A Straight Waveguide` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "A Straight Waveguide" --lang py` |
| Bent waveguide field evolution | `Python_Tutorials/Basics.md` -> `A 90` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "A 90" --lang py` |
| Reflectance/transmittance normalization workflow | `Python_Tutorials/Basics.md` -> `Transmittance Spectrum of a Waveguide Bend` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Transmittance Spectrum of a Waveguide Bend" --lang py` |
| Ring resonator mode frequencies and Q (Harminv) | `Python_Tutorials/Basics.md` -> `Modes of a Ring Resonator` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Modes of a Ring Resonator" --lang py` |
| Angular reflectance vs incident angle | `Python_Tutorials/Basics.md` -> `Angular Reflectance Spectrum of a Planar Interface` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Angular Reflectance Spectrum of a Planar Interface" --lang py` |
| Mie scattering / scattering cross section | `Python_Tutorials/Basics.md` -> `Mie Scattering of a Lossless Dielectric Sphere` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Mie Scattering of a Lossless Dielectric Sphere" --lang py` |
| Absorbed power density maps | `Python_Tutorials/Basics.md` -> `Absorbed Power Density Map of a Lossy Cylinder` | `python scripts/meep_docs.py compose Python_Tutorials/Basics.md --title "Absorbed Power Density Map of a Lossy Cylinder" --lang py` |
| Eigenmode source launch in waveguides | `Python_Tutorials/Eigenmode_Source.md` -> `Index-Guided Modes in a Ridge Waveguide` | `python scripts/meep_docs.py compose Python_Tutorials/Eigenmode_Source.md --title "Index-Guided Modes in a Ridge Waveguide" --lang py` |
| Planewave launch using eigenmode source | `Python_Tutorials/Eigenmode_Source.md` -> `Planewaves in Homogeneous Media` | `python scripts/meep_docs.py compose Python_Tutorials/Eigenmode_Source.md --title "Planewaves in Homogeneous Media" --lang py` |
| Mode decomposition in guided structures | `Python_Tutorials/Mode_Decomposition.md` -> `Reflectance of a Waveguide Taper` | `python scripts/meep_docs.py compose Python_Tutorials/Mode_Decomposition.md --title "Reflectance of a Waveguide Taper" --lang py` |
| Grating diffraction at oblique incidence | `Python_Tutorials/Mode_Decomposition.md` -> `Reflectance and Transmittance Spectra for Planewave at Oblique Incidence` | `python scripts/meep_docs.py compose Python_Tutorials/Mode_Decomposition.md --title "Reflectance and Transmittance Spectra for Planewave at Oblique Incidence" --lang py` |
| Near-to-far radiation pattern extraction | `Python_Tutorials/Near_to_Far_Field_Spectra.md` -> `Radiation Pattern of an Antenna` | `python scripts/meep_docs.py compose Python_Tutorials/Near_to_Far_Field_Spectra.md --title "Radiation Pattern of an Antenna" --lang py` |
| Finite grating near-to-far diffraction | `Python_Tutorials/Near_to_Far_Field_Spectra.md` -> `Diffraction Spectrum of a Finite Binary Grating` | `python scripts/meep_docs.py compose Python_Tutorials/Near_to_Far_Field_Spectra.md --title "Diffraction Spectrum of a Finite Binary Grating" --lang py` |
| Single-frequency steady-state solve | `Python_Tutorials/Frequency_Domain_Solver.md` -> `Frequency Domain Solver` | `python scripts/meep_docs.py compose Python_Tutorials/Frequency_Domain_Solver.md --title "Frequency Domain Solver" --lang py` |
| Dispersive material fitting/validation | `Python_Tutorials/Material_Dispersion.md` -> `Reflectance Spectrum of Air-Silica Interface` | `python scripts/meep_docs.py compose Python_Tutorials/Material_Dispersion.md --title "Reflectance Spectrum of Air-Silica Interface" --lang py` |
| GDS-imported photonic layout and S-parameters | `Python_Tutorials/GDSII_Import.md` -> `S-Parameters of a Directional Coupler` | `python scripts/meep_docs.py compose Python_Tutorials/GDSII_Import.md --title "S-Parameters of a Directional Coupler" --lang py` |
| Gradient-based inverse design (adjoint) | `Python_Tutorials/Adjoint_Solver.md` -> `Broadband Waveguide Mode Converter with Minimum Feature Size` | `python scripts/meep_docs.py compose Python_Tutorials/Adjoint_Solver.md --title "Broadband Waveguide Mode Converter with Minimum Feature Size" --lang py` |
| LDOS calculations in resonant cavities | `Python_Tutorials/Local_Density_of_States.md` -> `Planar Cavity with Lossless Metallic Walls` | `python scripts/meep_docs.py compose Python_Tutorials/Local_Density_of_States.md --title "Planar Cavity with Lossless Metallic Walls" --lang py` |
| Cylindrical-coordinate scattering problems | `Python_Tutorials/Cylindrical_Coordinates.md` -> `Scattering Cross Section of a Finite Dielectric Cylinder` | `python scripts/meep_docs.py compose Python_Tutorials/Cylindrical_Coordinates.md --title "Scattering Cross Section of a Finite Dielectric Cylinder" --lang py` |
| Gyrotropic/Faraday-rotation media setup | `Python_Tutorials/Gyrotropic_Media.md` -> `Faraday Rotation` | `python scripts/meep_docs.py compose Python_Tutorials/Gyrotropic_Media.md --title "Faraday Rotation" --lang py` |

## Accuracy Notes For Reuse

- Keep the extracted snippet structure intact first; change one block at a time.
- Preserve normalization-vs-scattering two-run layouts whenever flux subtraction is used.
- Keep `is_integrated=True` for planewave sources that extend into PML regions.
- Re-run convergence checks (resolution, runtime/decay, PML thickness) after adapting any copied example.
