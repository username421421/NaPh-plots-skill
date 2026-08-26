# Surface import - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034901973-Import-object-Surfaces  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Surface import - Simulation object` for the topic `Discovered from FDTD product reference manual`. It captured 6 heading(s), 9 link(s), 0 code block(s), 0 inline code term(s), and 5 table(s). Main headings: Surface import - Simulation object, File formats, Surface object import, Using GUI, Using Script, See also. Key detected terms: command, fdtd, import, mode, plane, port, script, structure.

## Key Terms

- command
- fdtd
- import
- mode
- plane
- port
- script
- structure

## Captured Headings

- Surface import - Simulation object
- File formats
- Surface object import
- Using GUI
- Using Script
- See also

## Official Text Excerpt

> Surface import - Simulation object FDTD MODE This section describes the data format for importing surface data Z(x,y) into the import primitive. It provides example data files and example script files that generate the data files. This object is sometimes used to import atomic force microscope (AFM) data. File formats The file formats are shown in the following tables. Spaces, commas or tabs can be used as separators in the files. The columns do not have to be aligned. Please note that as shown below, the data ranges go from 0 to m for x (0 to n for y). This means that there are actually m+1 data points in x and n+1 data points in y. Z = Z(x,y): It is often easy to reverse the meaning of x and y when exporting a file. The surface import window provides a check button to invert x and y to correct this problem easily. |Description|File format |type 1: The x and y data is contained in the file. An example file is usr_surface_3d_1.txt. A script file that generates this example ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Description, File format
  - First row sample: type 1: The x and y data is contained in the file. An example file is usr_surface_3d_1.txt . A script file that generates this example is usr_surface_3d_1.lsf . | 
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: importing surfaces for 2D simulations or other orientations (eg. X(y,z) or Y(x,z)) The import object always creates a surface as a function of x,y. If you need the a different surface orientation (such as when running 2D simulations w
- Table 3: 3 column(s), 2 row(s)
  - Headers: Command, Example files, Description
  - First row sample: importsurface | usr_surface_3d_1.txt usr_surface_3d_1.lsf | Import surface data from a file created by usr_surface_3d_1.lsf
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note: Related properties It is important to notice that the 'x, y scale' and 'x, y span' properties are linearly related. Doubling the object 'x span' will automatically double the 'x scale' property. Similarly, the 'lower, upper ref height
- Table 5: 1 column(s), 1 row(s)
  - First row sample: Note: Overlapping surfaces If the z span is small enough such that the upper and lower surfaces overlap (as shown below), no structure will be included in the simulation in that region.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Design](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface#toc_3)
- [Scripting chapter](https://optics.ansys.com/hc/en-us/articles/360034408654)
- [importsurface](https://optics.ansys.com/hc/en-us/articles/360034408654)
- [importsurface2](https://optics.ansys.com/hc/en-us/articles/360034928993)
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Import object](https://optics.ansys.com/hc/en-us/articles/360033154434)

## Ansys-Related External Links Found

- None

## External Links Found

- [Conformal coating](https://support.lumerical.com/hc/en-us/articles/1500010819261)
