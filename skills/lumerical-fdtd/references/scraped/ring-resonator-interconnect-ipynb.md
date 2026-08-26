# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/ring_resonator_interconnect/ring_resonator_interconnect.ipynb  
Area: Discovered official source  
Topic: Discovered from Simple Ring Resonator (INTERCONNECT)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Simple Ring Resonator (INTERCONNECT)`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: analysis, group, import, lumapi, mode, port, pylumerical, python, solver, source, transmission.

## Key Terms

- analysis
- group
- import
- lumapi
- mode
- port
- pylumerical
- python
- solver
- source
- transmission

## Captured Headings

- No headings extracted

## Official Text Excerpt

> { "cells": [ { "cell_type": "markdown", "id": "ac3edba8", "metadata": {}, "source": [ "# Simple Ring Resonator (INTERCONNECT)\n", "\n", "Getting started example for INTERCONNECT simulation with PyLumerical.\n", "Calculates the transmission spectrum of a ring resonator with 50 um radius.\n", "Prerequisites: Valid INTERCONNECT license is required." ] }, { "cell_type": "code", "execution_count": null, "id": "7cccddd8", "metadata": {}, "outputs": [], "source": [ "import matplotlib.pyplot as plt\n", "import numpy as np" ] }, { "cell_type": "code", "execution_count": null, "id": "055013ad", "metadata": {}, "outputs": [], "source": [ "import ansys.lumerical.core as lumapi" ] }, { "cell_type": "code", "execution_count": null, "id": "9f0268dd", "metadata": {}, "outputs": [], "source": [ "# Define ring properties\n", "radius = 50e-6 # in m\n", "coupling_coefficient = 0.05\n", "effective_index = 2.8\n", "group_index = 3.4\n", "loss = 300 # in dB/m\n", "\n", "# Define analysis properties\n", "center_frequency = 193.1e12 # in Hz\n", "frequency_range = 1e12 # in Hz\n", "num_points = 10000" ] }, { "cell_type": "code", "execution_count": null, "id": "ca2d1c4a", "metadata": {}, "outputs": [], "source": [ "# Build and run simulation in INTERCONNECT\n", "with lumapi.INTERCONNECT() as intc: # Open INTERCONNECT\n", " # Add circuit elements ...

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
