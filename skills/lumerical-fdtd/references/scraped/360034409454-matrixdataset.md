# matrixdataset - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `matrixdataset - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 20 link(s), 2 code block(s), 0 inline code term(s), and 1 table(s). Main headings: matrixdataset - Script command. Key detected terms: command, dataset, fdtd, mode, reflection, script, structure.

## Key Terms

- command
- dataset
- fdtd
- mode
- reflection
- script
- structure

## Captured Headings

- matrixdataset - Script command

## Official Text Excerpt

> matrixdataset - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Creates an empty matrix dataset. Matrix datasets are used for data (attributes and parameters) that don't have any spatial dependence (i.e. Reflection vs frequency). For datasets that do have x/y/z spatial coordinates (i.e. electric fields), use rectilineardataset or unstructureddataset. Matrix datasets can be parameterized, and can contain an arbitrary number of attributes (see addattribute) and parameters (see addparameter). See Dataset introduction for more information. | Syntax | Description | matrixdataset; | Creates an empty dataset. | matrixdataset("name"); | Creates an empty dataset with the name "name". Examples This example uses a matrix dataset to store cross section (sigma) data as a function of frequency. In this case, the cross section data sigma is the attribute, and frequency is the parameter. To allow the user to access the frequency parameter in terms of frequency or wavelength , both frequency (f) and wavelength (c/f) are added as interdependent parameters. The following script code generates some example data, then creates a R(radius,height) dataset. See Also rectilineardataset, addattribute, addparameter, visualize, datasets, getparameter, getattribute, ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `sigma = matrixdataset("cross_section");`
- Code block 2: 14 line(s); first line `# create example results`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: matrixdataset; | Creates an empty dataset.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [unstructureddataset](https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset)
- [addattribute)](https://optics.ansys.com/hc/en-us/articles/360034929873-addattribute)
- [addparameter)](https://optics.ansys.com/hc/en-us/articles/360034409494-addparameter)
- [Dataset introduction](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [addattribute](https://optics.ansys.com/hc/en-us/articles/360034929873-addattribute)
- [addparameter](https://optics.ansys.com/hc/en-us/articles/360034409494-addparameter)
- [visualize](https://optics.ansys.com/hc/en-us/articles/360034410514-visualize)
- [datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [getparameter](https://optics.ansys.com/hc/en-us/articles/360034409514-getparameter)
- [getattribute](https://optics.ansys.com/hc/en-us/articles/360034409534-getattribute)
- [matrixdataset](https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct)

## Ansys-Related External Links Found

- None

## External Links Found

- None
