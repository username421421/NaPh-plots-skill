# Binary spatial data - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382754-Import-object-Binary-spatial-data  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Binary spatial data - Simulation object` for the topic `Discovered from FDTD`. It captured 5 heading(s), 7 link(s), 1 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Binary spatial data - Simulation object, File formats, Binary import window, Importing binary data using script commands, See also. Key detected terms: boundary, command, fdtd, import, material, mesh, mode, monitor, plane, port, script, solver, structure.

## Key Terms

- boundary
- command
- fdtd
- import
- material
- mesh
- mode
- monitor
- plane
- port
- script
- solver
- structure

## Captured Headings

- Binary spatial data - Simulation object
- File formats
- Binary import window
- Importing binary data using script commands
- See also

## Official Text Excerpt

> Binary spatial data - Simulation object FDTD MODE This section describes the data format for importing binary data to define an object. In this binary import, the data should have values of 1 or 0, indicating that the object is or is not present. File formats The file formats are shown in the following tables. Spaces, commas or tabs can be used as separators in the files. The columns do not have to be aligned. |Description|File format | The values of x range from X1 to Xn, y from Y1 to Ym and z from Z1 to Zp. The values of x, y, and z must be uniformly spaced. The number n should be either 1 (the material is present at this location) or 0 (the material is not present). If other values are used, any non-zero value will be interpreted to be 1. Note that there must be at least 2 data points in each dimension (ie, n, m, p >= 2). | Binary import window The import binary button is in the “ Design ” tab in FDTD, ...

## Code Block Inventory

- Code block 1: 21 line(s); first line `x = [-3e-6;3e-6];`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Description, File format
  - First row sample: The values of x range from X1 to Xn, y from Y1 to Ym and z from Z1 to Zp. The values of x, y, and z must be uniformly spaced. The number n should be either 1 (the material is present at this location) or 0 (the material is not present). If 
- Table 2: 3 column(s), 2 row(s)
  - Headers: Command, Example files, Description
  - First row sample: importbinary | [[usr_importbinary_3d.fsp]] [[usr_importbinary_3d.lsf]] [[usr_importbinary_3d.txt]] | Import binary data from a file.
- Table 3: 1 column(s), 1 row(s)
  - First row sample: [[NOTE]]: Imported binary object boundaries The boundary of the import binary object is positioned between the vertices where the material is present and the vertices where the material is not present. The shape of this implied boundary can

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Design](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface#toc_3)
- [importbinary](https://optics.ansys.com/hc/en-us/articles/360034408734-importbinary-Script-command)
- [importbinary2](https://optics.ansys.com/hc/en-us/articles/360034929013-importbinary2-Script-command)
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Import object](https://optics.ansys.com/hc/en-us/articles/360033154434)

## Ansys-Related External Links Found

- None

## External Links Found

- None
