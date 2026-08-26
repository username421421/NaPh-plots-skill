# Profiler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#profiler)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Profiler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#profiler)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 14 link(s), 0 code block(s), 14 inline code term(s), and 1 table(s). Main headings: Profiler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#profiler). Key detected terms: lumopt.

## Key Terms

- lumopt

## Captured Headings

- Profiler [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#profiler)

## Official Text Excerpt

> Profiler # class lumopt2.utils.profiler. Profiler (enabled: bool = True) # Aggregate wall-clock time per named category. Categories are tracked hierarchically via a context-stack: nesting one``measure() inside another produces a slash-joined full path such as`"compute_gradient/dEps_phase/perturbation_loop"`. Each unique full path is its own bucket and gets its own count / total / min / max statistics. The profiler is enabled by default and can be globally toggled with``enable() /``disable(). When disabled,``measure() is a no-op with sub-microsecond overhead. Parameters: enabled bool,`optional` If True (the default),``measure() records timings. If False,``measure() is a no-op and no statistics are accumulated. Methods | ``Profiler.disable () | Disable timing measurements; subsequent`measure`calls are no-ops. | ``Profiler.enable () | Enable timing measurements. | ``Profiler.format_summary (*[, min_total_seconds]) | Return a tree-formatted string summarizing recorded categories. | ``Profiler.get_stats () | Return a snapshot of the current statistics. | ``Profiler.log_summary ([level, ...]) | Log the formatted summary to a logger. | ``Profiler.measure (name) | Time the wrapped block and accumulate it under`name`. | ``Profiler.reset () | Clear all accumulated statistics and the active context stack.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `"compute_gradient/dEps_phase/perturbation_loop"`
- `Profiler.disable`
- `Profiler.enable`
- `Profiler.format_summary`
- `Profiler.get_stats`
- `Profiler.log_summary`
- `Profiler.measure`
- `Profiler.reset`
- `disable()`
- `enable()`
- `measure`
- `measure()`
- `name`
- `optional`

## Table Inventory

- Table 1: 2 column(s), 7 row(s)
  - First row sample: Profiler.disable () | Disable timing measurements; subsequent measure calls are no-ops.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#profiler)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.html#lumopt2.utils.profiler.Profiler)
- [measure()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.measure.html#lumopt2.utils.profiler.Profiler.measure)
- [enable()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.enable.html#lumopt2.utils.profiler.Profiler.enable)
- [disable()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.disable.html#lumopt2.utils.profiler.Profiler.disable)
- [Profiler.disable](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.disable.html#lumopt2.utils.profiler.Profiler.disable)
- [Profiler.enable](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.enable.html#lumopt2.utils.profiler.Profiler.enable)
- [Profiler.format_summary](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.format_summary.html#lumopt2.utils.profiler.Profiler.format_summary)
- [Profiler.get_stats](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.get_stats.html#lumopt2.utils.profiler.Profiler.get_stats)
- [Profiler.log_summary](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.log_summary.html#lumopt2.utils.profiler.Profiler.log_summary)
- [Profiler.measure](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.measure.html#lumopt2.utils.profiler.Profiler.measure)
- [Profiler.reset](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.profiler.Profiler.reset.html#lumopt2.utils.profiler.Profiler.reset)

## Ansys-Related External Links Found

- None

## External Links Found

- [bool](https://docs.python.org/3/library/functions.html#bool)
- [bool](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values)
