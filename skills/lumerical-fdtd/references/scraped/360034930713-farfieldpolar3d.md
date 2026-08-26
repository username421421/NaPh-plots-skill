# farfieldpolar3d - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930713-farfieldpolar3d  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldpolar3d - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 6 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: farfieldpolar3d - Script command. Key detected terms: command, dataset, far, fdtd, mode, monitor, script.

## Key Terms

- command
- dataset
- far
- fdtd
- mode
- monitor
- script

## Captured Headings

- farfieldpolar3d - Script command

## Official Text Excerpt

> farfieldpolar3d - Script command FDTD MODE The function farfieldpolar3d is similar to farfield3d, but it returns the complex electric fields, rather than field intensity. The data is returned as matrix of NxMx3 (if one frequency point is projected) or NxMx3xP (if more than 1 frequency point is projected), where N and M are spatial indices, the third index refers to E r, E θ and E φ, in spherical coordinates, and P is the number of frequency points. The components E r, E θ and E φ are the complex components of the electric field vector. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations. Note: When viewing far fields from the GUI with the visualizer, three Attributes are available: E2, Ep, Es. E2 corresponds to |E|^2, Ep to Etheta, and Es to Ephi. | Syntax | Description | out = farfieldpolar3d( "mname",...); | Returns the spherical complex electric fields. Same arguments as farfield3d. | out = farfieldpolar3d( dataset,...); | Returns the spherical complex electric fields. Same arguments as farfield3d. Example See example ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldpolar3d( "mname",...); | Returns the spherical complex electric fields. Same arguments as farfield3d.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfieldvector3d](https://optics.ansys.com/hc/en-us/articles/360034410114-farfieldvector3d)
- [Far field projections - Field polarization](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)

## Ansys-Related External Links Found

- None

## External Links Found

- None
