# ocgetgeometry – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/49675520380691-ocgetgeometry-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ocgetgeometry – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 9 link(s), 1 code block(s), 0 inline code term(s), and 3 table(s). Main headings: ocgetgeometry – Script command. Key detected terms: command, fdtd, geometry, mode, port, script, script-command, structure.

## Key Terms

- command
- fdtd
- geometry
- mode
- port
- script
- script-command
- structure

## Captured Headings

- ocgetgeometry – Script command

## Official Text Excerpt

> ocgetgeometry – Script command FDTD MODE DGTD CHARGE HEAT FEEM Generates a gds file for a given cell from Synopsys OptoCompiler™ and returns a structure with port information and bounding box of the cell. This command is only available on Linux. |Syntax|Description |results =ocgetgeometry(inputs);|Generate a gds file and a port information structure using the input settings. The table below discusses the input settings and returned results.. The input settings is a structure that must contain the fields shown in the table below. |Field|Description |libDefs|Specifies the location of the lib.defs file. |library|Specifies the library that contains the cell. |cell|Specifies the cell. |view|Specifies the view to generate the gds from. |params|A structure that includes parameters for PCells. The key to each structure is the name of the parameter, and the value is the value of the parameter. |output|Specifies the output location of the gds file. |layermap|Specifies the layer map file. The returned results is a structure that contains the following fields: |Field|Description |portInfo|A structure with port information for the cell. |boundingBox|A cell array with bounding box information for the cell. Example See ...

## Code Block Inventory

- Code block 1: 13 line(s); first line `pcell_params= struct;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: results =ocgetgeometry(inputs); | Generate a gds file and a port information structure using the input settings. The table below discusses the input settings and returned results..
- Table 2: 2 column(s), 7 row(s)
  - Headers: Field, Description
  - First row sample: libDefs | Specifies the location of the lib.defs file.
- Table 3: 2 column(s), 2 row(s)
  - Headers: Field, Description
  - First row sample: portInfo | A structure with port information for the cell.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [a given cell from Synopsys OptoCompiler™](https://optics.ansys.com/hc/en-us/articles/47076085200787-Lumerical-OptoCompiler-integration)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [Lumerical-OptoCompiler integration](https://optics.ansys.com/hc/en-us/articles/47076085200787-Lumerical-OptoCompiler-integration)

## Ansys-Related External Links Found

- None

## External Links Found

- None
