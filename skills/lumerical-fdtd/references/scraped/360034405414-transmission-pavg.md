# transmission_pavg - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034405414-transmission-pavg  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `transmission_pavg - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 8 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: transmission_pavg - Script command. Key detected terms: boundary, command, fdtd, mode, monitor, normalization, script, source, symmetry, transmission.

## Key Terms

- boundary
- command
- fdtd
- mode
- monitor
- normalization
- script
- source
- symmetry
- transmission

## Captured Headings

- transmission_pavg - Script command

## Official Text Excerpt

> transmission_pavg - Script command FDTD MODE Returns the partial spectral average power through a monitor surface, normalized to the partial spectral average of the source. See the Units and normalization - Spectral averaging section for more information. $$ T_{pavg}(f) = \frac{\frac{1}{2} \int real(_{partial}).dS}{sourcepower_{pavg}(f)} $$ where T pavg is the normalized partial spectral average transmission is the partial spectral average Poynting vector dS is the surface normal The normalization state (cwnorm or nonorm) does not affect the result because of the source power normalization. | Syntax | Description | out = transmission_pavg ("monitorname"); | Returns the partial spectral average transmission through monitorname. It must be obvious from the shape of the monitor which axis is normal to the monitor surface. | out = transmission_pavg ("monitorname", option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = transmission_pavg ("monitorname"); | Returns the partial spectral average transmission through monitorname. It must be obvious from the shape of the monitor which axis is normal to the monitor surface.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
- [transmission](https://optics.ansys.com/hc/en-us/articles/360034405354-transmission)
- [Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)
- [sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg)
- [transmission_avg](https://optics.ansys.com/hc/en-us/articles/360034405374-transmission-avg)
- [Units and Normalization](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)

## Ansys-Related External Links Found

- None

## External Links Found

- None
