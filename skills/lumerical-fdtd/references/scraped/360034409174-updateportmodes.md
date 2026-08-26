# updateportmodes - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034409174-updateportmodes  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `updateportmodes - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 8 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: updateportmodes - Script command. Key detected terms: command, fdtd, mode, port, script, solver, source.

## Key Terms

- command
- fdtd
- mode
- port
- script
- solver
- source

## Captured Headings

- updateportmodes - Script command

## Official Text Excerpt

> updateportmodes - Script command FDTD MODE Selects the specified modes in the selected port object in FDTD or MODE's EME solver, or updates already selected port modes. Modes are specified by the mode number in the eigensolver's mode list. For more information about the port object in FDTD see Ports. | Syntax | Description | updateportmodes(modes_to_select); | Selects the specified modes in the the selected port object. This function returns 1 if modes were updated successfully and -1 if there was an error updating the modes. | updateportmodes; | Updates the mode profiles of the selected mode ports. Examples The following demonstrates different possible syntax that can be used to specify the list of modes to select. The following script adds a FDTD simulation region and port, then sets the name of the port, and selects the port modes and source mode. See Also Ports, addport, set, geteigensolver, seteigensolver, clearportmodedata

## Code Block Inventory

- Code block 1: 10 line(s); first line `# select the second mode`
- Code block 2: 12 line(s); first line `# add objects`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: updateportmodes(modes_to_select); | Selects the specified modes in the the selected port object. This function returns 1 if modes were updated successfully and -1 if there was an error updating the modes.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Ports](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports)
- [addport](https://optics.ansys.com/hc/en-us/articles/360034924793-addport)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
- [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
- [seteigensolver](https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver)
- [clearportmodedata](https://optics.ansys.com/hc/en-us/articles/360034409194-clearportmodedata)

## Ansys-Related External Links Found

- None

## External Links Found

- None
