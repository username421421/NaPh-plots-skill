# Basic Session Management [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Basic-Session-Management)

Source URL: https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html  
Area: PyLumerical  
Topic: Initialize local sessions using PyLumerical  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Basic Session Management [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Basic-Session-Management)` for the topic `Initialize local sessions using PyLumerical`. It captured 7 heading(s), 9 link(s), 10 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Basic Session Management [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Basic-Session-Management), Prerequisites: [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Prerequisites:), Perform required imports [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Perform-required-imports), Open an interactive session [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Open-an-interactive-session), Use the “with” context manager [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Use-the-%22with%22-context-manager), Session wrapped in a function [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Session-wrapped-in-a-function), Test the function and print out the result [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Test-the-function-and-print-out-the-result). Key detected terms: fdtd, import, mode, port, pylumerical, python, script.

## Key Terms

- fdtd
- import
- mode
- port
- pylumerical
- python
- script

## Captured Headings

- Basic Session Management [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Basic-Session-Management)
- Prerequisites: [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Prerequisites:)
- Perform required imports [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Perform-required-imports)
- Open an interactive session [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Open-an-interactive-session)
- Use the “with” context manager [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Use-the-%22with%22-context-manager)
- Session wrapped in a function [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Session-wrapped-in-a-function)
- Test the function and print out the result [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Test-the-function-and-print-out-the-result)

## Official Text Excerpt

> Download Jupyter Notebook (.ipynb) Download Python script (.py) Basic Session Management # This example demonstrates how to initialize a local Lumerical session. PyLumerical interacts with Lumerical products through sessions. Prerequisites: # Valid FDTD and MODE licenses are required. Perform required imports # Open an interactive session # Use the “with” context manager # Session wrapped in a function # Get the number of grid cells in FDTD region for set span Test the function and print out the result #

## Code Block Inventory

- Code block 1: 1 line(s); first line `[ ]:`
- Code block 2: 1 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 3: 1 line(s); first line `[ ]:`
- Code block 4: 16 line(s); first line `2fdtd = lumapi.FDTD()`
- Code block 5: 1 line(s); first line `[ ]:`
- Code block 6: 5 line(s); first line `18with lumapi.FDTD() as fdtd:`
- Code block 7: 1 line(s); first line `[ ]:`
- Code block 8: 9 line(s); first line `23def get_x_cells(fdtd_span):`
- Code block 9: 1 line(s); first line `[ ]:`
- Code block 10: 2 line(s); first line `32test = get_x_cells(1e-6)`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [Download Jupyter Notebook (.ipynb)](https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/basic_session_management/basic_session_management.ipynb)
- [Download Python script (.py)](https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/basic_session_management/basic_session_management.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Basic-Session-Management)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Prerequisites:)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Perform-required-imports)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Open-an-interactive-session)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Use-the-%22with%22-context-manager)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Session-wrapped-in-a-function)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/basic_session_management/basic_session_management.html#Test-the-function-and-print-out-the-result)

## Ansys-Related External Links Found

- None

## External Links Found

- None
