# tdrwritedataset – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/49705814878355-tdrwritedataset-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `tdrwritedataset – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 2 heading(s), 10 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: tdrwritedataset – Script command, Wrapper functions. Key detected terms: analysis, command, dataset, fdtd, import, mode, port, script, script-command, source.

## Key Terms

- analysis
- command
- dataset
- fdtd
- import
- mode
- port
- script
- script-command
- source

## Captured Headings

- tdrwritedataset – Script command
- Wrapper functions

## Official Text Excerpt

> tdrwritedataset – Script command FDTD MODE DGTD CHARGE HEAT FEEM Writes a Lumerical dataset to a Sentaurus TDR file. This command is only available on Linux. |Syntax|Description |tdrwritedataset(“file_name”, dataset, options);| Writes a rectilinear dataset to a TDR file with the following parameters: - file_name: Name of the destination TDR file. A new file is created if it does not exist, otherwise the file is overwritten. - dataset: A dataset to add to the TDR file. Only rectilinear datasets are supported. - options: Required and optional arguments for the operation, fields are shown below. This function does not return any data. Note: Take the following precautions with the units within the rectilinear dataset to write to a TDR file: - This script command does not account for the physical nature of the input dataset. To set the correct units for attributes in the dataset, you must use the X_unit field in the options struct. - Coordinates x,y,and z in the rectilinear dataset are always assumed to be provided in the units of m and are converted to microns prior to writing ...

## Code Block Inventory

- Code block 1: 10 line(s); first line `# Write optical generation from a completed simulation to a TDR file`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: tdrwritedataset(“file_name”, dataset, options); | Writes a rectilinear dataset to a TDR file with the following parameters: file_name: Name of the destination TDR file. A new file is created if it does not exist, otherwise the file is overw
- Table 2: 2 column(s), 6 row(s)
  - Headers: Syntax, Description
  - First row sample: region_name | Required. Specifies the name of the region to which the dataset applies. It can be arbitrary name. For example, to save the optical generation rate from the FDTD analysis object the region name can be set the same as the analy

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [Synopsys Sentaurus™ interoperability – import from and export to TDR files](https://optics.ansys.com/hc/en-us/articles/49705353405459-Synopsys-Sentaurus-interoperability-import-from-and-export-to-TDR-files)
- [tdrinfo](https://optics.ansys.com/hc/en-us/articles/49705705300243-tdrinfo-Script-command)
- [tdraddregion](https://optics.ansys.com/hc/en-us/articles/49705410349971-tdraddregion-Script-command)
- [tdrimportdataset](https://optics.ansys.com/hc/en-us/articles/52496768733331-tdrimportdataset-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
