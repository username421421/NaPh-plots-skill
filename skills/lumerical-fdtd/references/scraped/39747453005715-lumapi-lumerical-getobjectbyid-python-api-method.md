# lumapi – Lumerical.getObjectById – Python API Method

Source URL: https://optics.ansys.com/hc/en-us/articles/39747453005715-lumapi-Lumerical-getObjectById-Python-API-Method  
Area: Discovered official source  
Topic: Discovered from Lumerical Python API Reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lumapi – Lumerical.getObjectById – Python API Method` for the topic `Discovered from Lumerical Python API Reference`. It captured 1 heading(s), 5 link(s), 9 code block(s), 0 inline code term(s), and 2 table(s). Main headings: lumapi – Lumerical.getObjectById – Python API Method. Key detected terms: command, group, lumapi, python, python-api, script.

## Key Terms

- command
- group
- lumapi
- python
- python-api
- script

## Captured Headings

- lumapi – Lumerical.getObjectById – Python API Method

## Official Text Excerpt

> lumapi – Lumerical.getObjectById – Python API Method Returns a simulation object by ID. Syntax Parameters | Field | Type | Description | id | str | Object ID of the target simulation object. The object ID is the fully distinguished name of the object. For example, If a duplicate name exists, you should append #N to the name to unambiguously identify a single object. N is an integer identifying the Nth object in the tree with the given name. For example, The behavior is undefined if duplicate object names exist, and no specifier is used. If an unqualified name is given, the group scope will be prepended to the name. Returns | Field | Type | Description | outputObject | SimObject | Object obtained by the function. Examples Add a rectangle and obtain it by ID Returns The same command still works even if the scope is not specified Returns If multiple rectangles are defined, numbers can used to specify the correct one Returns See Also Python API overview – Ansys Optics, Lumerical Python API Reference, lumapi.getObjectbySelection, lumapi.getAllSelectedObjects

## Code Block Inventory

- Code block 1: 1 line(s); first line `outputObject = lumapi.getObjectById(id)`
- Code block 2: 1 line(s); first line `::model::group::rectangle`
- Code block 3: 1 line(s); first line `::model::group::rectangle#3`
- Code block 4: 5 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 5: 1 line(s); first line `<class 'lumapi.SimObject'>`
- Code block 6: 5 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 7: 1 line(s); first line `<class 'lumapi.SimObject'>`
- Code block 8: 8 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 9: 1 line(s); first line `Rectangle 1 z position: 0.0, Rectangle 2 z position: 1e-06`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 3 column(s), 1 row(s)
  - Headers: Field, Type, Description
  - First row sample: id | str | Object ID of the target simulation object. The object ID is the fully distinguished name of the object. For example, ::model::group::rectangle If a duplicate name exists, you should append #N to the name to unambiguously identify
- Table 2: 3 column(s), 1 row(s)
  - Headers: Field, Type, Description
  - First row sample: outputObject | SimObject | Object obtained by the function.

## Official Links Found

- [SimObject](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference#toc_2)
- [Python API overview – Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [lumapi.getObjectbySelection](https://optics.ansys.com/hc/en-us/articles/39747592765331-lumapi-Lumerical-getObjectBySelection-Python-API-Method)
- [lumapi.getAllSelectedObjects](https://optics.ansys.com/hc/en-us/articles/39747123391251-lumapi-Lumerical-getAllSelectedObjects-Python-API-Method)

## Ansys-Related External Links Found

- None

## External Links Found

- None
