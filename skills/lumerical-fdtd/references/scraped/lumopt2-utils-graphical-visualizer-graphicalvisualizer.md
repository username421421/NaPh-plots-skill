# GraphicalVisualizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#graphicalvisualizer)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `GraphicalVisualizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#graphicalvisualizer)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 23 link(s), 2 code block(s), 51 inline code term(s), and 1 table(s). Main headings: GraphicalVisualizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#graphicalvisualizer). Key detected terms: geometry, lumopt, monitor, optimization, python, symmetry.

## Key Terms

- geometry
- lumopt
- monitor
- optimization
- python
- symmetry

## Captured Headings

- GraphicalVisualizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#graphicalvisualizer)

## Official Text Excerpt

> GraphicalVisualizer # class lumopt2.utils.graphical_visualizer. GraphicalVisualizer (panels: List [Panel]|None = None, layout: Tuple [int, int]|None = None, figsize: Tuple [float, float] = (12, 5), update_interval: int = 1, block_on_end: bool = False, save_plots: bool = True, save_dpi: int = 150, filename_prefix: str = 'optimization_plot', show_window: bool = True) # Callback that visualizes optimization progress with live matplotlib plots. The visualizer arranges a list of`Panel`instances on a grid of subplots and dispatches the standard panel lifecycle calls (`setup`,`update`,`on_optimization_end`) on every iteration. Users compose figures by passing any combination of built-in panels (`FomPanel`,`GradientNormPanel`,`GeometryPanel`,`MonitorPanel`) and their own`Panel`subclasses. Parameters: panels``list`of``Panel`,`optional` Panels to render. Panels are laid out on the grid in row-major order:`panels[0]`goes in the top-left cell, the rest of the first row is filled left-to-right, then the next row, and so on until`panels[-1]`lands in the bottom-right area. When`None`(default), a sensible default list is built at``on_optimization_start(): - `FomPanel`is always included. - `GradientNormPanel`is always included; it falls back to an “N/A” title when no gradient data flows in. - `GeometryPanel`is included only when`project.parametrization`exposes a callable`visualize(ax, params, initial_params)`method. Pass an empty list (`[]`) to disable plotting entirely ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `>>> visualizer = lmpt.GraphicalVisualizer()`
- Code block 2: 17 line(s); first line `>>> from lumopt2 import (FomPanel, GradientNormPanel,`

## Inline Code Inventory

- `"optimization_plot"`
- `(12, 5)`
- `(rows, cols)`
- `1`
- `150`
- `False`
- `FomPanel`
- `GeometryPanel`
- `GradientNormPanel`
- `GraphicalVisualizer`
- `GraphicalVisualizer.on_function_eval`
- `GraphicalVisualizer.on_iteration_end`
- `GraphicalVisualizer.on_iteration_start`
- `GraphicalVisualizer.on_optimization_end`
- `GraphicalVisualizer.on_optimization_start`
- `MonitorPanel`
- `None`
- `Optimization`
- `Panel`
- `True`
- `TypeError`
- `ValueError`
- `[]`
- `_2`
- `_3`
- `block_on_end`
- `figsize`
- `float`
- `int`
- `layout`
- `list`
- `of`
- `on_optimization_end`
- `on_optimization_end()`
- `on_optimization_start()`
- `optional`
- `panels`
- `panels[-1]`
- `panels[0]`
- `project.parametrization`
- `rows * cols >= len(panels)`
- `save_dpi`
- `save_plots=True`
- `setup`
- `show_window`
- `str`
- `tuple`
- `update`
- `update_interval`
- `visualize(ax, params, initial_params)`
- `{filename_prefix}_iter_{iteration:04d}.png`

## Table Inventory

- Table 1: 2 column(s), 5 row(s)
  - First row sample: GraphicalVisualizer.on_function_eval (...[, ...]) | Record the initial parameter vector on the first evaluation.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#graphicalvisualizer)
- [Panel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#lumopt2.utils.panels.Panel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [on_optimization_start()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_start.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_start)
- [on_optimization_end()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_end.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_end)
- [GraphicalVisualizer](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer)
- [GraphicalVisualizer.on_function_eval](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_function_eval.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_function_eval)
- [GraphicalVisualizer.on_iteration_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_iteration_end.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_iteration_end)
- [GraphicalVisualizer.on_iteration_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_iteration_start.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_iteration_start)
- [GraphicalVisualizer.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_end.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_end)
- [GraphicalVisualizer.on_optimization_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_start.html#lumopt2.utils.graphical_visualizer.GraphicalVisualizer.on_optimization_start)

## Ansys-Related External Links Found

- None

## External Links Found

- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [None](https://docs.python.org/3/library/constants.html#None)
- [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)
- [int](https://docs.python.org/3/library/functions.html#int)
- [float](https://docs.python.org/3/library/functions.html#float)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
