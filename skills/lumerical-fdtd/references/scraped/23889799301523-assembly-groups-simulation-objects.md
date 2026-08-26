# Assembly Groups - Simulation Objects

Source URL: https://optics.ansys.com/hc/en-us/articles/23889799301523-Assembly-Groups-Simulation-Objects  
Area: Discovered official source  
Topic: Discovered from PyLumerical Metalens (FDTD)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Assembly Groups - Simulation Objects` for the topic `Discovered from PyLumerical Metalens (FDTD)`. It captured 11 heading(s), 6 link(s), 5 code block(s), 5 inline code term(s), and 0 table(s). Main headings: Assembly Groups - Simulation Objects, Elements of an assembly group, Prototype, Parameters, Mapping table, Creating an assembly group, Adding the prototype, Setting parameters and mapping. Key detected terms: analysis, command, fdtd, geometry, group, material, mode, script, structure.

## Key Terms

- analysis
- command
- fdtd
- geometry
- group
- material
- mode
- script
- structure

## Captured Headings

- Assembly Groups - Simulation Objects
- Elements of an assembly group
- Prototype
- Parameters
- Mapping table
- Creating an assembly group
- Adding the prototype
- Setting parameters and mapping
- Limitations on variations and number of objects
- Usage example
- See also

## Official Text Excerpt

> Assembly Groups - Simulation Objects Assembly groups allow to build complex structures, such as metalenses for instance, that are made of a large number of copies of similar objects. [[Note:]] assembly groups have been introduced with the 2024 R1 release. Elements of an assembly group An assembly group consists of: - a prototype - a list of parameters - a mapping table Prototype The prototype is the single, in-tree, child of the assembly group. It can be a primitive object or a structure group. The assembly group uses this prototype to build the assembly. Therefore, before defining the assembly group, you must first define the prototype. The prototype (include any variations of it from the mapping table) cannot contain: - Any 2D geometry - Any Assembly Group or Layer Builder objects - Any object that does not have use relative coordinates, such as a primitive shape with “use relative coordinates” unchecked in its “Geometry” tab. - Any spatially varying material, for example, either non-constant index or an object with a grid attribute name assigned Parameters Parameters are stored in a ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `params = {"x", "y", "radius"};`
- Code block 2: 1 line(s); first line `addassemblygroup({"name": "assembly_grp"});`
- Code block 3: 1 line(s); first line `addtogroup("::model::assembly_grp");`
- Code block 4: 1 line(s); first line `mapping = [0, 2, 0, 1;           0, 0, 2, 1;           1, 0.5, 0.5, 1]*1e-6;setnamed("assembly_grp", "parameters", params);setnamed("assembly_grp", "mapping", m`
- Code block 5: 1 line(s); first line `#Define the dimensions of the gridN = 10; # Number of elements in the x directionM = 10; # Number of elements in the y directionxstep = 1;ystep = 1;#Initialize `

## Inline Code Inventory

- `radius`
- `rotation 1`
- `x`
- `y`
- `z`

## Table Inventory

- No tables detected

## Official Links Found

- [addassemblygroup - Script command](https://optics.ansys.com/hc/en-us/articles/23974175403667)
- [addtogroup - Script command](https://optics.ansys.com/hc/en-us/articles/360034408454)
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Analysis groups](https://optics.ansys.com/hc/en-us/articles/360034901893)
- [Arrays of objects](https://optics.ansys.com/hc/en-us/articles/360034901633)
- [addstructuregroup (script command)](https://optics.ansys.com/hc/en-us/articles/360034924093)

## Ansys-Related External Links Found

- None

## External Links Found

- None
