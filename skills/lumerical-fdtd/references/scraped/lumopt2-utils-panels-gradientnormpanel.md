# GradientNormPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#gradientnormpanel)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `GradientNormPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#gradientnormpanel)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 17 link(s), 0 code block(s), 23 inline code term(s), and 2 table(s). Main headings: GradientNormPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#gradientnormpanel). Key detected terms: lumopt, optimization.

## Key Terms

- lumopt
- optimization

## Captured Headings

- GradientNormPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#gradientnormpanel)

## Official Text Excerpt

> GradientNormPanel # class lumopt2.utils.panels. GradientNormPanel (title: str|None = 'Gradient Norm', auto_log: bool = True, color: str = 'C3', marker: str = 's', linewidth: float = 2.0, markersize: float = 4.0) # Live plot of the gradient L2 norm vs. iteration. Renders a single line that auto-switches to a logarithmic y-axis once every observed gradient norm is strictly positive (the typical case for converging runs). Iterations without gradient data appear as`nan`and matplotlib draws gaps for them, so the panel works transparently for gradient-free optimizers - it simply re-titles itself to`'<title> (N/A)'`until a gradient shows up. Attributes: title``str,`optional` Panel title (default:`'Gradient Norm'`). auto_log bool,`optional` If`True`, switch to a logarithmic y-axis whenever every non-NaN gradient norm is strictly positive. Set to`False`to force a linear scale (default:`True`). color``str,`optional` Matplotlib color spec for the trace (default:`'C3'`). marker``str,`optional` Matplotlib marker for the trace (default:`'s'`). linewidth``float,`optional` Line width for the trace (default:`2.0`). markersize``float,`optional` Marker size for the trace (default:`4.0`). Methods | ``GradientNormPanel.on_optimization_end (ax, ...) | Optional hook called once when the optimization completes. | ``GradientNormPanel.setup (ax, fig, project) | Create the persistent gradient-norm line on`ax`. | ``GradientNormPanel.update ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `'<title> (N/A)'`
- `'C3'`
- `'Gradient Norm'`
- `'s'`
- `2.0`
- `4.0`
- `False`
- `GradientNormPanel.auto_log`
- `GradientNormPanel.color`
- `GradientNormPanel.linewidth`
- `GradientNormPanel.marker`
- `GradientNormPanel.markersize`
- `GradientNormPanel.on_optimization_end`
- `GradientNormPanel.requires_forward_results`
- `GradientNormPanel.setup`
- `GradientNormPanel.title`
- `GradientNormPanel.update`
- `True`
- `ax`
- `float`
- `nan`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: GradientNormPanel.on_optimization_end (ax, ...) | Optional hook called once when the optimization completes.
- Table 2: 2 column(s), 7 row(s)
  - First row sample: GradientNormPanel.auto_log | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#gradientnormpanel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.html#lumopt2.utils.panels.GradientNormPanel)
- [GradientNormPanel.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.on_optimization_end.html#lumopt2.utils.panels.GradientNormPanel.on_optimization_end)
- [GradientNormPanel.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.setup.html#lumopt2.utils.panels.GradientNormPanel.setup)
- [GradientNormPanel.update](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.update.html#lumopt2.utils.panels.GradientNormPanel.update)
- [GradientNormPanel.auto_log](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.auto_log.html#lumopt2.utils.panels.GradientNormPanel.auto_log)
- [GradientNormPanel.color](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.color.html#lumopt2.utils.panels.GradientNormPanel.color)
- [GradientNormPanel.linewidth](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.linewidth.html#lumopt2.utils.panels.GradientNormPanel.linewidth)
- [GradientNormPanel.marker](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.marker.html#lumopt2.utils.panels.GradientNormPanel.marker)
- [GradientNormPanel.markersize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.markersize.html#lumopt2.utils.panels.GradientNormPanel.markersize)
- [GradientNormPanel.requires_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.requires_forward_results.html#lumopt2.utils.panels.GradientNormPanel.requires_forward_results)
- [GradientNormPanel.title](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GradientNormPanel.title.html#lumopt2.utils.panels.GradientNormPanel.title)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [float](https://docs.python.org/3/library/functions.html#float)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
