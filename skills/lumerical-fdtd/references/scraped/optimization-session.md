# Optimization session in lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-in-lumopt2)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html  
Area: PyLumerical  
Topic: Project, base simulation, parametrization, FOM, callbacks  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Optimization session in lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-in-lumopt2)` for the topic `Project, base simulation, parametrization, FOM, callbacks`. It captured 14 heading(s), 49 link(s), 5 code block(s), 40 inline code term(s), and 0 table(s). Main headings: Optimization session in lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-in-lumopt2), Overview [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#overview), Project [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#project), Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#base-simulation), Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#parametrization), Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#figure-of-merit), FDTD session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#fdtd-session), Runner [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#runner). Key detected terms: convergence, fdtd, geometry, import, lumopt, monitor, optimization, port, python, script, source, structure, sweep.

## Key Terms

- convergence
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
- structure
- sweep

## Captured Headings

- Optimization session in lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-in-lumopt2)
- Overview [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#overview)
- Project [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#project)
- Base simulation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#base-simulation)
- Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#parametrization)
- Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#figure-of-merit)
- FDTD session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#fdtd-session)
- Runner [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#runner)
- Optimizer [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimizer)
- Callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#callbacks)
- Additional configurations [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#additional-configurations)
- Running the optimization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#running-the-optimization)
- Optimization results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-results)
- Diagnostics [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#diagnostics)

## Official Text Excerpt

> Optimization session in lumopt2 # The optimization session is the main interface for setting up and running a`lumopt2`optimization. Its key input is the optimization``Project, which defines the base simulation, parameterization, and figure of merit. You can also use the session inputs to choose the optimizer and specify what data is reported during and after the optimization. This article describes the overall optimization workflow in`lumopt2`through the optimization session, and includes links to detailed guides for each of the component. Note For installation and getting started information, see the introduction article. Overview # The overall workflow for running an inverse design problem is shown in the diagram below, with subsequent subsections describing in further detail each of the components. Base simulation `.fsp`,`.lsf`,`.py` #base-simulation Parametrization `lumopt2.Parametrization``lumopt2.ClosedCurve` #parametrization Figure of merit `lumopt2.Fom` #figure-of-merit FDTD Session `lumopt2.FdtdSession` #fdtd-session Runner `lumopt2.LocalRunner` #runner Project `lumopt2.Project` #project Optimizer `lumopt2.ScipyOptimizer` #optimizer Callbacks `lumopt2.GraphicalVisualizer``lumopt2.FileLogger` #callbacks Additional configurations `Optimization.store_all_simulations``Optimization.log_profiling_summary` #additional-configurations Optimization `lumopt2.Optimization` Run & Results `Optimization.run()` #running-the-optimization Project # The project object,``Project, defines the optimization problem by combining the following elements: - Base simulation (`Project.setup`): configures the simulation objects, such as ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `1fdtd_session = lmpt.FdtdSession(show_fdtd_cad = True)`
- Code block 2: 2 line(s); first line `1runner_gpu = lmpt.LocalRunner(resource = 'GPU') # GPU Runner`
- Code block 3: 1 line(s); first line `1optimizer = lmpt.ScipyOptimizer()`
- Code block 4: 1 line(s); first line `1Optimization.run()`
- Code block 5: 2 line(s); first line `1best_params, best_fom = result`

## Inline Code Inventory

- `.fsp`
- `.lsf`
- `.py`
- `ClosedCurve`
- `FdtdSession`
- `FileLogger`
- `Fom()`
- `GraphicalVisualizer`
- `LocalRunner`
- `Optimization`
- `Optimization.log_profiling_summary`
- `Optimization.run()`
- `Optimization.store_all_simulations`
- `Parametrization`
- `Project`
- `Project.fdtd_session`
- `Project.fom`
- `Project.parametrization`
- `Project.runner`
- `Project.save_project()`
- `Project.setup`
- `fd_sweep_perturbation()`
- `finite_difference_gradient()`
- `ftol`
- `gtol`
- `lumopt2`
- `lumopt2.ClosedCurve`
- `lumopt2.FdtdSession`
- `lumopt2.FileLogger`
- `lumopt2.Fom`
- `lumopt2.GraphicalVisualizer`
- `lumopt2.LocalRunner`
- `lumopt2.Optimization`
- `lumopt2.Parametrization`
- `lumopt2.Project`
- `lumopt2.ScipyOptimizer`
- `max_fval`
- `options`
- `scipy_optimizer`
- `validate_gradient()`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-session-in-lumopt2)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [introduction](https://lumerical.docs.pyansys.com/version/stable/user_guide/photonic_inverse_design_with_lumopt2.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#overview)
- [#base-simulation](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#base-simulation)
- [#parametrization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#parametrization)
- [#figure-of-merit](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#figure-of-merit)
- [#fdtd-session](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#fdtd-session)
- [#runner](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#runner)
- [#project](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#project)
- [#optimizer](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimizer)
- [#callbacks](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#callbacks)
- [#additional-configurations](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#additional-configurations)
- [#running-the-optimization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#running-the-optimization)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#project)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#base-simulation)
- [Base simulation](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/base_simulation.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#parametrization)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#lumopt2.parametrization.parametrization.Parametrization)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#figure-of-merit)
- [Fom()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#lumopt2.fom.fom.Fom)
- [field region](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
- [port](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object)
- [Figure of merit](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#fdtd-session)
- [FdtdSession](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.FdtdSession.html#lumopt2.core.fdtd_session.FdtdSession)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#runner)
- [LocalRunner](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#lumopt2.utils.runner.LocalRunner)
- [https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)
- [https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimizer)
- [scipy_optimizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/optimizer/scipy_optimizer.html#module-lumopt2.optimizer.scipy_optimizer)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#callbacks)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [FileLogger](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#lumopt2.utils.file_logger.FileLogger)
- [Callbacks](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#additional-configurations)
- [Optimization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#running-the-optimization)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#optimization-results)
- [Optimization.run()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [Project.save_project()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [Importing and exporting GDSII files](https://optics.ansys.com/hc/en-us/articles/1500006203341)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/optimization_session.html#diagnostics)
- [finite_difference_gradient()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#lumopt2.utils.fd_grad.finite_difference_gradient)
- [validate_gradient()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#lumopt2.utils.fd_grad.validate_gradient)
- [fd_sweep_perturbation()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#lumopt2.utils.fd_grad.fd_sweep_perturbation)

## Ansys-Related External Links Found

- None

## External Links Found

- None
