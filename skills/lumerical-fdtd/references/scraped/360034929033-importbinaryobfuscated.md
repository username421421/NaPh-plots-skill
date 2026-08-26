# importbinaryobfuscated - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034929033-importbinaryobfuscated  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `importbinaryobfuscated - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 4 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: importbinaryobfuscated - Script command. Key detected terms: command, fdtd, import, port, script, structure.

## Key Terms

- command
- fdtd
- import
- port
- script
- structure

## Captured Headings

- importbinaryobfuscated - Script command

## Official Text Excerpt

> importbinaryobfuscated - Script command FDTD This command is identical to importbinary but makes it possible to import data from a file that has been obfuscated. For details on how to obfuscate the data files, please see the Online Help in the User Guide, Structures section. | Syntax | Description | out = importbinaryobfuscated(key,filename,file_units,x0,y0,z0,reverse_index_order); | Import binary data from filename in three dimensional simulations. All arguments after the filename are optional. | Parameter | Default value | Type | Description | key | required | string | The key that is used to decrypt the obfuscated file. | filename | required | string | name of the file with binary data to import. May contain complete path to file, or path relative to current working directory | file_units | "m" | string | The optional string argument file_units can be "m", "cm, "mm", "microns" or "nm" to specify the units in the file. | x0 | 0 | number | The optional arguments x0, y0 and z0 specify the data origin in the global coordinates of the Graphical Layout Editor. For ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = importbinaryobfuscated(key,filename,file_units,x0,y0,z0,reverse_index_order); | Import binary data from filename in three dimensional simulations. All arguments after the filename are optional.
- Table 2: 4 column(s), 7 row(s)
  - Headers: Parameter, Default value, Type, Description
  - First row sample: key | required | string | The key that is used to decrypt the obfuscated file.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Obfuscating import data](https://optics.ansys.com/hc/en-us/articles/**%20to%20be%20defined%20**)
- [Manipulating objects](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [importbinary](https://optics.ansys.com/hc/en-us/articles/360034408734-importbinary)

## Ansys-Related External Links Found

- None

## External Links Found

- None
