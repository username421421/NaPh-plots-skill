# Using monitor data to define the spatial field profile of a source in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034383034-Custom-source-profile-from-monitor-data  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Using monitor data to define the spatial field profile of a source in FDTD` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 3 link(s), 0 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Using monitor data to define the spatial field profile of a source in FDTD, Example description, Step 1: Model taper section. Record field profile at output, Step 2: Create custom source and simulate nano-particle, See also. Key detected terms: dataset, fdtd, gaussian, import, material, mesh, mode, monitor, port, reflection, script, source, structure, transmission.

## Key Terms

- dataset
- fdtd
- gaussian
- import
- material
- mesh
- mode
- monitor
- port
- reflection
- script
- source
- structure
- transmission

## Captured Headings

- Using monitor data to define the spatial field profile of a source in FDTD
- Example description
- Step 1: Model taper section. Record field profile at output
- Step 2: Create custom source and simulate nano-particle
- See also

## Official Text Excerpt

> Using monitor data to define the spatial field profile of a source in FDTD FDTD This section describes how to create a custom source field profile from monitor data obtained from another simulation. The left screenshot shows a waveguide input coupler. Suppose we want to use this system to excite a small gold nano-particle located at the end of the coupler (lower figure). Example description In the left figure, we see the entire coupler (facet, coupler, and output waveguide). The taper and waveguide are 500nm high. The coupler input width is 8.5 microns. The waveguide tapers over 10 microns to a width of 500nm, where it still supports many modes at wavelengths around 500nm. The dielectric waveguide is assumed to have an index of 2. The operating wavelength is 500 nm. In the right figure, we see a 40 nm radius gold sphere, 200nm past the end of the taper region. To simulate the entire device, the simulation region must be about 20x20x10 wavelengths in size. This is a large simulation. To accurately model the gold nano-particle, a very small ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : Reflection sensitive structure It is important to note this method assumes that there is not much reflection back from the Gold defect and that the waves recorded at the field monitor are not perturbed by the defect. This would not b
- Table 2: 2 column(s), 1 row(s)
  - First row sample: |E| in the taper | |E| field profile exported to the .fld file
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note : Data interpolation The field profile in the mat file is saved on the mesh of the first simulation. The mesh in the second simulation is different. In such situations, the field data will be automatically interpolated onto the new mes

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Custom field profile](https://optics.ansys.com/hc/en-us/articles/360034383014)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114)

## Ansys-Related External Links Found

- None

## External Links Found

- None
