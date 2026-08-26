# validate_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#validate-gradient)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html  
Area: Discovered official source  
Topic: Discovered from Optimization session in lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `validate_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#validate-gradient)` for the topic `Discovered from Optimization session in lumopt2`. It captured 1 heading(s), 10 link(s), 0 code block(s), 8 inline code term(s), and 0 table(s). Main headings: validate_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#validate-gradient). Key detected terms: lumopt, optimization.

## Key Terms

- lumopt
- optimization

## Captured Headings

- validate_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#validate-gradient)

## Official Text Excerpt

> validate_gradient # lumopt2.utils.fd_grad. validate_gradient (project: Project, params: ndarray, indices: List [int] = None, perturbation: float = 0.01) → tuple [ndarray, ndarray, float] # Validate the adjoint gradient by comparing it to a finite difference gradient for specified parameter indices. Parameters: project`lumopt2.Project` Project instance for which the gradient is validated. params``np.ndarray Optimization parameters for gradient computation. indices`List```[int],`optional` List of parameter indices to validate (default: all). perturbation``float Small perturbation value for finite difference. Returns:``tuple (fd_grad, grad_adj_at_indices, err_rel): finite difference gradient, adjoint gradient, relative error. Raises:``ValueError If input types are invalid.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `List`
- `ValueError`
- `float`
- `int`
- `lumopt2.Project`
- `np.ndarray`
- `optional`
- `tuple`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#validate-gradient)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.validate_gradient.html#lumopt2.utils.fd_grad.validate_gradient)

## Ansys-Related External Links Found

- None

## External Links Found

- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [int](https://docs.python.org/3/library/functions.html#int)
- [float](https://docs.python.org/3/library/functions.html#float)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
