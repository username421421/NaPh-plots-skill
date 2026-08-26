# lumapi – Lumerical.putv - Python API method

Source URL: https://optics.ansys.com/hc/en-us/articles/39748892700435-lumapi-Lumerical-putv-Python-API-method  
Area: Discovered official source  
Topic: Discovered from Passing Data - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lumapi – Lumerical.putv - Python API method` for the topic `Discovered from Passing Data - Python API`. It captured 1 heading(s), 14 link(s), 3 code block(s), 0 inline code term(s), and 2 table(s). Main headings: lumapi – Lumerical.putv - Python API method. Key detected terms: dataset, lumapi, port, python, python-api, script.

## Key Terms

- dataset
- lumapi
- port
- python
- python-api
- script

## Captured Headings

- lumapi – Lumerical.putv - Python API method

## Official Text Excerpt

> lumapi – Lumerical.putv - Python API method Puts a variable from the local Python environment into an active Lumerical session via the Python API. Syntax Parameters | Field | Type | Description | varname | str | Desired name of the variable to be put into the Lumerical scripting workspace. Note that certain reserved constants cannot be used. | value | / | Python variable to put be put into the Lumerical scripting workspace. See below on how different types of variables are converted. Only the variable types listed below are supported, any other types will result in an error Returns None Variable Translation A quick reference guide for translated datatypes is shown in the table below, see the Knowledge Base article on Passing Data for more information on how types are converted. |Lumerical|Python |String|str |Real|float |Complex|np.array |Matrix|np.array |Cell array|list |Struct|dict |Dataset|dict Example Putting a string from Python to Lumerical, then retrieving it and printing its type. Returns See Also Python API overview, Lumerical Python API Reference, Passing Data – Python API

## Code Block Inventory

- Code block 1: 1 line(s); first line `lumapi.putv(varname, value)`
- Code block 2: 4 line(s); first line `with lumapi.FDTD(hide = True) as fdtd:`
- Code block 3: 1 line(s); first line `<class 'str'> Lumerical Inc`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 3 column(s), 2 row(s)
  - Headers: Field, Type, Description
  - First row sample: varname | str | Desired name of the variable to be put into the Lumerical scripting workspace. Note that certain reserved constants cannot be used.
- Table 2: 2 column(s), 8 row(s)
  - First row sample: Lumerical | Python

## Official Links Found

- [constants](https://optics.ansys.com/hc/en-us/articles/360034929833-Pre-defined-constants-in-Lumericals-scripting-environment)
- [Passing Data](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API)
- [Matrix](https://optics.ansys.com/hc/en-us/articles/360034929613-matrix-Script-command)
- [Cell array](https://optics.ansys.com/hc/en-us/articles/360034929913-cell-Script-command)
- [Struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [Dataset](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [Python API overview,](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [Passing Data – Python API](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [float](https://docs.python.org/3/library/functions.html#float)
- [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
