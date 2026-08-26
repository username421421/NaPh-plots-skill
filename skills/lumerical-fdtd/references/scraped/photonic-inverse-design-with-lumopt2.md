# Introduction to photonic inverse design with lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#introduction-to-photonic-inverse-design-with-lumopt2)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html  
Area: PyLumerical  
Topic: lumopt2 installation, import, and workflow overview  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Introduction to photonic inverse design with lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#introduction-to-photonic-inverse-design-with-lumopt2)` for the topic `lumopt2 installation, import, and workflow overview`. It captured 6 heading(s), 14 link(s), 5 code block(s), 3 inline code term(s), and 0 table(s). Main headings: Introduction to photonic inverse design with lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#introduction-to-photonic-inverse-design-with-lumopt2), Installation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#installation), Using PyLumerical [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-pylumerical), Using the in-product script editor [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-the-in-product-script-editor), Getting started [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#getting-started), Workflow [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#workflow). Key detected terms: command, fdtd, import, lumopt, optimization, port, pylumerical, python, script, structure, sweep.

## Key Terms

- command
- fdtd
- import
- lumopt
- optimization
- port
- pylumerical
- python
- script
- structure
- sweep

## Captured Headings

- Introduction to photonic inverse design with lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#introduction-to-photonic-inverse-design-with-lumopt2)
- Installation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#installation)
- Using PyLumerical [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-pylumerical)
- Using the in-product script editor [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-the-in-product-script-editor)
- Getting started [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#getting-started)
- Workflow [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#workflow)

## Official Text Excerpt

> Introduction to photonic inverse design with lumopt2 # Inverse design is a computational design approach in which the desired functionality of a component or system is specified first, and optimization algorithms are then used to determine the structure or parameters that best produce that response. Unlike traditional design workflows, which rely on iteratively adjusting a limited set of parameters and evaluating candidate geometries, inverse design enables systematic exploration of much larger design spaces. This makes it especially valuable for complex photonic designs, where brute-force parameter sweeps become increasingly costly and less effective as the number of parameters grows. The Ansys Lumerical solution for photonic inverse design, lumopt2, is named after the Python module of the same name included in the Ansys Lumerical installation. The`lumopt2`module provides a simple and intuitive Python interface for configuring and running inverse design optimizations with Ansys Lumerical FDTD. In just a few steps, you can define an optimization session with your custom parametrization and figure of merit, run the optimization, and analyze the results. Installation # The`lumopt2`module is included with the Ansys Lumerical products and requires ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `1python -m venv .venv`
- Code block 2: 4 line(s); first line `1python -m venv .venv`
- Code block 3: 4 line(s); first line `1python -m venv .venv`
- Code block 4: 1 line(s); first line `1import ansys.lumerical.core.lumopt2 as lmpt`
- Code block 5: 1 line(s); first line `1import lumopt2 as lmpt`

## Inline Code Inventory

- `ansys.lumerical.core`
- `lumopt2`
- `sys.path`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#introduction-to-photonic-inverse-design-with-lumopt2)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#installation)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-pylumerical)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#using-the-in-product-script-editor)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#getting-started)
- [Getting started with lumopt2: simple metalens](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html)
- [Getting started with lumopt2: L-bend](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html#workflow)
- [Optimization session in lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html)
- [Running the optimization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-run)
- [Optimization results](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-results)
- [Base simulation](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html)
- [Figure of merit](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html)

## Ansys-Related External Links Found

- None

## External Links Found

- None
