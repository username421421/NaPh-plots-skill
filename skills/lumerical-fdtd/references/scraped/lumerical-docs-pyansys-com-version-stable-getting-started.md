# Installation and getting started [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation-and-getting-started)

Source URL: https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html  
Area: PyLumerical  
Topic: ansys-lumerical-core, autodiscovery, LUMERICAL_HOME  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Installation and getting started [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation-and-getting-started)` for the topic `ansys-lumerical-core, autodiscovery, LUMERICAL_HOME`. It captured 7 heading(s), 17 link(s), 7 code block(s), 5 inline code term(s), and 0 table(s). Main headings: Installation and getting started [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation-and-getting-started), Installation [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation), Requirements [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#requirements), Importing modules [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#importing-modules), My first PyLumerical project [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#my-first-pylumerical-project), Further resources [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#further-resources), Recommended examples [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#recommended-examples). Key detected terms: command, fdtd, import, lumapi, lumopt, mode, plane, port, pylumerical, python, script, source, transmission.

## Key Terms

- command
- fdtd
- import
- lumapi
- lumopt
- mode
- plane
- port
- pylumerical
- python
- script
- source
- transmission

## Captured Headings

- Installation and getting started [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation-and-getting-started)
- Installation [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation)
- Requirements [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#requirements)
- Importing modules [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#importing-modules)
- My first PyLumerical project [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#my-first-pylumerical-project)
- Further resources [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#further-resources)
- Recommended examples [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#recommended-examples)

## Official Text Excerpt

> Installation and getting started # Installation # You can install PyLumerical using pip. First, create a virtual environment and activate it to avoid dependency conflicts and to keep your global Python environment clean. Linux Windows Command Prompt Windows Powershell Then, upgrade pip to the latest version, and install PyLumerical with the package name ansys-lumerical-core. Tip Using a virtual environment isn’t a requirement, but it’s a best practice for Python development. PyLumerical is compatible with various Python IDEs including VS Code, Jupyter Notebook, and Cursor. After installation, you can use your preferred editor to start using PyLumerical. Requirements # You must have an Ansys Lumerical GUI license along with Lumerical 2022 R1 or later on your computer to use PyLumerical. For more information, please visit the licensing page on the Ansys Optics website. Upon importing PyLumerical, the autodiscovery logic automatically locates the Lumerical installation path and configures interop. If autodiscovery fails, set the`LUMERICAL_HOME`environment variable before import and start a new Python session. To use the Lumerical photonic inverse design module lumopt2, you must have Ansys Lumerical FDTD™ version 2026 R1.2 or ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `1python -m venv .venv`
- Code block 2: 2 line(s); first line `1python -m venv .venv`
- Code block 3: 2 line(s); first line `1python -m venv .venv`
- Code block 4: 2 line(s); first line `1python -m pip install -U pip`
- Code block 5: 1 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 6: 1 line(s); first line `1import ansys.lumerical.core.lumopt2 as lmpt`
- Code block 7: 19 line(s); first line `1import ansys.lumerical.core as lumapi`

## Inline Code Inventory

- `LUMERICAL_HOME`
- `ansys.lumerical.core`
- `lumapi`
- `lumopt2`
- `sys.path`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation-and-getting-started)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#installation)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#requirements)
- [licensing page](https://optics.ansys.com/hc/en-us/articles/360033862333-Lumerical-product-components-and-licensing-overview)
- [autodiscovery](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#importing-modules)
- [lumopt2 introduction page](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#my-first-pylumerical-project)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#further-resources)
- [User guide](https://lumerical.docs.pyansys.com/version/stable/user_guide/index.html)
- [API reference](https://lumerical.docs.pyansys.com/version/stable/api/index.html)
- [Examples](https://lumerical.docs.pyansys.com/version/stable/examples.html)
- [Introduction to photonic inverse design with lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html#recommended-examples)
- [Basic FDTD Simulation - Python style commands](https://lumerical.docs.pyansys.com/version/stable/examples/Sessions_and_Objects/fdtd_example1_pythonic/fdtd_example1_pythonic.html)
- [Simple Waveguide (MODE FDE)](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/waveguide_FDE/waveguide_FDE.html)
- [Simple Ring Resonator (INTERCONNECT)](https://lumerical.docs.pyansys.com/version/stable/examples/Single_Solver_Workflows/ring_resonator_interconnect/ring_resonator_interconnect.html)

## Ansys-Related External Links Found

- None

## External Links Found

- None
