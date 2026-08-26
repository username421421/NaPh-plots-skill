# h5writeattr – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/19055540178963-h5writeattr-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `h5writeattr – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 13 link(s), 4 code block(s), 0 inline code term(s), and 2 table(s). Main headings: h5writeattr – Script command. Key detected terms: command, dataset, fdtd, group, mode, script, script-command.

## Key Terms

- command
- dataset
- fdtd
- group
- mode
- script
- script-command

## Captured Headings

- h5writeattr – Script command

## Official Text Excerpt

> h5writeattr – Script command FDTD MODE DGTD CHARGE HEAT FEEM Write a matrix or string as an attribute of a group or a dataset to an HDF5 file. | Syntax | Description | h5writeattr("filename", "location_name", "attribute_name", data); | Create an attribute named "attribute_name" to a group or dataset named " location_name" within an HDF5 file named "filename" from the given data. Will create the HDF5 file named "filename" if it does not exist. If there is no group or dataset called “location_name”, a new group called “location_name” will be created. If the attribute named "attribute_name" already exists in the given group/dataset within the HDF5 file, the attribute will be overwritten. Otherwise, the attribute is simply added to the existing group/dataset within the HDF5 file. | h5writeattr("filename", "location_name", "attribute_name", data, ["access_mode"]); | Optional argument: "append" or "overwrite" "append": The attribute named "attribute_name" is added to a group or dataset named "location_name" in the HDF5 file "filename" if the attribute does not exist yet. Otherwise, it is overwritten. This command creates a HDF5 file named “filename” if it does not exist. If ...

## Code Block Inventory

- Code block 1: 3 line(s); first line `a = [1, 2, pi; 4, 5, 2*pi];`
- Code block 2: 9 line(s); first line `?h5readattr("testfile.h5", "/test_group", "double_matrix");`
- Code block 3: 2 line(s); first line `b = [2, 3, 5, 7, 11, 13];`
- Code block 4: 9 line(s); first line `info = h5info("testfile.h5");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Syntax, Description
  - First row sample: h5writeattr("filename", "location_name", "attribute_name", data); | Create an attribute named "attribute_name" to a group or dataset named " location_name" within an HDF5 file named "filename" from the given data. Will create the HDF5 file 
- Table 2: 3 column(s), 6 row(s)
  - Headers: Parameter, Type, Description
  - First row sample: filename | string | Name of the HDF5 file.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [h5readattr](https://optics.ansys.com/hc/en-us/articles/360034927433-h5readattr)
- [h5info](https://optics.ansys.com/hc/en-us/articles/360034927413-h5info-Script-command)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [h5write](https://optics.ansys.com/hc/en-us/articles/19055251802899)
- [h5info](https://optics.ansys.com/hc/en-us/articles/360034927413-h5info)
- [h5read](https://optics.ansys.com/hc/en-us/articles/360034407214-h5read)
- [Reading HDF5 files](https://optics.ansys.com/hc/en-us/articles/360034936913-HDF5-files)

## Ansys-Related External Links Found

- None

## External Links Found

- None
