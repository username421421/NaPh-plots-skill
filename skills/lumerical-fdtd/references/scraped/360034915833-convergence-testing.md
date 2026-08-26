# Convergence testing process for FDTD simulations

Source URL: https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Convergence testing process for FDTD simulations` for the topic `Discovered from FDTD`. It captured 26 heading(s), 5 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Convergence testing process for FDTD simulations, Source of error in an FDTD simulation, Proximity of PML, Reflection from the PML, FDTD grid dispersion, Staircasing effect, Multi-coefficient model fit, Finite sized temporal mesh. Key detected terms: analysis, convergence, far, fdtd, geometry, group, import, material, mesh, mode, monitor, normalization, pml, port, reflection, script.

## Key Terms

- analysis
- convergence
- far
- fdtd
- geometry
- group
- import
- material
- mesh
- mode
- monitor
- normalization
- pml
- port
- reflection
- script
- source
- structure
- sweep
- tfsf
- transmission

## Captured Headings

- Convergence testing process for FDTD simulations
- Source of error in an FDTD simulation
- Proximity of PML
- Reflection from the PML
- FDTD grid dispersion
- Staircasing effect
- Multi-coefficient model fit
- Finite sized temporal mesh
- Non-uniform meshing
- Sources
- Monitors
- Example simulation
- Quantifying the level of convergence
- Determining your acceptable level of error
- Convergence testing steps
- PML distance
- PML layers
- Mesh accuracy
- Sweep the inner mesh
- Inner mesh and increase PML layers
- Multi-coefficient model fits
- Finite-sized dt
- Conformal mesh
- Non-uniform meshing
- Sources and monitors
- Conclusion

## Official Text Excerpt

> Convergence testing process for FDTD simulations FDTD Numerical simulation results will never give exactly the correct answer; there is always some numerical error. It is important to understand the sources of numerical error and steps that can be taken to reduce the error to an acceptable level. Reducing the error often involves increased simulation time and memory and so it is important to consider, for your application, what is an acceptable level of error so that you can run your simulations as quickly as possible. This page provides a thorough method for convergence testing of results from an FDTD simulation, so you can determine the possible sources of error in a simulation, and quantify the level of convergence. This topic uses a 2D Mie scattering example so that a highly accurate analytic result can be calculated using Mie theory. This will allow us to determine precisely the level of error from our FDTD simulations, but we will consider how to estimate your level of error when a more accurate solution is not available. Source of error in an FDTD simulation ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Spatial interpolation - NONE setting Disabling the spatial interpolation is a very advanced feature. Only expert users that are very familiar with the FDTD method should consider using this feature. Most standard analysis functions (s
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Limits on the size of the mesh Single precision numbers have approximately 7 decimals of precision. Finite-difference methods rely on taking spatial and temporal derivatives and performing integrals. Clearly, if we oversample a wave, 

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [getnumericalpermittivity](https://optics.ansys.com/hc/en-us/articles/360034930093)
- [Mode source - Broadband](https://optics.ansys.com/hc/en-us/articles/360034902213)
- [this link](https://optics.ansys.com/hc/en-us/articles/360034915693)
- [advanced tab](https://optics.ansys.com/hc/en-us/articles/360034902393)

## Ansys-Related External Links Found

- None

## External Links Found

- None
