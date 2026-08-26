# Examples And Commands

Use this file for reusable local snippets, command patterns, official example links, and workspace examples.

## Command Sources

Official command references:

| Command | Official source | Purpose |
| --- | --- | --- |
| `addfdtd` | [`addfdtd` script command](https://optics.ansys.com/hc/en-us/articles/360034924173-addfdtd-Script-command) | Add FDTD solver region |
| `addmesh` | [`addmesh` script command](https://optics.ansys.com/hc/en-us/articles/360034924253-addmesh-Script-command) | Add mesh override |
| `adddftmonitor` | [`adddftmonitor` script command](https://optics.ansys.com/hc/en-us/articles/36957320687763-adddftmonitor-Script-command) | Add frequency-domain monitor |
| `addmode` | [`addmode` script command](https://optics.ansys.com/hc/en-us/articles/360034924353-addmode-Script-command) | Add FDTD mode source |
| `addmodeexpansion` | [`addmodeexpansion` script command](https://optics.ansys.com/hc/en-us/articles/360034924573-addmodeexpansion-Script-command) | Add mode expansion monitor |
| `addport` | [`addport (FDTD)` script command](https://optics.ansys.com/hc/en-us/articles/360034924793-addport-FDTD-Script-command) | Add FDTD port |
| script index | [Lumerical scripting alphabetical list](https://optics.ansys.com/hc/en-us/articles/360034923553-Lumerical-scripting-language-Alphabetical-list) | Find related commands |

## End-To-End Builder Skeleton

```python
from collections import OrderedDict
from pathlib import Path
import importlib.util

UM = 1e-6
NM = 1e-9
FS = 1e-15
LUMAPI = Path(r"E:\Program Files\ANSYS Inc\v261\Lumerical\api\python\lumapi.py")


def load_lumapi():
    spec = importlib.util.spec_from_file_location("lumapi", LUMAPI)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add_solver(fdtd):
    fdtd.addfdtd(properties=OrderedDict([
        ("name", "FDTD"),
        ("dimension", "3D"),
        ("x span", 6.0 * UM),
        ("y span", 4.0 * UM),
        ("z span", 2.0 * UM),
        ("background material", "SiO2 (Glass) - Palik"),
        ("mesh accuracy", 2),
        ("simulation time", 1200 * FS),
        ("auto shutoff min", 1e-5),
        ("x min bc", "PML"),
        ("x max bc", "PML"),
        ("y min bc", "PML"),
        ("y max bc", "PML"),
        ("z min bc", "PML"),
        ("z max bc", "PML"),
    ]))


def add_mesh(fdtd):
    fdtd.addmesh(properties=OrderedDict([
        ("name", "mesh_device"),
        ("x span", 2.0 * UM),
        ("y span", 1.0 * UM),
        ("z span", 500 * NM),
        ("override x mesh", 1),
        ("override y mesh", 1),
        ("override z mesh", 1),
        ("dx", 20 * NM),
        ("dy", 20 * NM),
        ("dz", 10 * NM),
    ]))


def add_mode_source(fdtd):
    fdtd.addmode(properties=OrderedDict([
        ("name", "src_mode"),
        ("injection axis", "x"),
        ("direction", "Forward"),
        ("x", -2.5 * UM),
        ("y span", 1.5 * UM),
        ("z span", 1.0 * UM),
        ("mode selection", "fundamental mode"),
    ]))


def add_power_monitor(fdtd):
    fdtd.adddftmonitor(properties=OrderedDict([
        ("name", "T_out"),
        ("monitor type", "2D X-normal"),
        ("x", 2.5 * UM),
        ("y span", 1.5 * UM),
        ("z span", 1.0 * UM),
        ("use source limits", 1),
        ("output power", 1),
    ]))


def build(output_path):
    lumapi = load_lumapi()
    with lumapi.FDTD(hide=True) as fdtd:
        fdtd.newproject()
        fdtd.deleteall()
        add_solver(fdtd)
        fdtd.setglobalsource("set wavelength", 1)
        fdtd.setglobalsource("wavelength start", 1.50 * UM)
        fdtd.setglobalsource("wavelength stop", 1.60 * UM)
        fdtd.setglobalmonitor("use source limits", 1)
        fdtd.setglobalmonitor("frequency points", 51)
        add_mesh(fdtd)
        add_mode_source(fdtd)
        add_power_monitor(fdtd)
        fdtd.save(str(output_path))


if __name__ == "__main__":
    build(Path("reference_project.fsp").resolve())
```

## Official Example Index

Do not mirror full official example files locally unless the user has a license/right to store them. Keep official links and write local original examples.

| Example/page | What to learn |
| --- | --- |
| [PyLumerical examples](https://lumerical.docs.pyansys.com/version/stable/examples.html) | Basic session, FDTD styles, metalens, photonic crystal examples |
| [PyLumerical getting started](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html) | Thin-film example through Python and Lumerical commands |
| [Accessing Simulation Results - Python API](https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API) | `getresult` and `getdata` workflow |
| [Reflection and transmission calculations using a planewave](https://optics.ansys.com/hc/en-us/articles/360042089573-Reflection-and-transmission-calculations-using-a-planewave) | Planewave R/T, angle sweep, mesh sensitivity |
| [TFSF best practices](https://optics.ansys.com/hc/en-us/articles/360034382934-Tips-and-best-practices-when-using-the-FDTD-TFSF-source) | Scattering setup, normalization, source placement |
| [Convergence testing](https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing-process-for-FDTD-simulations) | Mesh/PML/source/monitor convergence examples |
| [Far field projections](https://optics.ansys.com/hc/en-us/articles/360034914713-Far-field-projections-in-FDTD-overview) | Near-field monitor placement and projection requirements |
| [Plane/beam source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object) | Plane and Gaussian beam source behavior |
| [Dipole source](https://optics.ansys.com/hc/en-us/articles/360034382794-Dipole-source-Simulation-object) | Electric/magnetic dipole setup and emission metrics |
| [Mode source](https://optics.ansys.com/hc/en-us/articles/360034902153-Mode-source-Simulation-object) | Guided-mode injection and mode selection |

## Local Workspace Examples

- `agent.md`: current `v261` Lumerical Python/API paths and project-building expectations.
- `MMI test/build_1x2_mmi_fdtd.py`: mode source, silicon/SiO2 materials, MMI geometry, local mesh override, power/profile monitors.
- `nanolens close-packed array/scripts/nanolens_array_lumerical.py`: template loading, dipole parity/symmetry setup, directivity analysis group, GPU run/export workflow, full-PML baseline mode.
- `Structural color inverse design/build_red_mma_d4_fdtd.py`: imported index design through `putv`/`eval`, plane-wave source, far-field monitor box, reference project creation.

## Command Pattern Notes

- Use `properties=OrderedDict([...])` for object creation when property order matters.
- Use `setnamed` for changing existing objects after creation.
- Use `setglobalsource` and `setglobalmonitor` once near the top of the builder.
- Use `putv`/`eval` for array-heavy imports or native script-only operations.
- Use `getresult` for named result datasets and `getdata` for raw arrays.
