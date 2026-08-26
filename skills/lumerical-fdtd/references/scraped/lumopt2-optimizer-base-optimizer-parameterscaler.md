# ParameterScaler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#parameterscaler)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ParameterScaler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#parameterscaler)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 10 link(s), 0 code block(s), 8 inline code term(s), and 2 table(s). Main headings: ParameterScaler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#parameterscaler). Key detected terms: lumopt, optimization, port.

## Key Terms

- lumopt
- optimization
- port

## Captured Headings

- ParameterScaler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#parameterscaler)

## Official Text Excerpt

> ParameterScaler # class lumopt2.optimizer.base_optimizer. ParameterScaler (bounds: List [tuple], target_range: str = 'centered') # Scales parameters between physical and normalized spaces. This class provides consistent parameter scaling for optimizers that work better with normalized parameters. It supports two target ranges: - ‘unit’: [0, 1] - typical for Bayesian optimization - ‘centered’: [-1, 1] - typical for most other optimizers Parameters: bounds``list`of```tuple Physical bounds as list of (min, max) tuples. target_range``str Target range for scaling: ‘unit’ for [0, 1] or ‘centered’ for [-1, 1]. Default is ‘centered’. Attributes: bounds_lower``np.ndarray Lower bounds in physical space. bounds_upper``np.ndarray Upper bounds in physical space. ranges``np.ndarray Parameter ranges (upper - lower). target_range``str The target range (‘unit’ or ‘centered’). Methods | ``ParameterScaler.to_physical (scaled_params[, ...]) | Convert scaled parameters back to physical space. | ``ParameterScaler.to_scaled (params) | Convert physical parameters to scaled space. Attributes | ``ParameterScaler.scaled_bounds | Return bounds in scaled space.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `ParameterScaler.scaled_bounds`
- `ParameterScaler.to_physical`
- `ParameterScaler.to_scaled`
- `list`
- `np.ndarray`
- `of`
- `str`
- `tuple`

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - First row sample: ParameterScaler.to_physical (scaled_params[, ...]) | Convert scaled parameters back to physical space.
- Table 2: 2 column(s), 1 row(s)
  - First row sample: ParameterScaler.scaled_bounds | Return bounds in scaled space.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#parameterscaler)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.html#lumopt2.optimizer.base_optimizer.ParameterScaler)
- [ParameterScaler.to_physical](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.to_physical.html#lumopt2.optimizer.base_optimizer.ParameterScaler.to_physical)
- [ParameterScaler.to_scaled](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.to_scaled.html#lumopt2.optimizer.base_optimizer.ParameterScaler.to_scaled)
- [ParameterScaler.scaled_bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.optimizer.base_optimizer.ParameterScaler.scaled_bounds.html#lumopt2.optimizer.base_optimizer.ParameterScaler.scaled_bounds)

## Ansys-Related External Links Found

- None

## External Links Found

- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
