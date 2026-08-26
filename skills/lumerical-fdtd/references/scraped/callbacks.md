# Callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#callbacks)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#callbacks)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 7 heading(s), 15 link(s), 9 code block(s), 18 inline code term(s), and 0 table(s). Main headings: Callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#callbacks), Built-in callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#built-in-callbacks), Visualization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#visualization), Logger [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#logger), Custom callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#custom-callbacks), Structure [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#structure), Trigger timings [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#trigger-timings). Key detected terms: geometry, lumopt, monitor, optimization, structure.

## Key Terms

- geometry
- lumopt
- monitor
- optimization
- structure

## Captured Headings

- Callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#callbacks)
- Built-in callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#built-in-callbacks)
- Visualization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#visualization)
- Logger [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#logger)
- Custom callbacks [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#custom-callbacks)
- Structure [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#structure)
- Trigger timings [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#trigger-timings)

## Official Text Excerpt

> Callbacks # Callbacks are functions that are called at specific points during the optimization, you can use callbacks to visualize and log results during the optimization. To use callbacks, pass a list of callback objects to the``Optimization class as the`callbacks`argument. If you do not explicitly provide any callbacks, a``FileLogger is automatically added so every run produces a log file in the project folder. To disable all callbacks, pass an empty list to the argument`callbacks`. Built-in callbacks # The lumopt2 module provides various built-in callbacks for simple visualization and logging. You can also define your own callbacks as seen in the section below. Visualization # ``GraphicalVisualizer creates a live matplotlib figure that updates as the optimization progresses. You compose the figure from a list of panels, each of which owns one subplot. The visualizer by default saves a PNG image of the figure to the project folder after every update. The following panels are available: - ``FomPanel: plots the figure of merit vs. iteration. - ``GradientNormPanel: plots the gradient norm vs. iteration. - ``GeometryPanel: shows the current geometry, only available for ...

## Code Block Inventory

- Code block 1: 5 line(s); first line `1optimization = lmpt.Optimization(`
- Code block 2: 5 line(s); first line `1optimization = lmpt.Optimization(`
- Code block 3: 2 line(s); first line `1visualizer = lmpt.GraphicalVisualizer()`
- Code block 4: 17 line(s); first line `1visualizer = lmpt.GraphicalVisualizer(`
- Code block 5: 1 line(s); first line `1visualizer = lmpt.GraphicalVisualizer(show_window=False, save_plots=True)`
- Code block 6: 1 line(s); first line `1visualizer = lmpt.GraphicalVisualizer(update_interval=5) # Update only once every 5 iterations`
- Code block 7: 2 line(s); first line `1file_logger = lmpt.FileLogger()`
- Code block 8: 1 line(s); first line `1file_logger = lmpt.FileLogger(log_file='path_to_my_logfile.log')`
- Code block 9: 8 line(s); first line `1import lumopt2 as lmpt`

## Inline Code Inventory

- `BaseCallback`
- `FileLogger`
- `FomPanel`
- `GeometryPanel`
- `GradientNormPanel`
- `GraphicalVisualizer`
- `MonitorPanel`
- `Optimization`
- `callbacks`
- `layout=(rows, cols)`
- `log_file`
- `on_function_eval(self, project, eval_num, params, fom_value, gradient=None, **kwargs)`
- `on_iteration_end(self, project, iteration, params, fom_value, gradient=None, **kwargs)`
- `on_iteration_start(self, iteration, params, **kwargs)`
- `on_optimization_end(self, success, final_fom, final_params, num_iterations, **kwargs)`
- `on_optimization_start(self, project, num_params, bounds, **kwargs)`
- `optimization.log`
- `show_window=False`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#callbacks)
- [Optimization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.Optimization.html#lumopt2.core.optimization.Optimization)
- [FileLogger](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#lumopt2.utils.file_logger.FileLogger)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#built-in-callbacks)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#visualization)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [FomPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#lumopt2.utils.panels.FomPanel)
- [GradientNormPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#lumopt2.utils.panels.GradientNormPanel)
- [GeometryPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#lumopt2.utils.panels.GeometryPanel)
- [MonitorPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#lumopt2.utils.panels.MonitorPanel)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#logger)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#custom-callbacks)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#structure)
- [BaseCallback](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#lumopt2.utils.callbacks.BaseCallback)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/callbacks.html#trigger-timings)

## Ansys-Related External Links Found

- None

## External Links Found

- None
