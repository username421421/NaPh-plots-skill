# lmapexport - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/50997817911699-lmapexport-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lmapexport - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 3 heading(s), 5 link(s), 2 code block(s), 6 inline code term(s), and 4 table(s). Main headings: lmapexport - Script command, Configuration structures for grating with spatial variation, Configuration structures for metalens. Key detected terms: command, fdtd, grating, mode, port, script, script-command, structure.

## Key Terms

- command
- fdtd
- grating
- mode
- port
- script
- script-command
- structure

## Captured Headings

- lmapexport - Script command
- Configuration structures for grating with spatial variation
- Configuration structures for metalens

## Official Text Excerpt

> lmapexport - Script command FDTD Creates a mapping information file (.lmap) for a metalens or a grating with spatial variation. This script command is used with the Lumerical Sub-Wavelength model plugin. For further information on the Lumerical Sub-Wavelength Model, please see the Knowledge Base article on Lumerical Sub-Wavelength Model plugin: Introduction and data Generation. Note: This script command does not support the legacy .json file format for the LSWM, only the .lswm format. |Syntax|Description |lmapexport(“lswm_file”, map_info);| Exports a .lmap file for a given .lswm file for a grating with spatial variation. The .lmap file is created in the same directory as the .lswm file, and carries the same name as the input .lswm file, except with an .lmap extension. Note: If the target .lmap file already exists, a suffix of “_n” is appended, and a message is shown in the script prompt to indicate the file saved. The arguments are as follows: - lswm_file: A string pointing to the corresponding .lswm file - map_info: A struct with information of the map, see below for further information on its attributes and ...

## Code Block Inventory

- Code block 1: 11 line(s); first line `map_type = "rect";`
- Code block 2: 9 line(s); first line `metalensSize = [2,2]; # size in mm`

## Inline Code Inventory

- `[0,0]`
- `[J_in_1; J_out_1; J_in_2; J_out_2]`
- `[Jx, Jy, phase_offset_xy]`
- `[lambda_1, lambda_2]`
- `[size_x, size_y]`
- `{focus_1, coeffA_1, coeffB_1, focus_2, coeffA_2, coeffB_2}`

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: lmapexport(“lswm_file”, map_info); | Exports a .lmap file for a given .lswm file for a grating with spatial variation. The .lmap file is created in the same directory as the .lswm file, and carries the same name as the input .lswm file, exc
- Table 2: 2 column(s), 3 row(s)
  - Headers: Field, Description
  - First row sample: map_type | Coordinates of the map, either “rect” for rectilinear coordinates, or “polar” for polar coordinates.
- Table 3: 2 column(s), 2 row(s)
  - Headers: Field, Description
  - First row sample: lens_size | A matrix indicating the total size of the x- and y-directions, in mm. The format of the array is [size_x, size_y] .
- Table 4: 2 column(s), 4 row(s)
  - Headers: Field, Description
  - First row sample: reference_wavelength | A matrix with reference wavelength for the phase design, in µm. The format is as follows: [lambda_1, lambda_2]

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Lumerical Sub-Wavelength Model plugin: Introduction and data Generation.](https://optics.ansys.com/hc/en-us/articles/8597760630163-Lumerical-Sub-Wavelength-Model-plugin-Introduction-and-Data-Generation)
- [Lumerical Sub-Wavelength Model: How to Simulate a Grating with Spatial Variations](https://optics.ansys.com/hc/en-us/articles/34239784945299-Lumerical-Sub-Wavelength-Model-How-to-Simulate-a-Grating-with-Spatial-Variations)
- [Eye tracking optical system with a metalens.](https://optics.ansys.com/hc/en-us/articles/27182763655571-Eye-tracking-optical-system-with-a-metalens)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
