# Tips for creating a 3D contour path object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034901693-Complex-structures-3D-contour  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Tips for creating a 3D contour path object` for the topic `Discovered from FDTD`. It captured 2 heading(s), 2 link(s), 2 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Tips for creating a 3D contour path object, Creating an arbitrary 3D contour. Key detected terms: command, fdtd, group, mode, port, script, structure.

## Key Terms

- command
- fdtd
- group
- mode
- port
- script
- structure

## Captured Headings

- Tips for creating a 3D contour path object
- Creating an arbitrary 3D contour

## Official Text Excerpt

> Tips for creating a 3D contour path object FDTD MODE This section describes how to create an arbitrary 3D contour with a polygonal cross section. Creating an arbitrary 3D contour This example uses a large number of polygon objects to create an arbitrary 3D contour. The user defines an arbitrary line contour path in 3 dimensions, and a polygonal cross sectional shape. The structure is created from sections of rotated and extruded polygons. The user can increase the number of sections used by increasing the number of sample points of the contour. The above structure shows the contour structure group from usr_contour.fsp. Only user properties and the first portion of the setup script in the structure group defining the cross section and contour path should be modified. For example, a simpler structure could be created by replacing the lines defining z: with The structure is now bound to z=0 as shown below. Contour paths can be defined analytically, or could be read from a text file with the readdata script command.

## Code Block Inventory

- Code block 1: 1 line(s); first line `z = matrix(N_sections);z(1) = 0;z(N_sections) = 0;z(2:N_sections-1) = 5e-6*sin(phi)*sin(phi/4);`
- Code block 2: 1 line(s); first line `z=0;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)

## Ansys-Related External Links Found

- None

## External Links Found

- None
