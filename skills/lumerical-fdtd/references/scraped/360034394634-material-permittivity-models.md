# Standard optical permittivity material models in FDTD and MODE

Source URL: https://optics.ansys.com/hc/en-us/articles/360034394634-Material-Permittivity-Models  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Standard optical permittivity material models in FDTD and MODE` for the topic `Discovered from FDTD product reference manual`. It captured 15 heading(s), 10 link(s), 0 code block(s), 0 inline code term(s), and 6 table(s). Main headings: Standard optical permittivity material models in FDTD and MODE, Sampled 3D data, Examples and more information, Dielectric, (n,k) material, Examples and more information, Conductive 3D, Plasma (Drude). Key detected terms: fdtd, import, material, mode, monitor, port, reflection, solver, source, sweep.

## Key Terms

- fdtd
- import
- material
- mode
- monitor
- port
- reflection
- solver
- source
- sweep

## Captured Headings

- Standard optical permittivity material models in FDTD and MODE
- Sampled 3D data
- Examples and more information
- Dielectric
- (n,k) material
- Examples and more information
- Conductive 3D
- Plasma (Drude)
- Debye
- Lorentz
- Sellmeier
- PEC
- Understanding the refractive index of PEC as reported in the Material Explorer and Refractive index monitors
- Analytic material
- Examples and more information

## Official Text Excerpt

> Standard optical permittivity material models in FDTD and MODE FDTD MODE This section describes the basic permittivity (or refractive index) material models supported by the Material Database. Model parameters can be edited in the Material property panel of the Material Database window. Sampled 3D data The Sampled data model is used to import experimental material data. The experimental data can be imported from a text file with the Import data button. This method can be used to create a lossless material. There are two types of sampled data models available: Sampled 3D data and Sampled 2D data. Sampled 2D data can be used for importing the surface conductivity data from 2D materials such as graphene. For more information about the Sampled 2D data material, see Material conductivity models. | Note: The Sampled data material definition uses an automatic fitting routine to generate a multi-coefficient material model of the experimental data over the frequency range specified by the source. The fits can be checked and adjusted in the Material Explorer. - TOLERANCE: The desired RMS error between the permittivity of the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : The Sampled data material definition uses an automatic fitting routine to generate a multi-coefficient material model of the experimental data over the frequency range specified by the source. The fits can be checked and adjusted in 
- Table 2: 1 column(s), 1 row(s)
  - First row sample: NOTE : Single frequency simulations only! This type of material model should only be used for single frequency simulations. The implementation of the (n,k) material model is such that the material properties will only be correct at the cent
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note : Comparison with PEC As the conductivity becomes very large, the performance of this model approaches the ideal PEC (Perfect Electrical Conductor) model described below.
- Table 4: 1 column(s), 1 row(s)
  - First row sample: NOTE : Lorentz model reference Kurt Oughstun and Natalie Cartwright, "On the Lorentz-Lorenz formula and the Lorentz model of dielectric dispersion," Opt. Express 11, 1541-1546 (2003)
- Table 5: 1 column(s), 1 row(s)
  - First row sample: NOTE : Single frequency simulations only! This type of material model should only be used for single frequency simulations. The implementation of the Sellmeier model is such that the material properties will only be correct at the center fr
- Table 6: 1 column(s), 1 row(s)
  - First row sample: Note : Spatial absorption measurements It is possible for the difference between the permittivity used in the solver (infinite) and the permittivity reported by the Refractive index monitor (1e6) to cause problems with the spatial absorptio

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Material conductivity models](https://optics.ansys.com/hc/en-us/articles/360034915113)
- [Creating sampled data materials](https://optics.ansys.com/hc/en-us/articles/360034915093)
- [Checking material fits with the material explorer](https://optics.ansys.com/hc/en-us/articles/360034915033)
- [n,k material model](https://optics.ansys.com/hc/en-us/articles/360034394654)
- [Simple analytic material model](https://optics.ansys.com/hc/en-us/articles/360034394674)
- [Advanced material models](https://optics.ansys.com/hc/en-us/articles/360034394734)
- [Flexible material plugin framework](https://optics.ansys.com/hc/en-us/articles/360034915213)

## Ansys-Related External Links Found

- None

## External Links Found

- [Graphene material (volumetric approach)](https://apps.lumerical.com/other_application_graphene_simulation_tips.html?anchor=volumetric_permittivity_approach)
