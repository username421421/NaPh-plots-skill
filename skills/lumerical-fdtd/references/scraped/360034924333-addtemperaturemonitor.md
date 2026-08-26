# addtemperaturemonitor - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034924333-addtemperaturemonitor  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addtemperaturemonitor - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 6 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addtemperaturemonitor - Script command. Key detected terms: command, mode, monitor, script, solver.

## Key Terms

- command
- mode
- monitor
- script
- solver

## Captured Headings

- addtemperaturemonitor - Script command

## Official Text Excerpt

> addtemperaturemonitor - Script command CHARGE HEAT Adds a temperature monitor to the Ansys Lumerical Multiphysics™. The monitor can only be added if the simulation environment already has a 'HEAT' or 'CHARGE' (or both) solver present. |Syntax|Description |addtemperaturemonitor;| Adds a temperature monitor to the simulation environment. This format of the command is only application when only one solver is present in the model tree. This function does not return any data. If multiple solvers are present then use the second format |addtemperaturemonitor("solver_name");|This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” For the CHARGE solver, the temperature monitor only works if the "temperature dependence" is set to "non-isothermal" or "coupled." |addtemperaturemonitor(struct_data);| Adds a temperature monitor and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This format of the command is only application when only one solver is present in the model tree. This function does not return any data. |addtemperaturemonitor("solver_name", struct_data);| This format ...

## Code Block Inventory

- Code block 1: 9 line(s); first line `addtemperaturemonitor("CHARGE");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: addtemperaturemonitor; | Adds a temperature monitor to the simulation environment. This format of the command is only application when only one solver is present in the model tree. This function does not return any data. If multiple solvers

## Official Links Found

- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
- [addheatfluxmonitor](https://optics.ansys.com/hc/en-us/articles/360034404414-addheatfluxmonitor)

## Ansys-Related External Links Found

- None

## External Links Found

- None
