# Simple Waveguide (MODE FDE) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Simple-Waveguide-(MODE-FDE))

Source URL: https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html  
Area: PyLumerical  
Topic: MODE workflow useful for mode-source and waveguide context  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Simple Waveguide (MODE FDE) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Simple-Waveguide-(MODE-FDE))` for the topic `MODE workflow useful for mode-source and waveguide context`. It captured 3 heading(s), 6 link(s), 22 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Simple Waveguide (MODE FDE) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Simple-Waveguide-(MODE-FDE)), Part 1: Set up structures and simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-1:-Set-up-structures-and-simulation-objects), Part 2: Calculate the supported modes of the waveguide [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-2:-Calculate-the-supported-modes-of-the-waveguide). Key detected terms: analysis, import, mode, port, python, script, solver, structure.

## Key Terms

- analysis
- import
- mode
- port
- python
- script
- solver
- structure

## Captured Headings

- Simple Waveguide (MODE FDE) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Simple-Waveguide-(MODE-FDE))
- Part 1: Set up structures and simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-1:-Set-up-structures-and-simulation-objects)
- Part 2: Calculate the supported modes of the waveguide [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-2:-Calculate-the-supported-modes-of-the-waveguide)

## Official Text Excerpt

> Download Jupyter Notebook (.ipynb) Download Python script (.py) Simple Waveguide (MODE FDE) #) A simple example using MODE. Waveguide (FDE): https://optics.ansys.com/hc/en-us/articles/360042800453-Waveguide-FDE The Finite Difference Eigenmode (FDE) solver in MODE is used to characterize a straight waveguide. In Part 1, we build the structure and set the FDE simulation region. In Part 2, we calculate the supported mode profiles of the waveguide. Prerequisites: Valid MODE license is required. Perform required imports Part 1: Set up structures and simulation objects # Part 2: Calculate the supported modes of the waveguide # The analysis_props are equivalent to the settings in the Eigensolver Analysis window in the GUI.

## Code Block Inventory

- Code block 1: 1 line(s); first line `[ ]:`
- Code block 2: 1 line(s); first line `1from collections import OrderedDict`
- Code block 3: 1 line(s); first line `[ ]:`
- Code block 4: 2 line(s); first line `2import matplotlib.pyplot as plt`
- Code block 5: 1 line(s); first line `[ ]:`
- Code block 6: 1 line(s); first line `4import ansys.lumerical.core as lumapi`
- Code block 7: 1 line(s); first line `[ ]:`
- Code block 8: 27 line(s); first line `5# Set hide = True to hide the Lumerical GUI.`
- Code block 9: 1 line(s); first line `[ ]:`
- Code block 10: 17 line(s); first line `32# Build waveguide`
- Code block 11: 1 line(s); first line `[ ]:`
- Code block 12: 3 line(s); first line `49# Add FDE solver region`
- Code block 13: 1 line(s); first line `[ ]:`
- Code block 14: 13 line(s); first line `52# Add mesh override region`
- Code block 15: 1 line(s); first line `[ ]:`
- Code block 16: 4 line(s); first line `65mode.setanalysis("wavelength", wavelength)`
- Code block 17: 1 line(s); first line `[ ]:`
- Code block 18: 1 line(s); first line `69mode.findmodes()`
- Code block 19: 1 line(s); first line `[ ]:`
- Code block 20: 7 line(s); first line `70# Select and plot the fundamental mode`
- Code block 21: 1 line(s); first line `[ ]:`
- Code block 22: 10 line(s); first line `77# Plot in Python - requires matplotlib`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [Download Jupyter Notebook (.ipynb)](https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.ipynb)
- [Download Python script (.py)](https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Simple-Waveguide-(MODE-FDE))
- [https://optics.ansys.com/hc/en-us/articles/360042800453-Waveguide-FDE](https://optics.ansys.com/hc/en-us/articles/360042800453-Waveguide-FDE)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-1:-Set-up-structures-and-simulation-objects)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html#Part-2:-Calculate-the-supported-modes-of-the-waveguide)

## Ansys-Related External Links Found

- None

## External Links Found

- None
