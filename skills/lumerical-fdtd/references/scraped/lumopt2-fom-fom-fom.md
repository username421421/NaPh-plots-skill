# Fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#fom)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#fom)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 8 link(s), 0 code block(s), 14 inline code term(s), and 0 table(s). Main headings: Fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#fom). Key detected terms: lumopt, monitor, port.

## Key Terms

- lumopt
- monitor
- port

## Captured Headings

- Fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#fom)

## Official Text Excerpt

> Fom # lumopt2.fom.fom. Fom (sim_results: FieldResults|PortResults|list, fct: callable = None) # Factory function that returns either a`FieldFom`or`PortFom`instance. Inspects the types in`sim_results`and instantiates the appropriate subclass. All monitors must be of the same type. Parameters: sim_results`FieldResults`or`PortResults`or``list`of``those` One or more monitor result objects. fct``callable(),`optional` User-supplied scalar function of the monitor values. If`None`, a sensible default is used:`mean()`for field-based monitors and``PNorm() (with default parameters) for port-based monitors. Returns:`FieldFom`or`PortFom` Appropriate FOM subclass instance. Raises:``ValueError If`sim_results`is empty. ``ValueError If`sim_results`contains objects that are neither`FieldResults`nor`PortResults`. ``ValueError If monitors are of mixed types (some field, some port).

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `FieldFom`
- `FieldResults`
- `None`
- `PNorm()`
- `PortFom`
- `PortResults`
- `ValueError`
- `callable()`
- `list`
- `mean()`
- `of`
- `optional`
- `sim_results`
- `those`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#fom)
- [FieldResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#lumopt2.fom.simulation_results.FieldResults)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#lumopt2.fom.fom.Fom)
- [PNorm()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.PNorm.html#lumopt2.utils.common.PNorm)

## Ansys-Related External Links Found

- None

## External Links Found

- [list](https://docs.python.org/3/library/stdtypes.html#list)
- [callable()](https://docs.python.org/3/library/functions.html#callable)
- [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)
