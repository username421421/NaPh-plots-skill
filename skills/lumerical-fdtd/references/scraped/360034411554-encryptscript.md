# encryptscript - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034411554-encryptscript  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `encryptscript - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 2 heading(s), 8 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: encryptscript - Script command, Example. Key detected terms: command, fdtd, mode, script.

## Key Terms

- command
- fdtd
- mode
- script

## Captured Headings

- encryptscript - Script command
- Example

## Official Text Excerpt

> encryptscript - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Save a copy of the specified script file in an encrypted format. The new file will have a .lsfx file extension. Encrypting a script allows a script to be shared with others, without allowing them to see the contents of the script. | Syntax | Description | encryptscript("filename.lsf"); | Recommended: Encrypt a copy of the script, not compatible with earlier versions. The new file will be named "filename.lsfx". | encryptscript("filename.lsf", 1); | Legacy: Encrypt a copy of the script, compatible with earlier versions. | encryptscript("filename.lsf", "new_filename"); | Specify an alternate file name, not compatible with earlier versions. The new file will be named "filename.lsfx". | encryptscript("filename.lsf", "new_filename", 1); | Specify an alternate file name, compatible with earlier versions. The new file will be named "filename.lsfx". Scripts encrypted with 2020B will not be compatible with 2020A and earlier, unless the additional argument (1) is passed to encryptscript specifying legacy compatibility. Scripts encrypted with 2020A and earlier will continue to be compatible with later versions. Example If the script file is ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `filename # it will run the encrypted script file filename.lsfx`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Syntax, Description
  - First row sample: encryptscript("filename.lsf"); | Recommended: Encrypt a copy of the script, not compatible with earlier versions. The new file will be named "filename.lsfx".

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
