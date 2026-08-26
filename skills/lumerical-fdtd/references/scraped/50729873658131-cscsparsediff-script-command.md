# cscsparsediff - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/50729873658131-cscsparsediff-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `cscsparsediff - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 9 link(s), 0 code block(s), 1 inline code term(s), and 1 table(s). Main headings: cscsparsediff - Script command. Key detected terms: command, dataset, fdtd, mode, script, script-command, structure.

## Key Terms

- command
- dataset
- fdtd
- mode
- script
- script-command
- structure

## Captured Headings

- cscsparsediff - Script command

## Official Text Excerpt

> cscsparsediff - Script command FDTD MODE CHARGE HEAT FEEM INTERCONNECT Determines the sparse difference between two rectilinear Lumerical datasets. |Syntax|Description |out=cscsparsediff(subject_dataset, reference_dataset);| Determines the sparse difference between the subject and reference datasets, by computing`subject-reference`. Both datasets must contain parameters x,y, and z. The subject dataset must contain x,y,z values that matches exactly with a section of the x,y,z values of the reference dataset. Each dataset may have one additional parameter that must match exactly. - subject_dataset: The subject Lumerical dataset. - reference_dataset: The reference Lumerical dataset. - out: A struct of structs containing the sparse difference in compressed sparse column (CSC) format for each dataset attribute. Each structure corresponds to a single attribute in the rectilinear dataset. In the CSC format, the column indices (1-based) represent the indices of the additional parameter, and the row indices (1-based) corresponds to a linear index converted from the \(x,y,z\) data in the reference dataset. For example, the \(i,j,k\)-th element in \(x,y,z\) in the reference dataset is converted to a linear row index via \(i+(j-1)\times\text{len}(x)+(k-1)\times\text{len}(x)\times\text{len}(y)\). See Also List of commands

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `subject-reference`

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out=cscsparsediff(subject_dataset, reference_dataset); | Determines the sparse difference between the subject and reference datasets, by computing subject-reference . Both datasets must contain parameters x,y, and z. The subject dataset mus

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Lumerical datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)

## Ansys-Related External Links Found

- None

## External Links Found

- [compressed sparse column (CSC) format](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html)
