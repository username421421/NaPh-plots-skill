# addimportheat - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034404394-addimportheat  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addimportheat - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 9 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addimportheat - Script command. Key detected terms: command, dataset, import, mode, monitor, port, script, solver, source, structure.

## Key Terms

- command
- dataset
- import
- mode
- monitor
- port
- script
- solver
- source
- structure

## Captured Headings

- addimportheat - Script command

## Official Text Excerpt

> addimportheat - Script command HEAT Adds a heat source to Ansys Lumerical Multiphysics™ where the profile of the heat source can be imported from an external source. For the CHARGE solver, the import heat source only gets applied if the "temperature dependence" is set to "coupled." |Syntax|Description |addimportheat;| Adds an import primitive to define a heat source. This format of the command is only application when only one solver is present/active in the model tree. This function does not return any data. If multiple solvers are present then use the second or fourth format. |addimportheat("solver_name");|This format of the command will add an import heat source to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” |addimportheat(struct_data);| Adds an import primitive to define a heat source and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. |addimportheat("solver_name", struct_data);| This format of the command will add a temperature monitor to the solver defined by the argument. The "solver ...

## Code Block Inventory

- Code block 1: 14 line(s); first line `addimportheat("HEAT");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: addimportheat; | Adds an import primitive to define a heat source. This format of the command is only application when only one solver is present/active in the model tree. This function does not return any data. If multiple solvers are pres

## Official Links Found

- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114-importdataset)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [addemasolver](https://optics.ansys.com/hc/en-us/articles/360034409254-linspace)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [select](https://optics.ansys.com/hc/en-us/articles/360034928593-select)
- [adduniformheat](https://optics.ansys.com/hc/en-us/articles/360034924313-adduniformheat)
- [addimporttemperature](https://optics.ansys.com/hc/en-us/articles/360034924273-addimporttemperature)

## Ansys-Related External Links Found

- None

## External Links Found

- None
