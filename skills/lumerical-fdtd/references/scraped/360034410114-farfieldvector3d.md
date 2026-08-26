# farfieldvector3d - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034410114-farfieldvector3d  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldvector3d - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 7 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: farfieldvector3d - Script command. Key detected terms: command, dataset, far, fdtd, mode, monitor, script.

## Key Terms

- command
- dataset
- far
- fdtd
- mode
- monitor
- script

## Captured Headings

- farfieldvector3d - Script command

## Official Text Excerpt

> farfieldvector3d - Script command FDTD MODE The function farfieldvector3d is similar to farfield3d, but it returns the complex electric fields, rather than field intensity. The data is returned as matrix of NxMx3 (if one frequency point is projected) or NxMx3xP (if more than 1 frequency point is projected), where N and M are spatial indices, the third index refers to Ex, Ey and Ez in spherical coordinates, and P is the number of frequency points. The components Ex, Ey and Ez are the complex components of the electric field vector. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations. | Syntax | Description | out = farfieldvector3d( "mname",...); | Returns the cartesian complex electric fields. Same arguments as farfield3d. | out = farfieldvector3d( dataset,...); | Returns the cartesian complex electric fields. Same arguments as farfield3d. Example See example in the farfield3d function description. Understanding field polarization in far field projections See Also List of commands, farfield3d, farfieldpolar3d, Far field projections - Field polarization

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldvector3d( "mname",...); | Returns the cartesian complex electric fields. Same arguments as farfield3d.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d)
- [Understanding field polarization in far field projections](https://optics.ansys.com/hc/en-us/search/click?data=BAh7DjoHaWRsKwjB0cDTUwA6D2FjY291bnRfaWRpA02AjDoJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ2aHR0cHM6Ly9vcHRpY3MuYW5zeXMuY29tL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkxNDc1My1VbmRlcnN0YW5kaW5nLWZpZWxkLXBvbGFyaXphdGlvbi1pbi1mYXItZmllbGQtcHJvamVjdGlvbnMGOwhUOg5zZWFyY2hfaWRJIilkYjc4YzM5Yy1iOWU1LTRjNWUtYjE0NC02MGQzNjA4MGRkYWIGOwhGOglyYW5raQg6C2xvY2FsZUkiCmVuLXVzBjsIVDoKcXVlcnlJIhNmYXJmaWVsZHZlY3RvcgY7CFQ6EnJlc3VsdHNfY291bnRpEg%3D%3D--90007a278d7628d12a8c14265df095c4975dd311)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfieldpolar3d](https://optics.ansys.com/hc/en-us/articles/360034930713-farfieldpolar3d)
- [Far field projections - Field polarization](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)

## Ansys-Related External Links Found

- None

## External Links Found

- None
