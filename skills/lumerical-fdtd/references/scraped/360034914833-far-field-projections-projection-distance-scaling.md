# Adjusting the projection distance in far field projections

Source URL: https://optics.ansys.com/hc/en-us/articles/360034914833-Far-field-projections-Projection-distance-scaling  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Adjusting the projection distance in far field projections` for the topic `Discovered from FDTD product reference manual`. It captured 3 heading(s), 2 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Adjusting the projection distance in far field projections, Projections to the intermediate field, See also. Key detected terms: boundary, command, far, far-field, fdtd, mode, plane, script, structure.

## Key Terms

- boundary
- command
- far
- far-field
- fdtd
- mode
- plane
- script
- structure

## Captured Headings

- Adjusting the projection distance in far field projections
- Projections to the intermediate field
- See also

## Official Text Excerpt

> Adjusting the projection distance in far field projections FDTD This section describes how to rescale far field projections to distances other than the default of 1m. It also describes how to use the farfieldexact functions to calculate the field distribution at arbitrary positions, including the so called intermediate field (beyond the simulation region boundary, but not yet the far field). Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basically still correct, although some subtle differences do exist. The script file first calculates the standard far field distribution. Rather than calculating the distribution on the entire hemisphere, we only get one line at y=0. This data is calculated with both the farfield3d and farfieldexact3d functions. As the following figure shows, both functions return the same result for the field distribution on a hemisphere with a radius of 1m. In most cases, the standard projection location is sufficient. However, if you wish to know the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 5 column(s), 3 row(s)
  - First row sample:  |  | Electric field scaling | Electric field intensity scaling | 
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Projections to surfaces other than hemispheres Use the farfieldexact functions when you want the field distribution on a surface other than a hemisphere. The following figure shows the field intensity along a straight line for x=-20:2

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
