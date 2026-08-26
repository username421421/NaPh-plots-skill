# Import liquid crystal orientation from CSV - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902033-Import-object-Liquid-crystal-from-CSV  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Import liquid crystal orientation from CSV - Simulation object` for the topic `Discovered from FDTD product reference manual`. It captured 12 heading(s), 7 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Import liquid crystal orientation from CSV - Simulation object, File format, 2D format, 3D format, Graphical import, Opening the wizard, Page 1, Page 2. Key detected terms: analysis, command, dataset, fdtd, group, import, material, plane, port, script, structure.

## Key Terms

- analysis
- command
- dataset
- fdtd
- group
- import
- material
- plane
- port
- script
- structure

## Captured Headings

- Import liquid crystal orientation from CSV - Simulation object
- File format
- 2D format
- 3D format
- Graphical import
- Opening the wizard
- Page 1
- Page 2
- Page 3
- Scripted import
- Imported object
- See also

## Official Text Excerpt

> Import liquid crystal orientation from CSV - Simulation object FDTD This section describes how to use the CSV import to directly import spatial Liquid Crystal (LC) orientation data from a CSV (comma-separated value) file. This file is typically created with TechWiz LCD from Sanayi System Co., Ltd. (http://sanayisystem.com/) and makes it easy to import spatial information on LC orientation from TechWiz LCD simulations. |Note: Other methods to define spatially-varying LC The required CSV file format is not simple to generate yourself, so data that is not already in the required format can be imported using the addgridattribute and importdataset script commands instead. See LC rotation for more information about adding spatially-varying LC grid attributes. The file format for the CSV file that defines the LC orientation as a function of space can be in a 2D format or 3D format. File format 2D format The file should have the form: Where - The orientation of the LC is defined by THETA and PHI. - PHI is the azimuthal angle in the X-Y plane with respect to the x-axis, in degrees, ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `THETA,X=-50,X=-49,X=-48,X=-47,X=-46,X=-45,X=-44,X=-43,X=-42,X=-41,X=-40,X=-39,X=-38,...Y=1,90,90,90,90,90,90,90,90,-,-,90,90,-,-,…Y=2,45,45,35,25,-,-,-,-,25,…….`
- Code block 2: 1 line(s); first line `THETAZ=0,X=0,X=1,X=2,X=3,…Y=1,90,90,90,90,90,90,90,90,-,-,90,90,-,-,…Y=2,45,10,22.5,15.7,-,-,-,-,75,……. PHIZ=0,X=0,X=1,X=2,X=3,…Y=1,0,0,0,0,90,90,90,90,-,-,90,9`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Other methods to define spatially-varying LC The required CSV file format is not simple to generate yourself, so data that is not already in the required format can be imported using the addgridattribute and importdataset script comma

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [addgridattribute](https://optics.ansys.com/hc/en-us/articles/360034404674)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114)
- [LC rotation](https://optics.ansys.com/hc/en-us/articles/360034915153)
- [importcsvlc](https://optics.ansys.com/hc/en-us/articles/360034924773)
- [Import object](https://optics.ansys.com/hc/en-us/articles/360033154434)

## Ansys-Related External Links Found

- None

## External Links Found

- [http://sanayisystem.com/](http://sanayisystem.com/)
