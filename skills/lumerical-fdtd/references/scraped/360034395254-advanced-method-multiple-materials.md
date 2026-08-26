# Calculating absorbed optical power - Higher accuracy method with multiple materials

Source URL: https://optics.ansys.com/hc/en-us/articles/360034395254-Advanced-method-multiple-materials  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Calculating absorbed optical power - Higher accuracy method with multiple materials` for the topic `Discovered from FDTD`. It captured 2 heading(s), 5 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Calculating absorbed optical power - Higher accuracy method with multiple materials, See also. Key detected terms: fdtd, group, material, monitor, script, transmission.

## Key Terms

- fdtd
- group
- material
- monitor
- script
- transmission

## Captured Headings

- Calculating absorbed optical power - Higher accuracy method with multiple materials
- See also

## Official Text Excerpt

> Calculating absorbed optical power - Higher accuracy method with multiple materials FDTD This example shows how to calculate the power absorbed in a specific material when there are two (or more) dispersive materials in a simulation and objects are of arbitrary shapes where it would be difficult to define the a spatial filter. This example applied both 2D and 3D cases. In this example of usr_absorption_advanced_material.fsp a silver particle of arbitrary shape is embedded in a silicon substrate. Suppose we are interested in the power absorbed in the silver particle. The advanced absorbed power monitor group returns the power absorbed as a function of space, ie Pabs(x,y,z). Once the project file is run, executing the usr_absorption_advanced_material.lsf file will multiply Pabs(x,y,z) by 1 if the (x,y,z) values are inside the silver particle and 0 if they are outside. We can use the material properties of Silicon and Silver to tell if a specific point (x,y,z) lies inside particle or not. The script, uses the index monitor inside the Pabs box to create the filters by comparing both the real and imaginary ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Simple method](https://optics.ansys.com/hc/en-us/articles/360034915673)
- [Advanced method](https://optics.ansys.com/hc/en-us/articles/360034915693)
- [Divergence of Poynting vector](https://optics.ansys.com/hc/en-us/articles/360034915713)
- [Power transmission box](https://optics.ansys.com/hc/en-us/articles/360034395294)

## Ansys-Related External Links Found

- None

## External Links Found

- None
