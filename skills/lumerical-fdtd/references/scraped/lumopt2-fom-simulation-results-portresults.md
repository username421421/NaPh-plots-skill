# PortResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#portresults)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `PortResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#portresults)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 12 link(s), 0 code block(s), 14 inline code term(s), and 1 table(s). Main headings: PortResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#portresults). Key detected terms: fdtd, lumopt, monitor, port, transmission.

## Key Terms

- fdtd
- lumopt
- monitor
- port
- transmission

## Captured Headings

- PortResults [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#portresults)

## Official Text Excerpt

> PortResults # class lumopt2.fom.simulation_results. PortResults (monitor_name: str, metric: str, wavelengths: List|float|int, tolerance: float = 1e-09, config: None = None) # Container for port monitor simulation results. Manages transmission data from Lumerical port monitors, providing methods to retrieve and process transmission values. Parameters: monitor_name``str Name of the port monitor in the FDTD simulation. metric``str Metric to extract (should be ‘transmission’). wavelengths`Union``List`,``[float,``int] Wavelength(s) at which to extract metric values, in meters. tolerance``float,`optional` Maximum allowed difference between requested and available wavelengths, in meters. Default is 1e-9. config`ProjectConfig```object,`optional` Multi-forward configuration (default: None). Attributes: monitor_name``str Name of the port monitor (inherited from BaseResults). values`anp.ndarray`or``None Transmission values, populated after get_results(). wavelengths``list Requested wavelengths; inherited from BaseResults. Methods | ``PortResults.extract_wavelengths (...) | Extract metric values at specific wavelengths. | ``PortResults.get_results (fdtd_session) | Retrieve and extract port monitor results from the FDTD session. | ``PortResults.get_transmission_results (...) | Retrieve transmission results from a port monitor.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `List`
- `None`
- `PortResults.extract_wavelengths`
- `PortResults.get_results`
- `PortResults.get_transmission_results`
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
  - First row sample: PortResults.extract_wavelengths (...) | Extract metric values at specific wavelengths.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#portresults)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [PortResults.extract_wavelengths](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.extract_wavelengths.html#lumopt2.fom.simulation_results.PortResults.extract_wavelengths)
- [PortResults.get_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.get_results.html#lumopt2.fom.simulation_results.PortResults.get_results)
- [PortResults.get_transmission_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.get_transmission_results.html#lumopt2.fom.simulation_results.PortResults.get_transmission_results)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [List](https://docs.python.org/3/library/typing.html#typing.List)
- [float](https://docs.python.org/3/library/functions.html#float)
- [int](https://docs.python.org/3/library/functions.html#int)
- [None](https://docs.python.org/3/library/constants.html#None)
- [object](https://docs.python.org/3/library/functions.html#object)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
