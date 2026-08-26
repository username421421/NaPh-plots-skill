# Tips for getting the actual mesh size in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382574-Getting-the-mesh-size  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Tips for getting the actual mesh size in FDTD` for the topic `Discovered from FDTD product reference manual`. It captured 4 heading(s), 2 link(s), 2 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Tips for getting the actual mesh size in FDTD, Measure the mesh with the ruler, Getting the mesh from Simulation region properties, Getting the mesh from monitor data. Key detected terms: command, fdtd, mesh, mode, monitor, plane, script.

## Key Terms

- command
- fdtd
- mesh
- mode
- monitor
- plane
- script

## Captured Headings

- Tips for getting the actual mesh size in FDTD
- Measure the mesh with the ruler
- Getting the mesh from Simulation region properties
- Getting the mesh from monitor data

## Official Text Excerpt

> Tips for getting the actual mesh size in FDTD FDTD MODE This section describes how to get the locations of the mesh points. Measure the mesh with the ruler The mesh can be viewed in the CAD layout editor by clicking the View simulation mesh button. The simulation mesh is not constantly updated as simulation objects are manipulated because it would make the interface too slow. The Recalculate simulation mesh (F5) button can be used to force a recalculation of the mesh. Once the mesh is visible, the Ruler (R) mouse mode can be used to measure the mesh size. The ruler measurements are visible at the bottom of the screen. When viewing the mesh (orange), it is often best to hide the drawing grid mesh (grey) to keep the screen from becoming too cluttered. To hide the drawing grid, click on the Edit drawing grid button, and unselect "Show grid". Getting the mesh from Simulation region properties Before a simulation has been run, some information about the mesh can be obtained by getting the Simulation region properties. Getting the ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `addfdtd;?getresult("FDTD","x"); # it will return the x positions of the grid pointsresult:-8.5e-007-8.10465e-007-7.7093e-007-7.31395e-007-6.9186e-007-6.52326e-0`
- Code block 2: 1 line(s); first line `m="monitor1";  # monitor namex=getdata(m,"x");  # x position data`

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
