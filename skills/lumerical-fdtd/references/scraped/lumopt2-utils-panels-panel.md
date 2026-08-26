# Panel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#panel)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Panel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#panel)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 13 link(s), 0 code block(s), 17 inline code term(s), and 2 table(s). Main headings: Panel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#panel). Key detected terms: fdtd, geometry, lumopt, monitor, optimization.

## Key Terms

- fdtd
- geometry
- lumopt
- monitor
- optimization

## Captured Headings

- Panel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#panel)

## Official Text Excerpt

> Panel # class lumopt2.utils.panels. Panel (title: str|None = None) # Abstract base class for a single subplot in a`GraphicalVisualizer`. Subclasses implement`setup`to create their persistent matplotlib artists and`update`to refresh those artists on every iteration. The default`on_optimization_end`is a no-op; override it for any end-of-run flourishes (e.g. drawing a “converged” marker). Attributes: title``str,`optional` Title for the panel’s subplot. Subclasses pick a sensible default when`None`(default:`None`). requires_forward_results bool Class-level flag. When`True`,`GraphicalVisualizer`ensures the project’s FDTD session has the latest forward simulation file loaded before calling``update(). Override in subclasses that read monitor data from the live FDTD session (e.g.``MonitorPanel). Defaults to`False`so panels whose data comes purely from``PanelState (FOM trace, gradient norm, geometry) avoid the disk reload cost. Methods | ``Panel.on_optimization_end (ax, fig, project, ...) | Optional hook called once when the optimization completes. | ``Panel.setup (ax, fig, project) | Initialise the panel on its assigned axes. | ``Panel.update (ax, fig, project, state) | Refresh the panel from a``PanelState snapshot. Attributes | ``Panel.requires_forward_results | | ``Panel.title |

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `False`
- `GraphicalVisualizer`
- `MonitorPanel`
- `None`
- `Panel.on_optimization_end`
- `Panel.requires_forward_results`
- `Panel.setup`
- `Panel.title`
- `Panel.update`
- `PanelState`
- `True`
- `on_optimization_end`
- `optional`
- `setup`
- `str`
- `update`
- `update()`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: Panel.on_optimization_end (ax, fig, project, ...) | Optional hook called once when the optimization completes.
- Table 2: 2 column(s), 2 row(s)
  - First row sample: Panel.requires_forward_results | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#panel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.html#lumopt2.utils.panels.Panel)
- [update()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.update.html#lumopt2.utils.panels.Panel.update)
- [MonitorPanel](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#lumopt2.utils.panels.MonitorPanel)
- [PanelState](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#lumopt2.utils.panels.PanelState)
- [Panel.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.on_optimization_end.html#lumopt2.utils.panels.Panel.on_optimization_end)
- [Panel.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.setup.html#lumopt2.utils.panels.Panel.setup)
- [Panel.update](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.update.html#lumopt2.utils.panels.Panel.update)
- [Panel.requires_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.requires_forward_results.html#lumopt2.utils.panels.Panel.requires_forward_results)
- [Panel.title](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.Panel.title.html#lumopt2.utils.panels.Panel.title)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
