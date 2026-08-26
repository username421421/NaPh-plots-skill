# sourcepower_avg - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034925333-sourcepower-avg  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `sourcepower_avg - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 12 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: sourcepower_avg - Script command. Key detected terms: boundary, command, fdtd, mode, monitor, normalization, script, source, symmetry, transmission.

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

- sourcepower_avg - Script command

## Official Text Excerpt

> sourcepower_avg - Script command FDTD MODE Returns the total spectral average power injected into the simulation by the source. See the Units and normalization - Spectral averaging section for more information. This script function calculates the following quantities, depending on whether the normalization state is cwnorm or nonorm: $$ \text {sourcepower}_{-}{\text {avg}_{nonorm}}=\int_{0}^{+\infty} \text {sourcepower}_{nonorm}(\omega) d\omega $$ $$ \text {sourcepower}_{-}{\text {avg}_{cwnorm}}(f)=\frac{\int_{0}^{+\infty}|s(\omega)|^2 \text {sourcepower}_{cwnorm}(\omega) d\omega}{\int_{0}^{+\infty}|s(\omega)|^2d\omega} $$ where sourcepower is the quantity returned by the sourcepower script function, s(w) is returned by sourcenorm, and ω=2πf. Typically, this function should be used in the cwnorm state. Also see the sourcenorm2_pavg script function. | Syntax | Description | out = sourcepower_avg; | Returns the spectrally averaged source power as defined above. | out = sourcepower_avg(option); | The additional argument, option, can have a value of 1 or 2. If it is 2, the data is unfolded where possible according to the symmetry or anti-symmetric boundaries if it comes from a monitor that intersect such a boundary at x min, y min or z min. The default value of option is 2. | out = sourcepower_avg(option, ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Syntax, Description
  - First row sample: out = sourcepower_avg; | Returns the spectrally averaged source power as defined above.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
- [sourcepower](https://optics.ansys.com/hc/en-us/articles/360034925313-sourcepower)
- [Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)
- [sourcenorm2_avg](https://optics.ansys.com/hc/en-us/articles/360034405474-sourcenorm2-avg)
- [sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg)
- [transmission_avg](https://optics.ansys.com/hc/en-us/articles/360034405374-transmission-avg)
- [sourceintensity_avg](https://optics.ansys.com/hc/en-us/articles/360034925393-sourceintensity-avg)
- [cwnorm](https://optics.ansys.com/hc/en-us/articles/360034405454-cwnorm)
- [nonorm](https://optics.ansys.com/hc/en-us/articles/360034405434-nonorm)
- [Units and Normalization](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)

## Ansys-Related External Links Found

- None

## External Links Found

- None
