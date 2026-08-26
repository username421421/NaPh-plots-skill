# ProjectConfig [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#projectconfig)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ProjectConfig [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#projectconfig)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 5 link(s), 1 code block(s), 3 inline code term(s), and 1 table(s). Main headings: ProjectConfig [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#projectconfig). Key detected terms: fdtd, lumopt, script.

## Key Terms

- fdtd
- lumopt
- script

## Captured Headings

- ProjectConfig [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#projectconfig)

## Official Text Excerpt

> ProjectConfig # class lumopt2.core.project_config. ProjectConfig (configurator: Callable|str, filename_suffix: str) # A class used to modify the base simulation in the Project. ProjectConfig objects will be owned by a SimulationResults object. Parameters: configurator`Callable`or``str A callable that takes the FDTD object and modifies the simulation, or a string path to a .lsf script file that will be executed. If it’s a callable, it should have the signature: filename_suffix``str A string suffix to add to the filenames of saved project files (not optional). Attributes: configurator`Callable`or``str A callable or string path to an Lumerical .lsf file filename_suffix``str A string suffix to add to the filenames of saved project files. Must NOT be an empty string. Methods | ``ProjectConfig.apply (sim) | Apply the configuration to fresh copy of the base FDTD simulation.

## Code Block Inventory

- Code block 1: 1 line(s); first line `>>> def my_config_function(fdtd: lumapi.FDTD) -> None:`

## Inline Code Inventory

- `Callable`
- `ProjectConfig.apply`
- `str`

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - First row sample: ProjectConfig.apply (sim) | Apply the configuration to fresh copy of the base FDTD simulation.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#projectconfig)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#lumopt2.core.project_config.ProjectConfig)
- [ProjectConfig.apply](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.apply.html#lumopt2.core.project_config.ProjectConfig.apply)

## Ansys-Related External Links Found

- None

## External Links Found

- [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
