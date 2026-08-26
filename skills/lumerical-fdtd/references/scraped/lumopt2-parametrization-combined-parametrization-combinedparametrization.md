# CombinedParametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#combinedparametrization)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `CombinedParametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#combinedparametrization)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 15 link(s), 1 code block(s), 17 inline code term(s), and 2 table(s). Main headings: CombinedParametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#combinedparametrization). Key detected terms: fdtd, lumopt, mesh, optimization, port, structure.

## Key Terms

- fdtd
- lumopt
- mesh
- optimization
- port
- structure

## Captured Headings

- CombinedParametrization [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#combinedparametrization)

## Official Text Excerpt

> CombinedParametrization # class lumopt2.parametrization.combined_parametrization. CombinedParametrization (parametrizations: List [BaseParametrization]) # Combine multiple parametrizations into a single parametrization. The optimization parameter vector is the concatenation of each child’s parameters. Bounds, initial values, structure updates, and gradient computations are automatically split and delegated to the corresponding child. All children must share the exact same optimization region. A`ValueError`is raised at construction time if any child’s region differs from the first child’s region. Nesting is not supported: any element of parametrizations that is itself a`CombinedParametrization`raises`TypeError`at construction time. Pass all parametrizations as a single flat list instead. Parameters: parametrizations`List`[`BaseParametrization`] Flat list of parametrization instances to combine. Accepted concrete types are`ClosedCurve`and`Parametrization`. Attributes: parametrizations`List`[`BaseParametrization`] The child parametrization instances. n_params``int Total number of optimization parameters across all children. Raises:``TypeError If any element of parametrizations is not an accepted type, or if any element is itself a`CombinedParametrization`(nesting is not supported). ``ValueError If parametrizations is empty, not a list, or the children have different optimization regions. Examples Methods | ``CombinedParametrization.compute_gradient_from_fields (...) | Compute the gradient by delegating to each child parametrization. | ``CombinedParametrization.compute_opt_params_direct_to_permittivity_jacobian (...) | Compute d_eps/dp, the (sparse) Jacobian of ...

## Code Block Inventory

- Code block 1: 6 line(s); first line `>>> import lumopt2 as lmpt`

## Inline Code Inventory

- `BaseParametrization`
- `ClosedCurve`
- `CombinedParametrization`
- `CombinedParametrization.bounds`
- `CombinedParametrization.compute_gradient_from_fields`
- `CombinedParametrization.compute_opt_params_direct_to_permittivity_jacobian`
- `CombinedParametrization.create_optimization_structures`
- `CombinedParametrization.get_bounds`
- `CombinedParametrization.get_initial_params`
- `CombinedParametrization.store_mesh_info`
- `CombinedParametrization.update_structure`
- `List`
- `Parametrization`
- `TypeError`
- `ValueError`
- `int`
- `structure`

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - First row sample: CombinedParametrization.compute_gradient_from_fields (...) | Compute the gradient by delegating to each child parametrization.
- Table 2: 2 column(s), 1 row(s)
  - First row sample: CombinedParametrization.bounds | Concatenated parameter bounds from all children.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#combinedparametrization)
- [BaseParametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.base_parametrization.BaseParametrization.html#lumopt2.parametrization.base_parametrization.BaseParametrization)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization)
- [CombinedParametrization.compute_gradient_from_fields](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.compute_gradient_from_fields.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.compute_gradient_from_fields)
- [CombinedParametrization.compute_opt_params_direct_to_permittivity_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.compute_opt_params_direct_to_permittivity_jacobian.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.compute_opt_params_direct_to_permittivity_jacobian)
- [CombinedParametrization.create_optimization_structures](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.create_optimization_structures.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.create_optimization_structures)
- [CombinedParametrization.get_bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.get_bounds.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.get_bounds)
- [CombinedParametrization.get_initial_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.get_initial_params.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.get_initial_params)
- [CombinedParametrization.store_mesh_info](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.store_mesh_info.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.store_mesh_info)
- [CombinedParametrization.update_structure](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.update_structure.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.update_structure)
- [CombinedParametrization.bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.bounds.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization.bounds)

## Ansys-Related External Links Found

- None

## External Links Found

- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [int](https://docs.python.org/3/library/functions.html#int)
- [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
