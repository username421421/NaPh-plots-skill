# setnamed - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed-Script-command  
Area: Discovered official source  
Topic: Discovered from Script Commands as Methods - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `setnamed - Script command` for the topic `Discovered from Script Commands as Methods - Python API`. It captured 1 heading(s), 14 link(s), 4 code block(s), 0 inline code term(s), and 1 table(s). Main headings: setnamed - Script command. Key detected terms: analysis, command, fdtd, group, mode, script, script-command.

## Key Terms

- analysis
- command
- fdtd
- group
- mode
- script
- script-command

## Captured Headings

- setnamed - Script command

## Official Text Excerpt

> setnamed - Script command FDTD RCWA MODE DGTD CHARGE HEAT FEEM INTERCONNECT Likes the set command, except that the object name must be specified. This command will return an error in analysis mode. | Syntax | Description | ?setnamed("name"); | Returns a list of the properties of the objects called name. | setnamed("name", "property", value); | The same as set, but acts on objects with a specific name, instead of selected objects. | setnamed("name", struct); | A struct can be accepted in place of "property"-value pair of arguments. | setnamed("name", "property", value,i); | This form can be used to set the property of the ith named object when multiple objects have the same name. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree. | setnamed("groupname::name", "property", value); | The same as set, but acts on objects within the group named "groupname" that are named "name", instead of selected objects. | setnamed("groupname::name", "property", value,i); | This form can be ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `setnamed("circle","radius",10e-9);`
- Code block 2: 4 line(s); first line `for (i=1:getnamednumber("circle")) {`
- Code block 3: 1 line(s); first line `coordinates = {"x" : -3e-7,               "x span" : 1e-6,               "y" : 5e-6,               "y span" : 1e-5,               "z" : 1e-7,               "z s`
- Code block 4: 1 line(s); first line `setnamed("ONA", "center frequency", 193.1e12);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 6 row(s)
  - Headers: Syntax, Description
  - First row sample: ?setnamed("name"); | Returns a list of the properties of the objects called name.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [RCWA](https://optics.ansys.com/hc/en-us/articles/4414567728787)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [ONA](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)
- [Manipulating objects](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
- [get](https://optics.ansys.com/hc/en-us/articles/360034928873-get)
- [getnamed](https://optics.ansys.com/hc/en-us/articles/360034408574-getnamed)
- [getnamednumber](https://optics.ansys.com/hc/en-us/articles/360034408594-getnamednumber)

## Ansys-Related External Links Found

- None

## External Links Found

- None
