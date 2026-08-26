# Passing data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#passing-data)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html  
Area: PyLumerical  
Topic: Type conversions, copies between Python and Lumerical, getv, putv  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Passing data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#passing-data)` for the topic `Type conversions, copies between Python and Lumerical, getv, putv`. It captured 19 heading(s), 35 link(s), 6 code block(s), 11 inline code term(s), and 1 table(s). Main headings: Passing data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#passing-data), Python to Lumerical conversions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#python-to-lumerical-conversions), String [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#string), Real number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#real-number), Complex number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#complex-number), Numpy array [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#numpy-array), List [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#list), Dict [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#dict). Key detected terms: command, dataset, fdtd, import, mode, monitor, port, pylumerical, python, script, structure.

## Key Terms

- command
- dataset
- fdtd
- import
- mode
- monitor
- port
- pylumerical
- python
- script
- structure

## Captured Headings

- Passing data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#passing-data)
- Python to Lumerical conversions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#python-to-lumerical-conversions)
- String [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#string)
- Real number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#real-number)
- Complex number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#complex-number)
- Numpy array [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#numpy-array)
- List [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#list)
- Dict [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#dict)
- Other types [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#other-types)
- Lumerical to Python conversions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#lumerical-to-python-conversions)
- String [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id1)
- Real number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id2)
- Complex number [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id3)
- Matrix [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id4)
- Struct [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id5)
- Cell array [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id6)
- Explicit transfer functions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#explicit-transfer-functions)
- Transfer speed [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#transfer-speed)
- Best practices [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#best-practices)

## Official Text Excerpt

> Passing data # When driving Lumerical’s tools using PyLumerical, the Lumerical environment is connected with the Python environment, but they don’t share a workspace. Instead, PyLumerical passes variables between the Lumerical and Python environments as exact copies. During the transition, PyLumerical translates variables between Lumerical types and Python types. This article describes how PyLumerical translates basic data types between the Python environment and the Lumerical product, performance considerations, and best practices associated with it. For more information on how to work with datasets, which includes these basic data types and typically contain simulation results, see the article on Accessing simulation results. | Lumerical | Python | String | ``str | Real | ``float | Complex | ``numpy.ndarray | Matrix | ``numpy.ndarray | Cell array | ``list | Struct | ``dict | Dataset | ``dict Python to Lumerical conversions # When you send a variable from the Python workspace to Lumerical products, such as when setting parameters, or when using Lumerical scripting functions for further post processing, PyLumerical uses the following rules. String # String values passed from Python are directly ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 2: 1 line(s); first line `1Returned value is of type , length 1 with value [1.+1.j]`
- Code block 3: 7 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 4: 5 line(s); first line `1The type of the returned value is <class 'dict'>, the values within are:`
- Code block 5: 3 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 6: 7 line(s); first line `1The type of the returned value is <class 'list'>, the values within are:`

## Inline Code Inventory

- `ansys.lumerical.core.DEVICE`
- `ansys.lumerical.core.FDTD.eval()`
- `ansys.lumerical.core.FDTD.getv()`
- `ansys.lumerical.core.FDTD.putv()`
- `ansys.lumerical.core.INTERCONNECT`
- `ansys.lumerical.core.MODE`
- `dict`
- `float`
- `list`
- `numpy.ndarray`
- `str`

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - Headers: Lumerical, Python
  - First row sample: String | str

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#passing-data)
- [Accessing simulation results](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html)
- [Matrix](https://optics.ansys.com/hc/en-us/articles/360034929613-matrix-Script-command)
- [Cell array](https://optics.ansys.com/hc/en-us/articles/360034929913-cell-Script-command)
- [Struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [Dataset](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#python-to-lumerical-conversions)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#string)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#real-number)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#complex-number)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#numpy-array)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#list)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#dict)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#other-types)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#lumerical-to-python-conversions)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id1)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id2)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id3)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id4)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id5)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#id6)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#explicit-transfer-functions)
- [ansys.lumerical.core.FDTD.getv()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#ansys.lumerical.core.FDTD.getv)
- [ansys.lumerical.core.FDTD.putv()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#ansys.lumerical.core.FDTD.putv)
- [ansys.lumerical.core.MODE](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.html#ansys.lumerical.core.MODE)
- [ansys.lumerical.core.DEVICE](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.DEVICE.html#ansys.lumerical.core.DEVICE)
- [ansys.lumerical.core.INTERCONNECT](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.INTERCONNECT.html#ansys.lumerical.core.INTERCONNECT)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#transfer-speed)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#best-practices)
- [ansys.lumerical.core.FDTD.eval()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.eval.html#ansys.lumerical.core.FDTD.eval)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [float](https://docs.python.org/3/library/functions.html#float)
- [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
