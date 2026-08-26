# boundingbox – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/52495698902419-boundingbox-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `boundingbox – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 3 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: boundingbox – Script command. Key detected terms: command, fdtd, group, mode, script, script-command.

## Key Terms

- command
- fdtd
- group
- mode
- script
- script-command

## Captured Headings

- boundingbox – Script command

## Official Text Excerpt

> boundingbox – Script command FDTD MODE Returns a cell array containing the bounding box for an object(s) in SI units with an optional argument to first make a hypothetical transformed copy. If a group is selected, the bounding box is for all objects in the group. If the bounding boxes of any objects overlap, their boxes are combined. Non-overlapping bounding boxes are each returned as a separate element in the cell array. Each bounding box is described by a 2x3 matrix as follows, with all values in SI units: $$\begin{bmatrix} x_{min} & y_{min} & z_{min}\\ x_{max} & y_{max} & z_{max} \end{bmatrix}$$ |Syntax|Description |boundingbox;|Returns a cell array containing the bounding box of the selected object(s). |boundingbox(obj_name);|Returns a cell array containing the bounding box of an object with name obj_name. |boundingbox(props_struct)| Uses props_struct to first construct a hypothetical transformed copy of the selected object and returns the bounding boxes for both the original and transformed objects. No changes are made to the object in the object tree. If the bounding box of the transformed copy overlaps with the original in any way, ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `#Single object`
- Code block 2: 11 line(s); first line `#Non overlapping multiple objects`
- Code block 3: 9 line(s); first line `# Incorporate a hypothetical transformed of the first that is centered at x=1e-6, the x-span of the bounding box is from -1.5e-6 to 2.5e-6, as the transformed o`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: boundingbox; | Returns a cell array containing the bounding box of the selected object(s).

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
