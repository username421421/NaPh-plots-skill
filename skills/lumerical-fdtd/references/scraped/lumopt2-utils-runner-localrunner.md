# LocalRunner [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#localrunner)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `LocalRunner [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#localrunner)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 22 link(s), 0 code block(s), 21 inline code term(s), and 1 table(s). Main headings: LocalRunner [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#localrunner). Key detected terms: fdtd, lumopt, mode, python, script, source.

## Key Terms

- fdtd
- lumopt
- mode
- python
- script
- source

## Captured Headings

- LocalRunner [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#localrunner)

## Official Text Excerpt

> LocalRunner # class lumopt2.utils.runner. LocalRunner (resource: str = 'GPU', max_retries: int = 2) # Class to manage simulation jobs locally. Parameters: resource``str,`optional` Resource type for computation: “CPU” or “GPU” (default: “GPU”). max_retries``int,`optional` Maximum number of retry attempts for failed simulations that remain in layout mode after running. This can help recover from transient issues like license checkout failures (default: 2). Methods | ``LocalRunner.add_job (task[, inputs, label, ...]) | Add a job to the runner. | ``LocalRunner.check_circular_dependencies () | Check for circular dependencies in the job graph. | ``LocalRunner.clear () | Remove the generated .fsp and .log files, the folder, and clears the jobs | ``LocalRunner.clear_jobs () | Clear all jobs | ``LocalRunner.get_job (label) | Get a job by its label. | ``LocalRunner.get_job_dependencies_ids (job) | Get the job IDs of a job's dependencies. | ``LocalRunner.get_job_result (label) | Get the result of a job by its label. | ``LocalRunner.get_task_type (task) | Get the type of task. | ``LocalRunner.print_job_statuses () | Log the status of all jobs. | ``LocalRunner.pyfct_to_script (fct, inputs, label) | Convert a Python function to a standalone script file. | ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `LocalRunner.add_job`
- `LocalRunner.check_circular_dependencies`
- `LocalRunner.clear`
- `LocalRunner.clear_jobs`
- `LocalRunner.get_job`
- `LocalRunner.get_job_dependencies_ids`
- `LocalRunner.get_job_result`
- `LocalRunner.get_task_type`
- `LocalRunner.print_job_statuses`
- `LocalRunner.pyfct_to_script`
- `LocalRunner.run`
- `LocalRunner.run_dependencies`
- `LocalRunner.run_jobs`
- `LocalRunner.run_queue`
- `LocalRunner.set_done`
- `LocalRunner.set_fdtd_session`
- `LocalRunner.set_job_result`
- `LocalRunner.set_jobid`
- `int`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 18 row(s)
  - First row sample: LocalRunner.add_job (task[, inputs, label, ...]) | Add a job to the runner.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#localrunner)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.html#lumopt2.utils.runner.LocalRunner)
- [LocalRunner.add_job](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.add_job.html#lumopt2.utils.runner.LocalRunner.add_job)
- [LocalRunner.check_circular_dependencies](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.check_circular_dependencies.html#lumopt2.utils.runner.LocalRunner.check_circular_dependencies)
- [LocalRunner.clear](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.clear.html#lumopt2.utils.runner.LocalRunner.clear)
- [LocalRunner.clear_jobs](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.clear_jobs.html#lumopt2.utils.runner.LocalRunner.clear_jobs)
- [LocalRunner.get_job](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.get_job.html#lumopt2.utils.runner.LocalRunner.get_job)
- [LocalRunner.get_job_dependencies_ids](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.get_job_dependencies_ids.html#lumopt2.utils.runner.LocalRunner.get_job_dependencies_ids)
- [LocalRunner.get_job_result](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.get_job_result.html#lumopt2.utils.runner.LocalRunner.get_job_result)
- [LocalRunner.get_task_type](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.get_task_type.html#lumopt2.utils.runner.LocalRunner.get_task_type)
- [LocalRunner.print_job_statuses](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.print_job_statuses.html#lumopt2.utils.runner.LocalRunner.print_job_statuses)
- [LocalRunner.pyfct_to_script](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.pyfct_to_script.html#lumopt2.utils.runner.LocalRunner.pyfct_to_script)
- [LocalRunner.run](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.run.html#lumopt2.utils.runner.LocalRunner.run)
- [LocalRunner.run_dependencies](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.run_dependencies.html#lumopt2.utils.runner.LocalRunner.run_dependencies)
- [LocalRunner.run_jobs](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.run_jobs.html#lumopt2.utils.runner.LocalRunner.run_jobs)
- [LocalRunner.run_queue](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.run_queue.html#lumopt2.utils.runner.LocalRunner.run_queue)
- [LocalRunner.set_done](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.set_done.html#lumopt2.utils.runner.LocalRunner.set_done)
- [LocalRunner.set_fdtd_session](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.set_fdtd_session.html#lumopt2.utils.runner.LocalRunner.set_fdtd_session)
- [LocalRunner.set_job_result](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.set_job_result.html#lumopt2.utils.runner.LocalRunner.set_job_result)
- [LocalRunner.set_jobid](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.runner.LocalRunner.set_jobid.html#lumopt2.utils.runner.LocalRunner.set_jobid)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [int](https://docs.python.org/3/library/functions.html#int)
