# Tips for using the (n,k) material model in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034394654--n-k-Material-Model  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Tips for using the (n,k) material model in FDTD` for the topic `Discovered from FDTD product reference manual`. It captured 6 heading(s), 3 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Tips for using the (n,k) material model in FDTD, Narrowband simulations, Example, Broadband simulations, Option 1 - Sampled data, Option 2 - (n,k) Material (Not recommended). Key detected terms: fdtd, import, material, mode, port, solver, source.

## Key Terms

- fdtd
- import
- material
- mode
- port
- solver
- source

## Captured Headings

- Tips for using the (n,k) material model in FDTD
- Narrowband simulations
- Example
- Broadband simulations
- Option 1 - Sampled data
- Option 2 - (n,k) Material (Not recommended)

## Official Text Excerpt

> Tips for using the (n,k) material model in FDTD FDTD MODE This page describes how to define a material based on a single complex refractive index value (e.g., n + ik = 2 + 0.05i) for single frequency simulation. This example shows images from FDTD but the same information is applicable to (n,k) material models in CHARGE, HEAT, DGTD and FEEM. For broadband simulations, n,k material is cannot be used as discussed below. | Note: For materials with \( n \in \mathbf{R} \), the situation is simplified as you can simply use a 'Dielectric' material model to avoid the following complications. Narrowband simulations In some cases, it may be convenient to define the refractive index of a material based on a single n,k value (e.g. n + ik = 2 + 0.05i). If you are using a single frequency source (i.e. the source 'Start' and 'Stop' wavelengths are equal), the best solution is likely to add an (n,k) Material to the database, as shown in the above screenshot. The n,k material allows you to enter the desired n,k values. It ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `wavelength    n k390    2    0.05400    2    0.05410    2    0.05420    2    0.05430    2    0.05440    2    0.05...`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : For materials with \( n \in \mathbf{R} \), the situation is simplified as you can simply use a 'Dielectric' material model to avoid the following complications.
- Table 2: 2 column(s), 2 row(s)
  - First row sample:  | Source wavelength limits: 500-500nm (n,k) Material values: 2, 0.05

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Creating sampled data materials](https://optics.ansys.com/hc/en-us/articles/360034915093)

## Ansys-Related External Links Found

- None

## External Links Found

- None
