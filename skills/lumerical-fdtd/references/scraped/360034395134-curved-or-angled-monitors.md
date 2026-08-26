# Creating curved and angled monitors

Source URL: https://optics.ansys.com/hc/en-us/articles/360034395134-Curved-or-angled-monitors  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Creating curved and angled monitors` for the topic `Discovered from FDTD product reference manual`. It captured 4 heading(s), 1 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Creating curved and angled monitors, Example 1 (using groups), Example 2 (using interpolation), Interpolating monitor data along an arbitrary path.. Key detected terms: analysis, fdtd, group, mesh, mode, monitor, plane, script, transmission.

## Key Terms

- analysis
- fdtd
- group
- mesh
- mode
- monitor
- plane
- script
- transmission

## Captured Headings

- Creating curved and angled monitors
- Example 1 (using groups)
- Example 2 (using interpolation)
- Interpolating monitor data along an arbitrary path.

## Official Text Excerpt

> Creating curved and angled monitors FDTD This page shows two examples to explain the idea of creating curved or angled monitors using groups and interpolation. This approach is required because the basic monitor objects can not be curved or rotated. Example 1 (using groups) This example shows how to use groups of point monitors to obtain frequency domain data along arbitrary paths and arbitrarily oriented planes. In the example below, the mode profiles for a bent wire waveguide are determined at 0 degrees and at 45 degrees into a bent waveguide. In addition, the electric field intensity is determined along a circular arc in these planes. To obtain the images shown below, run the usr_curved_monitor_group.fsp simulation. Then, run the usr_curved_monitor_group.lsf script file. Please note that to save on meshing time, the mesh refinement setting was set to staircase. The first two images shown below come from the two monitor groups located at the input section of the waveguide. The left image is obtained from the monitor plane2 group. Since the input to the waveguide is normal to the X-axis, the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : Minimizing data collected If you need to minimize the simulation time or the amount of data collected, this method of recording 2D data then interpolating to a 1D line is not ideal. An alternate approach is to create a line of point 

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)

## Ansys-Related External Links Found

- None

## External Links Found

- None
