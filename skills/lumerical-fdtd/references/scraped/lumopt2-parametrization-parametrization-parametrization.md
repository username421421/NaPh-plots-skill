# Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#parametrization)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#parametrization)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 25 link(s), 0 code block(s), 24 inline code term(s), and 2 table(s). Main headings: Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#parametrization). Key detected terms: fdtd, geometry, group, lumopt, mesh, optimization, structure.

## Key Terms

- fdtd
- geometry
- group
- lumopt
- mesh
- optimization
- structure

## Captured Headings

- Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#parametrization)

## Official Text Excerpt

> Parametrization # class lumopt2.parametrization.parametrization. Parametrization (func: Callable [[ndarray], dict [str, Any]], bounds: List [Tuple [float, float]], optimization_region: dict, initial_params: ndarray|None = None, directly_on_params: bool = True, use_jac: bool = True, dp: float|List [float]|None = None) # Parametrized geometry using a user-defined function to map parameters. Parameters: func`Callable`[``[np.ndarray],``dict ``[str,`Any`]] A function that takes a parameter array and returns a dictionary mapping FDTD geometry property paths (strings) to those parameters. Property paths should be in the format “group_name::object_name::property_name” to match Lumerical’s naming convention. bounds`List``Tuple`[``[float,``float]] List of (min, max) tuples defining bounds for each parameter. Should have a length of n_params. optimization_region``dict Dictionary defining the spatial region where optimization occurs. initial_params`Optional```[np.ndarray],`optional` Initial parameter values. If None, uses the midpoint of each bound (default: None). Will always be 1D array of shape (n_params,). directly_on_params bool,`optional` Compute d_eps/dp directly on the optimization parameters (‘p’) if True; if False, compute d_eps/dP with respect to the Lumerical geometry parameters (‘P’) first, and then use chain rule to obtain d_eps/dp. (Default: True). use_jac bool,`optional` If True, use the autograd-computed Jacobian dP/dp of the geometric parameters P with respect ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `Any`
- `Callable`
- `List`
- `None`
- `Optional`
- `Parametrization.bounds`
- `Parametrization.compute_dPgeom`
- `Parametrization.compute_gradient_from_fields`
- `Parametrization.compute_lumerical_to_permittivity_jacobian`
- `Parametrization.compute_opt_params_direct_to_permittivity_jacobian`
- `Parametrization.compute_params_to_lumerical_jacobian`
- `Parametrization.create_optimization_structures`
- `Parametrization.get_bounds`
- `Parametrization.get_initial_params`
- `Parametrization.store_mesh_info`
- `Parametrization.update_structure`
- `Tuple`
- `Union`
- `dict`
- `float`
- `np.ndarray`
- `optional`
- `str`
- `structure`

## Table Inventory

- Table 1: 2 column(s), 10 row(s)
  - First row sample: Parametrization.compute_dPgeom (params) | Compute the perturbation array for calculating d_Eps, i.e., how much ( dP ) should each Lumerical sim geometric property ('P') be perturbed for finite-difference gradient calculations given the opti
- Table 2: 2 column(s), 1 row(s)
  - First row sample: Parametrization.bounds | Parameter bounds for optimization.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#parametrization)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#lumopt2.parametrization.parametrization.Parametrization)
- [Parametrization.compute_dPgeom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.compute_dPgeom.html#lumopt2.parametrization.parametrization.Parametrization.compute_dPgeom)
- [Parametrization.compute_gradient_from_fields](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.compute_gradient_from_fields.html#lumopt2.parametrization.parametrization.Parametrization.compute_gradient_from_fields)
- [Parametrization.compute_lumerical_to_permittivity_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.compute_lumerical_to_permittivity_jacobian.html#lumopt2.parametrization.parametrization.Parametrization.compute_lumerical_to_permittivity_jacobian)
- [Parametrization.compute_opt_params_direct_to_permittivity_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.compute_opt_params_direct_to_permittivity_jacobian.html#lumopt2.parametrization.parametrization.Parametrization.compute_opt_params_direct_to_permittivity_jacobian)
- [Parametrization.compute_params_to_lumerical_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.compute_params_to_lumerical_jacobian.html#lumopt2.parametrization.parametrization.Parametrization.compute_params_to_lumerical_jacobian)
- [Parametrization.create_optimization_structures](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.create_optimization_structures.html#lumopt2.parametrization.parametrization.Parametrization.create_optimization_structures)
- [Parametrization.get_bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.get_bounds.html#lumopt2.parametrization.parametrization.Parametrization.get_bounds)
- [Parametrization.get_initial_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.get_initial_params.html#lumopt2.parametrization.parametrization.Parametrization.get_initial_params)
- [Parametrization.store_mesh_info](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.store_mesh_info.html#lumopt2.parametrization.parametrization.Parametrization.store_mesh_info)
- [Parametrization.update_structure](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.update_structure.html#lumopt2.parametrization.parametrization.Parametrization.update_structure)
- [Parametrization.bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.bounds.html#lumopt2.parametrization.parametrization.Parametrization.bounds)

## Ansys-Related External Links Found

- None

## External Links Found

- [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)
- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [Any](https://docs.python.org/3/library/typing.html#typing.Any)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)
- [float](https://docs.python.org/3/library/functions.html#float)
- [None](https://docs.python.org/3/library/constants.html#None)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
