# farfield2dintegrate - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930673-farfield2dintegrate  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfield2dintegrate - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 5 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: farfield2dintegrate - Script command. Key detected terms: command, far, fdtd, mode, script.

## Key Terms

- command
- far
- fdtd
- mode
- script

## Captured Headings

- farfield2dintegrate - Script command

## Official Text Excerpt

> farfield2dintegrate - Script command FDTD MODE Calculates the integral of the far field projection over some range of theta in 2D simulation. Angles are specified in degrees, but the integral is done in radians. $$ \int_{\theta} E^{2}(\theta) d \theta $$ | Syntax | Description | out = farfield2dintegrate(E2, theta, halfangle, theta0); | Integrate 2D far field projection data. | Parameter || Default value | Type | Description | E2 | required || matrix | E field data from farfield2d | theta | required || matrix | Theta from farfieldangle | halfangle | optional | 90 | vector | Half angle (in degrees) of the integration region. Must have same length as theta0 or length 1. Half angle should be between 0 to 90 degrees. | theta0 | optional | 0 | vector | Center angle (in degrees) theta of the integration region. Must have same length as halfangle or length 1. Theta0 should be between -90 to 90 degrees. Example Calculate the fraction of power in the far field from 20 to 70 degrees. See Also List of commands, farfield2d, ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `m="monitor1";`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfield2dintegrate(E2, theta, halfangle, theta0); | Integrate 2D far field projection data.
- Table 2: 5 column(s), 4 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: E2 | required |  | matrix | E field data from farfield2d

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfield2d](https://optics.ansys.com/hc/en-us/articles/360034410074-farfield2d)
- [farfieldangle](https://optics.ansys.com/hc/en-us/articles/360034930653-farfieldangle)

## Ansys-Related External Links Found

- None

## External Links Found

- None
