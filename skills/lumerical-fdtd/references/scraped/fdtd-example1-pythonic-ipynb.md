# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/0.3/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.ipynb  
Area: Discovered official source  
Topic: Discovered from Basic FDTD Simulation - Python style commands  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Basic FDTD Simulation - Python style commands`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: command, fdtd, gaussian, import, lumapi, monitor, port, pylumerical, python, source.

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
- source

## Captured Headings

- No headings extracted

## Official Text Excerpt

> { "cells": [ { "cell_type": "markdown", "id": "7680982a", "metadata": { "lines_to_next_cell": 2 }, "source": [ "# Basic FDTD Simulation - Python style commands\n", "\n", "A simple example to demonstrate using PyLumerical.\n", "\n", "Sets up and runs a basic FDTD simulation. E field results are plotted using Matplotlib\n", "Demonstrates initializing objects using keyword arguments and OrderedDict." ] }, { "cell_type": "markdown", "id": "a8325da2", "metadata": {}, "source": [ "## Prerequisites:\n", "\n", "Valid FDTD license is required.\n", "\n", "### Perform required imports" ] }, { "cell_type": "code", "execution_count": null, "id": "0a61eca6", "metadata": {}, "outputs": [], "source": [ "\n", "from collections import OrderedDict\n", "\n", "import matplotlib.pyplot as plt\n", "\n", "import ansys.lumerical.core as lumapi\n" ] }, { "cell_type": "markdown", "id": "d7abc553", "metadata": {}, "source": [ "### Open interactive session with the \"with\" context manager, run session, retrieve and plots results, and close session" ] }, { "cell_type": "code", "execution_count": null, "id": "1aeb6e1e", "metadata": {}, "outputs": [], "source": [ "# Set hide = True to hide the Lumerical GUI.\n", "with lumapi.FDTD() as fdtd:\n", " # Set up simulation region using keyword arguments\n", " fdtd.addfdtd(x=0, x_span=8e-6, y=0, ...

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
