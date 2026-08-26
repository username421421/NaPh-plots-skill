# Polygon - Simulation Object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034901493-Structures-Polygon  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Polygon - Simulation Object` for the topic `Discovered from FDTD`. It captured 7 heading(s), 13 link(s), 3 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Polygon - Simulation Object, Setting the vertices of the polygon object, Geometry tab, Material tab, Rotation tab, Graphical Rendering tab, See also. Key detected terms: command, fdtd, geometry, group, material, mesh, mode, plane, script, structure.

## Key Terms

- command
- fdtd
- geometry
- group
- material
- mesh
- mode
- plane
- script
- structure

## Captured Headings

- Polygon - Simulation Object
- Setting the vertices of the polygon object
- Geometry tab
- Material tab
- Rotation tab
- Graphical Rendering tab
- See also

## Official Text Excerpt

> Polygon - Simulation Object FDTD MODE DGTD CHARGE HEAT FEEM This section describes how to set and get the vertex positions of a polygon object. Polygons allow the user to define a custom object with a variable number of vertices. The location of each vertex can be independently positioned within a plane, and the vertices are connected with straight lines. For 3D simulations, the object is extruded in the z dimension. In Multiphysics, the vertices have to be entered in a counter clock wise manner for the structure to be defined and meshed properly. Setting the vertices of the polygon object The vertices of the polygon object can be edited by - moving them with the mouse, - manually editing the x,y location of each vertex in the polygon property editor, - script command For complex shapes, scripting in the structure group is usually best. Once the script has calculated the x,y vertex positions, they can be loaded into the polygon object with a single set("vertices",V); command. For example, use the following code to create an octagon shaped object. NOTE: ...

## Code Block Inventory

- Code block 1: 18 line(s); first line `# octagon properties`
- Code block 2: 2 line(s); first line `V=get("vertices");`
- Code block 3: 3 line(s); first line `V=get("vertices");`

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
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Creating rounded corners](https://optics.ansys.com/hc/en-us/articles/360034382314)
- [Extruding a polygon with a sidewall angle](https://optics.ansys.com/hc/en-us/articles/360034382334)

## Ansys-Related External Links Found

- None

## External Links Found

- None
