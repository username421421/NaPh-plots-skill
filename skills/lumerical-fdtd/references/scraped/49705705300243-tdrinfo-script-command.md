# tdrinfo – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/49705705300243-tdrinfo-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `tdrinfo – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 2 heading(s), 10 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: tdrinfo – Script command, Wrapper functions. Key detected terms: command, dataset, fdtd, geometry, import, material, mode, port, script, script-command.

## Key Terms

- command
- dataset
- fdtd
- geometry
- import
- material
- mode
- port
- script
- script-command

## Captured Headings

- tdrinfo – Script command
- Wrapper functions

## Official Text Excerpt

> tdrinfo – Script command FDTD MODE DGTD CHARGE HEAT FEEM Reads a Sentaurus TDR file and outputs its information as a struct. This script command is only available on Linux. |Syntax|Description |out= tdrinfo (“file_name”);|Returns the information in the TDR file specified by file_name as a struct. The details of the struct is shown below. The returned struct from this script command is as follows. |Syntax|Description |FileName|The file name of the TDR file being read. |Geometries| A cell array containing information of geometries stored in the TDR file. Each element is another struct containing information for regions stored in the geometry, which has the following fields: - CoordinateSystem: Coordinate system type of the geometry. See tdraddregion for description. - GeometryType: Type of geometry. - Name: Name of geometry. - NumVertices: Number of vertices in the geometry. - States: A cell array of structs, containing datasets of specific regions for a specific state of simulation, with the following fields: - Dataset: A struct containing the dataset and information contained within. - Name: Name of the state. - Tags: Tags of the state ...

## Code Block Inventory

- Code block 1: 7 line(s); first line `tdr_file_info = tdrinfo("test_file.tdr");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out= tdrinfo (“file_name”); | Returns the information in the TDR file specified by file_name as a struct. The details of the struct is shown below.
- Table 2: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: FileName | The file name of the TDR file being read.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [Synopsys Sentaurus™ interoperability – import from and export to TDR files](https://optics.ansys.com/hc/en-us/articles/49705353405459-Synopsys-Sentaurus-interoperability-import-from-and-export-to-TDR-files)
- [tdraddregion](https://optics.ansys.com/hc/en-us/articles/49705410349971-tdraddregion-Script-command)
- [tdrwritedataset](https://optics.ansys.com/hc/en-us/articles/49705814878355-tdrwritedataset-Script-command)
- [tdrimportdataset](https://optics.ansys.com/hc/en-us/articles/52496768733331-tdrimportdataset-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
