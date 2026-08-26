# INTERCONNECT application example

Source URL: https://optics.ansys.com/hc/en-us/articles/360034416594-INTERCONNECT-application-example  
Area: Discovered official source  
Topic: Discovered from Python API overview  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `INTERCONNECT application example` for the topic `Discovered from Python API overview`. It captured 6 heading(s), 10 link(s), 7 code block(s), 0 inline code term(s), and 2 table(s). Main headings: INTERCONNECT application example, Importing modules, Creating the Monte Carlo analysis, Running the Monte Carlo analysis, Plotting the results, See also. Key detected terms: analysis, command, grating, import, lumapi, optimization, port, python, script, sweep.

## Key Terms

- analysis
- command
- grating
- import
- lumapi
- optimization
- port
- python
- script
- sweep

## Captured Headings

- INTERCONNECT application example
- Importing modules
- Creating the Monte Carlo analysis
- Running the Monte Carlo analysis
- Plotting the results
- See also

## Official Text Excerpt

> INTERCONNECT application example This example demonstrates the feasibility of integrating Lumerical INTERCONNECT with Python. This interoperability is made possible using Application Programming Interface (API). In this example, a Monte Carlo analysis in INTERCONNECT will be generated using Python script based on the circuit defined in the file run_monte_carlo.icp and some of the results such as the histogram and probability density function (pdf) will be plotted using Python plot functions. This example is similar to the Monte Carlo scripting commands example in the Parameter sweeps, Optimization and Monte Carlo analysis section. Requirements: Lumerical products 2018a R4 or newer | Note: - Versions: The example files were created using Lumerical 2018a R4, Python 3.6 (and numpy), matplotlib 0.99.1.1, and Windows 7 - Working directory: It should be possible to store the files in any locations as desired. However, it is recommended to put the Lumerical and Python files in the same folder in order for the above script files to work properly. It is also important to check the Lumerical working directory has the correct path, see here for instructions to change ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `import importlib.util#The default paths for windows, linux and macspec_win = importlib.util.spec_from_file_location('lumapi', 'C:\\Program Files\\Lumerical\\202`
- Code block 2: 1 line(s); first line `ic = lumapi.INTERCONNECT("run_monte_carlo.icp")`
- Code block 3: 1 line(s); first line `ic.addsweep(2)MC_name = "MC_script"ic.setsweep("Monte Carlo analysis", "name", MC_name)setup = {    "number of trials": 200.0,    "enable seed": 1.0,    "seed":`
- Code block 4: 1 line(s); first line `sweep_parameters = [    {         "Name": "cpl_2",        "Parameter": "::Root Element::WC2::coupling coefficient 1",        "Value": ic.getnamed("WC2", "coupli`
- Code block 5: 1 line(s); first line `sweep_results = [    {        "Name": "fsr",        "Result": "::Root Element::Optical Network Analyzer::input 2/mode 1/peak/free spectral range",        "Estim`
- Code block 6: 1 line(s); first line `ic.runsweep(MC_name)`
- Code block 7: 1 line(s); first line `fsr = ic.getsweepresult(MC_name, "analysis/results/histogram/fsr")fsrCount = fsr["count"][0][0]fsr = fsr["fsr"][0][0]pdf = ic.getsweepresult(MC_name, "analysis/`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Versions : The example files were created using Lumerical 2018a R4, Python 3.6 (and numpy), matplotlib 0.99.1.1, and Windows 7 Working directory : It should be possible to store the files in any locations as desired. However, it is re
- Table 2: 2 column(s), 2 row(s)
  - First row sample: Linux | /opt/lumerical/interconnect/api/python/

## Official Links Found

- [here](https://optics.ansys.com/hc/en-us/articles/360034931553)
- [Session management - Python API](https://optics.ansys.com/hc/en-us/articles/360041873053)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [Python API](https://optics.ansys.com/hc/en-us/articles/360034416554)
- [Monte Carlo analysis](https://optics.ansys.com/hc/en-us/articles/360034403194)
- [Monte Carlo scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922993)
- [Parameter Sweep](https://optics.ansys.com/hc/en-us/articles/360034922873)

## Ansys-Related External Links Found

- None

## External Links Found

- [this page](https://kb.lumerical.com/installation_and_setup_python-integration.html)
- [Setting up Python API](https://kb.lumerical.com/installation_and_setup_python-integration.html)
- [Matlab API](https://kb.lumerical.com/pic_passive_matlab-driven-optimization.html)
