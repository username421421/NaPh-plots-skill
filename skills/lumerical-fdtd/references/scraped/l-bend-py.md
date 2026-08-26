# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/stable/_static/simulation_examples/lumopt2_lbend/L_bend.py  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: L-bend  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Getting started with lumopt2: L-bend`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: boundary, fdtd, geometry, import, lumopt, mesh, mode, monitor, optimization, port, reflection, source, sweep, transmission.

## Key Terms

- boundary
- fdtd
- geometry
- import
- lumopt
- mesh
- mode
- monitor
- optimization
- port
- reflection
- source
- sweep
- transmission

## Captured Headings

- No headings extracted

## Official Text Excerpt

> import numpy as np import ansys.lumerical.core.lumopt2 as lmpt import math # Parameters n_wg = math.sqrt(12.25) # Silicon (waveguide) refractive index n_bg = math.sqrt(2.25) # Silicon oxide background wg_width = 0.5e-6 # Waveguide width (500nm) wg_height = 0.22e-6 # Waveguide height (220nm) # Wavelength range for optimization (O-band telecom) wavelengths = np.linspace(1200e-9, 1400e-9, 21) # Design region parameters bend_radius = 1.0e-6 bend_start = wg_width/2+bend_radius dist_to_wall = 0.4e-6 # Distance from wall to start of the bend (lead waveguides) fdtd_min_x =-(bend_start + dist_to_wall) fdtd_max_x = 2*wg_width fdtd_min_y =-2*wg_width fdtd_max_y = bend_start + dist_to_wall fdtd_span_z = 1.6e-6 mode_width = 4 * wg_width mode_height = fdtd_span_z fdtd_buffer = 0.2e-6 # Extra buffer around optimization region for FDTD simulation mesh_size = 25e-9 # FDTD mesh size for optimization region # Create base simulation setup "conformal variant 0" or "precise volume average"} def generate_base_sim(fdtd): fdtd.addfdtd({"x min":fdtd_min_x-fdtd_buffer, "x max":fdtd_max_x+fdtd_buffer, "y min":fdtd_min_y-fdtd_buffer, "y max":fdtd_max_y+fdtd_buffer, "z span":fdtd_span_z+2*fdtd_buffer, "index": n_bg, "mesh accuracy": 3, "mesh refinement": "precise volume average"}) # Input waveguides (horizontal - extending beyond crossing region) fdtd.addrect({"name": "wg_in", "index": n_wg, "x min": 2*fdtd_min_x, "x max":-bend_start, "y":0, "y span":wg_width, "z ...

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
