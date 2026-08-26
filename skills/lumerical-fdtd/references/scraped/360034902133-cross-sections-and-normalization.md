# Understanding source normalization in the TFSF source

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902133-Cross-sections-and-normalization  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Understanding source normalization in the TFSF source` for the topic `Discovered from FDTD`. It captured 5 heading(s), 6 link(s), 2 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Understanding source normalization in the TFSF source, Source power vs source intensity, Angles of incidence, Periodic structures, Structures on multi-layer stacks or substrates. Key detected terms: analysis, bfast, bloch, boundary, command, fdtd, grating, import, mesh, mode, monitor, normalization, periodic, plane, port, reflection.

## Key Terms

- analysis
- bfast
- bloch
- boundary
- command
- fdtd
- grating
- import
- mesh
- mode
- monitor
- normalization
- periodic
- plane
- port
- reflection
- script
- source
- structure
- symmetry
- tfsf
- transmission

## Captured Headings

- Understanding source normalization in the TFSF source
- Source power vs source intensity
- Angles of incidence
- Periodic structures
- Structures on multi-layer stacks or substrates

## Official Text Excerpt

> Understanding source normalization in the TFSF source FDTD MODE When using finite size beams in linear systems, we typically normalize results involving power to the power spectrum of the source. When using plane waves, which in principle have infinite power, we need to consider the scattering and absorption cross sections instead. The cross section is defined such the scattered (or absorbed) power in Watts, P, is given by$$ P = \sigma I $$ where, \( I \) is the source intensity in Watts/m2 and the cross section has units of m2. In two dimensional simulations, which represent a structure which is infinite along the z axis, we generalize P to represent the power scattered per unit length, and the cross section has units of m. Source power vs source intensity By default, we normalize most power results to the power of the source. For example, the script command 'transmission' will calculate the power flux through a monitor surface and normalize to the source power, returning a dimensionless quantity. To normalize instead to the source intensity, we can use the script ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `sigma = transmission(f) * sourcepower(f) / sourceintensity(f);`
- Code block 2: 1 line(s); first line `theta = 30 * pi/180; # the nominal source angle is 30 degreesQscat = Qscat * cos(theta);Qabs = Qabs * cos(theta);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: The Mie scattering example considered here is a very particular case where the dependence of the angle of injection on wavelength does not affect the results. This is a consequence of the cross section of a sphere being independent of
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note : Since BFAST assumes periodic structure, users should not use BFAST source at an angle to replace TFSF to get oblique incidence result.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [TFSF tips](https://optics.ansys.com/hc/en-us/articles/360034382934)
- [Plane waves - Angled injection](https://optics.ansys.com/hc/en-us/articles/360034382894)
- [BFAST source](https://optics.ansys.com/hc/en-us/articles/360034902273)

## Ansys-Related External Links Found

- None

## External Links Found

- [Mie scattering](https://apps.lumerical.com/mie-scattering-fdtd.html)
