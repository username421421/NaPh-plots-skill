# getv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#getv)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html  
Area: Discovered official source  
Topic: Discovered from PyLumerical passing data  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#getv)` for the topic `Discovered from PyLumerical passing data`. It captured 1 heading(s), 15 link(s), 2 code block(s), 7 inline code term(s), and 0 table(s). Main headings: getv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#getv). Key detected terms: dataset, fdtd, python, script.

## Key Terms

- dataset
- fdtd
- python
- script

## Captured Headings

- getv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#getv)

## Official Text Excerpt

> getv # FDTD. getv (varname) # Low level script workspace method that gets a variable from the Lumerical session. The variable can be a string, real/complex numbers, matrix, cell or struct. This method is a low level method that interacts directly with the script workspace in Lumerical. It is not recommended to use this unless a specific function needs to be achieved. Parameters: varname``str Lumerical variable name of the variable to obtain. Returns:``any Retrieved Python variable, the type depends on the type of variable in Lumerical. - ``str for strings in Lumerical - ``float for real numbers in Lumerical - ``numpy.ndarray for complex numbers in Lumerical - ``numpy.ndarray for matrices in Lumerical - ``list for cell arrays in Lumerical - ``dict for structs in Lumerical - ``dict for datasets in Lumerical See also ``putv() Puts a variable from the local Python environment into an active Lumerical session. Passing data Information on how passing non-dataset variables are handled. Accessing simulation results Information on how passing datasets are handled. Examples Putting a string from Python to Lumerical, then retrieving it and printing ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `>>> with lumapi.FDTD(hide = True) as fdtd:`
- Code block 2: 1 line(s); first line `>>> <class 'str'> Ansys Inc`

## Inline Code Inventory

- `any`
- `dict`
- `float`
- `list`
- `numpy.ndarray`
- `putv()`
- `str`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#getv)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#ansys.lumerical.core.FDTD.getv)
- [matrices](https://optics.ansys.com/hc/en-us/articles/360034929613-matrix-Script-command)
- [cell arrays](https://optics.ansys.com/hc/en-us/articles/360034929913-cell-Script-command)
- [structs](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [putv()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#ansys.lumerical.core.FDTD.putv)
- [Passing data](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#ref-passing-data)
- [Accessing simulation results](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#ref-accessing-simulation-results)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [any](https://docs.python.org/3/library/functions.html#any)
- [float](https://docs.python.org/3/library/functions.html#float)
- [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
