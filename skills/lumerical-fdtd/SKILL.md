---
name: lumerical-fdtd
description: Use when creating, modifying, reviewing, or debugging Ansys Lumerical FDTD simulations, Python lumapi/PyLumerical automation, FDTD solver setup, mesh, boundaries, symmetry, sources, monitors, results, convergence, or script-command usage.
---

# Lumerical FDTD

Use local files first. This skill contains a local Lumerical FDTD reference corpus under `references/`; do not browse for routine API, setup, command, property, or example lookup unless the local corpus is missing the needed information or the user explicitly asks for live verification.

## Before writing code

Before writing code, complete the local research workflow first. Do not write or modify simulation code until all four checks below are complete:

1. **Search Similar Local Examples**: search `references/pylumerical.md`, `references/examples-and-commands.md`, `references/corpus-index.md`, and `references/keyword-index.md` for the closest official Ansys/Lumerical or PyLumerical documentation pattern before choosing an implementation style.
2. **Function And Argument Audit**: identify every Lumerical command/API method needed, then inspect the relevant local reference page(s) for required arguments, property names, object type strings, and result names.
3. **Implementation Notes Before Coding**: write short notes for the chosen source, monitor, boundary, mesh, and result-extraction approach, including any assumptions and convergence risks.
4. **Then Code**: implement only after the example pattern and function/property arguments are known.

Use `rg` first for local search. Good searches:

```powershell
rg -n "addfdtd|addmesh|adddftmonitor|addmode|addport|getresult|getdata" references
rg -n "PyLumerical|ansys\\.lumerical\\.core|serverArgs|OrderedDict|SimObject|lumopt2" references
rg -n "mode source|plane wave|dipole|TFSF|ports|far field|reflection" references
rg -n "mesh accuracy|mesh override|conformal|PML|Bloch|Symmetric|Anti-Symmetric" references
```

When working from inside the skill folder, `references/scraped/` contains local captured pages from official Ansys/PyAnsys docs. Use these local pages to inspect headings, key terms, table inventories, code inventories, and captured argument/property snippets.

## Reference Routing

- PyLumerical / PyAnsys package usage, `ansys.lumerical.core`, Pythonic constructors, object handles, PyLumerical examples, autodiscovery, `serverArgs`, `OrderedDict`, result dictionaries, and `lumopt2`: read `references/pylumerical.md`, then `references/python-api.md` for shared `lumapi` behavior.
- Legacy bundled `lumapi.py`, sessions, object creation, data transfer, `getresult`, and `getdata`: read `references/python-api.md`.
- FDTD solver region, background material/index, simulation time, auto shutoff, global source/monitor settings, materials, and geometry conventions: read `references/fdtd-setup.md`.
- Mesh accuracy, mesh overrides, conformal mesh, non-uniform mesh, mesh order, and mesh convergence: read `references/mesh.md`.
- PML, periodic, Bloch, symmetric/anti-symmetric boundaries, parity, monitor behavior with symmetry, and full-domain validation: read `references/boundaries-symmetry.md`.
- Plane/Gaussian/beam sources, mode sources, dipoles, TFSF, and ports: read `references/sources.md`.
- DFT monitors, time monitors, mode expansion, reflection/transmission placement, far-field projection, and result access: read `references/monitors-results.md`.
- Reusable local snippets, script-command links, and official example index: read `references/examples-and-commands.md`.
- Final review and convergence checklist: read `references/convergence-checklist.md`.
- Broad local source discovery: search `references/corpus-index.md`, `references/keyword-index.md`, and `references/link-graph.md`.

## Command And Property Audit

Before using a command, inspect local references for object type strings and properties. Common command targets:

| Task | Commands/properties to audit |
| --- | --- |
| Add FDTD region | `addfdtd`, `dimension`, spans, `background material`, `simulation time`, `auto shutoff min`, boundary properties |
| Mesh control | `addmesh`, `override x mesh`, `override y mesh`, `override z mesh`, `dx`, `dy`, `dz`, mesh order |
| Plane/beam source | `addplane` or source object, injection axis, direction, polarization, wavelength/global source settings |
| Mode source | `addmode`, injection axis, direction, transverse spans, mode selection, broadband mode settings |
| Dipole | `adddipole`, position, orientation, bandwidth, symmetry compatibility |
| Ports | `addport`, mode/source port settings, S-parameter extraction |
| DFT monitor | `adddftmonitor`, monitor type, spans, output power/components, frequency points |
| Time monitor | `addtime`, monitor type, sample location, simulation time adequacy |
| Mode expansion | `addmodeexpansion`, monitor plane, mode selection, expansion direction |
| Results | `getresult`, `getdata`, monitor names, result keys, dataset axes |

Use exact Lumerical property names, including spaces. Prefer `OrderedDict` when object type or mode must be set before dependent properties.

## Implementation Notes Before Coding

Before editing files, note:

- Chosen Ansys/Lumerical reference page(s) and why.
- Lumerical API style: bundled `lumapi.py` or PyLumerical. If using PyLumerical, name the closest local PyLumerical example and the API/user-guide page used for function/property syntax.
- Solver region dimensions, background material/index, simulation time, and shutoff target.
- Boundary choices and why symmetry/Bloch/periodic/PML are valid.
- Source type, source placement, bandwidth, and polarization/mode selection.
- Mesh accuracy, local overrides, and convergence plan.
- Monitor placement, monitor type, frequency points, and result names to extract.
- Any local reference pages used for function arguments/properties.

If these notes reveal uncertainty, inspect more local references before coding.

## Maintenance Only

The scraper in `scripts/scrape_lumerical_docs.py` is only for refreshing the local corpus. It is not part of the normal simulation-building workflow. Use it only when the local references need an update.
