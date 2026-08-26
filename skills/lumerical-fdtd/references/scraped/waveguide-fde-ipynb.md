# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.ipynb  
Area: Discovered official source  
Topic: Discovered from Simple Waveguide (MODE FDE)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Simple Waveguide (MODE FDE)`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: analysis, import, lumapi, material, mesh, mode, monitor, port, python, solver, source, structure.

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
- source
- structure

## Captured Headings

- No headings extracted

## Official Text Excerpt

> { "cells": [ { "cell_type": "markdown", "id": "9d30113e", "metadata": {}, "source": [ "# Simple Waveguide (MODE FDE)\n", "\n", "A simple example using MODE.\n", "Waveguide (FDE): https://optics.ansys.com/hc/en-us/articles/360042800453-Waveguide-FDE\n", "\n", "The Finite Difference Eigenmode (FDE) solver in MODE is used to characterize a straight waveguide.\n", "\n", "In Part 1, we build the structure and set the FDE simulation region.\n", "In Part 2, we calculate the supported mode profiles of the waveguide.\n", "\n", "Prerequisites:\n", "Valid MODE license is required." ] }, { "cell_type": "markdown", "id": "c26dd155", "metadata": {}, "source": [ "Perform required imports" ] }, { "cell_type": "code", "execution_count": null, "id": "3aa85971", "metadata": {}, "outputs": [], "source": [ "from collections import OrderedDict" ] }, { "cell_type": "code", "execution_count": null, "id": "6de779cf", "metadata": {}, "outputs": [], "source": [ "import matplotlib.pyplot as plt\n", "import numpy as np" ] }, { "cell_type": "code", "execution_count": null, "id": "013fe0f2", "metadata": {}, "outputs": [], "source": [ "import ansys.lumerical.core as lumapi" ] }, { "cell_type": "markdown", "id": "d474dd43", "metadata": {}, "source": [ "## Part 1: Set up structures and simulation objects" ] }, { "cell_type": "code", "execution_count": null, "id": "c020c2b7", "metadata": ...

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
