# PyLumerical Usage Reference

Use this file when the requested implementation uses the PyAnsys package for Lumerical automation: `ansys-lumerical-core`, imported as `ansys.lumerical.core`. This reference is local guidance synthesized from official PyLumerical and Ansys Optics documentation. Last checked: 2026-06-23.

## Agent Workflow

Before writing PyLumerical code, complete this checklist:

1. Search this file and the local captured corpus:

```powershell
rg -n "PyLumerical|ansys\.lumerical\.core|FDTD\(|serverArgs|OrderedDict|SimObject|lumopt2|getresult|getdata" references
rg -n "fdtd-example1-pythonic|fdtd-example1-lsf|metalens|photonic-crystal|basic session|waveguide|ring resonator" references
```

2. Pick the closest official example from the local corpus before designing code. Prefer `scraped/fdtd-example1-pythonic.md` for Pythonic constructor style, `scraped/fdtd-example1-lsf.md` for legacy script-command style, `scraped/photonic-crystal-bandstructure.md` for FDTD sweeps/groups/Bloch setup, and `scraped/metalens-fdtd-with-projections.md` for FDTD plus far-field and symmetry patterns.
3. Audit every command, constructor, object property, and result key against `references/python-api.md`, the relevant source/monitor/mesh reference, and the local scraped page for the closest example.
4. Prefer exact Lumerical property names in `properties=OrderedDict([...])` when property order matters. Use keyword arguments only when no linked property ordering risk exists.
5. Write implementation notes before coding: package choice, Lumerical version/license assumptions, session arguments, examples inspected, object-property audit, result keys, and convergence risks.

## Source Inventory

