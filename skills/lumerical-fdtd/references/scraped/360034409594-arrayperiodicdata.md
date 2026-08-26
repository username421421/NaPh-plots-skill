# arrayperiodicdata - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034409594-arrayperiodicdata  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `arrayperiodicdata - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 16 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: arrayperiodicdata - Script command. Key detected terms: command, dataset, periodic, plane, port, script, structure, symmetry.

## Key Terms

- command
- dataset
- periodic
- plane
- port
- script
- structure
- symmetry

## Captured Headings

- arrayperiodicdata - Script command

## Official Text Excerpt

> arrayperiodicdata - Script command DGTD CHARGE HEAT FEEM Generates an array of periodic data from a unit cell dataset based on a given plane of periodicity. This function is useful for obtaining the complete form of data from a periodic simulation which only contains data from one unit cell. Only unstructured datasets are supported by this command. | Syntax | Description | arrayperiodicdata(dataset,'periodic_plane',count); | Unfolds data from a symmetric dataset based on a given plane of symmetry. The first argument is a 2D or 3D unstructured dataset. The second argument is the plane with respect to which data is periodic in the format [+-][xyz], e.g. “-y” and refers to the axis of the plane of periodicity (i.e. the direction for the periodicity vector will be taken from the sign, and that plane, e.g. y-normal, will be used for arraying). The third argument count is number of unit cells to copy in the array (if 1, only returns the unit cell). Examples Below is a simple example of creating a periodic array of unstructured dataset generated from data available in the ...

## Code Block Inventory

- Code block 1: 7 line(s); first line `matlabload("unstructured_charge_example.mat");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: arrayperiodicdata(dataset,'periodic_plane',count); | Unfolds data from a symmetric dataset based on a given plane of symmetry. The first argument is a 2D or 3D unstructured dataset. The second argument is the plane with respect to which dat

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [unfoldsymmetricdata](https://optics.ansys.com/hc/en-us/articles/360034929953-unfoldsymmetricdata)
- [unstructureddataset](https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset)
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

- [unstructured_charge_example.mat](https://lumerical.zendesk.com/hc/article_attachments/360046127913/unstructured_charge_example.mat)
