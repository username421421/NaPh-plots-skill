# CallbackList [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#callbacklist)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `CallbackList [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#callbacklist)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 9 link(s), 0 code block(s), 15 inline code term(s), and 1 table(s). Main headings: CallbackList [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#callbacklist). Key detected terms: lumopt, optimization.

## Key Terms

- lumopt
- optimization

## Captured Headings

- CallbackList [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#callbacklist)

## Official Text Excerpt

> CallbackList # class lumopt2.utils.callbacks. CallbackList (callbacks: list) # Container for managing multiple callbacks. Each`BaseCallback`hook now defaults to a no-op, so this dispatcher simply forwards the event to every callback in turn - the previous`hasattr`/`callable`guards were defensive against callbacks that didn’t implement every hook, which is no longer a concern. Parameters: callbacks``list`of```BaseCallback List of callback objects to manage. Methods | ``CallbackList.on_function_eval (project, ...) | Call`on_function_eval`on every registered callback. | ``CallbackList.on_iteration_end (project, ...) | Call`on_iteration_end`on every registered callback. | ``CallbackList.on_iteration_start (iteration, ...) | Call`on_iteration_start`on every registered callback. | ``CallbackList.on_optimization_end (success, ...) | Call`on_optimization_end`on every registered callback. | ``CallbackList.on_optimization_start (project) | Call`on_optimization_start`on every registered callback.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `BaseCallback`
- `CallbackList.on_function_eval`
- `CallbackList.on_iteration_end`
- `CallbackList.on_iteration_start`
- `CallbackList.on_optimization_end`
- `CallbackList.on_optimization_start`
- `callable`
- `hasattr`
- `list`
- `of`
- `on_function_eval`
- `on_iteration_end`
- `on_iteration_start`
- `on_optimization_end`
- `on_optimization_start`

## Table Inventory

- Table 1: 2 column(s), 5 row(s)
  - First row sample: CallbackList.on_function_eval (project, ...) | Call on_function_eval on every registered callback.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#callbacklist)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.html#lumopt2.utils.callbacks.CallbackList)
- [BaseCallback](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.BaseCallback.html#lumopt2.utils.callbacks.BaseCallback)
- [CallbackList.on_function_eval](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.on_function_eval.html#lumopt2.utils.callbacks.CallbackList.on_function_eval)
- [CallbackList.on_iteration_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.on_iteration_end.html#lumopt2.utils.callbacks.CallbackList.on_iteration_end)
- [CallbackList.on_iteration_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.on_iteration_start.html#lumopt2.utils.callbacks.CallbackList.on_iteration_start)
- [CallbackList.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.on_optimization_end.html#lumopt2.utils.callbacks.CallbackList.on_optimization_end)
- [CallbackList.on_optimization_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.callbacks.CallbackList.on_optimization_start.html#lumopt2.utils.callbacks.CallbackList.on_optimization_start)

## Ansys-Related External Links Found

- None

## External Links Found

- [list](https://docs.python.org/3/library/stdtypes.html#list)
