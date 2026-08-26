# FieldResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#fieldresults)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `FieldResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#fieldresults)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 12 link(s), 0 code block(s), 14 inline code term(s), and 1 table(s). Main headings: FieldResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#fieldresults). Key detected terms: fdtd, lumopt, monitor.

## Key Terms

- fdtd
- lumopt
- monitor

## Captured Headings

- FieldResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#fieldresults)

## Official Text Excerpt

> FieldResults # class lumopt2.fom.simulation_results. FieldResults (monitor_name: str, metric: str, wavelengths: List|float|int, tolerance: float = 1e-09, config: object|None = None) # Container for field monitor simulation results. Manages field data (Ex, Ey, Ez) from Lumerical field monitors, providing methods to retrieve and process electromagnetic field distributions. Parameters: monitor_name``str Name of the field monitor in the FDTD simulation. metric``str Metric to extract (should be ‘intensity’). wavelengths`Union``List`,``[float,``int] Wavelength(s) at which to extract metric values, in meters. tolerance``float,`optional` Maximum allowed difference between requested and available wavelengths, in meters. Default is 1e-9. config`ProjectConfig```object,`optional` Multi-forward configuration (default: None). Attributes: monitor_name``str Name of the field monitor. values`anp.ndarray`or``None Total field intensity (|Ex|^2 + |Ey|^2 + |Ez|^2), populated after get_results(). wavelengths``list Requested wavelengths; inherited from BaseResults. Methods | ``FieldResults.extract_wavelengths (...) | Extract metric values at specific wavelengths. | ``FieldResults.get_field_intensity_results (...) | Retrieve field intensity results from a field monitor. | ``FieldResults.get_results (fdtd_session) | Retrieve and extract field monitor results from the FDTD session.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `FieldResults.extract_wavelengths`
- `FieldResults.get_field_intensity_results`
- `FieldResults.get_results`
- `List`
- `None`
- `ProjectConfig`
- `Union`
- `anp.ndarray`
- `float`
- `int`
- `list`
- `object`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: FieldResults.extract_wavelengths (...) | Extract metric values at specific wavelengths.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#fieldresults)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#lumopt2.fom.simulation_results.FieldResults)
- [FieldResults.extract_wavelengths](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.extract_wavelengths.html#lumopt2.fom.simulation_results.FieldResults.extract_wavelengths)
- [FieldResults.get_field_intensity_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.get_field_intensity_results.html#lumopt2.fom.simulation_results.FieldResults.get_field_intensity_results)
- [FieldResults.get_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.get_results.html#lumopt2.fom.simulation_results.FieldResults.get_results)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [float](https://docs.python.org/3/library/functions.html#float)
- [int](https://docs.python.org/3/library/functions.html#int)
- [object](https://docs.python.org/3/library/functions.html#object)
- [None](https://docs.python.org/3/library/constants.html#None)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
