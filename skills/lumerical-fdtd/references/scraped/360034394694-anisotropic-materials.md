# Creating anisotropic optical materials in FDTD and MODE

Source URL: https://optics.ansys.com/hc/en-us/articles/360034394694-Anisotropic-Materials  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Creating anisotropic optical materials in FDTD and MODE` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 13 link(s), 1 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Creating anisotropic optical materials in FDTD and MODE, Diagonal anisotropic materials, General anisotropic materials, Simple anisotropic indices, Example diagonal anisotropic simulation. Key detected terms: command, far, fdtd, material, mode, reflection, script, solver, structure.

## Key Terms

- command
- far
- fdtd
- material
- mode
- reflection
- script
- solver
- structure

## Captured Headings

- Creating anisotropic optical materials in FDTD and MODE
- Diagonal anisotropic materials
- General anisotropic materials
- Simple anisotropic indices
- Example diagonal anisotropic simulation

## Official Text Excerpt

> Creating anisotropic optical materials in FDTD and MODE FDTD RCWA MODE Anisotropic materials can be represented by a 9-element permittivity tensor \( \varepsilon _{ij} \) where the electric fields \(E\) and displacement fields \(D\) are related via the relation. $$ D_{i}=\varepsilon_{ij} E_{j} $$ where summation over j is implied on the right hand side. The full anisotropy tensor can be written as a matrix $$\boldsymbol{\varepsilon} = \begin{bmatrix} \varepsilon_{11} & \varepsilon_{12} & \varepsilon_{13} \\ \varepsilon_{21} & \varepsilon_{22} & \varepsilon_{23} \\ \varepsilon_{31} & \varepsilon_{32} & \varepsilon_{33} \end{bmatrix} $$ The input of anisotropic materials is simple when the permittivity tensor is diagonal $$\boldsymbol{\varepsilon} = \begin{bmatrix} \varepsilon_{x} & 0& 0 \\ 0 & \varepsilon_{y} & 0 \\ 0 & 0 & \varepsilon_{z} \end{bmatrix}$$ You may find the Liquid crystal simulation video helpful. Diagonal anisotropic materials To define an anisotropic material, set the Anisotropy field in the Material database to Diagonal and specify the material model parameters for each diagonal component. When viewing the material data with the material explorer, use the 'axis' property to select the diagonal component to visualize. General anisotropic materials If ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `#Calculate the diagonal matrix and unitary matrix to set up a fully anisotropic material.# Define permittivity tensor in the reference coordinate system(x,y,z) `

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [RCWA](https://optics.ansys.com/hc/en-us/articles/4414567728787)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Material database](https://optics.ansys.com/hc/en-us/articles/360034394614)
- [matrix transformation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915173-Matrix-Transformation-Simulation-object)
- [Grid attribute tips and introduction](https://optics.ansys.com/hc/en-us/articles/360034915193)
- [LC rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915153)
- [Permittivity rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034394714)
- [Matrix transformation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915173)

## Ansys-Related External Links Found

- None

## External Links Found

- [Liquid crystal simulation](https://www.lumerical.com/learn/video/liquid-crystal-simulations-with-fdtd-solutions/)
- [eig](https://support.lumerical.com/hc/en-us/articles/360034925793-eig-Script-command)
- [Magneto-optical Kerr Effect](https://support.lumerical.com/hc/en-us/articles/360042274794-Magneto-optical-Kerr-effect)
- [Faraday effect and optical isolator](https://support.lumerical.com/hc/en-us/articles/360042274774-Faraday-effect-and-optical-isolator)
