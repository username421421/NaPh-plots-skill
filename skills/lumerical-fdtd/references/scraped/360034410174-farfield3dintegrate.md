# farfield3dintegrate - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034410174-farfield3dintegrate  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfield3dintegrate - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 7 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: farfield3dintegrate - Script command. Key detected terms: command, far, fdtd, mode, monitor, script, source.

## Key Terms

- command
- far
- fdtd
- mode
- monitor
- script
- source

## Captured Headings

- farfield3dintegrate - Script command

## Official Text Excerpt

> farfield3dintegrate - Script command FDTD MODE Integrates the far field projection over a cone centered at theta0 and phi0, with a width specified by halfangle for 3D simulations. The far field electric field is a function of the direction cosines (ux,uy), but farfield3dintegrate automatically does the change of variables. Similarly, angles are specified in degrees, but converted to radians before the integral is calculated. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations. $$ \iint_{\theta, \phi} E^{2}(u x, u y) \sin (\theta) d \theta d \phi $$ | Syntax | Description | out = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); | Integrate 3D far field projection data. | Parameter || Default value | Type | Description | E2 | required || matrix | E field data from farfield3d | ux | required || vector | ux data from farfieldux. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point. | uy | required || vector | uy data from farfielduy. ...

## Code Block Inventory

- Code block 1: 13 line(s); first line `m="monitor1";`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); | Integrate 3D far field projection data.
- Table 2: 5 column(s), 6 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: E2 | required |  | matrix | E field data from farfield3d

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d)
- [farfieldux](https://optics.ansys.com/hc/en-us/articles/360034410134-farfieldux)
- [farfielduy](https://optics.ansys.com/hc/en-us/articles/360034410154-farfielduy)
- [farfieldspherical](https://optics.ansys.com/hc/en-us/articles/360034410194-farfieldspherical)

## Ansys-Related External Links Found

- None

## External Links Found

- None
