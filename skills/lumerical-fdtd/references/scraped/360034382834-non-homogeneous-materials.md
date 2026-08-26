# Understanding dipoles in non-homogeneous materials

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382834-Non-homogeneous-materials  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Understanding dipoles in non-homogeneous materials` for the topic `Discovered from FDTD`. It captured 4 heading(s), 3 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Understanding dipoles in non-homogeneous materials, Normalizing a dipole near a metal wall, Related publications, See also. Key detected terms: boundary, command, dipole, fdtd, import, material, mode, normalization, pml, port, script, source, structure.

## Key Terms

- boundary
- command
- dipole
- fdtd
- import
- material
- mode
- normalization
- pml
- port
- script
- source
- structure

## Captured Headings

- Understanding dipoles in non-homogeneous materials
- Normalizing a dipole near a metal wall
- Related publications
- See also

## Official Text Excerpt

> Understanding dipoles in non-homogeneous materials FDTD MODE The actual power emitted by a dipole is highly dependant on the surrounding materials, and can vary significantly from the analytic formula for a dipole in a homogeneous material. This section looks at a specific example of a dipole near a metal wall. In these cases, the CW normalization option will not work correctly because it will normalize data to the analytic formula, rather than the actual power emitted. For accurate power normalization, we must normalize results using the dipolepower function (actual radiated power) rather than the standard sourcepower function (analytic power radiated in homogeneous material). Normalizing a dipole near a metal wall In LEDs and OLEDs, the dipoles typically radiate near a metal wall. It is worthwhile to consider power normalization calculations near metal walls. Open the file usr_dipole_power_metal1.fsp. This structure we are modeling is shown in the following screenshot. All boundaries are PML, except for the lower z boundary, which is set to metal. There is a single dipole source in the simulation volume. Run the simulation, then paste the following ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `f1=c/1.5e-6;f2=c/1.0e-6;f=linspace(f1,f2,100);power1=sourcepower(f,2,"real_source"); power2=dipolepower(f, "real_source"); # actual power radiated by the dipole`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Dipole radiated power It may seem strange that the total power radiated by the dipole changes when it is near a metal wall, despite the fact that the dipole amplitude is fixed. To understand how this can be, we should realize that a d
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Beam sources As described above, the amount of power radiated by a source can change due to interference with another source, or when it interferes with itself. This is usually only relevant for dipole sources, but it can occur with a

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Testing FDTD dipole sources in homogeneous material](https://optics.ansys.com/hc/en-us/articles/360034382814)

## Ansys-Related External Links Found

- None

## External Links Found

- None
