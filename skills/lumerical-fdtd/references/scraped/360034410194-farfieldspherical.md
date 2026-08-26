# farfieldspherical - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034410194-farfieldspherical  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldspherical - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 9 link(s), 2 code block(s), 0 inline code term(s), and 2 table(s). Main headings: farfieldspherical - Script command. Key detected terms: command, far, fdtd, mesh, mode, monitor, script.

## Key Terms

- command
- far
- fdtd
- mesh
- mode
- monitor
- script

## Captured Headings

- farfieldspherical - Script command

## Official Text Excerpt

> farfieldspherical - Script command FDTD MODE Interpolates far field data (3D simulations) from E(ux,uy) to spherical coordinates E(theta,phi) 1D array. The far field projections functions generally return the projection as a function of ux,uy (direction cosines). farfieldspherical can be used to interpolate this data into the more common units of theta, phi. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations. | Syntax | Description | out = farfieldspherical( E2, ux, uy, theta, phi); | Interpolate far field data to spherical coordinates. The output has a size of (MxN,1) | Parameter || Default value | Type | Description | E2 | required || matrix | E field data from farfield3d | ux | required || vector | ux data from farfieldux. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point. | uy | required || vector | uy data from farfielduy. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command ...

## Code Block Inventory

- Code block 1: 8 line(s); first line `m="Monitor1";  # Monitor name`
- Code block 2: 5 line(s); first line `theta = linspace(-90,90,10);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldspherical( E2, ux, uy, theta, phi); | Interpolate far field data to spherical coordinates. The output has a size of (MxN,1)
- Table 2: 5 column(s), 5 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: E2 | required |  | matrix | E field data from farfield3d

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d)
- [farfieldux](https://optics.ansys.com/hc/en-us/articles/360034410134-farfieldux)
- [farfielduy](https://optics.ansys.com/hc/en-us/articles/360034410154-farfielduy)
- [Far field projections - Direction unit vector coordinates](https://optics.ansys.com/hc/en-us/articles/360034394294-FFP-Direction-unit-vector-coordinates)
- [meshgridx](https://optics.ansys.com/hc/en-us/articles/360034409334-meshgridx)
- [meshgridy](https://optics.ansys.com/hc/en-us/articles/360034929673-meshgridy)

## Ansys-Related External Links Found

- None

## External Links Found

- None
