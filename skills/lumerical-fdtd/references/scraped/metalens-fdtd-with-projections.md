# PyLumerical Metalens (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html#PyLumerical-Metalens-(FDTD))

Source URL: https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html  
Area: PyLumerical  
Topic: RCWA to FDTD metalens workflow, symmetry, far-field projection  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `PyLumerical Metalens (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html#PyLumerical-Metalens-(FDTD))` for the topic `RCWA to FDTD metalens workflow, symmetry, far-field projection`. It captured 1 heading(s), 4 link(s), 46 code block(s), 0 inline code term(s), and 0 table(s). Main headings: PyLumerical Metalens (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html#PyLumerical-Metalens-(FDTD)). Key detected terms: boundary, fdtd, geometry, group, import, monitor, optimization, periodic, port, pylumerical, python, script, solver, structure, sweep.

## Key Terms

- boundary
- fdtd
- geometry
- group
- import
- monitor
- optimization
- periodic
- port
- pylumerical
- python
- script
- solver
- structure
- sweep

## Captured Headings

- PyLumerical Metalens (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html#PyLumerical-Metalens-(FDTD))

## Official Text Excerpt

> Download Jupyter Notebook (.ipynb) Download Python script (.py) PyLumerical Metalens (FDTD) #) This example automates design and simulation of a metalens using Ansys Lumerical FDTD. A metalens is an array of pillars, also called unit cells or meta-atoms, that are arranged across a surface to create a macroscopic optical element. Each unit cell locally adjusts the phase of the light, and by arranging the unit cells across the surface, a global phase profile can be achieved. Typically, this phase profile is designed to act as a lens. In this example, we use Python to automate metalens design and simulation. We follow a standard approach of separately designing a target phase profile and a suitable library of unit cells under periodic boundary conditions. A target phase profile at a specific design wavelength must be provided; this can come from theory or an optimized phase profile from Zemax or another design process can be imported. The unit cell library is designed and simulated in Lumerical RCWA. Once the target phase profile and unit cell library are determined, we loop through each location ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `[ ]:`
- Code block 2: 8 line(s); first line `1# Import required modules`
- Code block 3: 1 line(s); first line `[ ]:`
- Code block 4: 10 line(s); first line `9# Global design parameters`
- Code block 5: 1 line(s); first line `[ ]:`
- Code block 6: 15 line(s); first line `19# Unit cell specifications`
- Code block 7: 1 line(s); first line `[ ]:`
- Code block 8: 17 line(s); first line `34# Target phase profile specifications`
- Code block 9: 1 line(s); first line `[ ]:`
- Code block 10: 44 line(s); first line `51# Define functions to generate target phase`
- Code block 11: 1 line(s); first line `[ ]:`
- Code block 12: 10 line(s); first line `95# Create phase mask grid`
- Code block 13: 1 line(s); first line `[ ]:`
- Code block 14: 22 line(s); first line `105# Calculate and plot phase mask`
- Code block 15: 1 line(s); first line `[ ]:`
- Code block 16: 83 line(s); first line `127# create a single RCWA unit cell simulation`
- Code block 17: 1 line(s); first line `[ ]:`
- Code block 18: 6 line(s); first line `210# Test the above function - run a single rcwa simulation and print results`
- Code block 19: 1 line(s); first line `[ ]:`
- Code block 20: 21 line(s); first line `216# Now run a sweep over a range of pillar widths`
- Code block 21: 1 line(s); first line `[ ]:`
- Code block 22: 14 line(s); first line `237# Plot results`
- Code block 23: 1 line(s); first line `[ ]:`
- Code block 24: 13 line(s); first line `251# Phase vs. radius table to use for mapping`
- Code block 25: 1 line(s); first line `[ ]:`
- Code block 26: 9 line(s); first line `264# Plot the design`
- Code block 27: 1 line(s); first line `[ ]:`
- Code block 28: 5 line(s); first line `273# Set options`
- Code block 29: 1 line(s); first line `[ ]:`
- Code block 30: 133 line(s); first line `278# Initialize session and build simulation objects.`
- Code block 31: 1 line(s); first line `[ ]:`
- Code block 32: 16 line(s); first line `411# Memory check`
- Code block 33: 1 line(s); first line `[ ]:`
- Code block 34: 11 line(s); first line `427# Configure resources and run simulations`
- Code block 35: 1 line(s); first line `[ ]:`
- Code block 36: 11 line(s); first line `438with lumapi.FDTD(full_lens_filename, hide=False) as fdtd:`
- Code block 37: 1 line(s); first line `[ ]:`
- Code block 38: 28 line(s); first line `449# Retrieve and plot results from monitors`
- Code block 39: 1 line(s); first line `[ ]:`
- Code block 40: 15 line(s); first line `477# Plot far-field projections out to the focal point`
- Code block 41: 1 line(s); first line `[ ]:`
- Code block 42: 9 line(s); first line `492proj_Ex, proj_Ey, proj_Ez = proj[0, 0, :, 0], proj[0, 0, :, 1], proj[0, 0, :, 2]`
- Code block 43: 1 line(s); first line `[ ]:`
- Code block 44: 12 line(s); first line `501# Now, plot a cross-sectional image of the xz plane`
- Code block 45: 1 line(s); first line `[ ]:`
- Code block 46: 11 line(s); first line `513proj_Ex, proj_Ey, proj_Ez = proj_image[:, 0, :, 0], proj_image[:, 0, :, 1], proj_image[:, 0, :, 2]`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [Download Jupyter Notebook (.ipynb)](https://lumerical.docs.pyansys.com/version/0.3/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.ipynb)
- [Download Python script (.py)](https://lumerical.docs.pyansys.com/version/0.3/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Multiple_Solver_Workflows/metalens_FDTD_with_projections/metalens_FDTD_with_projections.html#PyLumerical-Metalens-(FDTD))
- [https://optics.ansys.com/hc/en-us/articles/23889799301523-Assembly-Groups-Simulation-Objects](https://optics.ansys.com/hc/en-us/articles/23889799301523-Assembly-Groups-Simulation-Objects)

## Ansys-Related External Links Found

- None

## External Links Found

- None
