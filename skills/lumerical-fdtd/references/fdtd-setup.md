# FDTD Setup Reference

Use this file for solver-region setup, units, global settings, and object conventions. Primary official sources: [FDTD solver - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object), [Units and normalization conventions](https://optics.ansys.com/hc/en-us/articles/360034397034-Units-and-normalization-conventions-in-Lumerical-solvers), [FDTD product reference manual](https://optics.ansys.com/hc/en-us/articles/360033154434-FDTD-product-reference-manual), and [Convergence testing process](https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing-process-for-FDTD-simulations).

## Units And Naming

Lumerical solvers use SI units. In Python scripts, define constants and use them everywhere:

```python
UM = 1e-6
NM = 1e-9
FS = 1e-15
```

Use descriptive object names because monitor and analysis calls are name-based:

```python
("name", "source_TE_1550")
("name", "field_xy_device_center")
("name", "mesh_gap_10nm")
```

Avoid implicit defaults. Set the solver dimension, spans, background, boundaries, mesh accuracy, simulation time, and auto shutoff explicitly in every builder.

## Solver Region

Typical `addfdtd` setup:

```python
from collections import OrderedDict

fdtd.addfdtd(properties=OrderedDict([
    ("name", "FDTD"),
    ("dimension", "3D"),
    ("x", 0.0),
    ("x span", 6.0 * UM),
    ("y", 0.0),
    ("y span", 4.0 * UM),
    ("z", 0.0),
    ("z span", 2.0 * UM),
    ("background material", "SiO2 (Glass) - Palik"),
    ("simulation time", 1200 * FS),
    ("auto shutoff min", 1e-5),
    ("mesh accuracy", 2),
    ("x min bc", "PML"),
    ("x max bc", "PML"),
    ("y min bc", "PML"),
    ("y max bc", "PML"),
    ("z min bc", "PML"),
    ("z max bc", "PML"),
]))
```

Set the region large enough that PMLs are not in strong near fields or evanescent tails unless the physics specifically requires it. For periodic unit cells, the periodic axes should match the unit-cell pitch and use periodic or Bloch boundaries rather than extra air padding. Source: [FDTD solver - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object), [Periodic boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382734-Periodic-boundary-conditions-in-FDTD-and-MODE).

## Background Material And Index

Use `background material` when a named material is appropriate. Use a background index only for simple homogeneous backgrounds or reference calculations where a fixed nondispersive index is intended.

Guidelines:

- Use the same background in the reference and device simulations unless intentionally measuring against a changed environment.
- For far-field projections, keep the projection region homogeneous around the near-field monitor surface. Source: [Far field projections](https://optics.ansys.com/hc/en-us/articles/360034914713-Far-field-projections-in-FDTD-overview).
- For substrates or superstrates, model the real layers as geometry instead of hiding them in the solver background if field discontinuities or reflections matter.

## Simulation Time And Auto Shutoff

Set simulation time long enough for fields to leave the region or decay below the metric tolerance. Relying only on default time can under-resolve resonant structures, cavities, high-Q waveguides, or long propagation paths.

Use `auto shutoff min` as a convergence control, not as a substitute for checking the actual metric. A looser value can accelerate early design sweeps; tighten it for final runs and verify the result does not change.

## Global Source And Monitor Settings

Set source bandwidth once:

```python
fdtd.setglobalsource("set wavelength", 1)
fdtd.setglobalsource("wavelength start", 1.50 * UM)
fdtd.setglobalsource("wavelength stop", 1.60 * UM)
```

Set global monitor sampling once:

```python
fdtd.setglobalmonitor("use source limits", 1)
fdtd.setglobalmonitor("frequency points", 101)
```

Override locally only when a monitor or source deliberately uses a different range. Source: [Frequency-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-monitor-Simulation-object), [Plane wave and beam source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object).

## Geometry And Materials

Prefer named materials from the Lumerical material database for published optical constants. For local or inverse-design data, document the source of `n`, `k`, or permittivity grids and the wavelength range where the data is valid.

Recommended material helper pattern:

```python
def set_material_or_index(fdtd, material_name, fallback_index):
    try:
        fdtd.getmaterial(material_name)
        return material_name
    except Exception:
        return f"<Object defined dielectric n={fallback_index}>"
```

Use mesh order intentionally when overlapping materials or imported objects share volume. Source: [FDTD product reference manual](https://optics.ansys.com/hc/en-us/articles/360033154434-FDTD-product-reference-manual).

## Status Extraction

After a run, capture enough state to diagnose failures:

```python
fdtd.run()
status = fdtd.getresult("FDTD", "status") if "status" in fdtd.getresult("FDTD") else None
```

If the exact status result is unavailable in a version, log the project path, Lumerical version, source/monitor names, mesh settings, shutoff settings, and monitor result keys. The important practice is preserving enough metadata to reproduce the run.
