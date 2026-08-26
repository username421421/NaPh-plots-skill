# FomPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#fompanel)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `FomPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#fompanel)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 21 link(s), 0 code block(s), 28 inline code term(s), and 2 table(s). Main headings: FomPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#fompanel). Key detected terms: far, lumopt, mode, optimization.

## Key Terms

- far
- lumopt
- mode
- optimization

## Captured Headings

- FomPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#fompanel)

## Official Text Excerpt

> FomPanel # class lumopt2.utils.panels. FomPanel (title: str|None = 'Optimization Progress', show_best: bool = True, log_y: bool = False, color: str = 'C0', marker: str = 'o', linewidth: float = 2.0, markersize: float = 4.0, label: str = 'FOM') # Live plot of the figure of merit vs. iteration. A single`matplotlib.lines.Line2D`and an annotation`matplotlib.text.Text`are created in``setup() and mutated in place by``update(), so the panel stays inexpensive to redraw even for long runs. Attributes: title``str,`optional` Panel title (default:`'Optimization Progress'`). show_best bool,`optional` If`True`, annotate the best (maximum) FOM value seen so far in the upper-left corner of the panel (default:`True`). log_y bool,`optional` If`True`, render the FOM trace on a logarithmic y-axis. Useful when the FOM spans many decades. Note that non-positive values are clipped by matplotlib in log mode (default:`False`). color``str,`optional` Matplotlib color spec for the trace (default:`'C0'`). marker``str,`optional` Matplotlib marker for the trace (default:`'o'`). linewidth``float,`optional` Line width for the trace (default:`2.0`). markersize``float,`optional` Marker size for the trace (default:`4.0`). label``str,`optional` Legend label for the trace (default:`'FOM'`). Methods | ``FomPanel.on_optimization_end (ax, fig, ...) | Optional hook called once when the optimization completes. | ``FomPanel.setup (ax, ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `'C0'`
- `'FOM'`
- `'Optimization Progress'`
- `'o'`
- `2.0`
- `4.0`
- `False`
- `FomPanel.color`
- `FomPanel.label`
- `FomPanel.linewidth`
- `FomPanel.log_y`
- `FomPanel.marker`
- `FomPanel.markersize`
- `FomPanel.on_optimization_end`
- `FomPanel.requires_forward_results`
- `FomPanel.setup`
- `FomPanel.show_best`
- `FomPanel.title`
- `FomPanel.update`
- `True`
- `ax`
- `float`
- `matplotlib.lines.Line2D`
- `matplotlib.text.Text`
- `optional`
- `setup()`
- `str`
- `update()`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: FomPanel.on_optimization_end (ax, fig, ...) | Optional hook called once when the optimization completes.
- Table 2: 2 column(s), 9 row(s)
  - First row sample: FomPanel.color | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#fompanel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.html#lumopt2.utils.panels.FomPanel)
- [setup()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.setup.html#lumopt2.utils.panels.FomPanel.setup)
- [update()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.update.html#lumopt2.utils.panels.FomPanel.update)
- [FomPanel.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.on_optimization_end.html#lumopt2.utils.panels.FomPanel.on_optimization_end)
- [FomPanel.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.setup.html#lumopt2.utils.panels.FomPanel.setup)
- [FomPanel.update](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.update.html#lumopt2.utils.panels.FomPanel.update)
- [FomPanel.color](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.color.html#lumopt2.utils.panels.FomPanel.color)
- [FomPanel.label](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.label.html#lumopt2.utils.panels.FomPanel.label)
- [FomPanel.linewidth](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.linewidth.html#lumopt2.utils.panels.FomPanel.linewidth)
- [FomPanel.log_y](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.log_y.html#lumopt2.utils.panels.FomPanel.log_y)
- [FomPanel.marker](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.marker.html#lumopt2.utils.panels.FomPanel.marker)
- [FomPanel.markersize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.markersize.html#lumopt2.utils.panels.FomPanel.markersize)
- [FomPanel.requires_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.requires_forward_results.html#lumopt2.utils.panels.FomPanel.requires_forward_results)
- [FomPanel.show_best](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.show_best.html#lumopt2.utils.panels.FomPanel.show_best)
- [FomPanel.title](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.FomPanel.title.html#lumopt2.utils.panels.FomPanel.title)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [float](https://docs.python.org/3/library/functions.html#float)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
