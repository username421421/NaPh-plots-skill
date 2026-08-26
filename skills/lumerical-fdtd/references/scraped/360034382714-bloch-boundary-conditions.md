# Bloch boundary conditions in FDTD and MODE

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382714-Bloch-boundary-conditions  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Bloch boundary conditions in FDTD and MODE` for the topic `Discovered from FDTD product reference manual`. It captured 12 heading(s), 9 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Bloch boundary conditions in FDTD and MODE, Periodic structures illuminated by the plane wave source, Movie of plane wave propagating at an angle, Other uses, including bandstructure calculations, Tips and additional information, Can Bloch BC's be used for propagation at normal incidence, Computational cost, Implications of using complex valued time domain fields. Key detected terms: bfast, bloch, boundary, fdtd, gaussian, import, mesh, mode, monitor, periodic, plane, pml, port, reflection, source, structure.

## Key Terms

- bfast
- bloch
- boundary
- fdtd
- gaussian
- import
- mesh
- mode
- monitor
- periodic
- plane
- pml
- port
- reflection
- source
- structure
- sweep

## Captured Headings

- Bloch boundary conditions in FDTD and MODE
- Periodic structures illuminated by the plane wave source
- Movie of plane wave propagating at an angle
- Other uses, including bandstructure calculations
- Tips and additional information
- Can Bloch BC's be used for propagation at normal incidence
- Computational cost
- Implications of using complex valued time domain fields
- Broadband injection for sources at an angle
- Automatic calculation of the Bloch vector when using the plane wave source
- Edge Effects to the Mesh
- See also

## Official Text Excerpt

> Bloch boundary conditions in FDTD and MODE FDTD MODE This section describes Bloch Boundary Conditions (BC's), when they are required, and how they are different from periodic BC. Bloch boundary conditions are used in a variety of situations, but the most common is in simulations of periodic structures that are illuminated with a plane wave source propagating at an angle (as shown in the screenshot below). If a BFAST plane wave is used, this Bloch BCs are automatically overridden by use of its own built in BCs. Periodic structures illuminated by the plane wave source Bloch BC's are easiest to understand when compared with Periodic BC's for applications where a periodic structure is illuminated by a plane wave source, as shown in the above screenshot. Periodic BC's simply copy the fields at one edge of the simulation region and re-inject them at the other edge. Bloch BC's are very similar, but while copying the fields from one edge to the other they also apply a phase correction to the fields. $$ \vec{E}_{x_{min}} = e^{-ia_{x} \ {k}_{bloch x} } \vec{E}_{x_{max}} $$ ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# Code to reproduce figuret=linspace(0,20,1000);w=10;Ex1=sin(w*t)*exp(-(t-10)^2/5);Ex2=exp(1i*w*t)*exp(-(t-10)^2/5);plot(t,real(Ex1),abs(Ex1)^2,abs(Ex2)^2);lege`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: The blue line shows a sin wave modulated by a gaussian pulse. The green line shows |E|^2 of this signal (Ex1 in the following code). This is what you would see in an 'Intensity' movie from a simulation using real valued fields. The red line
- Table 2: 1 column(s), 1 row(s)
  - First row sample: [[Note]]: When using multiple plane wave sources and Bloch BC in the simulation, all sources should have the same bandwidth and angle. If not, a warning will be shown and the Bloch vector will be set to 0.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [BFAST plane wave](https://optics.ansys.com/hc/en-us/articles/360034902273)
- [Periodic](https://optics.ansys.com/hc/en-us/articles/360034382734)
- [Plane waves - Angled injection](https://optics.ansys.com/hc/en-us/articles/360034382894)
- [Bloch BCs in broadband sweeps over angle of incidence](https://optics.ansys.com/hc/en-us/articles/1500006417822)
- [Periodic boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382734)
- [PML reflection at angles](https://optics.ansys.com/hc/en-us/articles/360034382674)
- [Plane waves - Edge effects](https://optics.ansys.com/hc/en-us/articles/360034382874)

## Ansys-Related External Links Found

- None

## External Links Found

- None
