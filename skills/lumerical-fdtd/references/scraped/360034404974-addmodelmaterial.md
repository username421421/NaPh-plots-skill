# addmodelmaterial - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034404974-addmodelmaterial  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addmodelmaterial - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 6 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: addmodelmaterial - Script command. Key detected terms: command, geometry, material, mode, script, solver.

## Key Terms

- command
- geometry
- material
- mode
- script
- solver

## Captured Headings

- addmodelmaterial - Script command

## Official Text Excerpt

> addmodelmaterial - Script command DGTD CHARGE HEAT FEEM Adds an empty material model to the 'materials' folder in the objects tree. Different properties (electrical, thermal, or optical) can then be assigned to the material. Once created the material can be assigned to any geometry and be used in simulations using the CHARGE, HEAT, or DGTD solvers. |Syntax|Description |addmodelmaterial;| Adds a new material to the 'materials' folder in the objects tree in Lumerical Multiphysics. This function does not return any data. |addmodelmaterial(struct_data);| Adds a new material to the 'materials' and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. Example The following script commands will add a new material to the objects tree in Lumerical Multiphysics, name it, and assign optical properties to it using a material model in the optical material database. The script will then add electrical and thermal properties to the same material using an appropriate material model in the electrical/thermal material database. |NOTE: Once a material property is assigned ...

## Code Block Inventory

- Code block 1: 7 line(s); first line `addmodelmaterial;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addmodelmaterial; | Adds a new material to the 'materials' folder in the objects tree in Lumerical Multiphysics. This function does not return any data.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: NOTE: Once a material property is assigned to the material model the selection changes to the corresponding property. Therefore the material model must be re-selected before adding a new property to it.

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [addmaterialproperties](https://optics.ansys.com/hc/en-us/articles/360034924933-addmaterialproperties)

## Ansys-Related External Links Found

- None

## External Links Found

- None
