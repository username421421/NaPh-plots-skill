# Python API And Automation

Use this file for Lumerical FDTD automation through legacy bundled `lumapi.py` or the newer PyAnsys/PyLumerical package. Primary official sources: [Python API overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview), [Installation and Getting Started - Python API](https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API), [Session Management - Python API](https://optics.ansys.com/hc/en-us/articles/360041873053-Session-Management-Python-API), [Script Commands as Methods - Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-Commands-as-Methods-Python-API), [Working with Simulation Objects - Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API), [Passing Data - Python API](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API), [Accessing Simulation Results - Python API](https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API), [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference), and [PyLumerical](https://lumerical.docs.pyansys.com/version/stable/index.html).

## Local API Choice

Default for this workspace: use the installed bundled API from `v261`.

```python
from pathlib import Path
import importlib.util

LUMAPI = Path(r"E:\Program Files\ANSYS Inc\v261\Lumerical\api\python\lumapi.py")


def load_lumapi(path=LUMAPI):
    spec = importlib.util.spec_from_file_location("lumapi", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load lumapi from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
```

Use PyLumerical when you want package-managed Python environments, notebooks, or PyAnsys integration. Read `references/pylumerical.md` before writing PyLumerical code; it contains the local PyLumerical workflow, example routing, installation/autodiscovery notes, Pythonic object patterns, and `lumopt2` guidance. It is installed as `ansys-lumerical-core` and commonly imported as:

```python
import ansys.lumerical.core as lumapi
```

PyLumerical can reuse much of the legacy `lumapi` command style, but it is distinct from the bundled `lumapi.py`. Check installed Lumerical discovery or set `LUMERICAL_HOME` when autodiscovery fails. Source: [PyLumerical getting started](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html).

## Session Pattern

Use a context manager for normal project builders so the Lumerical process closes reliably:

```python
lumapi = load_lumapi()

with lumapi.FDTD(hide=True) as fdtd:
    fdtd.newproject()
    fdtd.deleteall()
    # build objects
    fdtd.save(r"C:\path\to\project.fsp")
```

Useful constructor options documented in the Python API reference include product sessions such as `FDTD`, `MODE`, `DEVICE`, and `INTERCONNECT`, plus options for hidden/headless use, remote server connection, and startup arguments. Source: [Session Management - Python API](https://optics.ansys.com/hc/en-us/articles/360041873053-Session-Management-Python-API), [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference).

When using remote Interop Server, keep the host/port explicit and do not bury it inside helper defaults. Document license/server assumptions in the calling script.

## Script Commands As Python Methods

Most Lumerical script commands can be called as Python methods on the session. Property names remain Lumerical property strings, including spaces:

```python
from collections import OrderedDict

fdtd.addfdtd(properties=OrderedDict([
    ("dimension", "3D"),
    ("x", 0.0),
    ("x span", 4e-6),
    ("mesh accuracy", 2),
]))

fdtd.setnamed("FDTD", "simulation time", 1000e-15)
fdtd.setglobalsource("wavelength start", 1.50e-6)
fdtd.setglobalmonitor("frequency points", 101)
```

Use `OrderedDict` where linked properties may depend on earlier properties, such as setting monitor type before spans, source type before direction, or mesh mode before dx/dy/dz. Source: [Working with Simulation Objects - Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API).

Use `eval` sparingly for blocks that are easier in native script syntax, especially import objects or array-heavy object construction:

```python
fdtd.putv("eps_grid", eps_grid)
fdtd.eval("""
addimport;
set("name", "spatial_index");
importnk2(eps_grid, x, y, z);
""")
```

Prefer method calls for normal object creation because they are easier to lint and refactor.

## Data Transfer

Use `putv` for arrays/scalars from Python into the Lumerical workspace and `getv` for variables back to Python. The official API maps Python numeric/string/list/NumPy-like values to Lumerical types; large arrays should be transferred once and reused by script variables rather than repeatedly crossing the API boundary. Source: [Passing Data - Python API](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API).

```python
fdtd.putv("x_um", [0.0, 0.1, 0.2])
fdtd.eval("x_m = x_um*1e-6;")
result = fdtd.getv("x_m")
```

## Results

Use `getresult` when you want a named result dataset with axes and fields. Use `getdata` for raw arrays from a specific monitor or object.

```python
transmission = fdtd.getresult("T_monitor", "T")
field = fdtd.getresult("field_xy", "E")
ex = fdtd.getdata("field_xy", "Ex")
frequency = fdtd.getdata("field_xy", "f")
```

Pattern for safe result access:

```python
def require_result(fdtd, object_name, result_name):
    available = fdtd.getresult(object_name)
    if result_name not in available:
        raise RuntimeError(f"{object_name!r} has no result {result_name!r}; available={available}")
    return fdtd.getresult(object_name, result_name)
```

Result datasets commonly contain coordinate axes plus fields. Inspect keys before assuming shape:

```python
data = fdtd.getresult("field_xy", "E")
print(data.keys())
```

Source: [Accessing Simulation Results - Python API](https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API).

## Failure Modes

- API import fails: verify `lumapi.py` path and bitness/Python compatibility.
- A command works in script but fails as a method: check command name, argument order, and whether a property should be passed through `properties=OrderedDict`.
- Object properties silently differ: set the object type/dimension/monitor type first, then dependent spans and options.
- Results missing: confirm the simulation ran, monitor name is correct, and the monitor recorded the requested component/result.
- Automation hangs: close sessions with a context manager, keep `hide=True` for builders, and avoid interactive GUI prompts in batch jobs.
