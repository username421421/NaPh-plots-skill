# sourceintensity - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034925373-sourceintensity  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `sourceintensity - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 11 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: sourceintensity - Script command. Key detected terms: boundary, command, dipole, fdtd, mode, monitor, normalization, script, source, symmetry, tfsf, transmission.

## Key Terms

- boundary
- command
- dipole
- fdtd
- mode
- monitor
- normalization
- script
- source
- symmetry
- tfsf
- transmission

## Captured Headings

- sourceintensity - Script command

## Official Text Excerpt

> sourceintensity - Script command FDTD MODE Returns the source power divided by the area of the source. In 3D simulations, the units will be in Watts/m 2 if CW norm is used, and Watts/m 2 /Hertz 2 if No norm is used. This function is often used when normalizing power measurements from simulations with a TFSF source. In the case of multiple sources, the sourceintensity(f) command will return the sum of all sourceintensity from all sources. | Syntax | Description | out = sourceintensity(f); | Returns the source intensity at the vector of frequency points f (f is the frequency in Hz). | out = sourceintensity(f, option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. | out = sourceintensity(f, option, name); | This function makes it possible to perform the normalization using ...

## Code Block Inventory

- Code block 1: 33 line(s); first line `newproject;          # create new simulation`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Syntax, Description
  - First row sample: out = sourceintensity(f); | Returns the source intensity at the vector of frequency points f (f is the frequency in Hz).

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [sourcenorm](https://optics.ansys.com/hc/en-us/articles/360034925273-sourcenorm)
- [sourcepower](https://optics.ansys.com/hc/en-us/articles/360034925313-sourcepower)
- [sourceintensity_avg](https://optics.ansys.com/hc/en-us/articles/360034925393-sourceintensity-avg)
- [sourceintensity_pavg](https://optics.ansys.com/hc/en-us/articles/360034925413-sourceintensity-pavg)
- [dipolepower](https://optics.ansys.com/hc/en-us/articles/360034925293-dipolepower)
- [transmission](https://optics.ansys.com/hc/en-us/articles/360034405354-transmission)
- [cwnorm](https://optics.ansys.com/hc/en-us/articles/360034405454-cwnorm)
- [nonorm](https://optics.ansys.com/hc/en-us/articles/360034405434-nonorm)
- [Units and normalization](https://optics.ansys.com/hc/en-us/articles/360034397034)

## Ansys-Related External Links Found

- None

## External Links Found

- None
