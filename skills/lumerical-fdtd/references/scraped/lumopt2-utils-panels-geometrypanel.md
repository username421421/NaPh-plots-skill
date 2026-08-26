# GeometryPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#geometrypanel)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `GeometryPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#geometrypanel)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 17 link(s), 0 code block(s), 25 inline code term(s), and 2 table(s). Main headings: GeometryPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#geometrypanel). Key detected terms: geometry, lumopt, optimization, port.

## Key Terms

- geometry
- lumopt
- optimization
- port

## Captured Headings

- GeometryPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#geometrypanel)

## Official Text Excerpt

> GeometryPanel # class lumopt2.utils.panels. GeometryPanel (title: str|None = 'Geometry Evolution', parametrization: Any|None = None, aspect: str = 'equal', xlabel: str = 'x (m)', ylabel: str = 'y (m)') # Live plot of the current geometry on top of the initial baseline. Defers all drawing to`parametrization.visualize(ax, params, initial_params)`. By default uses`project.parametrization`(the one being optimized), but an explicit override lets you display a secondary parametrization (e.g. a coarse preview during topology runs). The chosen parametrization is validated in``setup() so a missing`visualize`method is reported once at startup with a clear error rather than per-iteration tracebacks. Attributes: parametrization``object,`optional` Parametrization to render. When`None`(default), uses`project.parametrization`resolved at``setup() time. title``str,`optional` Panel title (default:`'Geometry Evolution'`). aspect``str,`optional` Matplotlib axes aspect for the plot.`'equal'`keeps x and y at the same scale, which is almost always what you want for spatial geometries (default:`'equal'`). xlabel``str,`optional` Label for the x-axis (default:`'x (m)'`). ylabel``str,`optional` Label for the y-axis (default:`'y (m)'`). Raises:``TypeError Raised by``setup() when neither the explicit`parametrization`nor`project.parametrization`exposes a callable`visualize(ax, params, initial_params)`. Methods | ``GeometryPanel.on_optimization_end (ax, fig, ...) | Optional hook called once when the optimization completes. | ``GeometryPanel.setup (ax, fig, project) | Resolve the parametrization, ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `'Geometry Evolution'`
- `'equal'`
- `'x (m)'`
- `'y (m)'`
- `GeometryPanel.aspect`
- `GeometryPanel.on_optimization_end`
- `GeometryPanel.parametrization`
- `GeometryPanel.requires_forward_results`
- `GeometryPanel.setup`
- `GeometryPanel.title`
- `GeometryPanel.update`
- `GeometryPanel.xlabel`
- `GeometryPanel.ylabel`
- `None`
- `TypeError`
- `object`
- `optional`
- `parametrization`
- `parametrization.visualize`
- `parametrization.visualize(ax, params, initial_params)`
- `project.parametrization`
- `setup()`
- `str`
- `visualize`
- `visualize(ax, params, initial_params)`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: GeometryPanel.on_optimization_end (ax, fig, ...) | Optional hook called once when the optimization completes.
- Table 2: 2 column(s), 6 row(s)
  - First row sample: GeometryPanel.aspect | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#geometrypanel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.html#lumopt2.utils.panels.GeometryPanel)
- [setup()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.setup.html#lumopt2.utils.panels.GeometryPanel.setup)
- [GeometryPanel.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.on_optimization_end.html#lumopt2.utils.panels.GeometryPanel.on_optimization_end)
- [GeometryPanel.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.setup.html#lumopt2.utils.panels.GeometryPanel.setup)
- [GeometryPanel.update](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.update.html#lumopt2.utils.panels.GeometryPanel.update)
- [GeometryPanel.aspect](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.aspect.html#lumopt2.utils.panels.GeometryPanel.aspect)
- [GeometryPanel.parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.parametrization.html#lumopt2.utils.panels.GeometryPanel.parametrization)
- [GeometryPanel.requires_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.requires_forward_results.html#lumopt2.utils.panels.GeometryPanel.requires_forward_results)
- [GeometryPanel.title](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.title.html#lumopt2.utils.panels.GeometryPanel.title)
- [GeometryPanel.xlabel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.xlabel.html#lumopt2.utils.panels.GeometryPanel.xlabel)
- [GeometryPanel.ylabel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.GeometryPanel.ylabel.html#lumopt2.utils.panels.GeometryPanel.ylabel)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [Any](https://docs.python.org/3/library/typing.html#typing.Any)
- [object](https://docs.python.org/3/library/functions.html#object)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
