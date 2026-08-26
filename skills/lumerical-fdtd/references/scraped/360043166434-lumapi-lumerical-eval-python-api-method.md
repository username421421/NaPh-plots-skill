# lumapi – Lumerical.eval – Python API Method

Source URL: https://optics.ansys.com/hc/en-us/articles/360043166434-lumapi-Lumerical-eval-Python-API-Method  
Area: Discovered official source  
Topic: Discovered from Script Commands as Methods - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lumapi – Lumerical.eval – Python API Method` for the topic `Discovered from Script Commands as Methods - Python API`. It captured 1 heading(s), 2 link(s), 5 code block(s), 0 inline code term(s), and 1 table(s). Main headings: lumapi – Lumerical.eval – Python API Method. Key detected terms: command, lumapi, python, python-api, script.

## Key Terms

- command
- lumapi
- python
- python-api
- script

## Captured Headings

- lumapi – Lumerical.eval – Python API Method

## Official Text Excerpt

> lumapi – Lumerical.eval – Python API Method Evaluates the input string as Lumerical Scripting Language. This function is useful when you want to reduce the number of API calls for performance. For example, if you want to execute many commands in a loop, writing commands in Lumerical Scripting Language and executing it in a single call can improve performance. Syntax Parameters | Field | Type | Description | code | str | Evaluates the argument code as Lumerical Scripting Language. The input code must be a string, and should follow syntaxes of the Lumerical Scripting Language. Escape characters in the string is ignored. Returns None Examples Adds a rectangle to the current simulation. Adds a rectangle to the current simulation using f-strings. Adds a rectangle to the current simulation using a text file, “code.txt” from the current working directory containing the commands. This text file can be in .lsf format or any other format that can be read by Python and turned into a string. Contents of code.txt Python Driver Code See Also Python API overview – Ansys Optics, Lumerical ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `lumapi.eval(code)`
- Code block 2: 1 line(s); first line `fdtd = lumapi.FDTD()fdtd.eval(f"addrect;")`
- Code block 3: 1 line(s); first line `fdtd = lumapi.FDTD()code = "addrect;addcircle;"fdtd.eval(f"{code}\n")`
- Code block 4: 1 line(s); first line `addrect;addcircle;`
- Code block 5: 1 line(s); first line `fdtd = lumapi.FDTD()code = open("code.txt", "r").read()fdtd.eval(code)`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 3 column(s), 1 row(s)
  - Headers: Field, Type, Description
  - First row sample: code | str | Evaluates the argument code as Lumerical Scripting Language. The input code must be a string, and should follow syntaxes of the Lumerical Scripting Language. Escape characters in the string is ignored.

## Official Links Found

- [Python API overview – Ansys Optics](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)

## Ansys-Related External Links Found

- None

## External Links Found

- None
