# addport (FDTD) - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034924793-addport-FDTD-Script-command  
Area: Script command  
Topic: Add FDTD port object  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addport (FDTD) - Script command` for the topic `Add FDTD port object`. It captured 1 heading(s), 9 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addport (FDTD) - Script command. Key detected terms: command, fdtd, group, mode, port, script, script-command, solver, source.

## Key Terms

- command
- fdtd
- group
- mode
- port
- script
- script-command
- solver
- source

## Captured Headings

- addport (FDTD) - Script command

## Official Text Excerpt

> addport (FDTD) - Script command FDTD Adds a port object to the ports group under the FDTD simulation region. A simulation region must be present in order to add a port. For more information about the port object see Ports. This topic addresses the addport command in FDTD - for information about the INTERCONNECT command, see addport (INTERCONNECT). | Syntax | Description | addport; | Adds a port. This function does not return any data. |addport(struct_data);| Adds a port and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. Example The following script adds a FDTD simulation region and port, then sets the name of the port, and selects the port modes and source mode. See Also Ports, set, geteigensolver, seteigensolver, updateportmodes, clearportmodedata

## Code Block Inventory

- Code block 1: 11 line(s); first line `addfdtd; # add FDTD simulation region`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addport; | Adds a port. This function does not return any data.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Ports](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports)
- [addport (INTERCONNECT)](https://optics.ansys.com/hc/en-us/articles/360034408934-addport)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
- [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
- [seteigensolver](https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver)
- [updateportmodes](https://optics.ansys.com/hc/en-us/articles/360034409174-updateportmodes)
- [clearportmodedata](https://optics.ansys.com/hc/en-us/articles/360034409194-clearportmodedata)

## Ansys-Related External Links Found

- None

## External Links Found

- None
