# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.py  
Area: Discovered official source  
Topic: Discovered from Basic FDTD Simulation - Lumerical style commands  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Basic FDTD Simulation - Lumerical style commands`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: command, fdtd, gaussian, import, lumapi, monitor, port, pylumerical, script, source.

## Key Terms

- command
- fdtd
- gaussian
- import
- lumapi
- monitor
- port
- pylumerical
- script
- source

## Captured Headings

- No headings extracted

## Official Text Excerpt

> # Basic FDTD Simulation - Lumerical style commands # A simple example to demonstrate using PyLumerical using Lumerical Script File (lsf) style commands. # Sets up and runs a basic FDTD simulation. E field results are plotted in Lumerical. # ## Prerequisites: # # Valid FDTD license is required. # # ### Perform required imports import ansys.lumerical.core as lumapi # ### Open an interactive session # + # Set hide = True to hide the Lumerical GUI. fdtd = lumapi.FDTD(hide=False) # - # # ### Set up simulation region fdtd.addfdtd() fdtd.set("x", 0) fdtd.set("x span", 8e-6) fdtd.set("y", 0) fdtd.set("y span", 8e-6) fdtd.set("z", 0.25e-6) fdtd.set("z span", 0.5e-6) # ### Set up source fdtd.addgaussian() fdtd.set("injection axis", "z") fdtd.set("direction", "forward") fdtd.set("x", 0) fdtd.set("x span", 16e-6) fdtd.set("y", 0) fdtd.set("y span", 16e-6) fdtd.set("z", 0.2e-6) fdtd.set("use scalar approximation", 1) fdtd.set("waist radius w0", 2e-6) fdtd.set("distance from waist", 0) fdtd.setglobalsource("wavelength start", 1e-6) fdtd.setglobalsource("wavelength stop", 1e-6) # ### Set up monitor fdtd.adddftmonitor() fdtd.set("monitor type", "2D Z-normal") fdtd.set("x", 0) fdtd.set("x span", 16e-6) fdtd.set("y", 0) fdtd.set("y span", 16e-6) fdtd.set("z", 0.3e-6) # ### Run and save simulation fdtd.save("fdtd_tutorial.fsp") fdtd.run() # ### Retrieve and ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- None

## Ansys-Related External Links Found

- None

## External Links Found

- None
