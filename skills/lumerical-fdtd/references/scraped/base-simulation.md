# Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#base-simulation)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html  
Area: Discovered official source  
Topic: Discovered from Introduction to photonic inverse design with lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#base-simulation)` for the topic `Discovered from Introduction to photonic inverse design with lumopt2`. It captured 3 heading(s), 17 link(s), 3 code block(s), 7 inline code term(s), and 0 table(s). Main headings: Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#base-simulation), Setting up the base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#setting-up-the-base-simulation), Passing base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#passing-base-simulation). Key detected terms: fdtd, lumopt, monitor, optimization, port, pylumerical, python, script, source.

## Key Terms

- fdtd
- lumopt
- monitor
- optimization
- port
- pylumerical
- python
- script
- source

## Captured Headings

- Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#base-simulation)
- Setting up the base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#setting-up-the-base-simulation)
- Passing base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#passing-base-simulation)

## Official Text Excerpt

> Base simulation # The base simulation defines the FDTD simulation that is used for optimization. In lumopt2, you can define the base simulation using an existing Lumerical FDTD`.fsp`project file, a Lumerical script file that sets up the simulation, or a Python callable that sets up the simulation. Setting up the base simulation # The base simulation contains sources, monitors, and geometries necessary for the optimization. Note You don’t need to set up the optimization region in the base simulation, as this is separately defined in Python and passed into the parametrization. To run optimization using`lumopt2`, the base simulation needs specific objects to capture the simulation results for the figure of merit. See the figure of merit article for more details. For a general parametric optimization that directly maps optimization parameters to object properties, include the source, field region monitor, and objects whose properties are being optimized in the base simulation. For parametric optimization using the``ClosedCurve class, typically used in photonic integrated circuit applications, include only the ports and any input and output waveguides. The optimizable section is set up separately ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `1project = lmpt.Project(setup = os.path.join(cwd_path, 'my_fdtd_project.fsp'), parametrization = parametrization, fom = fom,`
- Code block 2: 2 line(s); first line `1project = lmpt.Project(setup = os.path.join(cwd_path, 'setup_my_fdtd_project.lsf'), parametrization = parametrization, fom = fom,`
- Code block 3: 4 line(s); first line `1from my_setup_module import my_setup_function`

## Inline Code Inventory

- `.fsp`
- `ClosedCurve`
- `Project`
- `Project.setup`
- `ProjectConfig`
- `config`
- `lumopt2`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#base-simulation)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#setting-up-the-base-simulation)
- [figure of merit article](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [parametrization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html)
- [ProjectConfig](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#lumopt2.core.project_config.ProjectConfig)
- [simple metalens example](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html)
- [L-bend example](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html)
- [FDTD Product Reference Manual](https://optics.ansys.com/hc/en-us/articles/360033154434-FDTD-product-reference-manual)
- [Lumerical scripting language index](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)
- [Simulation automation section of the user guide](https://lumerical.docs.pyansys.com/version/stable/user_guide/index.html#simulation-automation)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html#passing-base-simulation)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [Project.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [figure of merit](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html)
- [FDTD session](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-fdtd-session)
- [runner](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-runner)

## Ansys-Related External Links Found

- None

## External Links Found

- None
