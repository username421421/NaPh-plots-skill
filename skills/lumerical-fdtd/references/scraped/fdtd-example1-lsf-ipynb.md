# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_lsf/fdtd_example1_lsf.ipynb  
Area: Discovered official source  
Topic: Discovered from Basic FDTD Simulation - Lumerical style commands  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Basic FDTD Simulation - Lumerical style commands`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: command, fdtd, gaussian, import, lumapi, monitor, port, pylumerical, python, script, source.

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
- script
- source

## Captured Headings

- No headings extracted

## Official Text Excerpt

> { "cells": [ { "cell_type": "markdown", "id": "bf4d0f28", "metadata": {}, "source": [ "# Basic FDTD Simulation - Lumerical style commands" ] }, { "cell_type": "markdown", "id": "a09c6156", "metadata": { "lines_to_next_cell": 2 }, "source": [ "A simple example to demonstrate using PyLumerical using Lumerical Script File (lsf) style commands.\n", "Sets up and runs a basic FDTD simulation. E field results are plotted in Lumerical." ] }, { "cell_type": "markdown", "id": "b6b46363", "metadata": {}, "source": [ "## Prerequisites:\n", "\n", "Valid FDTD license is required.\n", "\n", "### Perform required imports" ] }, { "cell_type": "code", "execution_count": null, "id": "09b41475", "metadata": {}, "outputs": [], "source": [ "import ansys.lumerical.core as lumapi" ] }, { "cell_type": "markdown", "id": "e9f2ecd5", "metadata": {}, "source": [ "### Open an interactive session" ] }, { "cell_type": "code", "execution_count": null, "id": "d362710c", "metadata": {}, "outputs": [], "source": [ "\n", "# Set hide = True to hide the Lumerical GUI.\n", "fdtd = lumapi.FDTD(hide=False)\n" ] }, { "cell_type": "markdown", "id": "a86a1842", "metadata": {}, "source": [ "\n", "### Set up simulation region" ] }, { "cell_type": "code", "execution_count": null, "id": "94ad6642", "metadata": {}, "outputs": ...

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
