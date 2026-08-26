# BaseCallback [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#basecallback)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `BaseCallback [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#basecallback)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 7 link(s), 0 code block(s), 11 inline code term(s), and 1 table(s). Main headings: BaseCallback [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#basecallback). Key detected terms: lumopt, monitor, optimization.

## Key Terms

- lumopt
- monitor
- optimization

## Captured Headings

- BaseCallback [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#basecallback)

## Official Text Excerpt

> BaseCallback # class lumopt2.utils.callbacks. BaseCallback # Base class for optimization callbacks. Callbacks are invoked at various points during optimization to enable logging, visualization, checkpointing, or other monitoring tasks. All hook methods default to no-ops, so subclasses only need to override the events they actually care about. Concrete callbacks typically implement either the`*_iteration_*`pair (for per-step bookkeeping such as the visualizer) or just`on_function_eval`(for everything-fires-on-every-eval loggers); both flavours coexist happily with the no-op defaults supplied here. Hooks fire in this order: - `on_optimization_start`– once at the beginning. - `on_function_eval`– after each objective-function evaluation. - `on_iteration_start`– before each iteration (if the optimizer exposes iteration boundaries). - `on_iteration_end`– after each iteration (idem). - `on_optimization_end`– once at the end. SciPy-driven optimizers expose both per-iteration and per-evaluation hooks; gradient-free or single-pass optimizers may only fire`on_function_eval`. Subclasses that only care about iteration boundaries can therefore safely leave`on_function_eval`at the no-op default and vice-versa. Methods | ``BaseCallback.on_function_eval (project, ...) | Called after each objective function evaluation. | ``BaseCallback.on_iteration_end (project, ...) | Called at the end of each iteration. | ``BaseCallback.on_iteration_start (iteration, ...) | Called at the start of each iteration. ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `*_iteration_*`
- `BaseCallback.on_function_eval`
- `BaseCallback.on_iteration_end`
- `BaseCallback.on_iteration_start`
- `BaseCallback.on_optimization_end`
- `BaseCallback.on_optimization_start`
- `on_function_eval`
- `on_iteration_end`
- `on_iteration_start`
- `on_optimization_end`
- `on_optimization_start`

## Table Inventory

- Table 1: 2 column(s), 5 row(s)
  - First row sample: BaseCallback.on_function_eval (project, ...) | Called after each objective function evaluation.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#basecallback)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#lumopt2.utils.callbacks.BaseCallback)
- [BaseCallback.on_function_eval](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.on_function_eval.html#lumopt2.utils.callbacks.BaseCallback.on_function_eval)
- [BaseCallback.on_iteration_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.on_iteration_end.html#lumopt2.utils.callbacks.BaseCallback.on_iteration_end)
- [BaseCallback.on_iteration_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.on_iteration_start.html#lumopt2.utils.callbacks.BaseCallback.on_iteration_start)
- [BaseCallback.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.on_optimization_end.html#lumopt2.utils.callbacks.BaseCallback.on_optimization_end)
- [BaseCallback.on_optimization_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.on_optimization_start.html#lumopt2.utils.callbacks.BaseCallback.on_optimization_start)

## Ansys-Related External Links Found

- None

## External Links Found

- None
