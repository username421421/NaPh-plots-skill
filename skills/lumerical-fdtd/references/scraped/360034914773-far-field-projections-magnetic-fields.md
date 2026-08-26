# Calculating magnetic fields in far field projections

Source URL: https://optics.ansys.com/hc/en-us/articles/360034914773-Far-field-projections-Magnetic-fields  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Calculating magnetic fields in far field projections` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 2 link(s), 2 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Calculating magnetic fields in far field projections, Calculating \( \vert H \vert^2\) in the far field, Calculating H in the intermediate and far field, Related publications, See also. Key detected terms: command, far, far-field, fdtd, script, structure.

## Key Terms

- command
- far
- far-field
- fdtd
- script
- structure

## Captured Headings

- Calculating magnetic fields in far field projections
- Calculating \( \vert H \vert^2\) in the far field
- Calculating H in the intermediate and far field
- Related publications
- See also

## Official Text Excerpt

> Calculating magnetic fields in far field projections FDTD This section discusses how to obtain the H field components of far field projections. Calculating \( \vert H \vert^2\) in the far field To calculate \(\mid H\mid^{2}\) in the far field, you can simply use the relation \(\mid H\mid^{2}=n^{2}\frac{\epsilon_0}{\mu_0}\mid E\mid^{2}\) Calculating H in the intermediate and far field We use the farfieldexact script commands to calculate the components of the electric field at any specific point in the farfield. In this example (based on the nanoslit device shown in Wang et. al.), we can calculate the E field intensity on top of the device to analyze the focusing properties of this nanoslit structure. This is done using the following script commands: Next, we can calculate the H fields numerically from the E fields using Maxwell's equation: $$\frac{\partial E_z}{\partial y}-\frac{\partial E_y}{\partial z}=i\omega \mu_0H_x$$ $$\frac{\partial E_x}{\partial z}-\frac{\partial E_z}{\partial x}=i\omega \mu_0H_y$$ $$\frac{\partial E_y}{\partial x}-\frac{\partial E_x}{\partial z}=i\omega \mu_0H_z$$ For example, in the attached script, Hz is calculated using the following script commands: Related publications B. Wang and G. P. Wang, "Directional beaming of light from a ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# define desired region of x and yx = linspace(-5e-6,5e-6,200);y = linspace(1e-6,50e-6,500);# do far field projectionE2 = farfieldexact2d('monitor1',x,y);E2 = s`
- Code block 2: 1 line(s); first line `delta = 1e-9; # used to calculate the numerical derivative;f = getdata("T","f");Ey1 = pinch(farfieldexact2d("T",x-delta,y),3,2);Ey2 = pinch(farfieldexact2d("T",`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
