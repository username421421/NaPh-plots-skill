# lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#lumopt2)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html  
Area: PyLumerical  
Topic: lumopt2 classes and methods  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#lumopt2)` for the topic `lumopt2 classes and methods`. It captured 3 heading(s), 50 link(s), 0 code block(s), 47 inline code term(s), and 10 table(s). Main headings: lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#lumopt2), Common lumopt2 API [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#common-lumopt2-api), All lumopt2 modules [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#all-lumopt2-modules). Key detected terms: convergence, fdtd, geometry, lumopt, monitor, optimization, port, s-parameter, solver, source, sweep.

## Key Terms

- convergence
- fdtd
- geometry
- lumopt
- monitor
- optimization
- port
- s-parameter
- solver
- source
- sweep

## Captured Headings

- lumopt2 [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#lumopt2)
- Common lumopt2 API [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#common-lumopt2-api)
- All lumopt2 modules [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#all-lumopt2-modules)

## Official Text Excerpt

> lumopt2 # The Lumerical photonic inverse design module lumopt2 provides a framework for the inverse design of photonic devices using Ansys Lumerical FDTD™. The following pages contains API documentation for the lumopt2 module. Note lumopt2 is only available in Ansys Lumerical FDTD™ version 2026 R1.2 and later. Common lumopt2 API # These classes are commonly used in the lumopt2 workflow, and you can directly initialize them from the top-level lumopt2 module. Optimization project Classes and functions for setting up the optimization project. Classes | ``Optimization | Coordinates the optimization workflow for photonic inverse design. | ``OptimizationResult | Immutable result object returned from an optimization run. | ``Project | Main project class that coordinates parametrization, FOM, and solver. | ``ProjectConfig | A class used to modify the base simulation in the Project. | ``FdtdSession | A class to manage the FDTD simulation session. | ``SimulationStatus | FDTD simulation status codes. | ``SimulationError | Exception raised when a simulation fails. Results and FoM Classes and functions for handling simulation results and figures of merit. Classes | ``PortResults | Container for port monitor ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `BaseCallback`
- `Box`
- `CallbackList`
- `ClosedCurve`
- `ClosedCurveCubicSegment`
- `ClosedCurveLinearSegment`
- `CombinedParametrization`
- `EqualSplit`
- `FdtdSession`
- `FieldFom`
- `FieldResults`
- `FileLogger`
- `Fom`
- `FomPanel`
- `GeometryPanel`
- `GradientNormPanel`
- `GraphicalVisualizer`
- `Job`
- `LocalRunner`
- `MonitorPanel`
- `Optimization`
- `OptimizationResult`
- `PNorm`
- `Panel`
- `PanelState`
- `ParamVertex`
- `ParameterScaler`
- `Parametrization`
- `Parametrize`
- `PortFom`
- `PortResults`
- `Profiler`
- `Project`
- `ProjectConfig`
- `ScipyOptimizer`
- `Segment`
- `SimulationError`
- `SimulationStatus`
- `extract_fom`
- `extract_fom_and_gradient`
- `fd_sweep_perturbation`
- `finite_difference_gradient`
- `lumopt2`
- `setup_default_logging`
- `update`
- `validate_bounds`
- `validate_gradient`

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - First row sample: Optimization | Coordinates the optimization workflow for photonic inverse design.
- Table 2: 2 column(s), 2 row(s)
  - First row sample: PortResults | Container for port monitor simulation results.
- Table 3: 2 column(s), 2 row(s)
  - First row sample: Fom | Factory function that returns either a FieldFom or PortFom instance.
- Table 4: 2 column(s), 10 row(s)
  - First row sample: Parametrization | Parametrized geometry using a user-defined function to map parameters.
- Table 5: 2 column(s), 2 row(s)
  - First row sample: ScipyOptimizer | Wrapper for scipy.optimize.minimize optimizers, particularly L-BFGS-B.
- Table 6: 2 column(s), 6 row(s)
  - First row sample: validate_bounds | Validate parameter bounds and return lower/upper arrays.
- Table 7: 2 column(s), 2 row(s)
  - First row sample: LocalRunner | Class to manage simulation jobs locally.
- Table 8: 2 column(s), 10 row(s)
  - First row sample: BaseCallback | Base class for optimization callbacks.
- Table 9: 2 column(s), 1 row(s)
  - First row sample: Profiler | Aggregate wall-clock time per named category.
- Table 10: 2 column(s), 1 row(s)
  - First row sample: setup_default_logging | Configure the lumopt2 logger with sensible defaults.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#lumopt2)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#common-lumopt2-api)
- [Optimization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [OptimizationResult](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#lumopt2.core.optimization.OptimizationResult)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [ProjectConfig](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#lumopt2.core.project_config.ProjectConfig)
- [FdtdSession](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.FdtdSession.html#lumopt2.core.fdtd_session.FdtdSession)
- [SimulationStatus](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationStatus.html#lumopt2.core.fdtd_session.SimulationStatus)
- [SimulationError](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.fdtd_session.SimulationError.html#lumopt2.core.fdtd_session.SimulationError)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [FieldResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#lumopt2.fom.simulation_results.FieldResults)
- [Fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#lumopt2.fom.fom.Fom)
- [PNorm](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.PNorm.html#lumopt2.utils.common.PNorm)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#lumopt2.parametrization.parametrization.Parametrization)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [ClosedCurveLinearSegment](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveLinearSegment.html#lumopt2.parametrization.closed_curve.ClosedCurveLinearSegment)
- [ClosedCurveCubicSegment](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment)
- [CombinedParametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization)
- [Segment](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Segment.html#lumopt2.parametrization.closed_curve.Segment)
- [EqualSplit](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.EqualSplit.html#lumopt2.parametrization.closed_curve.EqualSplit)
- [Parametrize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Parametrize.html#lumopt2.parametrization.closed_curve.Parametrize)
- [ParamVertex](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#lumopt2.parametrization.closed_curve.ParamVertex)
- [Box](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.Box.html#lumopt2.utils.common.Box)
- [ScipyOptimizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer)
- [ParameterScaler](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#lumopt2.optimizer.base_optimizer.ParameterScaler)
- [validate_bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#lumopt2.optimizer.base_optimizer.validate_bounds)
- [extract_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.extract_fom.html#lumopt2.optimizer.base_optimizer.extract_fom)
- [extract_fom_and_gradient](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.extract_fom_and_gradient.html#lumopt2.optimizer.base_optimizer.extract_fom_and_gradient)
- [finite_difference_gradient](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#lumopt2.utils.fd_grad.finite_difference_gradient)
- [validate_gradient](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#lumopt2.utils.fd_grad.validate_gradient)
- [fd_sweep_perturbation](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#lumopt2.utils.fd_grad.fd_sweep_perturbation)
- [LocalRunner](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#lumopt2.utils.runner.LocalRunner)
- [Job](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#lumopt2.utils.runner.Job)
- [BaseCallback](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#lumopt2.utils.callbacks.BaseCallback)
- [CallbackList](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#lumopt2.utils.callbacks.CallbackList)
- [FileLogger](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#lumopt2.utils.file_logger.FileLogger)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [Panel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#lumopt2.utils.panels.Panel)
- [PanelState](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#lumopt2.utils.panels.PanelState)
- [FomPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#lumopt2.utils.panels.FomPanel)
- [GeometryPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#lumopt2.utils.panels.GeometryPanel)
- [GradientNormPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#lumopt2.utils.panels.GradientNormPanel)
- [MonitorPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#lumopt2.utils.panels.MonitorPanel)
- [Profiler](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#lumopt2.utils.profiler.Profiler)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/index.html#all-lumopt2-modules)
- [lumopt2.core](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/core/index.html)
- [lumopt2.fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html)
- [lumopt2.parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/parametrization/index.html)
- [lumopt2.optimizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/optimizer/index.html)
- [lumopt2.utils](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/utils/index.html)

## Ansys-Related External Links Found

- None

## External Links Found

- None
