# getperiodicity - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034407174-getperiodicity  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getperiodicity - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 5 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: getperiodicity - Script command. Key detected terms: boundary, command, grating, periodic, script, solver, source.

## Key Terms

- boundary
- command
- grating
- periodic
- script
- solver
- source

## Captured Headings

- getperiodicity - Script command

## Official Text Excerpt

> getperiodicity - Script command DGTD Returns the periodicity vector(s) associated with the active periodic boundary conditions in the specified solver. | Syntax | Description | out = getperiodicity("solvername"); | Returns the periodicity vector(s) of the system based on the active periodic boundary conditions in the named solver. The output is a [3XN] matrix where N is the number of dimensions that have active periodic boundary conditions (typically one or two). | Parameter || Default value | Type | Description | solvername | required || string | Name of the solver from which to extract the periodicity vector(s). Example This example retrieves the periodicity vectors from a DGTD simulation with periodic boundary conditions. See Also List of commands, getsourcedirection, gratingorders, gratingprojection

## Code Block Inventory

- Code block 1: 1 line(s); first line `period = getperiodicity("DGTD");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = getperiodicity("solvername"); | Returns the periodicity vector(s) of the system based on the active periodic boundary conditions in the named solver. The output is a [3XN] matrix where N is the number of dimensions that have active pe
- Table 2: 5 column(s), 1 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: solvername | required |  | string | Name of the solver from which to extract the periodicity vector(s).

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [getsourcedirection](https://optics.ansys.com/hc/en-us/articles/360034927333-getsourcedirection)
- [gratingorders](https://optics.ansys.com/hc/en-us/articles/360034927353-gratingorders)
- [gratingprojection](https://optics.ansys.com/hc/en-us/articles/360034927373-gratingprojection)

## Ansys-Related External Links Found

- None

## External Links Found

- None
