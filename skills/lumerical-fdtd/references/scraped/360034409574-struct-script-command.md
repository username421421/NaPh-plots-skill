# struct - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command  
Area: Discovered official source  
Topic: Discovered from Passing Data - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `struct - Script command` for the topic `Discovered from Passing Data - Python API`. It captured 1 heading(s), 15 link(s), 5 code block(s), 0 inline code term(s), and 1 table(s). Main headings: struct - Script command. Key detected terms: command, dataset, fdtd, geometry, mode, monitor, script, script-command, structure.

## Key Terms

- command
- dataset
- fdtd
- geometry
- mode
- monitor
- script
- script-command
- structure

## Captured Headings

- struct - Script command

## Official Text Excerpt

> struct - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Creates a structure array. Any data type (such as matrix, string, dataset) can be added to structure arrays. Since Lumerical 2019b R4 version, users can also declare a structure array by using the braces declaration method. | Syntax | Description | a = {"one" : "fish", "two" : "fish", "red" : "fish", "blue" : "fish"} | Creates and initializes a structure array. | a = struct; | Creates an structure array. | a.a = "string"; | Adds a string field to the structure array. | a.b = matrix(5,5); | Adds a field of matrix of 5x5 to the structure array. Examples A structure can be created and initialized quickly as follows: The above structure array can also be declared more pedantically: Both structure arrays are equivalent and will produce the same output: When two or more objects share the same parameters, a "struct" can be used for all of them: In the above example, both the geometry "rectangle" and the profile monitor have the same x and y values, ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `C = {"a" : [1, 4, 9],     "b" : "a string",     "d" : matrix(5, 5),     "e" : getresult("monitor", "T")};`
- Code block 2: 1 line(s); first line `C = struct;C.a = [1, 4, 9]; C.b = "a string";C.d = matrix(5,5); C.e = getresult("monitor","T");`
- Code block 3: 5 line(s); first line `?C;Struct with fields:abde`
- Code block 4: 1 line(s); first line `addrect;    props = struct;    props.x = 1e-6;    props.y = 2e-6;    setnamed("rectangle",props);    addprofile;    set(props);`
- Code block 5: 1 line(s); first line `addcircle( {"name":"c1","x": 1e-6,"y": 2e-6,"radius":0.5e-6}); mystruct = {"name":"c2","x":-1e-6,"y":-2e-6,"radius":0.5e-6}; addcircle(mystruct);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: a = {"one" : "fish", "two" : "fish", "red" : "fish", "blue" : "fish"} | Creates and initializes a structure array.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [matrixdataset](https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [cell](https://optics.ansys.com/hc/en-us/articles/360034929913-cell)
- [isfield](https://optics.ansys.com/hc/en-us/articles/360034932293)
- [getfield](https://optics.ansys.com/hc/en-us/articles/360034411674)
- [setfield](https://optics.ansys.com/hc/en-us/articles/360034932313)
- [isstruct](https://optics.ansys.com/hc/en-us/articles/360034411654)

## Ansys-Related External Links Found

- None

## External Links Found

- None
