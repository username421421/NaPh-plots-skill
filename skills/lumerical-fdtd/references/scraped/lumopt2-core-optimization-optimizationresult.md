# OptimizationResult [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#optimizationresult)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `OptimizationResult [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#optimizationresult)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 15 link(s), 0 code block(s), 22 inline code term(s), and 1 table(s). Main headings: OptimizationResult [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#optimizationresult). Key detected terms: lumopt, optimization.

## Key Terms

- lumopt
- optimization

## Captured Headings

- OptimizationResult [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#optimizationresult)

## Official Text Excerpt

> OptimizationResult # class lumopt2.core.optimization. OptimizationResult (success: bool, initial_fom: float, final_fom: float, optimal_params: ~numpy.ndarray, num_iterations: int, message: str = '', history: dict = <factory>) # Immutable result object returned from an optimization run. Frozen so user code cannot silently rewrite`final_fom`or`optimal_params`after the fact. The`history`dict is still mutable; callers who need a fully immutable snapshot should`copy`it themselves. Attributes: success bool Whether the optimization completed successfully. initial_fom``float Initial figure of merit value. final_fom``float Final figure of merit value. optimal_params``np.ndarray Optimized parameter values. num_iterations``int Number of optimizer parameter updates performed. Iteration 0 is the baseline evaluation at the initial parameters and is not counted here, so a freshly-completed run with no improvements produces`num_iterations=0`. message``str,`optional` Message from the optimizer (default:`""`). history``dict,`optional` Optimization history with the following keys (default: empty dict): - `'fom'`list of float FOM value at each iteration. - `'params'`list of np.ndarray Parameter array at each iteration. - `'gradient'`list of np.ndarray Gradient array at each iteration (empty for gradient-free optimizers). Attributes | ``OptimizationResult.message | | ``OptimizationResult.success | | ``OptimizationResult.initial_fom | | ``OptimizationResult.final_fom | | ``OptimizationResult.optimal_params | | ``OptimizationResult.num_iterations | | ``OptimizationResult.history |

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `""`
- `'fom'`
- `'gradient'`
- `'params'`
- `OptimizationResult.final_fom`
- `OptimizationResult.history`
- `OptimizationResult.initial_fom`
- `OptimizationResult.message`
- `OptimizationResult.num_iterations`
- `OptimizationResult.optimal_params`
- `OptimizationResult.success`
- `copy`
- `dict`
- `final_fom`
- `float`
- `history`
- `int`
- `np.ndarray`
- `num_iterations=0`
- `optimal_params`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - First row sample: OptimizationResult.message | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#optimizationresult)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.html#lumopt2.core.optimization.OptimizationResult)
- [OptimizationResult.message](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.message.html#lumopt2.core.optimization.OptimizationResult.message)
- [OptimizationResult.success](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.success.html#lumopt2.core.optimization.OptimizationResult.success)
- [OptimizationResult.initial_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.initial_fom.html#lumopt2.core.optimization.OptimizationResult.initial_fom)
- [OptimizationResult.final_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.final_fom.html#lumopt2.core.optimization.OptimizationResult.final_fom)
- [OptimizationResult.optimal_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.optimal_params.html#lumopt2.core.optimization.OptimizationResult.optimal_params)
- [OptimizationResult.num_iterations](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.num_iterations.html#lumopt2.core.optimization.OptimizationResult.num_iterations)
- [OptimizationResult.history](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.optimization.OptimizationResult.history.html#lumopt2.core.optimization.OptimizationResult.history)

## Ansys-Related External Links Found

- None

## External Links Found

- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
- [float](https://docs.python.org/3/library/functions.html#float)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [int](https://docs.python.org/3/library/functions.html#int)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
