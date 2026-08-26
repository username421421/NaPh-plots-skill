# seteigensolver - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `seteigensolver - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 15 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: seteigensolver - Script command. Key detected terms: command, fdtd, mode, monitor, port, script, solver, source.

## Key Terms

- command
- fdtd
- mode
- monitor
- port
- script
- solver
- source

## Captured Headings

- seteigensolver - Script command

## Official Text Excerpt

> seteigensolver - Script command FDTD MODE Mode sources, mode expansion monitors, and ports in FDTD and MODE, and each individual cell in EME have embedded eigensolvers. This script command makes it possible to set the properties of that eigensolver without using the GUI. Changing any values of the embedded eigensolver with this command will automatically invalidate any existing mode data. This means that new updates based on overlap calculations with previous modes will fail after using this command. Therefore please call this command before making any calls to updatesourcemode or updatemodes. | Syntax | Description | ?seteigensolver; | Returns a list of the properties of the embedded eigensolver | seteigensolver("property",value); | This will set the eigensolver properties of the currently selected objects. Value can be a number or string. This function does not return any data. Example - Change the radius of curvature for a mode expansion calculation, and calculate the first 10 modes which can be subsequently used for mode expansion. Please open ring_resonator2.lms from the ring resonator example using the varFDTD solver in MODE: 2. Change the number ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `select("expansion");`
- Code block 2: 3 line(s); first line `seteigensolver("bent waveguide",true);`
- Code block 3: 1 line(s); first line `select("EME::Cells::cell_1");seteigensolver("number of trial modes",25);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: ?seteigensolver; | Returns a list of the properties of the embedded eigensolver

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [ring resonator example](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)
- [addmodeexpansion](https://optics.ansys.com/hc/en-us/articles/360034924573-addmodeexpansion)
- [addport](https://optics.ansys.com/hc/en-us/articles/360034924793-addport)
- [Manipulating objects](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [addmode](https://optics.ansys.com/hc/en-us/articles/360034924353-addmode)
- [clearsourcedata](https://optics.ansys.com/hc/en-us/articles/360034929093-clearsourcedata)
- [clearmodedata](https://optics.ansys.com/hc/en-us/articles/360034408774-clearmodedata)
- [clearportmodedata](https://optics.ansys.com/hc/en-us/articles/360034409194-clearportmodedata)
- [expand](https://optics.ansys.com/hc/en-us/articles/360034926653-expand)
- [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
- [updatemodes](https://optics.ansys.com/hc/en-us/articles/360034929073-updatemodes)
- [updatesourcemode](https://optics.ansys.com/hc/en-us/articles/360034408754-updatesourcemode)
- [updateportmodes](https://optics.ansys.com/hc/en-us/articles/360034409174-updateportmodes)

## Ansys-Related External Links Found

- None

## External Links Found

- None
