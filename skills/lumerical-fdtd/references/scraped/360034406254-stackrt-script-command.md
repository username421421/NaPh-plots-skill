# stackrt - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034406254-stackrt-Script-command  
Area: Discovered official source  
Topic: Discovered from Script Commands as Methods - Python API  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `stackrt - Script command` for the topic `Discovered from Script Commands as Methods - Python API`. It captured 4 heading(s), 14 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: stackrt - Script command, Example 1: Five-layer stack with isotropic materials, Example 2: Birefringent slab in air, Example 3: A fully anisotropic and dispersive slab in air. Key detected terms: command, dataset, fdtd, material, mode, plane, port, reflection, script, script-command, solver, transmission.

## Key Terms

- command
- dataset
- fdtd
- material
- mode
- plane
- port
- reflection
- script
- script-command
- solver
- transmission

## Captured Headings

- stackrt - Script command
- Example 1: Five-layer stack with isotropic materials
- Example 2: Birefringent slab in air
- Example 3: A fully anisotropic and dispersive slab in air

## Official Text Excerpt

> stackrt - Script command FDTD STACK MODE DGTD CHARGE HEAT FEEM INTERCONNECT Calculates the reflection and transmission of a plane wave through a multi-layer stack using the analytic transfer matrix method. This function returns the fraction of transmitted and reflected power (Ts, Tp, Rs, Rp), and the complex reflection and transmission coefficients (ts, tp, rs, rp), for both S and P polarizations. All results are returned in a single dataset as a function of frequency and incidence angle (optional). NOTE: From 2022 R1.2, stackrt script command supports fully anisotropic and dispersive materials by specifying the nine values of the second-order refractive index tensor. For anisotropic materials, the polarization of reflected light could vary from its incident polarization. The suffix sp and ps denote how polarization is changed in the returned power and coefficients. sp stands for s incident and p reflected/transmitted. The fully anisotropic calculations use a different sign convention than isotropic calculations, and will cause Rpp in the anisotropic case to have an opposite sign compared to Rp in the isotropic case. To calculate the fields within the stack, ...

## Code Block Inventory

- Code block 1: 26 line(s); first line `f = linspace(c/400e-9, c/1000e-9,100); # frequency vector`
- Code block 2: 17 line(s); first line `N_layers = 3;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: RT = stackrt(n,d,f); | n: Refractive index of each layer. Size can be Nlayers: isotropic and non-dispersive Nlayers x Nfreq: isotropic and dispersive Nlayers x 3: anisotropic and non-dispersive Nlayers x Nfreq x 3: anisotropic and dispersiv

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [STACK](https://optics.ansys.com/hc/en-us/articles/360037226394)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [stackfield](https://optics.ansys.com/hc/en-us/articles/360034406294-stackfield)
- [Stack optical solver overview](https://optics.ansys.com/hc/en-us/articles/360034914653)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [multilayer stack calculations](https://optics.ansys.com/hc/en-us/articles/360034914653)
- [getfdtdindex](https://optics.ansys.com/hc/en-us/articles/360034409694-getfdtdindex)
- [visualize](https://optics.ansys.com/hc/en-us/articles/360034410514-visualize)

## Ansys-Related External Links Found

- None

## External Links Found

- None
