# Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#figure-of-merit)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html  
Area: Discovered official source  
Topic: Discovered from Introduction to photonic inverse design with lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#figure-of-merit)` for the topic `Discovered from Introduction to photonic inverse design with lumopt2`. It captured 8 heading(s), 18 link(s), 15 code block(s), 17 inline code term(s), and 1 table(s). Main headings: Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#figure-of-merit), Simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#simulation-results), Defining a figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#defining-a-figure-of-merit), Default functions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#default-functions), Custom functions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#custom-functions), Multiple simulation configuration [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#multiple-simulation-configuration), Example - S-and P polarization sources [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-s-and-p-polarization-sources), Example - multi-wavelength for field region [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-multi-wavelength-for-field-region). Key detected terms: fdtd, import, lumopt, mode, monitor, optimization, port, script, source, transmission.

## Key Terms

- fdtd
- import
- lumopt
- mode
- monitor
- optimization
- port
- script
- source
- transmission

## Captured Headings

- Figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#figure-of-merit)
- Simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#simulation-results)
- Defining a figure of merit [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#defining-a-figure-of-merit)
- Default functions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#default-functions)
- Custom functions [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#custom-functions)
- Multiple simulation configuration [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#multiple-simulation-configuration)
- Example - S-and P polarization sources [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-s-and-p-polarization-sources)
- Example - multi-wavelength for field region [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-multi-wavelength-for-field-region)

## Official Text Excerpt

> Figure of merit # The figure of merit is the device performance metric being optimized. It can incorporate multiple competing objectives by combining them in a user-defined function based on results from the FDTD simulations. In`lumopt2`, the basis of the figure of merit comes from various monitors in the simulation. The monitor results in the simulation are extracted into`lumopt2`as`SimulationResult`objects, which requires the monitor input and a metric. These`SimulationResult`objects are then combined into a figure of merit using the``Fom() function, which takes in the results and applies a function to output a real-valued scalar value. Finally, the``Project class takes in the figure of merit as a part of its inputs. The diagram below illustrates how monitor results are transformed into the figure of merit in`lumopt2`. Simulation results # The lumopt2 module supports the following types of monitors, relating to different type of simulation results metrics. | Monitor | Simulation Result | Metric | Metric Definition | Field region | ``FieldResults | intensity | Sum of \(|E|^2\) over spatial coordinates. | FDTD port object | ``PortResults | transmission | Transmission accounting for ...

## Code Block Inventory

- Code block 1: 3 line(s); first line `1# Create a field result object for a wavelength of 940 nm`
- Code block 2: 4 line(s); first line `1# Create a port result object for a wavelength between 1200nm and 1400nm (O-Band)`
- Code block 3: 4 line(s); first line `1# Define a figure of merit based on a simulation result, using the default function`
- Code block 4: 6 line(s); first line `1intensity_focus = lmpt.FieldResults(monitor_name='focus', metric='intensity', wavelengths = 940e-9)`
- Code block 5: 15 line(s); first line `1trans_ch1 = lmpt.PortResults('port_out1', metric='transmission', wavelengths=wdm_wavelengths[0], tolerance=5e-9)`
- Code block 6: 11 line(s); first line `1#Setup code`
- Code block 7: 2 line(s); first line `1setnamed("source","polarization definition", "S");`
- Code block 8: 2 line(s); first line `1setnamed("source","polarization definition", "P");`
- Code block 9: 9 line(s); first line `1config_S = lmpt.ProjectConfig(configurator='path/to/s1_config.lsf', filename_suffix='S')`
- Code block 10: 6 line(s); first line `1# Configurator scripts included in fom`
- Code block 11: 20 line(s); first line `1#Setup code`
- Code block 12: 4 line(s); first line `1# red_config.lsf`
- Code block 13: 4 line(s); first line `1# blue_config.lsf`
- Code block 14: 10 line(s); first line `1config_red = lmpt.ProjectConfig(configurator=configfile_red, filename_suffix='red')`
- Code block 15: 6 line(s); first line `1# Configurator scripts included in fom`

## Inline Code Inventory

- `FieldResults`
- `Fom()`
- `P-norm`
- `PNorm()`
- `PortResults`
- `Project`
- `ProjectConfig`
- `SimulationResult`
- `T_out`
- `base_simulation.lsf`
- `blue_config.lsf`
- `config`
- `fct`
- `lumopt2`
- `red_config.lsf`
- `s1_config.lsf`
- `s2_config.lsf`

## Table Inventory

- Table 1: 4 column(s), 2 row(s)
  - Headers: Monitor, Simulation Result, Metric, Metric Definition
  - First row sample: Field region | FieldResults | intensity | Sum of \(|E|^2\) over spatial coordinates.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#figure-of-merit)
- [Fom()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.fom.Fom.html#lumopt2.fom.fom.Fom)
- [Project](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project.Project.html#lumopt2.core.project.Project)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#simulation-results)
- [Field region](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
- [FieldResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.FieldResults.html#lumopt2.fom.simulation_results.FieldResults)
- [FDTD port object](https://optics.ansys.com/hc/en-us/articles/360034382554-Ports-FDTD-Simulation-Object)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#defining-a-figure-of-merit)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#default-functions)
- [P-norm](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.PNorm.html#lumopt2.utils.common.PNorm)
- [PNorm()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.PNorm.html#lumopt2.utils.common.PNorm)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#custom-functions)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#multiple-simulation-configuration)
- [ProjectConfig](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.core.project_config.ProjectConfig.html#lumopt2.core.project_config.ProjectConfig)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-s-and-p-polarization-sources)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/figure_of_merit.html#example-multi-wavelength-for-field-region)

## Ansys-Related External Links Found

- None

## External Links Found

- [autograd documentation](https://github.com/HIPS/autograd/blob/master/docs/tutorial.md)
