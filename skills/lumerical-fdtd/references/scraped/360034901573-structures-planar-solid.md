# Planar solid - Simulation Object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034901573-Structures-Planar-solid  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Planar solid - Simulation Object` for the topic `Discovered from FDTD product reference manual`. It captured 7 heading(s), 10 link(s), 1 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Planar solid - Simulation Object, Setting the vertices of the polygon object, Geometry tab, Material tab, Rotation tab, Graphical Rendering tab, Scripting example. Key detected terms: command, fdtd, geometry, material, mesh, mode, script, structure.

## Key Terms

- command
- fdtd
- geometry
- material
- mesh
- mode
- script
- structure

## Captured Headings

- Planar solid - Simulation Object
- Setting the vertices of the polygon object
- Geometry tab
- Material tab
- Rotation tab
- Graphical Rendering tab
- Scripting example

## Official Text Excerpt

> Planar solid - Simulation Object FDTD MODE DGTD CHARGE HEAT FEEM The planar solid object behaves somewhat like the polygon structure, but generalized to 3D. The object vertices cannot be set via the GUI; a script command must be used. The image below shows how a facet is defined to denote positive or negative spaces. In the shape below one facet comprises of two paths : p1=[1,3,2,5,4] , p2=[16,17,18,19]. Setting the vertices of the polygon object The vertices of the planar solid object can be edited using scripting by two methods: - Specifying the vertices as a cell array. - Specifying the vertices as a matrix. For complex shapes, one can use multiple primitives and set the mesh orders of overlapping structures to achieve the desired shape, but using the planar solid primitive allows you to use just one object to implement complex shapes. Geometry tab - X, Y, Z: The center position of the object Material tab The material options are as follows: MATERIAL: This field can be set to any material included in the material database. It is ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# Select method of formatting data used to create the objectmethod_type = 1;# Specify vertex locations (Refer to the figure above)vtx = [0,0,0;       1,0,0;    `

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [mesh order (optical)](https://optics.ansys.com/hc/en-us/articles/360034915233)
- [mesh order (electrical)](https://optics.ansys.com/hc/en-us/articles/360034915233)
- [Equation interpreter](https://optics.ansys.com/hc/en-us/articles/360034953733)
- [grid attribute](https://optics.ansys.com/hc/en-us/articles/360034394694)

## Ansys-Related External Links Found

- None

## External Links Found

- None
