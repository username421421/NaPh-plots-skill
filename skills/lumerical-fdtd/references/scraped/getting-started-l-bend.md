# Getting started with lumopt2: L-bend [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#getting-started-with-lumopt2-l-bend)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html  
Area: PyLumerical  
Topic: Closed-curve parametrization, ports, FOM, optimizer, callbacks  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Getting started with lumopt2: L-bend [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#getting-started-with-lumopt2-l-bend)` for the topic `Closed-curve parametrization, ports, FOM, optimizer, callbacks`. It captured 9 heading(s), 31 link(s), 14 code block(s), 22 inline code term(s), and 0 table(s). Main headings: Getting started with lumopt2: L-bend [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#getting-started-with-lumopt2-l-bend), Base geometry [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#base-geometry), Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#parametrization), Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#figure-of-merit), Project configuration [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#project-configuration), Optimizer [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#optimizer), Visualization and logging [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#visualization-and-logging), Results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#results). Key detected terms: analysis, fdtd, geometry, import, lumopt, monitor, optimization, port, python, script, source, symmetry, transmission.

## Key Terms

- analysis
- fdtd
- geometry
- import
- lumopt
- monitor
- optimization
- port
- python
- script
- source
- symmetry
- transmission

## Captured Headings

- Getting started with lumopt2: L-bend [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#getting-started-with-lumopt2-l-bend)
- Base geometry [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#base-geometry)
- Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#parametrization)
- Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#figure-of-merit)
- Project configuration [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#project-configuration)
- Optimizer [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#optimizer)
- Visualization and logging [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#visualization-and-logging)
- Results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#results)
- Further resources [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#further-resources)

## Official Text Excerpt

> Download Python Script (.py) Getting started with lumopt2: L-bend # This example demonstrates using lumopt2 to optimize an L-bend waveguide coupler. This example uses the closed curve parametrization approach, typically used for photonic integrated circuit applications, and demonstrates the use of a Python callable function for setup, and callbacks to customize the visualization. For a more basic example demonstrating lumopt2 workflow, see the simple metalens example. The Python script associated with this example is attached to the article. Base geometry # In this example, the base simulation is set up using a Python function, which defines the simulation region, optical ports, source settings, and monitor settings. This function is passed later to the project setup. The function also sets up the geometry of the fixed input and output straight waveguides; however, the actual bend geometry to be optimized is defined by the``ClosedCurve class, as explained later. For the L-bend geometry, first construct a closed path as a list of``Segment class instances. Each``Segment object is described by the (x, y) coordinates of the start point and the type of segment (`linear`for ...

## Code Block Inventory

- Code block 1: 24 line(s); first line `35def generate_base_sim(fdtd):`
- Code block 2: 9 line(s); first line `68path = [ (lmpt.Segment([ fdtd_min_x,              wg_width/2],             'linear')),  # Segment 1`
- Code block 3: 7 line(s); first line `81optimization_region = lmpt.Box(x_min=fdtd_min_x, x_max=fdtd_max_x,`
- Code block 4: 1 line(s); first line `88closed_curve.plot() # Visualize the base geometry`
- Code block 5: 10 line(s); first line `90## CLOSED CURVE - PARAMETRIZATION ##`
- Code block 6: 1 line(s); first line `99closed_curve.make_segments_parametric(segments_to_parametrize)`
- Code block 7: 1 line(s); first line `101closed_curve.plot() # Visualize the base geometry`
- Code block 8: 2 line(s); first line `109port_out = lmpt.PortResults('port_out', metric='transmission', wavelengths=wavelengths)`
- Code block 9: 1 line(s); first line `118project = lmpt.Project(setup=generate_base_sim, parametrization=closed_curve, fom=l_bend_fom, fdtd_session=fdtd_session)`
- Code block 10: 1 line(s); first line `119project.visualize_fom()`
- Code block 11: 1 line(s); first line `123optimizer = lmpt.ScipyOptimizer(method='L-BFGS-B', max_iter=10)`
- Code block 12: 13 line(s); first line `128visualizer = lmpt.GraphicalVisualizer(`
- Code block 13: 5 line(s); first line `143optimization = lmpt.Optimization(`
- Code block 14: 2 line(s); first line `153best_params, best_fom = result`

## Inline Code Inventory

- `"normal"`
- `ClosedCurve`
- `ClosedCurve.make_segments_parametric`
- `ClosedCurve.plot()`
- `FileLogger`
- `GraphicalVisualizer`
- `L_bend_optimization_final.fsp`
- `Optimization`
- `PNorm()`
- `Parametrization`
- `Parametrize`
- `PortResults`
- `Project.save_project()`
- `Project.visualize_fom()`
- `ScipyOptimizer`
- `Segment`
- `cubic`
- `linear`
- `lumopt2.core.fdtd_session.FdtdSession`
- `lumopt2.core.project.Project`
- `lumopt2.utils.runner.LocalRunner`
- `optimization.run()`

## Table Inventory

- No tables detected

## Official Links Found

- [Download Python Script (.py)](https://lumerical.docs.pyansys.com/version/stable/_static/simulation_examples/lumopt2_lbend/L_bend.py)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#getting-started-with-lumopt2-l-bend)
- [simple metalens example](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#base-geometry)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [Segment](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Segment.html#lumopt2.parametrization.closed_curve.Segment)
- [ClosedCurve.plot()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#parametrization)
- [Parametrize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Parametrize.html#lumopt2.parametrization.closed_curve.Parametrize)
- [ClosedCurve.make_segments_parametric](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [parametrization page](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#figure-of-merit)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [PNorm()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.PNorm.html#lumopt2.utils.common.PNorm)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#project-configuration)
- [lumopt2.core.project.Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [lumopt2.core.fdtd_session.FdtdSession](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.FdtdSession.html#lumopt2.core.fdtd_session.FdtdSession)
- [lumopt2.utils.runner.LocalRunner](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#lumopt2.utils.runner.LocalRunner)
- [Project.visualize_fom()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#optimizer)
- [ScipyOptimizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#visualization-and-logging)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [FileLogger](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#lumopt2.utils.file_logger.FileLogger)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#results)
- [optimization.run()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [Project.save_project()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [Importing and exporting GDSII files](https://optics.ansys.com/hc/en-us/articles/360034901933-Importing-and-exporting-GDSII-files)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_l_bend.html#further-resources)
- [Introduction to photonic inverse design with lumopt2](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [lumopt2](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html)

## Ansys-Related External Links Found

- None

## External Links Found

- None
