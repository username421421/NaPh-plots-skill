# finite_difference_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#finite-difference-gradient)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html  
Area: Discovered official source  
Topic: Discovered from Optimization session in lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `finite_difference_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#finite-difference-gradient)` for the topic `Discovered from Optimization session in lumopt2`. It captured 1 heading(s), 9 link(s), 0 code block(s), 8 inline code term(s), and 0 table(s). Main headings: finite_difference_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#finite-difference-gradient). Key detected terms: geometry, lumopt, optimization.

## Key Terms

- geometry
- lumopt
- optimization

## Captured Headings

- finite_difference_gradient [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#finite-difference-gradient)

## Official Text Excerpt

> finite_difference_gradient # lumopt2.utils.fd_grad. finite_difference_gradient (project: Project, params: List [float]|ndarray, indices: List [int], perturbation: float = 0.01) → ndarray # Compute the gradient of the figure of merit using finite difference. All perturbed simulations are independent and are queued together then run concurrently, rather than executed one at a time. Parameters: project`lumopt2.Project` Project instance for which the gradient is computed. params`Union``List`,``[np.ndarray] Optimization parameters to update geometry with before computing FOM. indices`List```[int] List of parameter indices to compute the finite difference gradient for. perturbation``float,`optional` Small perturbation value (default: 1e-2). Returns:``np.ndarray Array of computed finite difference gradient values corresponding to the provided indices. Raises:``ValueError If input types are invalid or project is not a lumopt2.Project instance.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `List`
- `Union`
- `ValueError`
- `float`
- `int`
- `lumopt2.Project`
- `np.ndarray`
- `optional`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#finite-difference-gradient)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.finite_difference_gradient.html#lumopt2.utils.fd_grad.finite_difference_gradient)

## Ansys-Related External Links Found

- None

## External Links Found

- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [float](https://docs.python.org/3/library/functions.html#float)
- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [int](https://docs.python.org/3/library/functions.html#int)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
