# addstructuregroup - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034924093-addstructuregroup  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addstructuregroup - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 13 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addstructuregroup - Script command. Key detected terms: analysis, command, fdtd, geometry, group, mode, monitor, script, source, structure.

## Key Terms

- analysis
- command
- fdtd
- geometry
- group
- mode
- monitor
- script
- source
- structure

## Captured Headings

- addstructuregroup - Script command

## Official Text Excerpt

> addstructuregroup - Script command FDTD MODE DGTD CHARGE HEAT FEEM Adds a structure group to the simulation environment. Structure groups are very convenient when you want to parametrize your design. You can define different parameters for the structure group and use the "setup" script to create your geometry (along with monitors and/or sources) according to those parameter values. | Syntax | Description | addstructuregroup; | Adds a structure group to the simulation environment. This function does not return any data. | addstructuregroup(struct_data); | Adds a structure group and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. Example Add a structure group and put a rectangle in it. Create a structure group. Add a user property named "radius" and set up the script in the structure group to add two circles to the group and set their radius to the value of the user property "radius". NOTE: The "myscript" string in the script above uses the escape character \n for new line ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `addstructuregroup;`
- Code block 2: 8 line(s); first line `addstructuregroup;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addstructuregroup; | Adds a structure group to the simulation environment. This function does not return any data.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [addtogroup](https://optics.ansys.com/hc/en-us/articles/360034408454-addtogroup)
- [adduserprop](https://optics.ansys.com/hc/en-us/articles/360034928733-adduserprop)
- [addgroup](https://optics.ansys.com/hc/en-us/articles/360034924073-addgroup)
- [addanalysisgroup](https://optics.ansys.com/hc/en-us/articles/360034404074-addanalysisgroup)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)

## Ansys-Related External Links Found

- None

## External Links Found

- None
