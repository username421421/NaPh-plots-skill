# putv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#putv)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html  
Area: Discovered official source  
Topic: Discovered from PyLumerical passing data  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `putv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#putv)` for the topic `Discovered from PyLumerical passing data`. It captured 1 heading(s), 8 link(s), 2 code block(s), 5 inline code term(s), and 0 table(s). Main headings: putv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#putv). Key detected terms: dataset, fdtd, lumapi, port, python, script.

## Key Terms

- dataset
- fdtd
- lumapi
- port
- python
- script

## Captured Headings

- putv [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#putv)

## Official Text Excerpt

> putv # FDTD. putv (varname, value) # Low level script workspace method that puts a variable from the local Python environment into an active Lumerical session. This method is a low level method that interacts directly with the script workspace in Lumerical. It is not recommended to use this unless a specific function needs to be achieved. Parameters: varname``str The name of the variable to retrieve from the Lumerical session. value``any The value to put into the Lumerical session. The type depends on the type of variable in Python. See the “See also” section below for more details on supported data types and how they are handled. Returns:``None Raises:`LumApiError` If the method cannot retrieve the variable or the data type is unsupported. See also ``getv() Gets a variable from the Lumerical session. Passing data Information on how passing non-dataset variables are handled. Accessing simulation results Information on how passing datasets are handled. Examples Putting a string from Python to Lumerical, then retrieving it and printing its type. Returns

## Code Block Inventory

- Code block 1: 4 line(s); first line `>>> with lumapi.FDTD(hide = True) as fdtd:`
- Code block 2: 1 line(s); first line `>>> <class 'str'> Ansys Inc`

## Inline Code Inventory

- `LumApiError`
- `None`
- `any`
- `getv()`
- `str`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#putv)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.putv.html#ansys.lumerical.core.FDTD.putv)
- [getv()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.getv.html#ansys.lumerical.core.FDTD.getv)
- [Passing data](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html#ref-passing-data)
- [Accessing simulation results](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#ref-accessing-simulation-results)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [any](https://docs.python.org/3/library/functions.html#any)
- [None](https://docs.python.org/3/library/constants.html#None)
