# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/ring_resonator_interconnect/ring_resonator_interconnect.py  
Area: Discovered official source  
Topic: Discovered from Simple Ring Resonator (INTERCONNECT)  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Simple Ring Resonator (INTERCONNECT)`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: analysis, group, import, lumapi, mode, port, pylumerical, solver, transmission.

## Key Terms

- analysis
- group
- import
- lumapi
- mode
- port
- pylumerical
- solver
- transmission

## Captured Headings

- No headings extracted

## Official Text Excerpt

> # Simple Ring Resonator (INTERCONNECT) # # Getting started example for INTERCONNECT simulation with PyLumerical. # Calculates the transmission spectrum of a ring resonator with 50 um radius. # Prerequisites: Valid INTERCONNECT license is required. import matplotlib.pyplot as plt import numpy as np import ansys.lumerical.core as lumapi # + # Define ring properties radius = 50e-6 # in m coupling_coefficient = 0.05 effective_index = 2.8 group_index = 3.4 loss = 300 # in dB/m # Define analysis properties center_frequency = 193.1e12 # in Hz frequency_range = 1e12 # in Hz num_points = 10000 # - # Build and run simulation in INTERCONNECT with lumapi.INTERCONNECT() as intc: # Open INTERCONNECT # Add circuit elements and set properties intc.addelement("Waveguide Coupler", {"name": "Add Coupler", "coupling coefficient 1": coupling_coefficient}) intc.addelement("Waveguide Coupler", {"name": "Drop Coupler", "coupling coefficient 1": coupling_coefficient}) intc.addelement( "Straight Waveguide", {"name": "Waveguide 1", "length": np.pi * radius, "loss 1": loss, "effective index 1": effective_index, "group index 1": group_index}, ) intc.addelement( "Straight Waveguide", {"name": "Waveguide 2", "length": np.pi * radius, "loss 1": loss, "effective index 1": effective_index, "group index 1": group_index}, ) # Connect ...

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
