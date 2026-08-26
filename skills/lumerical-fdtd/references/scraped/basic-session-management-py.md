# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/basic_session_management/basic_session_management.py  
Area: Discovered official source  
Topic: Discovered from Basic session management  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Basic session management`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: fdtd, import, lumapi, mode, port, pylumerical.

## Key Terms

- fdtd
- import
- lumapi
- mode
- port
- pylumerical

## Captured Headings

- No headings extracted

## Official Text Excerpt

> # Basic Session Management # # This example demonstrates how to initialize a local Lumerical session. # PyLumerical interacts with Lumerical products through sessions. # # ## Prerequisites: # # Valid FDTD and MODE licenses are required. # # ### Perform required imports import ansys.lumerical.core as lumapi # # ### Open an interactive session # + fdtd = lumapi.FDTD() # Wait for a second, then add FDTD region fdtd.pause(1) fdtd.addfdtd() fdtd.print("Example complete. Press space bar to close.") fdtd.pause(30) # Will close in 30 seconds if left idle fdtd.close() mode = lumapi.MODE() mode.print("Example complete. Press space bar to close.") mode.pause(30) mode.close() # Load a session but hide the application window fdtd = lumapi.FDTD(hide=True) fdtd.close() # - # ### Use the "with" context manager with lumapi.FDTD() as fdtd: fdtd.addfdtd() fdtd.print("Example complete. Press space bar to close.") fdtd.pause(30) # FDTD closes automatically # ### Session wrapped in a function # Get the number of grid cells in FDTD region for set span def get_x_cells(fdtd_span): """Return the number of grid cells in FDTD region for a set span.""" with lumapi.FDTD() as fdtd: # Adds ...

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
