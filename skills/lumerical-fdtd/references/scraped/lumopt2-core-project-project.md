# Project [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#project)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Project [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#project)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 21 link(s), 0 code block(s), 21 inline code term(s), and 1 table(s). Main headings: Project [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#project). Key detected terms: fdtd, geometry, lumopt, optimization, script, solver.

## Key Terms

- fdtd
- geometry
- lumopt
- optimization
- script
- solver

## Captured Headings

- Project [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#project)

## Official Text Excerpt

> Project # class lumopt2.core.project. Project (setup: Callable|str, parametrization: BaseParametrization, fdtd_session: FdtdSession = None, fom: BaseFom = None, runner: BaseRunner = None, project_name: str = None) # Main project class that coordinates parametrization, FOM, and solver. Parameters: setup`Union``Callable`,``[str] Either a callable that sets up the simulation, or a path to a .lsf script or .fsp project file. parametrization`BaseParametrization` BaseParametrization instance for optimization geometry. fdtd_session`FdtdSession`,`optional` Existing FdtdSession instance (will create new if None, default: None). fom`BaseFom`,`optional` Figure of merit instance (default: None). runner`BaseRunner`,`optional` Runner instance for job management (default: None). project_name``str,`optional` Custom name for saved project files (default: None, uses “lumopt2_project”). Methods | ``Project.compute_fom ([params]) | Compute the figure of merit for the current simulation. | ``Project.compute_gradient ([params]) | Compute the gradient of the figure of merit with respect to parameters. | ``Project.generate ([params]) | Generate the optimization project by setting up the base simulation. | ``Project.load_forward_results ([config_key]) | Reload a completed forward simulation file into the FDTD session. | ``Project.run_adjoint () | Run adjoint simulation(s). | ``Project.run_forward () | Run forward simulation. | ``Project.save_project (filename[, params]) | Saves the current project ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `BaseFom`
- `BaseParametrization`
- `BaseRunner`
- `Callable`
- `FdtdSession`
- `Project.compute_fom`
- `Project.compute_gradient`
- `Project.generate`
- `Project.load_forward_results`
- `Project.run_adjoint`
- `Project.run_forward`
- `Project.save_project`
- `Project.set_adj`
- `Project.set_fwd`
- `Project.setup_base_simulation`
- `Project.update_geometry`
- `Project.visualize_fom`
- `Project.visualize_geometry`
- `Union`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 13 row(s)
  - First row sample: Project.compute_fom ([params]) | Compute the figure of merit for the current simulation.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#project)
- [BaseParametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.base_parametrization.BaseParametrization.html#lumopt2.parametrization.base_parametrization.BaseParametrization)
- [FdtdSession](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.FdtdSession.html#lumopt2.core.fdtd_session.FdtdSession)
- [BaseFom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.base_fom.BaseFom.html#lumopt2.fom.base_fom.BaseFom)
- [BaseRunner](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.BaseRunner.html#lumopt2.utils.runner.BaseRunner)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [Project.compute_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.compute_fom.html#lumopt2.core.project.Project.compute_fom)
- [Project.compute_gradient](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.compute_gradient.html#lumopt2.core.project.Project.compute_gradient)
- [Project.generate](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.generate.html#lumopt2.core.project.Project.generate)
- [Project.load_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.load_forward_results.html#lumopt2.core.project.Project.load_forward_results)
- [Project.run_adjoint](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.run_adjoint.html#lumopt2.core.project.Project.run_adjoint)
- [Project.run_forward](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.run_forward.html#lumopt2.core.project.Project.run_forward)
- [Project.save_project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.save_project.html#lumopt2.core.project.Project.save_project)
- [Project.set_adj](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.set_adj.html#lumopt2.core.project.Project.set_adj)
- [Project.set_fwd](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.set_fwd.html#lumopt2.core.project.Project.set_fwd)
- [Project.setup_base_simulation](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.setup_base_simulation.html#lumopt2.core.project.Project.setup_base_simulation)
- [Project.update_geometry](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.update_geometry.html#lumopt2.core.project.Project.update_geometry)
- [Project.visualize_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.visualize_fom.html#lumopt2.core.project.Project.visualize_fom)
- [Project.visualize_geometry](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.visualize_geometry.html#lumopt2.core.project.Project.visualize_geometry)

## Ansys-Related External Links Found

- None

## External Links Found

- [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
