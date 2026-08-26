# Monte Carlo analysis utility

Source URL: https://optics.ansys.com/hc/en-us/articles/360034403194-Monte-Carlo-analysis  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Monte Carlo analysis utility` for the topic `Discovered from FDTD product reference manual`. It captured 20 heading(s), 13 link(s), 5 code block(s), 0 inline code term(s), and 7 table(s). Main headings: Monte Carlo analysis utility, Monte Carlo properties, Configuration, Parameters, Libraries, Models, Processes, Correlations. Key detected terms: analysis, boundary, command, dataset, fdtd, gaussian, group, mode, optimization, script, sweep.

## Key Terms

- analysis
- boundary
- command
- dataset
- fdtd
- gaussian
- group
- mode
- optimization
- script
- sweep

## Captured Headings

- Monte Carlo analysis utility
- Monte Carlo properties
- Configuration
- Parameters
- Libraries
- Models
- Processes
- Correlations
- Master table
- Results
- Creating the Monte Carlo analysis project
- Monte Carlo seed
- Running the Monte Carlo analysis
- Viewing the results
- Using the library file
- .lib file syntax
- Using the process file
- Process file syntax
- Spatial correlations
- See also

## Official Text Excerpt

> Monte Carlo analysis utility FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT The Monte Carlo analysis tool allows users to run extensive Monte Carlo analysis, sweeping across multiple parameters. This can be useful for assessing statistical variations of circuit elements on overall circuit performance, as well as the effects of variations in component-level simulations. User can specify the parameters to vary and the variation includes "Global" variation, "Local" variation or both. The analyzed parameters can also be defined in a .lib file and if the same element appears several times in a circuit, they could be grouped up as the same "model" and have the same "Global" variation. The correlation between different parameters can also be defined. The available variational distribution types in the tool are: Uniform, Gaussian, Lognormal, Truncated Gaussian, Truncated lognormal, Discrete and Pearson IV. If a .lib file is used, spatial correlations can also be defined for the model parameters (see the “Spatial correlations” section for more information). The tool runs a number of trials with parameters values generated according to a specified distribution and returns the analysis ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `yfsr=getsweepdata("yield ng","fsr");histc(yfsr);`
- Code block 2: 1 line(s); first line `.LIB sigma_1.GLOBALGROUP group_a=(normal,0.1).MODEL WGD "group index 1"=8.05894 GLOBALGROUP=group_a library="".ENDL.LIB sigma_2.GLOBALGROUP group_a=(uniform,0.2`
- Code block 3: 1 line(s); first line `.MODEL MNAME TYPE [PAR=VAL] .GLOBALGROUP group_name[/distrib_type]=val[%]`
- Code block 4: 1 line(s); first line `<process_variation><statistical name="string"> <pattern name="string" distribution="(string,float array)" delta="float" pattern_growth_delta="float array"/><sta`
- Code block 5: 1 line(s); first line `<process_variation><statistical name="statistical_1"><pattern name="hard_mask_bias" distribution="(normal,5e-9)" delta="0" pattern_growth_delta="0 0 0 1"/><stac`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: This feature is only available in INTERCONNECT.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: This feature is only available in INTERCONNECT. The "model" property is in the element's "General" setting tab. All the elements have the same "model" are considered to have identical process hence have the same global variation. Sele
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: This feature is only available in Multiphysics tools and it need to be used with the Layer Builder.
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note: All the parameters that defined in the previous tabs will be listed in the "Master table". The "Master table" is not editable.
- Table 5: 1 column(s), 1 row(s)
  - First row sample: Note: Data Visualization In case no histogram is being populated, try changing the units in the visualizer. Ensuring that the magnitude of values in Axis min and Axis max are larger than 1e-9 can fix the issue.
- Table 6: 1 column(s), 1 row(s)
  - First row sample: Note: All the parameters that defined in the previous tabs will be listed in the "Master table". The "Master table" is not editable.
- Table 7: 2 column(s), 5 row(s)
  - First row sample: distribution: | The variation distribution = (distribution type, standard deviation). Example: distribution = "(normal,5e-9)"

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Custom Element with user defined properties.](https://optics.ansys.com/hc/en-us/articles/360036109594-Custom-Element-with-user-defined-properties)
- [Layer builder - Simulation object](https://optics.ansys.com/hc/en-us/articles/360034382394)
- [Monte Carlo analysis with spatial correlations](https://optics.ansys.com/hc/en-us/articles/360051762393)
- [Monte Carlo scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922993)

## Ansys-Related External Links Found

- None

## External Links Found

- [Optical filters for more information about this circuit.](https://apps.lumerical.com/pic_circuits_optical_filters.html)
- [Optical filters](https://apps.lumerical.com/pic_circuits_optical_filters.html)
