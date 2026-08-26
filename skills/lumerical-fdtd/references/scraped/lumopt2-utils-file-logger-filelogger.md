# FileLogger [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#filelogger)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: L-bend  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `FileLogger [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#filelogger)` for the topic `Discovered from Getting started with lumopt2: L-bend`. It captured 1 heading(s), 14 link(s), 4 code block(s), 23 inline code term(s), and 1 table(s). Main headings: FileLogger [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#filelogger). Key detected terms: fdtd, lumopt, optimization, structure.

## Key Terms

- fdtd
- lumopt
- optimization
- structure

## Captured Headings

- FileLogger [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#filelogger)

## Official Text Excerpt

> FileLogger # class lumopt2.utils.file_logger. FileLogger (log_file: str|None = None, log_params: bool = True, log_gradients: bool = True, max_logged_params: int|None = 10000) # Record the numerical history of one optimization run to a text file. This callback is a data record, not a progress log. Each evaluation and each iteration is written as a single line containing the FOM value, the parameter vector, optionally the gradient, and the elapsed wall time. The resulting file is intended for plotting, post-hoc inspection, and debugging – not for human-readable status updates (which are handled by the standard`lumopt2`module logger / console). The two streams are orthogonal:`FileLogger`writes dense per-eval numerical data to its own file, while`Optimization.run`emits high-level progress messages through`logging.getLogger("lumopt2")`. The only message`FileLogger`itself emits through the module logger is a single`"Optimization data log: <path>"`info line at the start of the run, so the user knows where the data file lives. All other output – banners, eval rows, iteration rows, gradient rows, the final summary – goes only to`log_file`. Parameters: log_file``str,`optional` Path to the output file. If`None`, automatically saves as`optimization.log`in the project folder (default:`None`). log_params bool,`optional` If`True`, ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `1eval    1, 0.421000, 12.34s, [ 1.000e-06  2.000e-06]`
- Code block 2: 1 line(s); first line `1ITER    3, 0.756000, [ 1.234e-06  5.678e-06]`
- Code block 3: 3 line(s); first line `1file_logger = FileLogger()`
- Code block 4: 3 line(s); first line `1file_logger = FileLogger(log_file="/path/to/run_history.txt")`

## Inline Code Inventory

- `"Optimization data log: <path>"`
- `# Gradient: |grad|=..., [...]`
- `10000`
- `False`
- `FileLogger`
- `FileLogger.close`
- `FileLogger.on_function_eval`
- `FileLogger.on_iteration_end`
- `FileLogger.on_iteration_start`
- `FileLogger.on_optimization_end`
- `FileLogger.on_optimization_start`
- `JSONLogger`
- `None`
- `Optimization.run`
- `True`
- `initial_params`
- `int`
- `log_file`
- `logging.getLogger("lumopt2")`
- `lumopt2`
- `optimization.log`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 6 row(s)
  - First row sample: FileLogger.close () | Close the underlying log-file handle if one is open.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#filelogger)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.html#lumopt2.utils.file_logger.FileLogger)
- [JSONLogger](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.JSONLogger.html#lumopt2.utils.file_logger.JSONLogger)
- [FileLogger.close](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.close.html#lumopt2.utils.file_logger.FileLogger.close)
- [FileLogger.on_function_eval](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.on_function_eval.html#lumopt2.utils.file_logger.FileLogger.on_function_eval)
- [FileLogger.on_iteration_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.on_iteration_end.html#lumopt2.utils.file_logger.FileLogger.on_iteration_end)
- [FileLogger.on_iteration_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.on_iteration_start.html#lumopt2.utils.file_logger.FileLogger.on_iteration_start)
- [FileLogger.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.on_optimization_end.html#lumopt2.utils.file_logger.FileLogger.on_optimization_end)
- [FileLogger.on_optimization_start](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.file_logger.FileLogger.on_optimization_start.html#lumopt2.utils.file_logger.FileLogger.on_optimization_start)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [bool](https://docs.python.org/3/library/functions.html#bool)
- [int](https://docs.python.org/3/library/functions.html#int)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
