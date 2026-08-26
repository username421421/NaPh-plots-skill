# Using spatial filtering to avoid truncating fields in far field projections

Source URL: https://optics.ansys.com/hc/en-us/articles/360034394314-Far-field-projections-Spatial-filtering  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Using spatial filtering to avoid truncating fields in far field projections` for the topic `Discovered from FDTD product reference manual`. It captured 2 heading(s), 2 link(s), 0 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Using spatial filtering to avoid truncating fields in far field projections, See also. Key detected terms: dipole, far, far-field, fdtd, import, mode, monitor, periodic, port, script, structure.

## Key Terms

- dipole
- far
- far-field
- fdtd
- import
- mode
- monitor
- periodic
- port
- script
- structure

## Captured Headings

- Using spatial filtering to avoid truncating fields in far field projections
- See also

## Official Text Excerpt

> Using spatial filtering to avoid truncating fields in far field projections FDTD This section describes the far field spatial filtering option. |Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basically still correct, although some subtle differences do exist. For far field projections to be accurate, all radiation that will propagate to the far field must pass through the monitor being used for the projection. The far field projection functions assume that the EM fields are zero beyond the edge of the monitor. This effectively truncates the near fields at the monitor edge. In some cases, the monitor (and simulation region) would have to be impractically large to ensure that all of the radiation passes through the monitor. One such simulation is the angular distribution of a dipole near an interface. To reproduce these results, run the simulation file and then the script. The blue line in the following figure shows the near field ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basical
- Table 2: 2 column(s), 1 row(s)
  - First row sample: farfieldfilter(0); | farfieldfilter(1);
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: Periodic structures - far field filter The far field filter option should not be used for periodic structures. Set it to zero when using the 'assume periodic' option.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [farfieldfilter script function](https://optics.ansys.com/hc/en-us/articles/360034930613)

## Ansys-Related External Links Found

- None

## External Links Found

- None
