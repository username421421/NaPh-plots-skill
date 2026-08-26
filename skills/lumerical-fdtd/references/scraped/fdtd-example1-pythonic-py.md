# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.py  
Area: Discovered official source  
Topic: Discovered from Basic FDTD Simulation - Python style commands  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Basic FDTD Simulation - Python style commands`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: command, fdtd, gaussian, import, lumapi, monitor, port, pylumerical, python, source.

## Key Terms

- command
- fdtd
- gaussian
- import
- lumapi
- monitor
- port
- pylumerical
- python
- source

## Captured Headings

- No headings extracted

## Official Text Excerpt

> # Basic FDTD Simulation - Python style commands # # A simple example to demonstrate using PyLumerical. # # Sets up and runs a basic FDTD simulation. E field results are plotted using Matplotlib # Demonstrates initializing objects using keyword arguments and OrderedDict. # ## Prerequisites: # # Valid FDTD license is required. # # ### Perform required imports # + from collections import OrderedDict import matplotlib.pyplot as plt import ansys.lumerical.core as lumapi # - # ### Open interactive session with the "with" context manager, run session, retrieve and plots results, and close session # Set hide = True to hide the Lumerical GUI. with lumapi.FDTD() as fdtd: # Set up simulation region using keyword arguments fdtd.addfdtd(x=0, x_span=8e-6, y=0, y_span=8e-6, z=0.25e-6, z_span=0.5e-6) # Set up source using Python OrderedDict # OrderedDict is recommended when order is important # Here, the scalar appproximation prop should be set before waist radius props = OrderedDict( [ ("injection axis", "z"), ("direction", "forward"), ("x", 0), ("x span", 16e-6), ("y", 0), ("y span", 16e-6), ("z", 0.2e-6), ("use scalar approximation", 1), ("waist radius w0", 2e-6), ("distance from ...

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
