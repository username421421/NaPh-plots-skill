# Photonic Crystal Bandstructure (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Photonic-Crystal-Bandstructure-(FDTD))

Source URL: https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html  
Area: PyLumerical  
Topic: FDTD structure/analysis groups, Bloch boundaries, sweeps  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Photonic Crystal Bandstructure (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Photonic-Crystal-Bandstructure-(FDTD))` for the topic `FDTD structure/analysis groups, Bloch boundaries, sweeps`. It captured 3 heading(s), 6 link(s), 16 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Photonic Crystal Bandstructure (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Photonic-Crystal-Bandstructure-(FDTD)), Part 1: Set up structures and simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-1:-Set-up-structures-and-simulation-objects), Part 2: Set up and run sweeps to extract resonant frequencies and plot the bandstructure [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-2:-Set-up-and-run-sweeps-to-extract-resonant-frequencies-and-plot-the-bandstructure). Key detected terms: analysis, dipole, fdtd, group, import, material, port, python, script, solver, source, structure, sweep.

## Key Terms

- analysis
- dipole
- fdtd
- group
- import
- material
- port
- python
- script
- solver
- source
- structure
- sweep

## Captured Headings

- Photonic Crystal Bandstructure (FDTD) [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Photonic-Crystal-Bandstructure-(FDTD))
- Part 1: Set up structures and simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-1:-Set-up-structures-and-simulation-objects)
- Part 2: Set up and run sweeps to extract resonant frequencies and plot the bandstructure [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-2:-Set-up-and-run-sweeps-to-extract-resonant-frequencies-and-plot-the-bandstructure)

## Official Text Excerpt

> Download Jupyter Notebook (.ipynb) Download Python script (.py) Photonic Crystal Bandstructure (FDTD) #) This example demonstrates a photonic crystal simulation utilizing Structure and Analysis Group objects. Based on: https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure In Part 1, we build the structure and set the FDTD simulation region. In this case, the spheres are holes (filled with air, n = 1) and the background material is a simple dielectric material. Some advanced simulation objects, including the dipole cloud source and bandstructure analysis groups, are imported from the Object Library. We run a single simulation and visualize the resulting spectrum. In Part 2, we set up a series of sweeps to collect the resonant frequencies. In this example, we use the built-in sweep tool in Lumerical, but the parameter sweeps could also be set up from Python. We then run the sweeps and plot the results. Prerequisites: Valid FDTD license is required. Perform required imports Part 1: Set up structures and simulation objects # Part 2: Set up and run sweeps to extract resonant frequencies and plot the bandstructure #

## Code Block Inventory

- Code block 1: 1 line(s); first line `[ ]:`
- Code block 2: 7 line(s); first line `1from collections import OrderedDict`
- Code block 3: 1 line(s); first line `[ ]:`
- Code block 4: 23 line(s); first line `8# Define parameters`
- Code block 5: 1 line(s); first line `[ ]:`
- Code block 6: 46 line(s); first line `31# Initialize session and build simulation objects. Set hide = True to hide the Lumerical GUI.`
- Code block 7: 1 line(s); first line `[ ]:`
- Code block 8: 19 line(s); first line `77# Open the file and run a single simulation. Visualize the spectrum.`
- Code block 9: 1 line(s); first line `[ ]:`
- Code block 10: 42 line(s); first line `96# Normalization factor for SI units; see note above.`
- Code block 11: 1 line(s); first line `[ ]:`
- Code block 12: 8 line(s); first line `138# Now run all the sweeps - this may take a few minutes`
- Code block 13: 1 line(s); first line `[ ]:`
- Code block 14: 18 line(s); first line `146# Retrieve and analyze data from the sweeps`
- Code block 15: 1 line(s); first line `[ ]:`
- Code block 16: 9 line(s); first line `164k = np.linspace(1, 3 * num_points, 3 * num_points)`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [Download Jupyter Notebook (.ipynb)](https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.ipynb)
- [Download Python script (.py)](https://lumerical.docs.pyansys.com/version/0.3/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Photonic-Crystal-Bandstructure-(FDTD))
- [https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure](https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-1:-Set-up-structures-and-simulation-objects)
- [#](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/photonic_crystal_bandstructure/photonic_crystal_bandstructure.html#Part-2:-Set-up-and-run-sweeps-to-extract-resonant-frequencies-and-plot-the-bandstructure)

## Ansys-Related External Links Found

- None

## External Links Found

- None
