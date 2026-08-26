# 2D Polygon - Simulation Object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034901613-Structures-2D-Polygon  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `2D Polygon - Simulation Object` for the topic `Discovered from FDTD`. It captured 8 heading(s), 13 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: 2D Polygon - Simulation Object, Geometry tab, Setting the vertices of the polygon object, Getting and modifying polygon vertices, Material tab, Rotations tab, Graphical Rendering tab, See also. Key detected terms: command, fdtd, geometry, group, material, mesh, mode, port, script, structure.

## Key Terms

- command
- fdtd
- geometry
- group
- material
- mesh
- mode
- port
- script
- structure

## Captured Headings

- 2D Polygon - Simulation Object
- Geometry tab
- Setting the vertices of the polygon object
- Getting and modifying polygon vertices
- Material tab
- Rotations tab
- Graphical Rendering tab
- See also

## Official Text Excerpt

> 2D Polygon - Simulation Object FDTD MODE DGTD CHARGE HEAT FEEM The object is defined in 2d surface and does not have thickness in the surface-normal direction. It can be used with 2D materials such as graphene, PEC and sampled 2d data. [[Note:]] 2d objects always take priority over 3d objects when it comes to mesh orders. Please refer to the Understanding mesh order for overlapping objects for further information. Here are some of the example structures that can be created using a 2D polygon object. To create any one of these structures, open the 2d_poly_examples.lsf and run the corresponding part of the script. Geometry tab - X, Y, Z: The center position of the object Setting the vertices of the polygon object The vertices of the polygon object can be edited by - moving them with the mouse, - manually editing the x,y location of each vertex in the polygon property editor, - script command For complex shapes, scripting in the structure group is usually best. Once the script has calculated the x,y vertex positions, they can be loaded ...

## Code Block Inventory

- Code block 1: 18 line(s); first line `# octagon properties`
- Code block 2: 2 line(s); first line `V=get("vertices");`
- Code block 3: 3 line(s); first line `V=get("vertices");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Axis rotation This object does not support an arbitrary angle of rotation on the non-normal axis. For example, with z axis being the normal, rotation of 30 degrees along z is allowed. However, rotation of 30 degrees along x or y axis 

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [Understanding mesh order for overlapping objects](https://optics.ansys.com/hc/en-us/articles/360034915233)
- [mesh order (optical)](https://optics.ansys.com/hc/en-us/articles/360034915233)
- [mesh order (electrical)](https://optics.ansys.com/hc/en-us/articles/360034915233)
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Structure - 2D Rectangle](https://optics.ansys.com/hc/en-us/articles/360034901593)
- [Material conductivity models](https://optics.ansys.com/hc/en-us/articles/360034915113)
- [add2dpoly](https://optics.ansys.com/hc/en-us/articles/360034404774)

## Ansys-Related External Links Found

- None

## External Links Found

- None
