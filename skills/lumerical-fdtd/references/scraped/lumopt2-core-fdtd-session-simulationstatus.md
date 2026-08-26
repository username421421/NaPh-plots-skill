# SimulationStatus [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#simulationstatus)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `SimulationStatus [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#simulationstatus)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 8 link(s), 0 code block(s), 6 inline code term(s), and 2 table(s). Main headings: SimulationStatus [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#simulationstatus). Key detected terms: fdtd, lumopt, material, mesh, mode.

## Key Terms

- fdtd
- lumopt
- material
- mesh
- mode

## Captured Headings

- SimulationStatus [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#simulationstatus)

## Official Text Excerpt

> SimulationStatus # class lumopt2.core.fdtd_session. SimulationStatus (* values) # FDTD simulation status codes. Attributes: LAYOUT_MODE``int Simulation is in layout mode (status 0). This indicates the simulation did not run, possibly due to a setup error or license issue. FULL_TIME``int Simulation ran to full simulation time (status 1). Success. AUTOSHUTOFF``int Simulation ran to autoshutoff (status 2). Success. DIVERGED``int Simulation diverged (status 3). The electromagnetic fields became unstable, often due to material dispersion or mesh issues. Methods | ``SimulationStatus.from_bytes (/, bytes[, ...]) | Return the integer represented by the given array of bytes. Attributes | ``SimulationStatus.LAYOUT_MODE | | ``SimulationStatus.FULL_TIME | | ``SimulationStatus.AUTOSHUTOFF | | ``SimulationStatus.DIVERGED |

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `SimulationStatus.AUTOSHUTOFF`
- `SimulationStatus.DIVERGED`
- `SimulationStatus.FULL_TIME`
- `SimulationStatus.LAYOUT_MODE`
- `SimulationStatus.from_bytes`
- `int`

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - First row sample: SimulationStatus.from_bytes (/, bytes[, ...]) | Return the integer represented by the given array of bytes.
- Table 2: 2 column(s), 4 row(s)
  - First row sample: SimulationStatus.LAYOUT_MODE | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#simulationstatus)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#lumopt2.core.fdtd_session.SimulationStatus)
- [SimulationStatus.from_bytes](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.from_bytes.html#lumopt2.core.fdtd_session.SimulationStatus.from_bytes)
- [SimulationStatus.LAYOUT_MODE](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.LAYOUT_MODE.html#lumopt2.core.fdtd_session.SimulationStatus.LAYOUT_MODE)
- [SimulationStatus.FULL_TIME](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.FULL_TIME.html#lumopt2.core.fdtd_session.SimulationStatus.FULL_TIME)
- [SimulationStatus.AUTOSHUTOFF](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.AUTOSHUTOFF.html#lumopt2.core.fdtd_session.SimulationStatus.AUTOSHUTOFF)
- [SimulationStatus.DIVERGED](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.DIVERGED.html#lumopt2.core.fdtd_session.SimulationStatus.DIVERGED)

## Ansys-Related External Links Found

- None

## External Links Found

- [int](https://docs.python.org/3/library/functions.html#int)
