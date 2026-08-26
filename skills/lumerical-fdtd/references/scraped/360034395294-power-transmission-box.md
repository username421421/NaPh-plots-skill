# Calculating the net power flow with a Power transmission box

Source URL: https://optics.ansys.com/hc/en-us/articles/360034395294-Power-transmission-box  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Calculating the net power flow with a Power transmission box` for the topic `Discovered from FDTD product reference manual`. It captured 2 heading(s), 2 link(s), 1 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Calculating the net power flow with a Power transmission box, See also. Key detected terms: analysis, boundary, command, far, fdtd, group, mode, monitor, plane, symmetry, transmission.

## Key Terms

- analysis
- boundary
- command
- far
- fdtd
- group
- mode
- monitor
- plane
- symmetry
- transmission

## Captured Headings

- Calculating the net power flow with a Power transmission box
- See also

## Official Text Excerpt

> Calculating the net power flow with a Power transmission box FDTD This page provides a simple analysis group that calculates the net power flow out of a rectangular volume within a simulation. The files in this section were created using FDTD, but the same analysis group can be found in the Component library in MODE. Lumerical provides many built in analysis groups in our object library. Please press this button to open the online library of analysis groups and select optical power category to insert transmission boxes. The monitor group in the associated files (usr_transmission_3Dbox.fsp and usr_transmission_2Dbox.fsp) calculates the net power flow out of the box of monitors. To use this group to calculate net power flow into the box, just multiply the result by -1. For example, in the associated files, we have a small silicon particle in a focused beam. The box of monitors can be used to measure the power absorbed by the particle. After running the simulation, use the following commands to plot the absorption vs wavelength. Once the visualizer is open, you may want to ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `runanalysis;net_power = getresult("trans_box","T");visualize(net_power);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : Symmetry These monitor boxes work properly when symmetry boundary conditions are used. When symmetry boundary conditions are used, the monitor group assumes there will be equal power flows on both sides of the plane of symmetry.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note : Field data not saved The monitors in these groups are set to record the net power only, to minimize the amount of data saved to file.
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: Spherical transmission monitors The files usr_transmission_3Dsphere.fsp and usr_transmission_2Dsphere.fsp contain spherical transmission monitor objects. These are very similar to the transmission boxes described above, but they use a

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Loss per unit volume](https://optics.ansys.com/hc/en-us/articles/360034915653)

## Ansys-Related External Links Found

- None

## External Links Found

- None
