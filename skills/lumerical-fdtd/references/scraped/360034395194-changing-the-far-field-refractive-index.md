# Changing the far field refractive index analysis object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034395194-Changing-the-far-field-refractive-index  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Changing the far field refractive index analysis object` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 4 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Changing the far field refractive index analysis object, Setting the far field refractive index in the far field projection functions, Example, Fresnel correction, See also. Key detected terms: analysis, command, far, far-field, fdtd, gaussian, group, import, material, mode, monitor, plane, port, reflection, script.

## Key Terms

- analysis
- command
- far
- far-field
- fdtd
- gaussian
- group
- import
- material
- mode
- monitor
- plane
- port
- reflection
- script

## Captured Headings

- Changing the far field refractive index analysis object
- Setting the far field refractive index in the far field projection functions
- Example
- Fresnel correction
- See also

## Official Text Excerpt

> Changing the far field refractive index analysis object FDTD By default, far field projections assume that the material at the monitor location extends to infinity. In the following figure, this implies the substrate material extends to infinity. Obviously this is not always true. This page describes how to calculate the far field distribution assuming the refractive index in the far field is different from the index in the near field, which makes it possible to include effects such as the Substrate-Air interface shown above. Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basically still correct, although some subtle differences do exist. Two methods are available: Directly setting the far field refractive index in the far field projection functions, and applying the Fresnel equations to the far field data in an additional post processing step. Setting the far field refractive index in the far field projection functions The far field projection functions have an ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `out = farfield3d("mname",f, na, nb, illumination,                  periodsa, periodsb, index, direction);`
- Code block 2: 1 line(s); first line `Efar = farfield3d("T",1,res,res);Efar_air = farfield3d("T",1,res,res,1,1,1,n_air);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: It is important to understand that multiple reflections (between the interface and the device in the FDTD simulation) effects are not taken into account by this technique. Fortunately, such reflections are often small, making this app

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Far field projection toolbox](https://optics.ansys.com/hc/en-us/articles/360034914713)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [stackrt](https://optics.ansys.com/hc/en-us/articles/360034406254)

## Ansys-Related External Links Found

- None

## External Links Found

- None
