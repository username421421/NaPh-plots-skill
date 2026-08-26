# farfieldvector2d - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930633-farfieldvector2d  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldvector2d - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 7 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: farfieldvector2d - Script command. Key detected terms: command, dataset, far, fdtd, mode, monitor, script.

## Key Terms

- command
- dataset
- far
- fdtd
- mode
- monitor
- script

## Captured Headings

- farfieldvector2d - Script command

## Official Text Excerpt

> farfieldvector2d - Script command FDTD MODE Projects a given power or field profile monitor or a rectilinear dataset to the far field to a 1 meter radius semi-circle. This is similar to the farfield2d script command except the complex electric fields are returned, rather than field intensity. The data is returned as matrix of NxP if one frequency point is projected, or NxPx3 when multiple frequency points are projected where N is the resolution of the far field projection, P is the number frequency points projected, and the last index refers to Ex, Ey and Ez which are the complex components of the electric field vector in Cartesian coordinates. | Syntax | Description | out = farfieldvector2d( "mname",...); | Returns the Cartesian complex electric fields. Same arguments as farfield2d. | out = farfieldvector2d( dataset,...); | Returns the Cartesian complex electric fields. Same arguments as farfield2d. Example This example plots the amplitude of the Ex component of the far field projection of a 1D monitor called "monitor". In this example the second frequency point is projected. If the monitor only contains ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `E=farfieldvector2d("monitor",2,501);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldvector2d( "mname",...); | Returns the Cartesian complex electric fields. Same arguments as farfield2d.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [farfield2d](https://optics.ansys.com/hc/en-us/articles/360034410074-farfield2d)
- [Far field projection](https://optics.ansys.com/hc/en-us/articles/360034914713)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfieldpolar2d](https://optics.ansys.com/hc/en-us/articles/360034410094-farfieldpolar2d)
- [farfieldangle](https://optics.ansys.com/hc/en-us/articles/360034930653-farfieldangle)

## Ansys-Related External Links Found

- None

## External Links Found

- None
