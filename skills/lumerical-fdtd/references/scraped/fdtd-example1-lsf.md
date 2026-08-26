# Basic FDTD Simulation - Lumerical style commands [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Basic-FDTD-Simulation---Lumerical-style-commands)

Source URL: https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html  
Area: PyLumerical  
Topic: FDTD setup using command-style PyLumerical calls  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Basic FDTD Simulation - Lumerical style commands [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Basic-FDTD-Simulation---Lumerical-style-commands)` for the topic `FDTD setup using command-style PyLumerical calls`. It captured 10 heading(s), 12 link(s), 16 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Basic FDTD Simulation - Lumerical style commands [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Basic-FDTD-Simulation---Lumerical-style-commands), Prerequisites: [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Prerequisites:), Perform required imports [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Perform-required-imports), Open an interactive session [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Open-an-interactive-session), Set up simulation region [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-simulation-region), Set up source [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-source), Set up monitor [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-monitor), Run and save simulation [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Run-and-save-simulation). Key detected terms: command, fdtd, import, monitor, port, pylumerical, python, script, source.

## Key Terms

- command
- fdtd
- import
- monitor
- port
- pylumerical
- python
- script
- source

## Captured Headings

- Basic FDTD Simulation - Lumerical style commands [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Basic-FDTD-Simulation---Lumerical-style-commands)
- Prerequisites: [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Prerequisites:)
- Perform required imports [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Perform-required-imports)
- Open an interactive session [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Open-an-interactive-session)
- Set up simulation region [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-simulation-region)
- Set up source [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-source)
- Set up monitor [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-monitor)
- Run and save simulation [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Run-and-save-simulation)
- Retrieve and plot results [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Retrieve-and-plot-results)
- Keep session open until user clicks space bar [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Keep-session-open-until-user-clicks-space-bar)

## Official Text Excerpt

> Download Jupyter Notebook (.ipynb) Download Python script (.py) Basic FDTD Simulation - Lumerical style commands # A simple example to demonstrate using PyLumerical using Lumerical Script File (lsf) style commands. Sets up and runs a basic FDTD simulation. E field results are plotted in Lumerical. Prerequisites: # Valid FDTD license is required. Perform required imports # Open an interactive session # Set up simulation region # Set up source # Set up monitor # Run and save simulation # Retrieve and plot results # Keep session open until user clicks space bar #

## Code Block Inventory

- Code block 1: 1 line(s); first line `[ ]:`
- Code block 2: 1 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 3: 1 line(s); first line `[ ]:`
- Code block 4: 2 line(s); first line `2# Set hide = True to hide the Lumerical GUI.`
- Code block 5: 1 line(s); first line `[ ]:`
- Code block 6: 7 line(s); first line `4fdtd.addfdtd()`
- Code block 7: 1 line(s); first line `[ ]:`
- Code block 8: 13 line(s); first line `11fdtd.addgaussian()`
- Code block 9: 1 line(s); first line `[ ]:`
- Code block 10: 7 line(s); first line `24fdtd.adddftmonitor()`
- Code block 11: 1 line(s); first line `[ ]:`
- Code block 12: 2 line(s); first line `31fdtd.save("fdtd_tutorial.fsp")`
- Code block 13: 1 line(s); first line `[ ]:`
- Code block 14: 2 line(s); first line `33E = fdtd.getresult("monitor", "E")`
- Code block 15: 1 line(s); first line `[ ]:`
- Code block 16: 2 line(s); first line `35fdtd.print("Example complete. Hit space bar to close.")`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [Download Jupyter Notebook (.ipynb)](https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.ipynb)
- [Download Python script (.py)](https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Basic-FDTD-Simulation---Lumerical-style-commands)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Prerequisites:)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Perform-required-imports)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Open-an-interactive-session)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-simulation-region)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-source)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Set-up-monitor)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Run-and-save-simulation)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Retrieve-and-plot-results)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.html#Keep-session-open-until-user-clicks-space-bar)

## Ansys-Related External Links Found

- None

## External Links Found

- None
