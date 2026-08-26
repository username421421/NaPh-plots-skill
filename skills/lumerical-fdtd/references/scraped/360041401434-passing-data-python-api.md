# Passing Data - Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API  
Area: Python API  
Topic: Python/Lumerical type conversion, getv, putv, performance  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Passing Data - Python API` for the topic `Python/Lumerical type conversion, getv, putv, performance`. It captured 19 heading(s), 18 link(s), 6 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Passing Data - Python API, Python to Lumerical Conversions, String, Real Number, Complex Number, Numpy Array, List, Dict. Key detected terms: command, dataset, import, monitor, port, python, python-api, script, structure.

## Key Terms

- command
- dataset
- import
- monitor
- port
- python
- python-api
- script
- structure

## Captured Headings

- Passing Data - Python API
- Python to Lumerical Conversions
- String
- Real Number
- Complex Number
- Numpy Array
- List
- Dict
- Other Types
- Lumerical to Python Conversions
- String
- Real Number
- Complex Number
- Matrix
- Struct
- Cell Array
- Explicit Transfer Functions
- Transfer Speed
- Best Practices

## Official Text Excerpt

> Passing Data - Python API Automation API When driving Lumerical's tools from the Python API, a connection is established between the environments, but they do not share a workspace. Instead, as variables are passed back and forth as exact copies. When variables are passed back and forth, they are also translated between Lumerical types and Python types. This article describes how basic datatypes are translated between the Python environment and the Lumerical product, performance considerations, and best practices associated with it. For more information on how to work with datasets, which are composed of these basic datatypes, and are typically used for processing of simulation results and handling of Lumerical datasets, see the Knowledge Base article on Accessing Simulation Results in Python API. | Lumerical | Python |String| str |Real|float |Complex|np.array |Matrix|np.array |Cell array|list |Struct|dict |Dataset|dict Python to Lumerical Conversions When a variable is sent from the Python workspace to Lumerical products, such as when setting parameters, or when using Lumerical scripting functions for further post processing, the following rules are followed. String String values passed from Python are directly ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 2: 1 line(s); first line `Returned value is of type , length 1 with value [1.+1.j]`
- Code block 3: 7 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 4: 1 line(s); first line `The type of the returned value is <class 'dict'>, the values within are: Field - complex value, Value - [[1.+1.j]], Type - <class 'numpy.ndarray'>Field - matrix`
- Code block 5: 3 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 6: 1 line(s); first line `The type of the returned value is <class 'list'>, the values within are:Value - Hello World, Type - <class 'str'>Value - [[0. 0.] [0. 0.]], Type - <class 'numpy`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - Headers: Lumerical, Python
  - First row sample: String | str

## Official Links Found

- [Automation API](https://optics.ansys.com/hc/en-us/articles/360037824513)
- [Accessing Simulation Results](https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API)
- [Matrix](https://optics.ansys.com/hc/en-us/articles/360034929613-matrix-Script-command)
- [Cell array](https://optics.ansys.com/hc/en-us/articles/360034929913-cell-Script-command)
- [Struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [Dataset](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [getv()](https://optics.ansys.com/hc/en-us/articles/39748719848211-lumapi-Lumerical-getv-Python-API-method)
- [putv()](https://optics.ansys.com/hc/en-us/articles/39748892700435-lumapi-Lumerical-putv-Python-API-method)
- [Python API Overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Working with Simulation Objects – Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods – Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [Installation and Getting Started – Python API](https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API)
- [Accessing Simulation Results – Python API](https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [float](https://docs.python.org/3/library/functions.html#float)
- [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
