# Optimization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#optimization)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: L-bend  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Optimization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#optimization)` for the topic `Discovered from Getting started with lumopt2: L-bend`. It captured 1 heading(s), 14 link(s), 2 code block(s), 40 inline code term(s), and 1 table(s). Main headings: Optimization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#optimization). Key detected terms: far, fdtd, lumopt, monitor, optimization, port.

## Key Terms

- far
- fdtd
- lumopt
- monitor
- optimization
- port

## Captured Headings

- Optimization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#optimization)

## Official Text Excerpt

> Optimization # class lumopt2.core.optimization. Optimization (project, optimizer, callbacks = None, store_all_simulations = False, log_profiling_summary = False) # Coordinates the optimization workflow for photonic inverse design. This class manages the interaction between a Project (which handles simulation and gradient computation) and an Optimizer (which performs the parameter updates). It handles different optimization flows for topology optimization and shape optimization. Parameters: project`Project` The project instance containing the simulation setup, FOM definition, and parametrization. Must have methods for computing FOM and gradients. optimizer`BaseOptimizer` The optimizer instance that will perform the parameter updates. Must have an optimize method that accepts objective and gradient functions. callbacks``list`of``BaseCallback`,`optional` List of callbacks invoked at the standard optimization events (`on_optimization_start`,`on_iteration_start`,`on_function_eval`,`on_iteration_end`,`on_optimization_end`). A single callback may be passed in place of a list. All visualization is performed via callbacks; pass an instance of`lumopt2.utils.GraphicalVisualizer`to monitor optimization progress with live plots. If`None`(the default), a`lumopt2.utils.FileLogger`is installed automatically so that every run produces an`optimization.log`in the project folder. Pass an empty list (`[]`) to disable callbacks entirely. store_all_simulations bool,`optional` If`True`, each iteration writes uniquely-named`.fsp`files (`fwd_default_iter1.fsp`,`fwd_default_iter2.fsp`, …) so the full simulation history is preserved on disk. If`False`(default), ...

## Code Block Inventory

- Code block 1: 9 line(s); first line `>>> project = lmpt.Project(`
- Code block 2: 4 line(s); first line `>>> bounds = [(0, 1) for _ in range(n_pixels)]`

## Inline Code Inventory

- `.fsp`
- `<stem>_output.h5`
- `BaseCallback`
- `BaseOptimizer`
- `DEBUG`
- `False`
- `INFO`
- `None`
- `Optimization.get_history`
- `Optimization.get_optimization_type`
- `Optimization.prepare_optimization`
- `Optimization.run`
- `Project`
- `Project.compute_gradient()`
- `T`
- `True`
- `TypeError`
- `ValueError`
- `[]`
- `adj_default_<monitor>.fsp`
- `dEps/dP`
- `float`
- `fom_eval_count`
- `fwd_default.fsp`
- `fwd_default_iter1.fsp`
- `fwd_default_iter2.fsp`
- `int`
- `list`
- `lumopt2.profiler.log_summary()`
- `lumopt2.utils.FileLogger`
- `lumopt2.utils.GraphicalVisualizer`
- `np.ndarray`
- `of`
- `on_function_eval`
- `on_iteration_end`
- `on_iteration_start`
- `on_optimization_end`
- `on_optimization_start`
- `optimization.log`
- `optional`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - First row sample: Optimization.get_history () | Get the optimization history from the optimizer.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#optimization)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [Optimization.get_history](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.get_history.html#lumopt2.core.optimization.Optimization.get_history)
- [Optimization.get_optimization_type](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.get_optimization_type.html#lumopt2.core.optimization.Optimization.get_optimization_type)
- [Optimization.prepare_optimization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.prepare_optimization.html#lumopt2.core.optimization.Optimization.prepare_optimization)
- [Optimization.run](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.run.html#lumopt2.core.optimization.Optimization.run)

## Ansys-Related External Links Found

- None

## External Links Found

- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
- [int](https://docs.python.org/3/library/functions.html#int)
- [float](https://docs.python.org/3/library/functions.html#float)
- [None](https://docs.python.org/3/library/constants.html#None)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
