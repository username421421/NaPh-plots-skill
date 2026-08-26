# PanelState [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#panelstate)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `PanelState [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#panelstate)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 19 link(s), 0 code block(s), 22 inline code term(s), and 1 table(s). Main headings: PanelState [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#panelstate). Key detected terms: lumopt.

## Key Terms

- lumopt

## Captured Headings

- PanelState [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#panelstate)

## Official Text Excerpt

> PanelState # class lumopt2.utils.panels. PanelState (iteration: int, iterations: List [int], fom_values: List [float], gradient_norms: List [float], has_gradient_data: bool, current_params: ndarray, initial_params: ndarray|None, current_fom: float) # Immutable per-update snapshot handed to every panel’s`update`call. The`GraphicalVisualizer`builds one`PanelState`at the start of every refresh and passes the same instance to each panel. Panels therefore never have to reach into the visualizer’s internals, which keeps them independently testable. Attributes: iteration``int Current iteration number. Iteration 0 is the baseline evaluation at the initial parameters; 1, 2, … are the optimizer’s updates. iterations``list`of float FOM value recorded at each entry of`iterations`. gradient_norms``list`of```float `||gradient||`recorded at each entry of`iterations`. Entries are`nan`when no gradient was available (e.g. gradient-free optimizers, or iterations where the gradient wasn’t requested). has_gradient_data bool `True`when at least one finite gradient norm has been observed. Lets gradient-aware panels render an “N/A” message instead of a blank chart for purely gradient-free runs. current_params``np.ndarray Parameter vector evaluated at the current iteration. initial_params``np.ndarray or``None Parameter vector at iteration 0 (the baseline).`None`until the first evaluation has happened. current_fom``float FOM value at the current iteration. Convenience alias for`fom_values[-1]`when`iterations`is non-empty. Attributes | ``PanelState.iteration | ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `GraphicalVisualizer`
- `None`
- `PanelState`
- `PanelState.current_fom`
- `PanelState.current_params`
- `PanelState.fom_values`
- `PanelState.gradient_norms`
- `PanelState.has_gradient_data`
- `PanelState.initial_params`
- `PanelState.iteration`
- `PanelState.iterations`
- `True`
- `float`
- `fom_values[-1]`
- `int`
- `iterations`
- `list`
- `nan`
- `np.ndarray`
- `of`
- `update`
- `||gradient||`

## Table Inventory

- Table 1: 2 column(s), 8 row(s)
  - First row sample: PanelState.iteration | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#panelstate)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.html#lumopt2.utils.panels.PanelState)
- [PanelState.iteration](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.iteration.html#lumopt2.utils.panels.PanelState.iteration)
- [PanelState.iterations](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.iterations.html#lumopt2.utils.panels.PanelState.iterations)
- [PanelState.fom_values](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.fom_values.html#lumopt2.utils.panels.PanelState.fom_values)
- [PanelState.gradient_norms](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.gradient_norms.html#lumopt2.utils.panels.PanelState.gradient_norms)
- [PanelState.has_gradient_data](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.has_gradient_data.html#lumopt2.utils.panels.PanelState.has_gradient_data)
- [PanelState.current_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.current_params.html#lumopt2.utils.panels.PanelState.current_params)
- [PanelState.initial_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.initial_params.html#lumopt2.utils.panels.PanelState.initial_params)
- [PanelState.current_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.PanelState.current_fom.html#lumopt2.utils.panels.PanelState.current_fom)

## Ansys-Related External Links Found

- None

## External Links Found

- [int](https://docs.python.org/3/library/functions.html#int)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [float](https://docs.python.org/3/library/functions.html#float)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [None](https://docs.python.org/3/library/constants.html#None)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
