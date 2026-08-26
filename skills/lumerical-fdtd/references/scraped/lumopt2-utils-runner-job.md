# Job [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#job)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Job [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#job)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 8 link(s), 0 code block(s), 20 inline code term(s), and 0 table(s). Main headings: Job [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#job). Key detected terms: lumopt, material, python.

## Key Terms

- lumopt
- material
- python

## Captured Headings

- Job [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#job)

## Official Text Excerpt

> Job # class lumopt2.utils.runner. Job (task: str|Callable, label: str, inputs: List [Any]|None = None, dependencies: List [str]|None = None) # Class representing a single job. Parameters: task`Union```[str,`Callable`] Either a path to a .fsp or .py file, or a callable Python function. label``str Unique identifier for the job. Other jobs reference this label in their`dependencies`list to express ordering constraints. inputs`Optional`[`List`[`Any`]],`optional` Input arguments for a Python function task.`None`(the default) indicates that the task should be invoked with no arguments and is treated as such by the runner; pass an empty list explicitly if you want to make the “no arguments” intent visible at the call site. dependencies`Optional``List`[``[str]],`optional` Labels of jobs that must reach the ``’done’`` state before this job is allowed to start.`None`(the default) and an empty list both mean “no dependencies; this job is free to run as soon as the runner picks it up”. Semantics across runner backends: - `LocalRunner`walks the dependency list recursively (`run_dependencies`) and runs each missing dependency synchronously before the dependent job; circular dependencies are detected up front (`check_circular_dependencies`). - Cluster runners (`BashRunner`/ SLURM-style) translate the labels ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `Any`
- `BashRunner`
- `Callable`
- `Job`
- `Job(...)`
- `List`
- `LocalRunner`
- `None`
- `Optional`
- `Union`
- `__init__`
- `afterok:<id1>:<id2>:...`
- `check_circular_dependencies`
- `dependencies`
- `dependencies=[]`
- `inputs=[]`
- `optional`
- `run_dependencies`
- `runjobs`
- `str`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#job)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#lumopt2.utils.runner.Job)
- [Job](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.Job.html#lumopt2.utils.runner.Job)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [Any](https://docs.python.org/3/library/typing.html#typing.Any)
- [None](https://docs.python.org/3/library/constants.html#None)
