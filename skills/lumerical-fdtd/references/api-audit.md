# Lumerical API audit details

For a new builder or changed object configuration, consult only the relevant rows
and notes below. Reuse verified evidence for unchanged behavior.

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

For new or changed simulation behavior, note the applicable items below. Keep notes proportional to the change and identify reused campaign evidence:

- Chosen Ansys/Lumerical reference page(s) and why.
- Lumerical API style: bundled `lumapi.py` or PyLumerical. If using PyLumerical, name the closest local PyLumerical example and the API/user-guide page used for function/property syntax.
- Solver region dimensions, background material/index, simulation time, and shutoff target.
- Boundary choices and why symmetry/Bloch/periodic/PML are valid.
- Source type, source placement, bandwidth, and polarization/mode selection.
- Mesh accuracy, local overrides, and convergence plan.
- Monitor placement, monitor type, frequency points, and result names to extract.
- Any local reference pages used for function arguments/properties.

If these notes reveal uncertainty, inspect more local references before coding.

