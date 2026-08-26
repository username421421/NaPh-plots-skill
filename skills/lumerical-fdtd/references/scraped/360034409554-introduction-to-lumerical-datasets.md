# Introduction to Lumerical datasets

Source URL: https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets  
Area: Discovered official source  
Topic: Discovered from Passing Data - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Introduction to Lumerical datasets` for the topic `Discovered from Passing Data - Python API`. It captured 12 heading(s), 14 link(s), 9 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Introduction to Lumerical datasets, Ex. 1 – Reflection vs radius and height (matrix dataset), Ex. 2 – Electric field data from a monitor (rectilinear dataset), Attributes and parameters, Attribute dimensions, What is in a dataset? Icons and the '?' operator, Accessing data in a dataset: the dot '.' operator, Dataset types. Key detected terms: command, dataset, fdtd, mesh, mode, monitor, reflection, script, structure, sweep.

## Key Terms

- command
- dataset
- fdtd
- mesh
- mode
- monitor
- reflection
- script
- structure
- sweep

## Captured Headings

- Introduction to Lumerical datasets
- Ex. 1 – Reflection vs radius and height (matrix dataset)
- Ex. 2 – Electric field data from a monitor (rectilinear dataset)
- Attributes and parameters
- Attribute dimensions
- What is in a dataset? Icons and the '?' operator
- Accessing data in a dataset: the dot '.' operator
- Dataset types
- Operations on datasets
- Scalar and Vector Attributes
- Scalar
- Vector

## Official Text Excerpt

> Introduction to Lumerical datasets Lumerical datasets are structured data objects that collect a set of related matrices into a single convenient object. To introduce this concept, we'll start by providing two examples. Additional information follows. Ex. 1 – Reflection vs radius and height (matrix dataset) Suppose you have a parameter sweep that measures the reflection from a particle as a function of particle radius and height. Saving this information generally requires 3 matrix variables. The 2D matrix R contains the reflection value from each simulation, while the 1D vectors radius and height contain the associated position values. A dataset object can be used to collect all three matrices into a single dataset variable. The following script code generates some example data, creates a R(radius,height) dataset, and finally creates several plots of the data. Ex. 2 – Electric field data from a monitor (rectilinear dataset) Field monitors in FDTD and MODE are used to calculate and save spatial electric field data. The raw electric field data within the monitor is distributed between several matrices: Each vector field component is stored in ...

## Code Block Inventory

- Code block 1: 14 line(s); first line `# create example results`
- Code block 2: 26 line(s); first line `# monitor name`
- Code block 3: 2 line(s); first line `?E_field = getresult("monitor","E");`
- Code block 4: 6 line(s); first line `?E_field.x;  # output the 'x' position vector`
- Code block 5: 3 line(s); first line `x = E_field.x;`
- Code block 6: 1 line(s); first line `R.addattribute("R",reflection); # add reflection attribute`
- Code block 7: 1 line(s); first line `R.R;`
- Code block 8: 1 line(s); first line `E.addattribute("E",Ex_raw,Ey_raw,Ez_raw); # add vector E field attribute`
- Code block 9: 5 line(s); first line `E.Ex; # get Ex component`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [pinch - Script command.](https://optics.ansys.com/hc/en-us/articles/360034405674)
- [Matrix dataset](https://optics.ansys.com/hc/en-us/articles/360034409454-matrixdataset)
- [Rectilinear spatial dataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [Unstructured spatial dataset](https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset)
- [Arbitrary unstructured dataset](https://optics.ansys.com/hc/en-us/articles/360034409574-struct)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
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
