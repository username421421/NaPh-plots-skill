# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.py  
Area: Discovered official source  
Topic: Discovered from Simple Waveguide (MODE FDE)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Simple Waveguide (MODE FDE)`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: analysis, import, lumapi, material, mesh, mode, monitor, port, python, solver, structure.

## Key Terms

- analysis
- import
- lumapi
- material
- mesh
- mode
- monitor
- port
- python
- solver
- structure

## Captured Headings

- No headings extracted

## Official Text Excerpt

> # Simple Waveguide (MODE FDE) # # A simple example using MODE. # Waveguide (FDE): https://optics.ansys.com/hc/en-us/articles/360042800453-Waveguide-FDE # # The Finite Difference Eigenmode (FDE) solver in MODE is used to characterize a straight waveguide. # # In Part 1, we build the structure and set the FDE simulation region. # In Part 2, we calculate the supported mode profiles of the waveguide. # # Prerequisites: # Valid MODE license is required. # Perform required imports from collections import OrderedDict import matplotlib.pyplot as plt import numpy as np import ansys.lumerical.core as lumapi # ## Part 1: Set up structures and simulation objects # + # Set hide = True to hide the Lumerical GUI. mode = lumapi.MODE(hide=False) # Set key parameters wavelength = 1.55e-6 # Center wavelength # Set the waveguide cross-section and material wg_width = 0.5e-6 wg_height = 0.22e-6 wg_material = "Si (Silicon) - Palik" # Set substrate and cladding cross-section and material sub_width = 10e-6 sub_height = 5e-6 sub_material = "SiO2 (Glass) - Palik" clad_width = 10e-6 clad_height = 5e-6 clad_material = "SiO2 (Glass) - Palik" # Set FDE region ...

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
