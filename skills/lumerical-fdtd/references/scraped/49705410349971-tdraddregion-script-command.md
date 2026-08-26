# tdraddregion – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/49705410349971-tdraddregion-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `tdraddregion – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 2 heading(s), 13 link(s), 1 code block(s), 4 inline code term(s), and 2 table(s). Main headings: tdraddregion – Script command, Wrapper functions. Key detected terms: boundary, command, dataset, fdtd, geometry, import, material, mesh, mode, port, script, script-command, structure.

## Key Terms

- boundary
- command
- dataset
- fdtd
- geometry
- import
- material
- mesh
- mode
- port
- script
- script-command
- structure

## Captured Headings

- tdraddregion – Script command
- Wrapper functions

## Official Text Excerpt

> tdraddregion – Script command FDTD MODE DGTD CHARGE HEAT FEEM Add a specific region from a geometry in a Sentaurus TDR file into Lumerical. The added regions are either a polygon in 2D or planar solid in 3D. This command is only available on Linux. |Syntax|Description |tdraddregion (“file_name”,”region_name”, options );| Adds the geometry region specified by region_name from the TDR file specified by file_name, with additional settings provided with struct options. This function does not return any data. The parameters are as follows: - file_name: A string pointing to the name of the TDR file. - region_name: A string specifying the region to add from the TDR file. The region name must follow the format`geometryname:regionname`, or`geometryname/regionname`, or`geometryname:regionname:materialname`, or`geometryname/regionname/materialname`where names are from the TDR file, as can be inspected by tdrinfo. Note: You can only add regions of type Solid2d and Solid3d to Lumerical (i.e. 2D and 3D MixedElement geometry type in the TDR terminology). Other types, such as Envelope (i.e. boundary element) or Rectilinear (i.e. tensor grid) are not supported. - options: A struct detailing specific options for the geometry ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `# Add the region with the name Aluminum_1 from the geometry with the name geometry_0,from a test tdr file`

## Inline Code Inventory

- `geometryname/regionname`
- `geometryname/regionname/materialname`
- `geometryname:regionname`
- `geometryname:regionname:materialname`

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: tdraddregion (“file_name”,”region_name”, options ); | Adds the geometry region specified by region_name from the TDR file specified by file_name, with additional settings provided with struct options. This function does not return any data.
- Table 2: 2 column(s), 6 row(s)
  - Headers: Syntax, Description
  - First row sample: material | The material name to use for the added region. Must correspond to one of the materials in the Lumerical material database. If none is given, the script command uses the default material for simulation objects.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [polygon](https://optics.ansys.com/hc/en-us/articles/360034901493-Polygon-Simulation-Object)
- [planar solid](https://optics.ansys.com/hc/en-us/articles/360034901573-Planar-solid-Simulation-Object)
- [extractstructure](https://optics.ansys.com/hc/en-us/articles/360034924713-extractstructure-Script-command)
- [Synopsys Sentaurus™ interoperability – import from and export to TDR files](https://optics.ansys.com/hc/en-us/articles/49705353405459-Synopsys-Sentaurus-interoperability-import-from-and-export-to-TDR-files)
- [tdrinfo](https://optics.ansys.com/hc/en-us/articles/49705705300243-tdrinfo-Script-command)
- [tdrwritedataset](https://optics.ansys.com/hc/en-us/articles/49705814878355-tdrwritedataset-Script-command)
- [tdrimportdataset](https://optics.ansys.com/hc/en-us/articles/52496768733331-tdrimportdataset-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
