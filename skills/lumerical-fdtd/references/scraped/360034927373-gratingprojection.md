# gratingprojection - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034927373-gratingprojection  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `gratingprojection - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 5 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: gratingprojection - Script command. Key detected terms: boundary, command, far, grating, monitor, periodic, plane, script, source, structure.

## Key Terms

- boundary
- command
- far
- grating
- monitor
- periodic
- plane
- script
- source
- structure

## Captured Headings

- gratingprojection - Script command

## Official Text Excerpt

> gratingprojection - Script command DGTD Takes the near fields from a frequency domain monitor together with the periodicity vectors of the system, the source wave vector and the background refractive index and performs a far field projection to determine the relative power in each propagating grating order. | Syntax | Description | out = gratingprojection(nearfield, period, source, index); | Returns a matrix data set with all the projection results. The parameters of the data set are the grating orders (integers n and m) and frequency. Indexes n and m correspond to the first and second periodicity directions specified by the input periodicity vectors. The attributes of the data set are the same as those returned by the gratingorders command with the addition of the relative power into each propagating grating order (called projection). The projection result is normalized so that its sum over all grating orders is always equal to one. The frequency parameter is the same as that of the input field data. | Parameter || Default value | Type | Description | nearfield | required || unstructured data ...

## Code Block Inventory

- Code block 1: 9 line(s); first line `# unstructured data set with the near field`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = gratingprojection(nearfield, period, source, index); | Returns a matrix data set with all the projection results. The parameters of the data set are the grating orders (integers n and m) and frequency. Indexes n and m correspond to th
- Table 2: 5 column(s), 4 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: nearfield | required |  | unstructured data set | Field data from a frequency domain monitor.

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [getperiodicity](https://optics.ansys.com/hc/en-us/articles/360034407174-getperiodicity)
- [getsourcedirection](https://optics.ansys.com/hc/en-us/articles/360034927333-getsourcedirection)
- [gratingorders](https://optics.ansys.com/hc/en-us/articles/360034927353-gratingorders)

## Ansys-Related External Links Found

- None

## External Links Found

- None
