# Reflection and transmission calculations using a planewave

Source URL: https://optics.ansys.com/hc/en-us/articles/360042089573-Reflection-and-transmission-calculations-using-a-planewave  
Area: Examples  
Topic: Plane-wave R/T, angle sweep, mesh sensitivity, steep-angle PML  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Reflection and transmission calculations using a planewave` for the topic `Plane-wave R/T, angle sweep, mesh sensitivity, steep-angle PML`. It captured 6 heading(s), 5 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Reflection and transmission calculations using a planewave, Simulation setup, Results, PML, Detailed comparison with analytic results, See also. Key detected terms: bloch, boundary, dipole, fdtd, grating, mesh, monitor, optimization, periodic, plane, pml, reflection, script, source, sweep, transmission.

## Key Terms

- bloch
- boundary
- dipole
- fdtd
- grating
- mesh
- monitor
- optimization
- periodic
- plane
- pml
- reflection
- script
- source
- sweep
- transmission

## Captured Headings

- Reflection and transmission calculations using a planewave
- Simulation setup
- Results
- PML
- Detailed comparison with analytic results
- See also

## Official Text Excerpt

> Reflection and transmission calculations using a planewave FDTD STACK In this page we compare the Analytic results from STACK with 1D FDTD simulation for a 4 layer dielectric. We use the plane wave source technique to calculate the transmission and reflection from an n = 1:1.5:2.5:1.5 dielectric stack as a function of angle. Results for s-polarization (TM) are shown here. The simulation can be easily modified to calculate the p-polarization. Simulation setup The above figure shows the simulation file plane_4layer.fsp. The n = 1:1.5:2.5:1.5 dielectric stack is visible, along with the plane wave source (white line, 1 um single wavelength) and profile monitors (yellow line). A plane wave source with Bloch boundary conditions is the typical setup for this type of simulation, which makes the simulation volume is basically 1D. Each simulation will provide R and T at a single angle. A series of simulations must be run to calculate R and T vs theta. After opening the fsp file, run the parameter sweep followed by the plane_4layer.lsf script file to reproduce the following results. Advantages: - This technique can ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [STACK](https://optics.ansys.com/hc/en-us/articles/360037226394)

## Ansys-Related External Links Found

- None

## External Links Found

- [PML boundary conditions](https://support.lumerical.com/hc/en-us/articles/360034382674-PML-boundary-conditions-in-FDTD-and-MODE)
- [Analytic solution](https://support.lumerical.com/hc/en-us/articles/360034914653-Stack-optical-solver-overview)
- [Dipole technique](https://support.lumerical.com/hc/en-us/articles/360042089593-Reflection-calculation-using-a-dipole-source)
