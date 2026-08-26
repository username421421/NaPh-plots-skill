# Creating optimization tasks using a script

Source URL: https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Creating optimization tasks using a script` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 15 link(s), 5 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Creating optimization tasks using a script, Creating the optimization analysis project, Running the optimization analysis, Viewing the results, See also. Key detected terms: analysis, command, fdtd, mode, optimization, reflection, script, sweep.

## Key Terms

- analysis
- command
- fdtd
- mode
- optimization
- reflection
- script
- sweep

## Captured Headings

- Creating optimization tasks using a script
- Creating the optimization analysis project
- Running the optimization analysis
- Viewing the results
- See also

## Official Text Excerpt

> Creating optimization tasks using a script FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT This page describes how to generate and run an optimization analysis using script commands. The optimization of the design is done using an advanced optimization algorithm, which requires running a large number of simulations. This can be much more efficient than running a parameter sweep, particularly if there is more than one parameter to optimize. The same example used in the section "Optimization" will be re-generated in this page. Using script commands to generate the optimization is a convenient way when users already have the parameters at their hands. For additional information and detailed implementation of the script commands, please see the "Measurement and optimization data" section. Please note that, all the script commands used in this example could also be applied to sweep and yield analysis. To generate and run the optimization analysis using script commands, user can open the sweep_AR_coating_example_script.fsp file and follow the three steps listed below; or, open and run the script file optimization_AR_coating_example_script.lsf. In this article: - Creating the optimization analysis project ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# add a new optimization and set basic propertiesaddsweep(1);setsweep("optimization", "name", "thickness_optimization_script");setsweep("thickness_optimization_`
- Code block 2: 1 line(s); first line `# define the parameter thicknesspara = struct;para.Parameter = "::model::AR structure::thickness";para.Type = "Length";para.Min = 0.05e-6;para.Max = 0.15e-6;par`
- Code block 3: 1 line(s); first line `# define figure of meritresult_1 = struct;result_1.Name = "R";result_1.Result = "::model::R::T";result_1.Optimize = true;result_2 = struct;result_2.Name = "T";r`
- Code block 4: 1 line(s); first line `# run optimizationrunsweep("thickness_optimization_script");`
- Code block 5: 1 line(s); first line `# get & view the results - parameter valueR = getsweepresult("thickness_optimization_script", "parameter trend");value = R.getattribute("parameter value");gen =`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Creating the optimization analysis project](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands#h_8f936971-543d-4c9e-afa4-c97376040e98)
- [Running the optimization analysis](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands#h_484ad43d-1be0-46d3-8c98-b1c1526f5293)
- [Viewing the results](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands#h_24cf740d-1ff9-47bd-8f76-d44557fd5f66)
- [Sweep scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922893)
- [Yield scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922993)
- [Parameter sweeps](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [Optimization](https://optics.ansys.com/hc/en-us/articles/360034922953)
- [Yield analysis](https://optics.ansys.com/hc/en-us/articles/360034403194)

## Ansys-Related External Links Found

- None

## External Links Found

- None
