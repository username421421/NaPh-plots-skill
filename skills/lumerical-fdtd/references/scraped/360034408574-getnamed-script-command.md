# getnamed - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034408574-getnamed-Script-command  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getnamed - Script command` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 14 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: getnamed - Script command. Key detected terms: command, fdtd, group, mode, script, script-command.

## Key Terms

- command
- fdtd
- group
- mode
- script
- script-command

## Captured Headings

- getnamed - Script command

## Official Text Excerpt

> getnamed - Script command FDTD RCWA MODE DGTD CHARGE HEAT FEEM INTERCONNECT Gets a property from objects with a given name. If multiple objects are selected, and the values are different, the smallest value is returned. To be certain of the results, be sure that only one object is selected, or use the form of getnamed that allows a specific object to be selected. | Syntax | Description | ?getnamed("name"); | Returns a list of the properties of the objects called name. | out = getnamed("name", "property"); | Returns the value of the specific property of the named object. |out = getnamed("name", "properties_array");| Return the values of the properties of the named object as struct. The "properties_array" is a cell array of strings. | out=getnamed("name", "property", i); | Gets the property of the ith named object. Use this to act on a series of objects. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree. | out = getnamed("groupname::name", ...

## Code Block Inventory

- Code block 1: 7 line(s); first line `addrect;`
- Code block 2: 4 line(s); first line `for (i=1:getnamednumber("circle")) {`
- Code block 3: 1 line(s); first line `addrect({"name":"substrate"});A = getnamed("substrate",{"x","y","z"});?A.x;result: 0`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 6 row(s)
  - Headers: Syntax, Description
  - First row sample: ?getnamed("name"); | Returns a list of the properties of the objects called name.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [RCWA](https://optics.ansys.com/hc/en-us/articles/4414567728787)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Manipulating objects](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [get](https://optics.ansys.com/hc/en-us/articles/360034928873-get)
- [getnumber](https://optics.ansys.com/hc/en-us/articles/360034928913-getnumber)
- [getnamednumber](https://optics.ansys.com/hc/en-us/articles/360034408594-getnamednumber)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
- [setnamed](https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed)

## Ansys-Related External Links Found

- None

## External Links Found

- None
