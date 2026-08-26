# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.ipynb  
Area: Discovered official source  
Topic: Discovered from Photonic Crystal Bandstructure (FDTD)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Photonic Crystal Bandstructure (FDTD)`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: analysis, bloch, boundary, dipole, fdtd, geometry, group, import, lumapi, material, mesh, mode, monitor, normalization, port, python.

## Key Terms

- analysis
- bloch
- boundary
- dipole
- fdtd
- geometry
- group
- import
- lumapi
- material
- mesh
- mode
- monitor
- normalization
- port
- python
- solver
- source
- structure
- sweep

## Captured Headings

- No headings extracted

## Official Text Excerpt

> { "cells": [ { "cell_type": "markdown", "id": "77722cb5", "metadata": {}, "source": [ "# Photonic Crystal Bandstructure (FDTD)\n", "\n", "This example demonstrates a photonic crystal simulation utilizing Structure and Analysis Group objects.\n", "Based on: https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure\n", "\n", "\n", "In Part 1, we build the structure and set the FDTD simulation region.\n", "In this case, the spheres are holes (filled with air, n = 1) and the background material is a simple dielectric material.\n", "Some advanced simulation objects, including the dipole cloud source and bandstructure analysis groups, are imported from the Object Library.\n", "We run a single simulation and visualize the resulting spectrum.\n", "\n", "In Part 2, we set up a series of sweeps to collect the resonant frequencies.\n", "In this example, we use the built-in sweep tool in Lumerical, but the parameter sweeps could also be set up from Python.\n", "We then run the sweeps and plot the results.\n", "\n", "Prerequisites: Valid FDTD license is required." ] }, { "cell_type": "markdown", "id": "93de611c", "metadata": {}, "source": [ "Perform required imports" ] }, { "cell_type": "code", "execution_count": null, "id": "78e1e502", "metadata": {}, "outputs": ...

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
