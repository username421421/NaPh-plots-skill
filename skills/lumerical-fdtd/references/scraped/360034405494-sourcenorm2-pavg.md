# sourcenorm2_pavg - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034405494-sourcenorm2-pavg  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `sourcenorm2_pavg - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 10 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: sourcenorm2_pavg - Script command. Key detected terms: command, fdtd, mode, normalization, script, source.

## Key Terms

- command
- fdtd
- mode
- normalization
- script
- source

## Captured Headings

- sourcenorm2_pavg - Script command

## Official Text Excerpt

> sourcenorm2_pavg - Script command FDTD MODE Returns the source normalization spectrum used to normalize data in the cwnorm state for the partial spectral averaged quantities. See the Units and normalization - Spectral averaging section for more information. If the source time signal of the j th source in the simulation is s j (t), and N is the number of active sources then $$ s(\omega)=\operatorname{sourcenorm}(\omega)=\frac{1}{N} \sum_{s o u r c s s} \int \exp (i \omega t) s_{j}(t) d t $$ Partial spectral averaging uses a Lorentzian weighting of the following form. Delta is the FWHM of |h|2. $$ \begin{array}{c}{\left|h_{2}\left(\omega, \omega^{\prime}\right)\right|^{2}=\frac{\delta}{2 \pi} \frac{1}{\left(\omega-\omega^{\prime}\right)^{2}+(\delta / 2)^{2}}} \\ {\int\left|h\left(\omega, \omega^{\prime}\right)\right|^{2} d \omega^{\prime}=1}\end{array} $$ If this function is called without any arguments, it returns $$ sourcenorm2_{pavg }=\int_{-\infty}^{+\infty}\left|h\left(\omega, \omega^{\prime}\right)\right|^{2}\left|s\left(\omega^{\prime}\right)\right|^{2} d \omega^{\prime} $$ | Syntax | Description | out = sourcenorm2_pavg( f, delta); | This function returns the source normalization for partial spectral averaged quantities. | out = sourcenorm2_pavg( f, delta, "sourcename"); | This function makes it possible to perform the normalization using the spectrum of one source, rather than the sum of all the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = sourcenorm2_pavg( f, delta); | This function returns the source normalization for partial spectral averaged quantities.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Spectral averaging](https://optics.ansys.com/hc/en-us/articles/360034394254-Spectral-averaging)
- [sourcenorm](https://optics.ansys.com/hc/en-us/articles/360034925273-sourcenorm)
- [Spectral averaging - Usage](https://optics.ansys.com/hc/en-us/articles/360034383174-Spectral-averaging)
- [sourcenorm2_avg](https://optics.ansys.com/hc/en-us/articles/360034405474-sourcenorm2-avg)
- [sourcepower_pavg](https://optics.ansys.com/hc/en-us/articles/360034925353-sourcepower-pavg)
- [cwnorm](https://optics.ansys.com/hc/en-us/articles/360034405454-cwnorm)
- [nonorm](https://optics.ansys.com/hc/en-us/articles/360034405434-nonorm)
- [Units and Normalization](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)

## Ansys-Related External Links Found

- None

## External Links Found

- None
