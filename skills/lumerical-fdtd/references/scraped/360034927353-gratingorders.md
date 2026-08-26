# gratingorders - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034927353-gratingorders  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `gratingorders - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 5 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: gratingorders - Script command. Key detected terms: boundary, command, grating, monitor, periodic, plane, script, source.

## Key Terms

- boundary
- command
- grating
- monitor
- periodic
- plane
- script
- source

## Captured Headings

- gratingorders - Script command

## Official Text Excerpt

> gratingorders - Script command DGTD Returns a matrix data set with the propagating grating orders, a unit vector in the direction of the wave vector (or k-vector) of each order, and the grating angles. The grating orders are the same as those used by the gratingprojection command to perform a projection. | Syntax | Description | out = gratingorders(period, source, frequency, index); | Returns a matrix data set with the propagating grating orders (integers n and m), a unit vector in the direction of the k-vector of each order (call them u (n,m)) and their corresponding angles (theta and phi). The parameters of the data set are n,m and frequency. Indexes n and m correspond to the first and second periodicity directions specified by the input periodicity vectors. The attributes of the data set are the unit vectors u (n,m) and their corresponding angles (theta and phi). The grating angles are defined with respect to the normal incidence direction of the source (call it the n -axis). The first angle (theta) is an elevation from the n -axis and the ...

## Code Block Inventory

- Code block 1: 10 line(s); first line `# frequency vector of the near fields`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = gratingorders(period, source, frequency, index); | Returns a matrix data set with the propagating grating orders (integers n and m), a unit vector in the direction of the k-vector of each order (call them u (n,m)) and their correspond
- Table 2: 5 column(s), 4 row(s)
  - Headers: Parameter, , Default value, Type, Description
  - First row sample: period | required |  | vector | [3x1] or [3x2] matrix with the periodicity vectors. These are typically retrieved using the getperiodicity command.

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [getperiodicity](https://optics.ansys.com/hc/en-us/articles/360034407174-getperiodicity)
- [getsourcedirection](https://optics.ansys.com/hc/en-us/articles/360034927333-getsourcedirection)
- [gratingprojection](https://optics.ansys.com/hc/en-us/articles/360034927373-gratingprojection)

## Ansys-Related External Links Found

- None

## External Links Found

- None
