# Tips for adding surface roughness to structures

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382374-Complex-structures-Surface-roughness  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Tips for adding surface roughness to structures` for the topic `Discovered from FDTD product reference manual`. It captured 3 heading(s), 2 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Tips for adding surface roughness to structures, Simple roughness example, Advanced surface roughness. Key detected terms: fdtd, group, import, mesh, mode, port, script, structure.

## Key Terms

- fdtd
- group
- import
- mesh
- mode
- port
- script
- structure

## Captured Headings

- Tips for adding surface roughness to structures
- Simple roughness example
- Advanced surface roughness

## Official Text Excerpt

> Tips for adding surface roughness to structures FDTD MODE This section describes how to create objects with surface roughness. Simple roughness example The structure group named surface roughness simple which is located in usr_surface_roughness.fsp shows a simple technique for adding surface roughness to a ridge waveguide. Rather than creating the structure from a single rectangle, it is composed of many thin slices, each with a random variance in width. Advanced surface roughness The structure group named surface roughness advanced which is located in usr_surface_roughness.fsp shows a more advanced surface roughness model. In this case, the roughness is characterized by a specified sigma RMS (s) and correlation length (Lc). These quantities are related to the correlation function by $$ \langle H( r )H( r + \delta) \rangle = \sigma^2 e^{\left( -\left( \frac{\delta}{L_c} \right)^2 \right)} $$ The roughness is generated creating a matrix of uniform random numbers in k space. The high frequency components are removed, and the resulting values are transformed back to real space. || In this case, a single import object (surface option) is used to define the entire ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - First row sample:  | 

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)

## Ansys-Related External Links Found

- None

## External Links Found

- None
