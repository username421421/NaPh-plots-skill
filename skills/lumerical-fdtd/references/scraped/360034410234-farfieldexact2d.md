# farfieldexact2d - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034410234-farfieldexact2d  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldexact2d - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 7 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: farfieldexact2d - Script command. Key detected terms: command, dataset, far, fdtd, material, mode, monitor, script.

## Key Terms

- command
- dataset
- far
- fdtd
- material
- mode
- monitor
- script

## Captured Headings

- farfieldexact2d - Script command

## Official Text Excerpt

> farfieldexact2d - Script command FDTD MODE This function projects complete complex vector fields to specific locations. It is expected to be correct down to distances on the order of one wavelength. The projections from multiple monitors can be added to create a total far field projection - see Projections from a monitor box. farfieldexact2d projects any surface to the grid points defined by the vectors x, y. If only E field is returned as the result, the data is returned in the form of a matrix that is of dimension NxMxPx3 where N is the length of the x vector, M is the length of the y vector, P is the number of frequency points, and the final index represents Ex, Ey, and Ez. Note that N and M can be 1; when they are both 1, the function is the same as farfieldexact. If both E and H fileds are returned, the data is returned as a dataset with the E and H fields packaged with the corresponding x,y, and frequency/wavelength. | Syntax | Description | out = farfieldexact2d( ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldexact2d( "mname", x, y, f, index); | Projects a given power or field profile monitor to the far field at grid points specified by the vectors x,y. Returns E field only.
- Table 2: 5 column(s), 7 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: mname | required |  | string | name of the monitor from which far field is calculated.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Projections from a monitor box](https://optics.ansys.com/hc/en-us/articles/360034915613-Projections-from-a-monitor-box)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfield2d](https://optics.ansys.com/hc/en-us/articles/360034410074-farfield2d)
- [farfieldexact3d](https://optics.ansys.com/hc/en-us/articles/360034930733-farfieldexact3d)
- [farfieldexact](https://optics.ansys.com/hc/en-us/articles/360034410214-farfieldexact)

## Ansys-Related External Links Found

- None

## External Links Found

- None
