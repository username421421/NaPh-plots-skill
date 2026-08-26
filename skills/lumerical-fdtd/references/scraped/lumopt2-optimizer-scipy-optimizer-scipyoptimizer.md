# ScipyOptimizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#scipyoptimizer)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ScipyOptimizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#scipyoptimizer)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 15 link(s), 3 code block(s), 21 inline code term(s), and 2 table(s). Main headings: ScipyOptimizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#scipyoptimizer). Key detected terms: lumopt, optimization, port.

## Key Terms

- lumopt
- optimization
- port

## Captured Headings

- ScipyOptimizer [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#scipyoptimizer)

## Official Text Excerpt

> ScipyOptimizer # class lumopt2.optimizer.scipy_optimizer. ScipyOptimizer (method: str = 'L-BFGS-B', max_iter: int|None = None, max_feval: int|None = None, ftol: float = 1e-06, gtol: float = 1e-05, bounds: list|None = None, options: Dict [str, Any]|None = None, max_eval: int|None = None) # Wrapper for scipy.optimize.minimize optimizers, particularly L-BFGS-B. This class provides a clean interface to scipy’s optimization methods with proper handling of gradients, bounds, and optimization parameters commonly used in photonic inverse design. Parameters: method``str,`optional` Optimization method to use. Supported methods include ‘L-BFGS-B’, ‘BFGS’, ‘CG’, ‘Nelder-Mead’, ‘Powell’, ‘SLSQP’, etc. See scipy.optimize.minimize documentation for full list (default: ‘L-BFGS-B’). max_iter``int,`optional` Maximum number of iterations (default: 100). max_feval``int,`optional` Hard upper bound on the number of objective-function evaluations. A single SciPy iteration may request many evaluations (line search, finite-difference gradients, simplex updates, …), so this knob is independent of`max_iter`. Translates to`maxfun`for`L-BFGS-B`and`maxfev`for`Nelder-Mead`/`Powell`. If the chosen method does not expose a function-evaluation budget, the value is ignored with a warning (default: None). ftol``float,`optional` Tolerance for termination by the change of the objective function. For L-BFGS-B, this is the factr parameter multiplied by machine precision (default: 1e-6). gtol``float,`optional` Tolerance ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `>>> optimizer = ScipyOptimizer(method='L-BFGS-B', max_iter=50)`
- Code block 2: 3 line(s); first line `>>> bounds = [(0, 1) for _ in range(n_params)]`
- Code block 3: 2 line(s); first line `>>> optimizer = ScipyOptimizer(method='SLSQP', max_iter=100, ftol=1e-8)`

## Inline Code Inventory

- `L-BFGS-B`
- `Nelder-Mead`
- `None`
- `Powell`
- `ScipyOptimizer.get_history`
- `ScipyOptimizer.get_result`
- `ScipyOptimizer.is_gradient_free`
- `ScipyOptimizer.optimize`
- `dict`
- `float`
- `int`
- `list`
- `max_feval`
- `max_iter`
- `maxfev`
- `maxfun`
- `of`
- `optional`
- `scipy.optimize.OptimizeResult`
- `str`
- `tuple`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: ScipyOptimizer.get_history () | Get the optimization history.
- Table 2: 2 column(s), 1 row(s)
  - First row sample: ScipyOptimizer.is_gradient_free | Return True if the optimizer uses a gradient-free method.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#scipyoptimizer)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer)
- [ScipyOptimizer.get_history](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.get_history.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.get_history)
- [ScipyOptimizer.get_result](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.get_result.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.get_result)
- [ScipyOptimizer.optimize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.optimize.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.optimize)
- [ScipyOptimizer.is_gradient_free](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.is_gradient_free.html#lumopt2.optimizer.scipy_optimizer.ScipyOptimizer.is_gradient_free)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [int](https://docs.python.org/3/library/functions.html#int)
- [None](https://docs.python.org/3/library/constants.html#None)
- [float](https://docs.python.org/3/library/functions.html#float)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [Dict](https://docs.python.org/3/library/typing.html#typing.Dict)
- [Any](https://docs.python.org/3/library/typing.html#typing.Any)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
