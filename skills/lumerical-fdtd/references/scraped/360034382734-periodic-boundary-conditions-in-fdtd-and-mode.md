# Periodic boundary conditions in FDTD and MODE

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382734-Periodic-boundary-conditions-in-FDTD-and-MODE  
Area: Boundaries  
Topic: Unit-cell setup, periodic field requirement, PML pairing  
Discovery depth: 0  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Periodic boundary conditions in FDTD and MODE` for the topic `Unit-cell setup, periodic field requirement, PML pairing`. It captured 3 heading(s), 9 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Periodic boundary conditions in FDTD and MODE, Additional Tips, See also. Key detected terms: bfast, bloch, boundary, dipole, fdtd, import, material, mesh, mode, periodic, plane, pml, port, source, structure, symmetry.

## Key Terms

- bfast
- bloch
- boundary
- dipole
- fdtd
- import
- material
- mesh
- mode
- periodic
- plane
- pml
- port
- source
- structure
- symmetry

## Captured Headings

- Periodic boundary conditions in FDTD and MODE
- Additional Tips
- See also

## Official Text Excerpt

> Periodic boundary conditions in FDTD and MODE FDTD MODE When studying periodic systems, Periodic BC's allow you to calculate the response of the entire system by only simulating one unit cell. Periodic BC's are relatively straightforward to use in your simulation: simply set the simulation span to be one unit cell wide and select Periodic BC's for that boundary. When the simulation runs, the Periodic BC's simply copy the EM fields that occur at one side of the simulation and inject them at the other side. The most important detail to remember is that when using Periodic BC's, everything in the system must be periodic: both the the physical structure AND the EM fields. A common source of error is to use periodic boundary conditions in systems where the structure is periodic, but the EM fields are not. Examples include: - A periodic structure is illuminated by a plane wave propagating at an angle. The fields will not be quite periodic in this case, as there will be a phase difference between each period of the device. Use Bloch BC's ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Bloch BC's](https://optics.ansys.com/hc/en-us/articles/360034382714)
- [planewave](https://optics.ansys.com/hc/en-us/articles/360034382854)
- [BFAST](https://optics.ansys.com/hc/en-us/articles/360034902273)
- [Symmetric and anti-symmetric BCs](https://optics.ansys.com/hc/en-us/articles/360034382694)
- [PML profile](https://optics.ansys.com/hc/en-us/articles/360034382674)
- [Bloch boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382714)

## Ansys-Related External Links Found

- None

## External Links Found

- [Metamaterial Parameter Extraction Example](https://apps.lumerical.com/metamaterial-parameter-extraction-smith.html)
