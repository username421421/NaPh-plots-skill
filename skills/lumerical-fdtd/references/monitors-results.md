# Monitors And Results

Use this file for monitor placement, result extraction, reflection/transmission calculations, and far-field projection. Primary official sources: [Frequency-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-monitor-Simulation-object), [Field time monitor](https://optics.ansys.com/hc/en-us/articles/360034902353-Field-time-monitor-Simulation-object), [Mode expansion monitor](https://optics.ansys.com/hc/en-us/articles/360034902413-Mode-expansion-monitor-Simulation-object), [Using Mode Expansion Monitors](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors), [Tips for accurately measuring reflection](https://optics.ansys.com/hc/en-us/articles/360034915753-Tips-for-accurately-measuring-reflection-in-an-FDTD-simulation), and [Far field projections](https://optics.ansys.com/hc/en-us/articles/360034914713-Far-field-projections-in-FDTD-overview).

## Global Monitor Settings

```python
fdtd.setglobalmonitor("use source limits", 1)
fdtd.setglobalmonitor("frequency points", 101)
```

Keep frequency points low for early sweeps and high enough for final spectra, resonances, and post-processing. Disable unused field components to control file size and memory.

## Frequency-Domain Monitors

Use DFT monitors for spectra, steady-state fields, power flux, mode expansion input, and far-field projection source data. Source: [Frequency-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-monitor-Simulation-object).

```python
fdtd.adddftmonitor(properties=OrderedDict([
    ("name", "T_after_device"),
    ("monitor type", "2D X-normal"),
    ("x", 3.5 * UM),
    ("y", 0.0),
    ("y span", 2.0 * UM),
    ("z", 0.11 * UM),
    ("z span", 1.2 * UM),
    ("use source limits", 1),
    ("output power", 1),
]))
```

Use 2D monitors for flux through a plane, profile plots, and mode expansion. Use 3D field monitors only when volumetric fields are required because they are expensive.

## Time Monitors

Use time monitors for transient decay, pulse arrival, ringing, and checking whether the simulation time/auto shutoff is sufficient. Source: [Field time monitor](https://optics.ansys.com/hc/en-us/articles/360034902353-Field-time-monitor-Simulation-object).

```python
fdtd.addtime(properties=OrderedDict([
    ("name", "time_probe_cavity"),
    ("monitor type", "Point"),
    ("x", 0.0),
    ("y", 0.0),
    ("z", 0.11 * UM),
]))
```

Use time monitors near resonant hot spots to confirm decay rather than trusting only final spectra.

## Mode Expansion

Use mode expansion monitors to decompose fields into guided modes and obtain forward/backward amplitudes. They require a monitor plane and mode basis consistent with the waveguide cross section. Source: [Mode expansion monitor](https://optics.ansys.com/hc/en-us/articles/360034902413-Mode-expansion-monitor-Simulation-object), [Using Mode Expansion Monitors](https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors).

```python
fdtd.addmodeexpansion(properties=OrderedDict([
    ("name", "mode_exp_out"),
    ("monitor type", "2D X-normal"),
    ("x", 3.5 * UM),
    ("y span", 1.6 * UM),
    ("z span", 1.0 * UM),
    ("mode selection", "fundamental mode"),
]))
```

Validate mode selection and monitor placement for multimode outputs; a monitor too close to discontinuities can mix radiation and guided modes.

## Reflection And Transmission Placement

Official reflection guidance warns that monitor placement relative to the source matters. Source: [Tips for accurately measuring reflection](https://optics.ansys.com/hc/en-us/articles/360034915753-Tips-for-accurately-measuring-reflection-in-an-FDTD-simulation).

Practical placement:

- Transmission monitor: after the device, far enough that near fields and evanescent content are not dominating unless intentionally measured.
- Reflection monitor: between source and device, placed so it captures reflected fields without being contaminated by the source injection plane.
- Reference monitor: use a consistent blank/reference simulation when normalizing device response.
- Shift source and monitors slightly as a sensitivity check for final results.

## Far Field

Far-field projection uses near-field monitor data to project into a homogeneous region. The near-field monitor surface must enclose the radiating/scattering region sufficiently and avoid cutting through materials that violate projection assumptions. Source: [Far field projections](https://optics.ansys.com/hc/en-us/articles/360034914713-Far-field-projections-in-FDTD-overview).

Checklist:

- Projection medium is homogeneous.
- Near-field monitor box or planes capture all outgoing radiation needed for the metric.
- PML and monitor surfaces are separated enough to avoid boundary artifacts.
- For periodic structures, use grating/far-field methods appropriate for periodicity.

## Result Access

```python
fdtd.run()

T = fdtd.getresult("T_after_device", "T")
E = fdtd.getresult("field_xy", "E")
Ex = fdtd.getdata("field_xy", "Ex")
f = fdtd.getdata("field_xy", "f")
```

Before assuming keys, inspect:

```python
print(fdtd.getresult("T_after_device"))
```

Store metadata with exported results: project path, Lumerical version, source band, mesh settings, boundary settings, monitor names, and run date.
