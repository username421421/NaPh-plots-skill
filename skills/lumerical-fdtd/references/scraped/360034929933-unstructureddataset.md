# unstructureddataset - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `unstructureddataset - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 21 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: unstructureddataset - Script command. Key detected terms: command, dataset, fdtd, import, mesh, mode, plane, port, script, structure, transmission.

## Key Terms

- command
- dataset
- fdtd
- import
- mesh
- mode
- plane
- port
- script
- structure
- transmission

## Captured Headings

- unstructureddataset - Script command

## Official Text Excerpt

> unstructureddataset - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Creates an empty dataset that is associated with arbitrary x/y/z coordinate in space, and with additional matrix, a connectivity matrix to connect them. The connectivity matrix comes after x, y, and z. Like rectilinear datasets, unstructured datasets can be parameterized, and can contain an arbitrary number of attributes (see addattribute) and parameters (see addparameter). See Dataset introduction for more information. For datasets that are not associated with the x/y/z coordinates (ex. transmission as a function of frequency), see matrixdataset. | Syntax | Description | unstructureddataset(x,y,z,C); | Creates an empty unstructured dataset associated with the coordinates x/y/z and a connectivity matrix to connect them. Arguments 'x', 'y' and 'z' must be the same length; equivalent to the total number of points. The argument 'C' should be a matrix of integers where the number of rows equal to number of shapes in the mesh, the number of columns should be 2 (line segments), 3 (triangles) or 4 (tetrahedra), and values should be integers. Examples Below is a simple example of the ...

## Code Block Inventory

- Code block 1: 16 line(s); first line `# constructing an unstructured dataset`
- Code block 2: 5 line(s); first line `Absorption = unstructureddataset("Absorption",x,y,z,cm);`
- Code block 3: 5 line(s); first line `x = [0;1;2];`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: unstructureddataset(x,y,z,C); | Creates an empty unstructured dataset associated with the coordinates x/y/z and a connectivity matrix to connect them. Arguments 'x', 'y' and 'z' must be the same length; equivalent to the total number of poi

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [addattribute)](https://optics.ansys.com/hc/en-us/articles/360034929873-addattribute)
- [addparameter)](https://optics.ansys.com/hc/en-us/articles/360034409494-addparameter)
- [Dataset introduction](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [matrixdataset](https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset)
- [unstructured_charge_example.mat](https://optics.ansys.com/hc/article_attachments/360046127873/unstructured_charge_example.mat)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114-importdataset)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [addattribute](https://optics.ansys.com/hc/en-us/articles/360034929873-addattribute)
- [addparameter](https://optics.ansys.com/hc/en-us/articles/360034409494-addparameter)
- [visualize](https://optics.ansys.com/hc/en-us/articles/360034410514-visualize)
- [datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [getparameter](https://optics.ansys.com/hc/en-us/articles/360034409514-getparameter)
- [getattribute](https://optics.ansys.com/hc/en-us/articles/360034409534-getattribute)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct)

## Ansys-Related External Links Found

- None

## External Links Found

- None