| Official page | Local captured file | Use for |
| --- | --- | --- |
| [PyLumerical home](https://lumerical.docs.pyansys.com/version/stable/index.html) | `references/scraped/lumerical-docs-pyansys-com-version-stable.md` | Package positioning, products, PyAnsys ecosystem, lumopt/lumopt2 note |
| [Installation and getting started](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html) | `references/scraped/lumerical-docs-pyansys-com-version-stable-getting-started.md` | Install, requirements, `LUMERICAL_HOME`, import forms, first project |
| [User guide](https://lumerical.docs.pyansys.com/version/stable/user_guide/index.html) | `references/scraped/lumerical-docs-pyansys-com-version-stable-user-guide.md` | Router for simulation automation and lumopt2 topics |
| [Session management](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html) | `references/scraped/session-management.md` | Product sessions, context managers, multiple sessions, `serverArgs`, close behavior |
| [Script commands as methods](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html) | `references/scraped/script-commands-as-methods.md` | Lumerical command methods, constructor command patterns, custom `.lsf` import, unsupported methods |
| [Working with simulation objects](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html) | `references/scraped/working-with-simulation-objects.md` | `OrderedDict`, keyword arguments, direct/dict object access, duplicate-name risk, tree traversal |
| [Passing data](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html) | `references/scraped/passing-data.md` | Type conversion, `getv`, `putv`, copy semantics, transfer costs |
| [Accessing simulation results](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html) | `references/scraped/accessing-simulation-results.md` | `getresult`, `getdata`, dataset dictionaries, array shapes |
| [API reference](https://lumerical.docs.pyansys.com/version/stable/api/index.html) | `references/scraped/lumerical-docs-pyansys-com-version-stable-api.md` | API page router |
| [Interface classes](https://lumerical.docs.pyansys.com/version/stable/api/interface_class.html) | `references/scraped/interface-class.md` | `FDTD`, `MODE`, `DEVICE`, `INTERCONNECT` sessions |
| [Auxiliary classes](https://lumerical.docs.pyansys.com/version/stable/api/simobject_class.html) | `references/scraped/simobject-class.md` | `SimObject`, `SimObjectResults`, `SimObjectId` behavior |
| [Autodiscovery](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html) | `references/scraped/autodiscovery.md` | Installation discovery paths and fallback |
| [Examples](https://lumerical.docs.pyansys.com/version/stable/examples.html) | `references/scraped/examples.md` | Official example index |
| [Basic session management](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html) | `references/scraped/basic-session-management.md` | Session startup and context-manager examples |
| [Basic FDTD Simulation - Lumerical style commands](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html) | `references/scraped/fdtd-example1-lsf.md` | PyLumerical with script-command style |
| [Basic FDTD Simulation - Python style commands](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.html) | `references/scraped/fdtd-example1-pythonic.md` | PyLumerical keyword/object style |
| [Photonic Crystal Bandstructure (FDTD)](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html) | `references/scraped/photonic-crystal-bandstructure.md` | Structure groups, analysis groups, Bloch boundaries, sweeps |
| [PyLumerical Metalens (FDTD)](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html) | `references/scraped/metalens-fdtd-with-projections.md` | RCWA/FDTD workflow, symmetry, far-field projection |
| [Introduction to photonic inverse design with lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html) | `references/scraped/photonic-inverse-design-with-lumopt2.md` | `lumopt2` import and workflow entry point |
| [Getting started with lumopt2: simple metalens](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html) | `references/scraped/getting-started-simple-metalens.md` | Basic `lumopt2` project setup, run, and result pattern |
| [Getting started with lumopt2: L-bend](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html) | `references/scraped/getting-started-l-bend.md` | Closed-curve parametrization, ports, FOM, optimizer, callbacks |
| [Optimization session in lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html) | `references/scraped/optimization-session.md` | Project, base simulation, parametrization, FOM, callback architecture |
| [lumopt2 API reference](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html) | `references/scraped/lumerical-docs-pyansys-com-version-stable-api-lumopt2.md` | Inverse-design classes and functions |

## What PyLumerical Is

PyLumerical is the PyAnsys Python automation package for controlling installed Ansys Lumerical products from a normal Python environment. The package controls FDTD, MODE, Multiphysics/DEVICE, and INTERCONNECT sessions and can use Lumerical Scripting Language commands through Python methods. It is separate from the legacy `lumapi.py` module bundled inside a Lumerical installation, although the official docs explicitly support importing PyLumerical as `lumapi` so many legacy scripts can keep the same session-object style.

Use PyLumerical when:

- You want a package-managed Python environment, notebook, IDE, or PyAnsys workflow.
- You want to combine Lumerical automation with NumPy, SciPy, Matplotlib, pandas, or other Python tools without relying on the in-product interpreter.
- You want Pythonic object creation and object handles, while still retaining access to Lumerical script commands.

Use bundled `lumapi.py` when:

- The existing repo script is already pinned to an installed Lumerical path such as `E:\Program Files\ANSYS Inc\v261\Lumerical\api\python\lumapi.py`.
- You need to reproduce a workspace script exactly with the installed API version.
- The project relies on in-product bundled modules or local environment assumptions that are not yet validated in a PyLumerical virtual environment.

## Installation And Requirements

Official installation pattern:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install ansys-lumerical-core
```

Runtime requirements:

- A local Ansys Lumerical installation is still required. PyLumerical is an automation package, not a solver replacement.
- The official PyLumerical docs state that Lumerical 2022 R1 or later is required for PyLumerical.
- A GUI license is required for normal product automation.
- `lumopt2` requires an installed Ansys Lumerical FDTD version new enough to include the module; the current docs call out Ansys Lumerical 2026 R1.2 or later.

Autodiscovery behavior:

- Importing `ansys.lumerical.core` triggers installation discovery.
- On Windows, discovery checks the registry and default install locations such as `C:\Program Files\Lumerical\` and `C:\Program Files\ANSYS Inc\ANSYS Optics\`.
- On Linux, discovery checks default install locations such as `/opt/Lumerical/` and `~/Ansys/ansys_inc/`.
- If discovery fails, set `LUMERICAL_HOME` before starting Python and importing PyLumerical.

```powershell
$env:LUMERICAL_HOME = "E:\Program Files\ANSYS Inc\v261\Lumerical"
python your_script.py
```

## Imports

Simulation automation:

```python
import ansys.lumerical.core as lumapi
```

This import intentionally aliases the package to `lumapi`; it keeps the common `lumapi.FDTD()` style and eases migration from legacy scripts.

Inverse design through PyLumerical:

```python
import ansys.lumerical.core.lumopt2 as lmpt
```

Use only the `ansys.lumerical.core.lumopt2` import path for PyLumerical-driven inverse design. Do not manually add Lumerical install folders to `sys.path` for `lumopt2`; the official docs warn that manual `sys.path` overrides are unsupported. In the in-product script editor, the import form differs and is usually `import lumopt2 as lmpt` because that environment uses Lumerical's bundled Python.

## Session Management

Main product session classes:

| Product | PyLumerical class | Typical file |
| --- | --- | --- |
| Ansys Lumerical FDTD | `lumapi.FDTD` | `.fsp` |
| Ansys Lumerical MODE | `lumapi.MODE` | `.lms` / solver-specific |
| Ansys Lumerical Multiphysics / DEVICE | `lumapi.DEVICE` | `.ldev` |
| Ansys Lumerical INTERCONNECT | `lumapi.INTERCONNECT` | `.icp` |

Use context managers for scripts that create, run, and close solver sessions:

```python
import ansys.lumerical.core as lumapi

with lumapi.FDTD(hide=True) as fdtd:
    fdtd.newproject()
    fdtd.deleteall()
    fdtd.addfdtd()
    fdtd.save("example.fsp")
```

Context managers are preferred because the session closes even when an exception is raised. Without a context manager, call `close()` explicitly when done:

```python
fdtd = lumapi.FDTD(hide=True)
try:
    fdtd.addfdtd()
finally:
    fdtd.close()
```

Open an existing file or run a startup script by passing a filename or script-related keyword argument:

```python
with lumapi.FDTD("existing_project.fsp", hide=True) as fdtd:
    fdtd.run()
```

For command-line solver arguments, use `serverArgs`:

```python
with lumapi.FDTD(
    hide=True,
    serverArgs={"platform": "offscreen", "threads": "4", "use-solve": True},
) as fdtd:
    fdtd.run()
```

Treat `serverArgs` as execution configuration. Keep it visible in the top-level script or configuration file because it affects licensing, GUI behavior, threading, and remote/headless runs.

## Script Commands As Methods

Most Lumerical script commands can be called directly as methods on the PyLumerical session object:

```python
with lumapi.FDTD(hide=True) as fdtd:
    fdtd.addfdtd()
    fdtd.set("dimension", "3D")
    fdtd.set("x span", 4e-6)
    fdtd.set("mesh accuracy", 3)
    fdtd.setglobalsource("wavelength start", 1.5e-6)
    fdtd.setglobalmonitor("frequency points", 101)
```

Rules for agent-generated code:

- Constructor-like commands that add objects can use `properties=...`, a positional dict, or keyword arguments.
- Non-constructor commands such as `set`, `setnamed`, `getresult`, `getdata`, `addsweepparameter`, and many custom functions should use positional arguments unless the official page explicitly shows keyword support.
- If a Lumerical property contains spaces, keyword style replaces spaces with underscores, for example `x_span=1e-6` for `x span`.
- Keep exact Lumerical property strings when using `set`, `setnamed`, dicts, or `OrderedDict`.
- When in doubt, prefer `properties=OrderedDict([...])` plus exact Lumerical names because it mirrors the GUI/property-table order.

Original minimal FDTD setup snippet:

```python
from collections import OrderedDict
import ansys.lumerical.core as lumapi

fdtd_props = OrderedDict([
    ("dimension", "3D"),
    ("x", 0.0),
    ("x span", 4.0e-6),
    ("y", 0.0),
    ("y span", 4.0e-6),
    ("z", 0.0),
    ("z span", 2.0e-6),
    ("background material", "Air"),
    ("mesh accuracy", 3),
    ("simulation time", 1000e-15),
    ("auto shutoff min", 1e-5),
    ("x min bc", "PML"),
    ("x max bc", "PML"),
    ("y min bc", "PML"),
    ("y max bc", "PML"),
    ("z min bc", "PML"),
    ("z max bc", "PML"),
])

with lumapi.FDTD(hide=True) as fdtd:
    fdtd.addfdtd(properties=fdtd_props)
    fdtd.save("base_fdtd.fsp")
```

## Pythonic Constructors And Object Handles

PyLumerical supports Pythonic object creation. For simple independent properties, keyword arguments are concise:

```python
rect = fdtd.addrect(
    name="core",
    x=0.0,
    y=0.0,
    z=0.0,
    x_span=2.0e-6,
    y_span=450e-9,
    z_span=220e-9,
    index=3.48,
)
```

For linked properties or object-type changes, use `OrderedDict`:

```python
power_monitor = fdtd.addpower(properties=OrderedDict([
    ("name", "T"),
    ("monitor type", "2D X-normal"),
    ("override global monitor settings", True),
    ("frequency points", 201),
    ("x", 1.5e-6),
    ("y", 0.0),
    ("y span", 2.0e-6),
    ("z", 0.0),
    ("z span", 1.0e-6),
]))
```

Why `OrderedDict` matters: some object properties only become valid after another property is set. Common examples include monitor type before spans and frequency points, source/injection axis before direction and transverse spans, solver dimension before unavailable axes, and override flags before global-setting overrides.

Object handles returned by constructor commands can be manipulated directly:

```python
source = fdtd.addgaussian(name="src", injection_axis="z", direction="Forward")
source["x span"] = 3.0e-6
source["y span"] = 3.0e-6
source["wavelength start"] = 1.50e-6
source["wavelength stop"] = 1.60e-6
```

Use direct or dict-like object-handle edits only when object names are unique. The official docs warn that duplicate names can cause undefined or surprising behavior because name-based object lookup may target the wrong object. Agent-generated scripts should assign unique names for every source, monitor, mesh override, structure, and analysis group.

Tree traversal is available through object parent/child helpers. Use it for introspection, not as a substitute for explicit names in production builders.

## Custom Script Commands

PyLumerical can import custom Lumerical script functions from `.lsf` files during session creation or through `eval()`:

```python
with lumapi.FDTD(script=["helpers.lsf"], hide=True) as fdtd:
    value = fdtd.custom_function(1.0, 2.0)
```

or:

```python
with lumapi.FDTD(hide=True) as fdtd:
    fdtd.eval(Path("helpers.lsf").read_text(encoding="utf-8"))
    value = fdtd.custom_function(1.0, 2.0)
```

Do not assume keyword arguments work for custom Lumerical script functions. The PyLumerical user guide shows positional arguments as the safe pattern for non-constructor functions.

Unsupported or awkward script-language constructs:

- Lumerical operator syntax does not overload directly into Python. Use Python operators or `eval()` when a native script expression is unavoidable.
- Reserved script variables such as the speed-of-light symbol `c` may not be available as direct Python methods/variables. Define them in Python or use `eval()` deliberately.
- Variables in Python and Lumerical script workspaces are not automatically shared. Use method calls, return values, `putv`, or `getv` explicitly.

## Passing Data

PyLumerical passes copies between Python and the Lumerical workspace. Avoid repeated transfer of large arrays inside loops.

Common conversions:

| Lumerical value | Python value |
| --- | --- |
| String | `str` |
| Real | `float` |
| Complex | `numpy.ndarray` representation when returned; wrap complex inputs carefully |
| Matrix | `numpy.ndarray` |
| Cell array | `list` |
| Struct | `dict` |
| Dataset | `dict` with metadata |

Use normal method arguments for ordinary values:

```python
fdtd.setnamed("FDTD", "simulation time", 1000e-15)
fdtd.setglobalsource("wavelength start", 1.50e-6)
```

Use `putv` and `getv` only when you intentionally need variables in the Lumerical script workspace:

```python
import numpy as np

wavelengths = np.linspace(1.50e-6, 1.60e-6, 51)
fdtd.putv("lambda_sweep", wavelengths)
fdtd.eval("freq_sweep = c/lambda_sweep;")
frequencies = fdtd.getv("freq_sweep")
```

For large fields, material grids, or optimization arrays, transfer once and reuse script-side variable names. Prefer direct method return values for normal results.

## Accessing Results

Use `getresult` for datasets with axes, attributes, and metadata:

```python
with lumapi.FDTD("project.fsp", hide=True) as fdtd:
    fdtd.run()
    transmission = fdtd.getresult("T", "T")
    field = fdtd.getresult("field_xy", "E")

print(transmission.keys())
print(field.keys())
```

Dataset dictionaries typically include axes such as `lambda`, `f`, `x`, `y`, `z`, or `t`, field/data keys such as `T` or `E`, and a `Lumerical_dataset` metadata key. Do not assume a single shape. Print keys and shapes during development, then codify only the verified keys.

Use `getdata` for raw arrays:

```python
ex = fdtd.getdata("field_xy", "Ex")
freq = fdtd.getdata("field_xy", "f")
x = fdtd.getdata("field_xy", "x")
```

Use `numpy.squeeze()` only after verifying singleton dimensions are not meaningful for later broadcasting or coordinate alignment.

Safe access helper:

```python
def require_dataset(fdtd, object_name, result_name):
    names = fdtd.getresult(object_name)
    if result_name not in names:
        raise RuntimeError(
            f"{object_name!r} has no result {result_name!r}; available={names}"
        )
    return fdtd.getresult(object_name, result_name)
```

## FDTD Example Patterns

### Basic FDTD, Pythonic Style

Use this pattern for new PyLumerical scripts unless a local repo file already uses legacy command style:

```python
from collections import OrderedDict
import ansys.lumerical.core as lumapi

with lumapi.FDTD(hide=True) as fdtd:
    fdtd.addfdtd(
        dimension="2D",
        x=0.0,
        y=0.0,
        x_span=3.0e-6,
        y_span=1.0e-6,
        mesh_accuracy=3,
    )
    fdtd.addgaussian(
        name="source",
        injection_axis="y",
        direction="Forward",
        x=0.0,
        x_span=1.0e-6,
        y=-0.45e-6,
        waist_radius_w0=0.25e-6,
        wavelength_start=1.50e-6,
        wavelength_stop=1.60e-6,
    )
    fdtd.addmesh(
        name="mesh_core",
        x=0.0,
        x_span=0.8e-6,
        y=0.0,
        y_span=0.8e-6,
        override_x_mesh=True,
        override_y_mesh=True,
        dx=20e-9,
        dy=20e-9,
    )
    fdtd.addpower(properties=OrderedDict([
        ("name", "T"),
        ("monitor type", "Linear X"),
        ("override global monitor settings", True),
        ("frequency points", 101),
        ("x", 0.0),
        ("y", 0.45e-6),
        ("x span", 1.0e-6),
    ]))
    fdtd.save("basic_pythonic_fdtd.fsp")
```

Before using this pattern, inspect:

- `references/scraped/fdtd-example1-pythonic.md`
- `references/fdtd-setup.md`
- `references/mesh.md`
- `references/monitors-results.md`

### Basic FDTD, Lumerical Command Style

Use this pattern when migrating `.lsf`-style automation:

```python
with lumapi.FDTD(hide=True) as fdtd:
    fdtd.addfdtd()
    fdtd.set("dimension", "2D")
    fdtd.set("x span", 3e-6)
    fdtd.set("y span", 1e-6)

    fdtd.addgaussian()
    fdtd.set("name", "source")
    fdtd.set("injection axis", "y")
    fdtd.set("direction", "Forward")
    fdtd.set("y", -0.45e-6)

    fdtd.addpower()
    fdtd.set("name", "T")
    fdtd.set("monitor type", "Linear X")
    fdtd.set("y", 0.45e-6)
```

Before using this pattern, inspect `references/scraped/fdtd-example1-lsf.md`.

### Periodic/Bloch Sweep Pattern

For photonic crystals or periodic cells, inspect `references/scraped/photonic-crystal-bandstructure.md` before coding. The official example uses:

- `addstructuregroup` and `addtogroup` for programmatic geometry grouping.
- `addobject("dipole_cloud", properties=...)` and `addobject("bandstructure", properties=...)` for object-library analysis groups.
- FDTD boundaries set to `Bloch` and a background index.
- Sweep creation with `addsweep`, `setsweep`, `addsweepparameter`, `addsweepresult`, and `runsweep`.
- Result extraction with `getresult("bandstructure", "spectrum")`.

Agent rule: for Bloch/periodic PyLumerical scripts, read `references/boundaries-symmetry.md` and `references/scraped/photonic-crystal-bandstructure.md`, then record the `kx/ky/kz`, units, period, source, and monitor assumptions before coding.

### Metalens / Far-Field Pattern

For metasurfaces, metalenses, and focusing calculations, inspect `references/scraped/metalens-fdtd-with-projections.md` before coding. The official example is a multi-solver workflow: it uses RCWA to build phase/unit-cell data and FDTD to simulate the full lens with symmetric boundaries, downstream field monitors, and far-field calculations. Agent-generated variants must also inspect:

- `references/boundaries-symmetry.md` for symmetry validation.
- `references/monitors-results.md` for DFT/far-field monitors.
- `references/examples-and-commands.md` for far-field commands and official example links.

## lumopt2 Notes

`lumopt2` is the current PyLumerical-connected inverse-design module. It is not included inside the `ansys-lumerical-core` wheel itself; it is discovered from an installed Lumerical product when available. Current official pages say the module is available in Ansys Lumerical 2026 R1.2 or later.

PyLumerical import:

```python
import ansys.lumerical.core.lumopt2 as lmpt
```

Common workflow objects from the official user guide and examples:

- Parametrization/geometry: `Box`, `Segment`, `ClosedCurve`, `Parametrize`, and geometry-specific classes.
- Base simulation: a Python callable such as `generate_base_sim(fdtd)` that creates FDTD region, materials, structures, sources/ports, monitors, and global settings.
- Figure of merit: result adapters such as `PortResults` combined with `Fom` and objective functions such as `PNorm`.
- Project/session: `Project`, optional FDTD session/runner configuration, visualization of the initial setup and FOM.
- Optimizer: `ScipyOptimizer` and related optimizer configuration.
- Callbacks: graphical visualizers, monitor panels, file logging, geometry/FOM/gradient panels.
- Result export: save the final FDTD project after optimization with the best parameters.

Before writing `lumopt2` code, inspect:

```powershell
rg -n "lumopt2|Project|ClosedCurve|Parametrize|PortResults|ScipyOptimizer|Optimization|FileLogger" references
```

Do not treat lumopt2 as a generic optimizer wrapper. Its setup function must build a valid FDTD base simulation with correct ports/monitors and a figure of merit that matches the desired physical quantity.

## Troubleshooting

| Symptom | Checks |
| --- | --- |
| `ModuleNotFoundError: ansys.lumerical.core` | Confirm the active venv, `python -m pip show ansys-lumerical-core`, and interpreter used by the IDE/notebook. |
| Import warns that Lumerical cannot be found | Set `LUMERICAL_HOME` before import; verify installed version and default install path. |
| Session opens GUI during batch work | Pass `hide=True`; for headless/offscreen runs, audit `serverArgs`. |
| Command exists in script but fails in Python | Check whether it is a constructor command, whether keyword args are unsupported, and whether exact property strings are needed. |
| Property silently ignored or overwritten | Use `OrderedDict`; set object type/dimension/monitor type/override flags before dependent properties. |
| Object-handle edit changes the wrong object | Check duplicate names; enforce unique names. |
| Results dictionary lacks expected key | Call `getresult(object_name)` first, inspect available result names, confirm the simulation ran and the monitor recorded that output. |
| Raw arrays have unexpected dimensions | Inspect `.shape`, axes from `getdata`, and dataset metadata; only squeeze singleton axes after confirming intent. |
| `lumopt2` import fails | Confirm Lumerical version includes `lumopt2`, import through `ansys.lumerical.core.lumopt2`, and avoid manual `sys.path` overrides. |

## Pre-Code Notes Template

Use this template before editing or generating PyLumerical scripts:

```text
PyLumerical pre-code notes
- Package/import: ansys-lumerical-core via `import ansys.lumerical.core as lumapi`
- Version/license assumptions:
- Closest local example(s) inspected:
- Commands/properties audited:
- Session settings: hide/serverArgs/file/script:
- Solver region/background/boundaries:
- Source setup:
- Mesh setup and convergence plan:
- Monitor/result setup:
- Result keys expected:
- Risks/validation checks:
```
