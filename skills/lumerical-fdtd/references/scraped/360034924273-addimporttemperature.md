# addimporttemperature - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034924273-addimporttemperature  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addimporttemperature - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 8 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addimporttemperature - Script command. Key detected terms: command, dataset, import, port, script, solver, source, structure.

## Key Terms

- command
- dataset
- import
- port
- script
- solver
- source
- structure

## Captured Headings

- addimporttemperature - Script command

## Official Text Excerpt

> addimporttemperature - Script command CHARGE Adds an import temperature source to the CHARGE solver (only applicable to non-isothermal transport). The import temperature object can be used to import a temperature map for non-isothermal simulation. A CHARGE solver region must be present in the objects tree for this command to work. | Syntax | Description | addimporttemperature; | Adds an import temperature source to the CHARGE solver. The source only gets applied if the "temperature dependence" is set to "non-isothermal." This function does not return any data. |addimporttemperature(struct_data);| Adds an import temperature source and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. Once the import temperature source is created, the data can be imported from a matlab (.mat) file using the GUI or by assigning a dataset to the object using the importdataset script command. The dataset can either be in rectilinear or unstructured (finite-element) format. Example The following script command will add an import temperature source and will load an analytic ...

## Code Block Inventory

- Code block 1: 14 line(s); first line `addimporttemperature;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addimporttemperature; | Adds an import temperature source to the CHARGE solver. The source only gets applied if the "temperature dependence" is set to "non-isothermal." This function does not return any data.

## Official Links Found

- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114-importdataset)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [linspace](https://optics.ansys.com/hc/en-us/articles/360034409254-linspace)
- [rectilineardataset](https://optics.ansys.com/hc/en-us/articles/360034409474-rectilineardataset)
- [select](https://optics.ansys.com/hc/en-us/articles/360034928593-select)
- [addimportheat](https://optics.ansys.com/hc/en-us/articles/360034404394-addimportheat)

## Ansys-Related External Links Found

- None

## External Links Found

- None
