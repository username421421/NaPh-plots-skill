# validate_bounds [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#validate-bounds)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `validate_bounds [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#validate-bounds)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 12 link(s), 0 code block(s), 6 inline code term(s), and 0 table(s). Main headings: validate_bounds [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#validate-bounds). Key detected terms: lumopt.

## Key Terms

- lumopt

## Captured Headings

- validate_bounds [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#validate-bounds)

## Official Text Excerpt

> validate_bounds # lumopt2.optimizer.base_optimizer. validate_bounds (bounds: List [tuple], n_params: int, algorithm_name: str = 'Optimizer', require_finite: bool = True) → Tuple [ndarray, ndarray] # Validate parameter bounds and return lower/upper arrays. Parameters: bounds`List```[tuple] Bounds as list of (min, max) tuples. n_params``int Expected number of parameters. algorithm_name``str Name of algorithm for error messages (default: “Optimizer”). require_finite bool If True, reject infinite or None bounds (default: True). Returns: bounds_lower``np.ndarray Lower bounds array of shape (n_params,). bounds_upper``np.ndarray Upper bounds array of shape (n_params,). Raises:``ValueError If bounds are missing, size mismatched, invalid, or non-finite when required.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `List`
- `ValueError`
- `int`
- `np.ndarray`
- `str`
- `tuple`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#validate-bounds)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.validate_bounds.html#lumopt2.optimizer.base_optimizer.validate_bounds)

## Ansys-Related External Links Found

- None

## External Links Found

- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [int](https://docs.python.org/3/library/functions.html#int)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)
- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
