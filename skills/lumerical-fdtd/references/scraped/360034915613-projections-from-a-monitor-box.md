# Far field projections from a box of monitors

Source URL: https://optics.ansys.com/hc/en-us/articles/360034915613-Projections-from-a-monitor-box  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Far field projections from a box of monitors` for the topic `Discovered from FDTD product reference manual`. It captured 3 heading(s), 4 link(s), 1 code block(s), 0 inline code term(s), and 5 table(s). Main headings: Far field projections from a box of monitors, Related publications, See also. Key detected terms: analysis, boundary, command, dipole, far, fdtd, group, import, material, mode, monitor, pml, port, script, source, structure.

## Key Terms

- analysis
- boundary
- command
- dipole
- far
- fdtd
- group
- import
- material
- mode
- monitor
- pml
- port
- script
- source
- structure
- symmetry

## Captured Headings

- Far field projections from a box of monitors
- Related publications
- See also

## Official Text Excerpt

> Far field projections from a box of monitors FDTD This page describes how to calculate fields outside of a closed surface using a box of monitors and the far field projection functions. Lumerical provides many built in analysis groups in our object library. Please press this button to open the online library of analysis groups and select the far field category to see which analysis groups are available. |Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basically still correct, although some subtle differences do exist. Using the surface equivalence theorem, it is possible to show that fields radiated outside of a closed box by sources located inside the box can be determined exactly from the field components at the surface of the box. Since Maxwell's equations are linear, the fields outside of the box can be computed by calculating the far field projections for each surface of the monitor box and then summing ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `E2_far =   farfieldexact("x2",x,y,z) - farfieldexact("x1",x,y,z)         + farfieldexact("y2",x,y,z) - farfieldexact("y1",x,y,z)         + farfieldexact("z2",x,`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basical
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Particle scattering with a substrate The 'box of monitor' far field projection is frequently used when studying particle scattering. This is fine, but it's important to remember the requirement that everything beyond the monitor box m
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: Negative signs in front of far field projections when the normal to the monitor box points along the negative axis. In the case where no symmetry is used, the scat analysis group contained in the usr_farfield_symmetry.fsp simulation c
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note: Far field projections and symmetric/anti-symmetric FDTD region boundaries When symmetric or anti-symmetric boundary conditions are used in FDTD simulations, it is possible that a monitor will lie entirely outside of the simulation reg
- Table 5: 1 column(s), 1 row(s)
  - First row sample: Note: Far field half space analysis vs resolution and number of frequency points This calculation will take longer than the polar plot. In particular, the resolution and the number of frequency points can significantly affect the time it ta

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [polar](https://optics.ansys.com/hc/en-us/articles/360034931153)

## Ansys-Related External Links Found

- None

## External Links Found

- [3D Mie scattering](https://apps.lumerical.com/particle_scattering_mie_3d.html)
