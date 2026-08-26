# set - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034928773-set-Script-command  
Area: Discovered official source  
Topic: Discovered from Script Commands as Methods - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `set - Script command` for the topic `Discovered from Script Commands as Methods - Python API`. It captured 1 heading(s), 16 link(s), 13 code block(s), 0 inline code term(s), and 1 table(s). Main headings: set - Script command. Key detected terms: analysis, boundary, command, fdtd, group, material, mode, pml, reflection, script, script-command, solver.

## Key Terms

- analysis
- boundary
- command
- fdtd
- group
- material
- mode
- pml
- reflection
- script
- script-command
- solver

## Captured Headings

- set - Script command

## Official Text Excerpt

> set - Script command FDTD RCWA MODE DGTD CHARGE HEAT FEEM INTERCONNECT Sets a property of currently selected objects. Note that most objects can not be modified when the solver is in Analysis mode. In such situations, this command will return an error. | Syntax | Description | ?set; | Returns a list of the properties of the selected object(s) that can be changed with the set command. | set("property",value); | This will set the properties of a currently selected object, including pull-downs and check boxes. It cannot be used to set the value of a selected object in a group. Value can be a number or string. This function does not return any data. | set(struct); | A struct can be accepted in place of "property"-value pair of arguments. | set("property",value,i); | This form can be used to set the property of the ith selected object when multiple objects are selected. It cannot be used to set the value of a selected object in a group. The objects are ordered by their location in the object tree. The uppermost ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `set("radius",1e-6);`
- Code block 2: 1 line(s); first line `set("name","reflection");`
- Code block 3: 1 line(s); first line `set("check box label name",0);  # unselect checkbox`
- Code block 4: 1 line(s); first line `set("enabled",0);`
- Code block 5: 1 line(s); first line `set("x min bc",1);`
- Code block 6: 1 line(s); first line `set("x min bc","PML");`
- Code block 7: 1 line(s); first line `set("pml profile", 2);`
- Code block 8: 2 line(s); first line `set("same settings on all boundaries",0);`
- Code block 9: 5 line(s); first line `select("circle");`
- Code block 10: 17 line(s); first line `addpoly;`
- Code block 11: 35 line(s); first line `addrect;`
- Code block 12: 1 line(s); first line `coordinates = {"x" : -3e-7,               "x span" : 1e-6,               "y" : 5e-6,               "y span" : 1e-5,               "z" : 1e-7,               "z s`
- Code block 13: 2 line(s); first line `select("ONA");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: ?set; | Returns a list of the properties of the selected object(s) that can be changed with the set command.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [RCWA](https://optics.ansys.com/hc/en-us/articles/4414567728787)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [ONA](https://optics.ansys.com/hc/en-us/articles/360036617973)
- [get](https://optics.ansys.com/hc/en-us/articles/360034928873-get)
- [setnamed](https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed)
- [setmaterial](https://optics.ansys.com/hc/en-us/articles/360034409654-setmaterial)
- [addmaterial](https://optics.ansys.com/hc/en-us/articles/360034930013-addmaterial)
- [haveproperty](https://optics.ansys.com/hc/en-us/articles/360034928973-haveproperty)
- [runsetup](https://optics.ansys.com/hc/en-us/articles/360034928893-runsetup)
- [runanalysis](https://optics.ansys.com/hc/en-us/articles/360034409874-runanalysis)

## Ansys-Related External Links Found

- None

## External Links Found

- None
