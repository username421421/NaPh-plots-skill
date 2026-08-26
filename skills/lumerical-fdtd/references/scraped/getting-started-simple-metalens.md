# Getting started with lumopt2: simple metalens [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#getting-started-with-lumopt2-simple-metalens)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html  
Area: PyLumerical  
Topic: Basic lumopt2 project setup and run pattern  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Getting started with lumopt2: simple metalens [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#getting-started-with-lumopt2-simple-metalens)` for the topic `Basic lumopt2 project setup and run pattern`. It captured 10 heading(s), 46 link(s), 15 code block(s), 33 inline code term(s), and 0 table(s). Main headings: Getting started with lumopt2: simple metalens [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#getting-started-with-lumopt2-simple-metalens), Base simulation file [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#base-simulation-file), Importing libraries [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#importing-libraries), Optimization region setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#optimization-region-setup), Parametrization setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#parametrization-setup), Figure of merit setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#figure-of-merit-setup), Project setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#project-setup), Validate and run optimization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#validate-and-run-optimization). Key detected terms: command, convergence, fdtd, gaussian, geometry, group, import, lumopt, mesh, normalization, optimization, plane, port, pylumerical, python, script.

## Key Terms

- command
- convergence
- fdtd
- gaussian
- geometry
- group
- import
- lumopt
- mesh
- normalization
- optimization
- plane
- port
- pylumerical
- python
- script
- source
- structure

## Captured Headings

- Getting started with lumopt2: simple metalens [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#getting-started-with-lumopt2-simple-metalens)
- Base simulation file [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#base-simulation-file)
- Importing libraries [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#importing-libraries)
- Optimization region setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#optimization-region-setup)
- Parametrization setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#parametrization-setup)
- Figure of merit setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#figure-of-merit-setup)
- Project setup [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#project-setup)
- Validate and run optimization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#validate-and-run-optimization)
- Results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#results)
- Further resources [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#further-resources)

## Official Text Excerpt

> Download Python Script (.py) Download Simulation File (.fsp) Getting started with lumopt2: simple metalens # This article discusses the usage of the lumopt2 inverse design module in Lumerical FDTD for a basic parametric optimization. Using a basic metalens formed by a 3x3 array of pillars, this example highlights key functionalities of the lumopt2 module and walks you through the steps necessary to create and run a simple optimization. The simulation file and script associated with this example can be downloaded using the download buttons above. Prior to working through the example, please ensure that lumopt2 is successfully set up and importable as seen from the introduction page. Base simulation file # The base simulation file consists of an array of 9 silicon cylinders, arranged in a 3x3 array, embedded in an silicon oxide substrate. Each cylinder has a fixed height, but the radius can vary within set bounds for optimization. This structure mimics a simple metalens arrangements with cylindrical meta-atoms. A Gaussian source illuminates the metalens from above. The optimization aims to maximize the field intensity in a central region ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `5import ansys.lumerical.core.lumopt2 as lmpt`
- Code block 2: 2 line(s); first line `12optimization_region = lmpt.Box(x_span = 1e-6, y_span = 1e-6, z_min = 1e-6, z_max = 1e-6 + 750e-9,`
- Code block 3: 5 line(s); first line `16num_cyl = 3*3`
- Code block 4: 1 line(s); first line `17bounds = [(0.05e-6, 0.1e-6)]*num_cyl`
- Code block 5: 2 line(s); first line `18def param_func(params):`
- Code block 6: 1 line(s); first line `18parametrization = lmpt.Parametrization(func=param_func, bounds=bounds, optimization_region=optimization_region)`
- Code block 7: 6 line(s); first line `26# Sum of field intensity at 'focus' normalized by sum of field intensity at 'norm'`
- Code block 8: 2 line(s); first line `27intensity_focus = lmpt.FieldResults(monitor_name='focus', metric='intensity', wavelengths = 940e-9)`
- Code block 9: 2 line(s); first line `29def custom_fct(result_list):`
- Code block 10: 1 line(s); first line `31fom = lmpt.Fom([intensity_focus, intensity_norm], fct = custom_fct)`
- Code block 11: 2 line(s); first line `34project = lmpt.Project(setup = os.path.join(cwd_path, 'metalens_3x3.fsp'), parametrization = parametrization, fom = fom,`
- Code block 12: 5 line(s); first line `1XX:XX:XX - INFO - FDTD version '8.35.4519' meets the minimum requirement.`
- Code block 13: 3 line(s); first line `41optimizer = lmpt.ScipyOptimizer(bounds = bounds, max_iter = 15, gtol = 1e-9)`
- Code block 14: 1 line(s); first line `44 optimization.run()`
- Code block 15: 10 line(s); first line `1XX:XX:XX - INFO - ============================================================`

## Inline Code Inventory

- `(lower_bound, upper_bound)`
- `::`
- `Box`
- `ClosedCurve`
- `FdtdSession`
- `FieldResults`
- `Fom()`
- `GraphicalVisualizer`
- `LocalRunner`
- `Parametrization`
- `PortResults`
- `Project`
- `Project.save_project()`
- `ScipyOptimizer`
- `cyl0`
- `cyl1`
- `cyl{idx}::radius`
- `fdtd_session`
- `focus`
- `group_name::object_name::property_name`
- `intensity`
- `intensity_focus`
- `intensity_norm`
- `lumopt2_project_<time_stamp>`
- `norm`
- `optimization.run()`
- `optimization_dft`
- `optimization_index`
- `optimization_mesh`
- `param_func`
- `parametrization`
- `project.visualize_fom(params=params)`
- `runner`

## Table Inventory

- No tables detected

## Official Links Found

- [Download Python Script (.py)](https://lumerical.docs.pyansys.com/version/stable/_static/simulation_examples/lumopt2_3x3pillar/metalens_3x3.py)
- [Download Simulation File (.fsp)](https://lumerical.docs.pyansys.com/version/stable/_static/simulation_examples/lumopt2_3x3pillar/metalens_3x3.fsp)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#getting-started-with-lumopt2-simple-metalens)
- [introduction](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#base-simulation-file)
- [simulation region](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object)
- [gaussian source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object)
- [cylinder geometries](https://optics.ansys.com/hc/en-us/articles/360034901513-Circle-Simulation-Object)
- [field region objects](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
- [FDTD GUI interface](https://optics.ansys.com/hc/en-us/articles/360033154434-FDTD-product-reference-manual)
- [Lumerical Scripting Language](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)
- [PyLumerical](https://lumerical.docs.pyansys.com/version/stable/user_guide/index.html)
- [field region](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
- [ports](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#importing-libraries)
- [API reference](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#optimization-region-setup)
- [Box](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.Box.html#lumopt2.utils.common.Box)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#parametrization-setup)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#lumopt2.parametrization.parametrization.Parametrization)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [L-bend example](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html)
- [getnamed](https://optics.ansys.com/hc/en-us/articles/360034408574-getnamed-Script-command)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#figure-of-merit-setup)
- [FieldResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#lumopt2.fom.simulation_results.FieldResults)
- [Fom()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#lumopt2.fom.fom.Fom)
- [multiple configurations](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#multi-sim-config)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#project-setup)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [FdtdSession](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.FdtdSession.html#lumopt2.core.fdtd_session.FdtdSession)
- [LocalRunner](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#lumopt2.utils.runner.LocalRunner)
- [FDTD Resource Configuration](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)
- [Resource configuration elements and controls Knowledge Base article](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#validate-and-run-optimization)
- [ScipyOptimizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [optimizer section of the optimization session article](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-optimizers)
- [callback article](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#results)
- [Project.save_project()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html#further-resources)
- [Introduction to photonic inverse design with lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [lumopt2](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html)
- [Getting started with lumopt2: L-bend](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html)

## Ansys-Related External Links Found

- None

## External Links Found

- [scipy](https://scipy.org/)
