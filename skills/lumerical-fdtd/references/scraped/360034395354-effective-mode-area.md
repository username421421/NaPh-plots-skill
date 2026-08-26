# Calculating the effective mode area of a waveguide mode

Source URL: https://optics.ansys.com/hc/en-us/articles/360034395354-Effective-mode-area  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Calculating the effective mode area of a waveguide mode` for the topic `Discovered from FDTD product reference manual`. It captured 3 heading(s), 2 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Calculating the effective mode area of a waveguide mode, Example, See also. Key detected terms: analysis, fdtd, group, mode, script.

## Key Terms

- analysis
- fdtd
- group
- mode
- script

## Captured Headings

- Calculating the effective mode area of a waveguide mode
- Example
- See also

## Official Text Excerpt

> Calculating the effective mode area of a waveguide mode FDTD This page provides a simple analysis group that calculates the effective mode area. The effective mode area, A, is the ratio of a mode's total energy density per unit length and its peak energy density $$A = \frac{1}{max\{W( r )\}} \int_{A_{\infty}} { W( r )dA } $$ where W(r) is the energy density, $$W( r ) = \frac{1}{2} Re \left\{ \frac{d[\omega \varepsilon ( r )]}{d \omega} \right\} \vert E( r ) \vert ^2 + \frac{1}{2} \mu _0 \vert H( r ) \vert ^2$$ Example The simulation file usr_effective_mode_area.fsp contains a simple silicon on insulator (SOI) waveguide shown in the image above. To get the effective mode area for the injected mode, first run the simulation. Then edit the effective mode area analysis group and press the RUN ANALYSIS button in the ANALYSIS-->SCRIPT tab. As can be seen in the image below, the analysis script output will contain the calculated effective mode area. In the screen shot above, you can see that the analysis script contained in the usr_effective_mode_area.fsp simulation uses ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Modal volume](https://optics.ansys.com/hc/en-us/articles/360034395374)

## Ansys-Related External Links Found

- None

## External Links Found

- None
