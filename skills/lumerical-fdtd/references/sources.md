# Sources

Use this file for source selection and placement. Primary official sources: [Plane wave and beam source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object), [Understanding injection angles](https://optics.ansys.com/hc/en-us/articles/360034382894-Understanding-injection-angles-in-broadband-simulations), [Mode source](https://optics.ansys.com/hc/en-us/articles/360034902153-Mode-source-Simulation-object), [Dipole source](https://optics.ansys.com/hc/en-us/articles/360034382794-Dipole-source-Simulation-object), [TFSF best practices](https://optics.ansys.com/hc/en-us/articles/360034382934-Tips-and-best-practices-when-using-the-FDTD-TFSF-source), and [Ports (FDTD)](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object).

## Global Source Settings

Set wavelength/frequency range once for consistent monitors and normalization:

```python
fdtd.setglobalsource("set wavelength", 1)
fdtd.setglobalsource("wavelength start", 450 * NM)
fdtd.setglobalsource("wavelength stop", 750 * NM)
```

Use local source limits only when a source intentionally differs from the global band.

## Plane Wave, Gaussian, And Beam Sources

Use plane waves for uniform illumination of periodic cells, films, metasurfaces, and large-area scattering where a finite waist is not desired. Use Gaussian/beam variants when finite beam waist or focus matters. Source: [Plane wave and beam source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object).

```python
fdtd.addplane(properties=OrderedDict([
    ("name", "src_plane_z"),
    ("injection axis", "z"),
    ("direction", "Backward"),
    ("x", 0.0),
    ("x span", 1.0 * UM),
    ("y", 0.0),
    ("y span", 1.0 * UM),
    ("z", 1.0 * UM),
    ("polarization angle", 0),
]))
```

For angled injection, pair the source with valid boundary conditions. Periodic boundaries are not enough when the field has phase shift across the cell; use Bloch or official angled-injection methods. Source: [Understanding injection angles](https://optics.ansys.com/hc/en-us/articles/360034382894-Understanding-injection-angles-in-broadband-simulations).

## Mode Source

Use a mode source to inject a guided mode into a waveguide, fiber, port-like cross section, or MMI. The source plane should be normal to propagation and span enough of the transverse cross section to capture the mode field. Source: [Mode source](https://optics.ansys.com/hc/en-us/articles/360034902153-Mode-source-Simulation-object).

```python
fdtd.addmode(properties=OrderedDict([
    ("name", "src_mode_te0"),
    ("injection axis", "x"),
    ("direction", "Forward"),
    ("x", -3.0 * UM),
    ("y", 0.0),
    ("y span", 1.6 * UM),
    ("z", 0.11 * UM),
    ("z span", 1.0 * UM),
    ("mode selection", "fundamental mode"),
]))
```

For multimode or polarization-sensitive devices, explicitly choose mode number or mode properties and log the selected effective index. For broadband runs, confirm the mode calculation method is appropriate over the band.

## Dipole Source

Use dipoles for emitters, spontaneous-emission/Purcell calculations, local excitation, and point-source radiation. Set orientation, position, and bandwidth explicitly. Source: [Dipole source](https://optics.ansys.com/hc/en-us/articles/360034382794-Dipole-source-Simulation-object).

```python
fdtd.adddipole(properties=OrderedDict([
    ("name", "dipole_z_center"),
    ("x", 0.0),
    ("y", 0.0),
    ("z", 50 * NM),
    ("theta", 0),
    ("phi", 0),
]))
```

If using symmetry with dipoles, verify parity for the selected dipole orientation and position. A centered dipole can have different valid symmetry settings depending on whether it is x-, y-, or z-oriented.

## TFSF Source

Use TFSF for scattering problems where the incident field and scattered field need to be separated. Keep the TFSF box in a homogeneous region where the injected plane wave is valid, and avoid intersecting the source boundary with scatterers or nonuniform mesh features unless official guidance says otherwise. Source: [TFSF best practices](https://optics.ansys.com/hc/en-us/articles/360034382934-Tips-and-best-practices-when-using-the-FDTD-TFSF-source).

TFSF checklist:

- Scatterer fully inside the TFSF total-field region.
- Source boundary not cutting through geometry.
- Mesh uniform or adequately controlled at the source boundary.
- Normalization uses source power appropriate for TFSF.
- Monitors distinguish incident, scattered, and total-field regions correctly.

## Ports

Use FDTD ports for integrated photonics workflows where source, mode expansion, and S-parameter extraction should be grouped. Ports are especially useful in waveguide circuits and multiport devices. Source: [Ports (FDTD)](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object).

```python
fdtd.addport(properties=OrderedDict([
    ("name", "port_in"),
    ("injection axis", "x"),
    ("direction", "Forward"),
    ("x", -3.0 * UM),
    ("y span", 1.6 * UM),
    ("z span", 1.0 * UM),
]))
```

## Placement Rules

- Place sources far enough from high-Q resonators, scatterers, and PML that the injected field is clean.
- Ensure the source plane spans the intended field support.
- For reflection monitors, account for the source position and normalization; see `monitors-results.md`.
- For broadband and angled sources, validate that the source/boundary combination is physically meaningful over the full band.
