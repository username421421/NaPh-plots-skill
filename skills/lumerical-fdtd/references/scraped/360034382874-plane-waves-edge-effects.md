# Understanding field truncation issues with finite sized plane wave sources

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382874-Plane-waves-Edge-effects  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Understanding field truncation issues with finite sized plane wave sources` for the topic `Discovered from FDTD`. It captured 5 heading(s), 4 link(s), 0 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Understanding field truncation issues with finite sized plane wave sources, Examples of correct usage, Truncation by PML boundaries, Truncation due to short source span, See also. Key detected terms: analysis, bloch, boundary, far, fdtd, material, mode, periodic, plane, pml, reflection, script, source, structure, tfsf.

## Key Terms

- analysis
- bloch
- boundary
- far
- fdtd
- material
- mode
- periodic
- plane
- pml
- reflection
- script
- source
- structure
- tfsf

## Captured Headings

- Understanding field truncation issues with finite sized plane wave sources
- Examples of correct usage
- Truncation by PML boundaries
- Truncation due to short source span
- See also

## Official Text Excerpt

> Understanding field truncation issues with finite sized plane wave sources FDTD MODE This section describes problems that can occur when using the plane wave source is truncated, either because the span is too small, or when PML boundary conditions are used. Examples of correct usage Ideally the plane wave source should be used in the following manner: The source should span the entire simulation. Periodic or Bloch boundary conditions should be used in the directions normal to the propagation. PML should be used to to absorb the transmitted and reflected light.The first two examples illustrate this situation. || Description Simulate a plane wave propagating through free space at normal incidence. Simulation Settings - Periodic BC for Y boundaries. PML for X boundaries. - Plane wave source extends through simulation boundary. - No physical structures Results - An ideal plane wave propagates forward from the source, and is absorbed by the PML on the right side of the simulation. - In front of the source, a uniform intensity of 1 is measured at all locations. This is expected for a plane ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - First row sample:  | Description Simulate a plane wave propagating through free space at normal incidence. Simulation Settings Periodic BC for Y boundaries. PML for X boundaries. Plane wave source extends through simulation boundary. No physical structures R
- Table 2: 2 column(s), 1 row(s)
  - First row sample:  | Description Simulate a plane wave propagating through free space, but with PML on all boundaries. Simulation Settings PML BC on all boundaries. Plane wave extends through simulation boundary. No physical structures. Results This simulati
- Table 3: 2 column(s), 1 row(s)
  - First row sample:  | Description Simulating a finite sized plane wave propagating in free space with the planewave source. Simulation Settings PML BC on all boundaries. Plane wave source does not extend through simulation boundary. No physical structures. Re

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [TFSF sources](https://optics.ansys.com/hc/en-us/articles/360034902093)

## Ansys-Related External Links Found

- None

## External Links Found

- [Source field profiles and movies](https://kx.lumerical.com/t/source-movies/33599)
