# eval [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#eval)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html  
Area: Discovered official source  
Topic: Discovered from PyLumerical script commands as methods  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `eval [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#eval)` for the topic `Discovered from PyLumerical script commands as methods`. It captured 1 heading(s), 5 link(s), 4 code block(s), 2 inline code term(s), and 0 table(s). Main headings: eval [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#eval). Key detected terms: command, mode, python, script.

## Key Terms

- command
- mode
- python
- script

## Captured Headings

- eval [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#eval)

## Official Text Excerpt

> eval # MODE. eval (code) # Low level script workspace method that evaluates the input string as Lumerical Scripting Language. This method is a low level method that interacts directly with the script workspace in Lumerical. It is not recommended to use this unless a specific function needs to be achieved. This function is useful when you want to reduce the number of API calls for performance. For example, if you want to execute many commands in a loop, writing commands in Lumerical Scripting Language and executing it in a single call can improve performance. Parameters: code``str Evaluates the argument code as Lumerical Scripting Language. The input code must be a string, and should follow syntaxes of the Lumerical Scripting Language. The method ignores characters in the string. Returns:``None Examples Adds a rectangle to the current simulation. Adds a rectangle to the current simulation using f-strings. Adds a rectangle to the current simulation using a text file, “code.txt” from the current working directory containing the commands. This text file can be in .lsf format or any other format that can ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `>>> fdtd = lumapi.FDTD()`
- Code block 2: 3 line(s); first line `>>> fdtd = lumapi.FDTD()`
- Code block 3: 2 line(s); first line `>>> addrect;`
- Code block 4: 3 line(s); first line `>>> fdtd = lumapi.FDTD()`

## Inline Code Inventory

- `None`
- `str`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#eval)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#ansys.lumerical.core.MODE.eval)
- [Lumerical Scripting Language](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
