# addmesh - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034924253-addmesh-Script-command  
Area: Script command  
Topic: Add mesh override region  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addmesh - Script command` for the topic `Add mesh override region`. It captured 1 heading(s), 6 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addmesh - Script command. Key detected terms: command, fdtd, mesh, mode, script, script-command, solver.

## Key Terms

- command
- fdtd
- mesh
- mode
- script
- script-command
- solver

## Captured Headings

- addmesh - Script command

## Official Text Excerpt

> addmesh - Script command FDTD MODE CHARGE Adds a mesh override region to the simulation environment. The mesh override region can be used to control the size of the mesh in a certain region. In Ansys Lumerical Multiphysics™, a CHARGE solver region must be present in the objects tree for this command to work. |Syntax|Description |addmesh;| Adds a mesh override region to the simulation environment. In Lumerical Multiphysics, this command adds an electrical mesh which applies only to the 'CHARGE' solver. This function does not return any data. |addmesh(struct_data);| Adds a mesh override region to the simulation environment. object and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. In Lumerical Multiphysics, this command adds an electrical mesh which applies only to the 'CHARGE' solver. This function does not return any data. Example The following script commands will add a mesh override region in FDTD, name it, set its dimension, and set the mesh constraints. The mesh object will be set to restrict the mesh in X direction only. ...

## Code Block Inventory

- Code block 1: 16 line(s); first line `addmesh;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addmesh; | Adds a mesh override region to the simulation environment. In Lumerical Multiphysics, this command adds an electrical mesh which applies only to the 'CHARGE' solver. This function does not return any data.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)

## Ansys-Related External Links Found

- None

## External Links Found

- None
