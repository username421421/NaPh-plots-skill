# farfieldfilter - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930613-farfieldfilter  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `farfieldfilter - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 6 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: farfieldfilter - Script command. Key detected terms: command, far, fdtd, mode, monitor, periodic, script, structure.

## Key Terms

- command
- far
- fdtd
- mode
- monitor
- periodic
- script
- structure

## Captured Headings

- farfieldfilter - Script command

## Official Text Excerpt

> farfieldfilter - Script command FDTD MODE Sets or gets the filter width for far field filter which is used to remove ripples in the far field projection due to clipping of the near fields. It should be used when the near fields at the edge of the monitor are small but not precisely zero. The bumpy blue line of the figure shows the near field electric field that will be used for a far field projection. In this case, the field does not go to zero at the edge of the monitor, which will lead to ripples in the far field projection. The green line shows the spatial filter that will be applied to the fields, ensuring they go to zero. The filter parameter defines the width of the filter by the following formula: α=(a)/(a+b). | Syntax | Description | out = farfieldfilter; | Get the current far field filter setting. | farfieldfilter(α); | Set the current far field filter setting. α=(a)/(a+b). The far field filter has a single input parameter, which is a number between 0 and 1. By ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = farfieldfilter; | Get the current far field filter setting.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Periodic structures The far field filter option should not be used for periodic structures. Set it to zero when using the 'assume periodic' option.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Far field projection - spatial filtering](https://optics.ansys.com/hc/en-us/articles/360034394314-FFP-Spatial-filtering)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [farfield2d](https://optics.ansys.com/hc/en-us/articles/360034410074-farfield2d)
- [farfield3d](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d)

## Ansys-Related External Links Found

- None

## External Links Found

- None
