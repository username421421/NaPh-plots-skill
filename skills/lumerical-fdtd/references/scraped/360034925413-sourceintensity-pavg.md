# sourceintensity_pavg - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034925413-sourceintensity-pavg  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `sourceintensity_pavg - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 13 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: sourceintensity_pavg - Script command. Key detected terms: boundary, command, fdtd, mode, monitor, normalization, script, source, symmetry, transmission.

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

- sourceintensity_pavg - Script command

## Official Text Excerpt

> sourceintensity_pavg - Script command FDTD MODE Returns the partial spectral average intensity injected into the simulation by the source. The partial average intensity is equal to the partial average power divided by the source area. See the sourcepower_pavg command and the Units and normalization - Spectral averaging section for more information. | Syntax | Description | out = sourceintensity_pavg (f,df); | Returns the spectrally averaged source power as defined above. The quantity f is the frequency and the quantity df is the frequency range around which the averaging is performed, both in Hz. | out = sourceintensity_pavg(f,df, option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. | out = sourceintensity_pavg(f,df, option, "sourcename"); | This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Syntax, Description
  - First row sample: out = sourceintensity_pavg (f,df); | Returns the spectrally averaged source power as defined above. The quantity f is the frequency and the quantity df is the frequency range around which the averaging is performed, both in Hz.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg)
- [Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
- [sourceintensity](https://optics.ansys.com/hc/en-us/articles/360034925373-sourceintensity)
- [Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)
- [sourcenorm2_pavg](https://optics.ansys.com/hc/en-us/articles/360034405494-sourcenorm2-pavg)
- [sourcepower](https://optics.ansys.com/hc/en-us/articles/360034925313-sourcepower)
- [sourcepower_avg](https://optics.ansys.com/hc/en-us/articles/360034925333-sourcepower-avg)
- [transmission_pavg](https://optics.ansys.com/hc/en-us/articles/360034405414-transmission-pavg)
- [cwnorm](https://optics.ansys.com/hc/en-us/articles/360034405454-cwnorm)
- [nonorm](https://optics.ansys.com/hc/en-us/articles/360034405434-nonorm)
- [Units and Normalization](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)

## Ansys-Related External Links Found

- None

## External Links Found

- None
