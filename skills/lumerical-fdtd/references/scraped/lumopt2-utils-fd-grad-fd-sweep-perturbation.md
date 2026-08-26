# fd_sweep_perturbation [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#fd-sweep-perturbation)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html  
Area: Discovered official source  
Topic: Discovered from Optimization session in lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `fd_sweep_perturbation [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#fd-sweep-perturbation)` for the topic `Discovered from Optimization session in lumopt2`. It captured 1 heading(s), 11 link(s), 0 code block(s), 6 inline code term(s), and 0 table(s). Main headings: fd_sweep_perturbation [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#fd-sweep-perturbation). Key detected terms: convergence, lumopt, optimization, sweep.

## Key Terms

- convergence
- lumopt
- optimization
- sweep

## Captured Headings

- fd_sweep_perturbation [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#fd-sweep-perturbation)

## Official Text Excerpt

> fd_sweep_perturbation # lumopt2.utils.fd_grad. fd_sweep_perturbation (project: Project, params: ndarray, index: int, perturbation_values: List [float]|ndarray) → tuple [ndarray, ndarray] # Finite difference convergence test: compute the finite difference gradient for a range of perturbation values and plot the results. All perturbed simulations across all perturbation values are queued together and run concurrently. Parameters: project`lumopt2.Project` Project instance for which the convergence test is performed. params``np.ndarray Optimization parameters for gradient computation. index``int Parameter index to test. perturbation_values``list or``np.ndarray List of perturbation values to test. Returns:``tuple (fd_grad_val, fd_grad_diff): finite difference gradients for each perturbation, difference between consecutive gradients. Raises:``ValueError If input types are invalid.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `ValueError`
- `int`
- `list`
- `lumopt2.Project`
- `np.ndarray`
- `tuple`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#fd-sweep-perturbation)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.fd_grad.fd_sweep_perturbation.html#lumopt2.utils.fd_grad.fd_sweep_perturbation)

## Ansys-Related External Links Found

- None

## External Links Found

- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [int](https://docs.python.org/3/library/functions.html#int)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [float](https://docs.python.org/3/library/functions.html#float)
- [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
