# Running Monte Carlo analysis using a script

Source URL: https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Running Monte Carlo analysis using a script` for the topic `Discovered from FDTD`. It captured 5 heading(s), 16 link(s), 7 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Running Monte Carlo analysis using a script, Creating the Monte Carlo analysis, Running the Monte Carlo analysis, Viewing the results, See also. Key detected terms: analysis, command, fdtd, group, mode, optimization, script, sweep.

## Key Terms

- analysis
- command
- fdtd
- group
- mode
- optimization
- script
- sweep

## Captured Headings

- Running Monte Carlo analysis using a script
- Creating the Monte Carlo analysis
- Running the Monte Carlo analysis
- Viewing the results
- See also

## Official Text Excerpt

> Running Monte Carlo analysis using a script FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT This page describes how to generate and run a Monte Carlo analysis using script commands. The Monte Carlo analysis tool allows users to run extensive Monte Carlo analysis, sweeping across multiple parameters. This can be useful for assessing statistical variations of circuit elements on overall circuit performance, as well as the effects of variations in component-level simulations. The same example used in the section "Monte Carlo analysis" will be re-generated in this page. For additional information and detailed implementation of the script commands, please see the "Measurement and optimization data" section. Please note that, all the script commands used in this example could also be applied to sweep and optimization analyses. To generate and run the Monte Carlo analysis using script commands, user can open the run_monte_carlo.icp file and follow the three steps listed below; or, open and run the script file run_monte_carlo_script.lsf. In this article: - Creating the Monte Carlo analysis - Running the Monte Carlo analysis - Viewing the results Creating the Monte Carlo ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `addsweep(2);MC_name = "MC_script";setsweep("Monte Carlo analysis", "name", MC_name);setsweep(MC_name, "number of trials", 50);setsweep(MC_name, "enable seed", 1`
- Code block 2: 1 line(s); first line `# define the parameter cplsetsweep(MC_name, "type", "Parameters");cpl2 = struct;cpl2.Name = "cpl_2";cpl2.Parameter = "::Root Element::WC2::coupling coefficient `
- Code block 3: 1 line(s); first line `# define the model ngwgd_model = struct;wgd_model.Name = "wgd_model";wgd_model.Model = "WGD::group index 1";wgd_model.Value = getnamed("SW1", "group index 1");g`
- Code block 4: 1 line(s); first line `# define the correlationwgd_corr = struct;wgd_corr.Name = "wgd_corr";wgd_corr.Parameters = "SW1_group_index_1,SW2_group_index_1,SW3_group_index_1";wgd_corr.Valu`
- Code block 5: 1 line(s); first line `# define resultsfsr = struct;fsr.Name = "fsr";fsr.Result = "::Root Element              ::Optical Network Analyzer              ::input 2/mode 1/peak/free spect`
- Code block 6: 1 line(s); first line `# run the Monte Carlo analysisrunsweep(MC_name);`
- Code block 7: 1 line(s); first line `# get & view Monte Carlo resultsfsr = getsweepresult(MC_name, "analysis/results/histogram/fsr");fsrCount = fsr.count;fsr = fsr.fsr;pdf = getsweepresult(MC_name,`

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
- [Creating the Monte Carlo analysis](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands#h_21fbd39e-2c29-493d-b4ca-2836e7ba8567)
- [Running the Monte Carlo analysis](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands#h_d4d87076-9409-44f2-8747-b7eeb0e5d3da)
- [Viewing the results](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands#h_84bd0ec4-7554-422f-995d-03a9862bdbd1)
- [Sweep scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922893)
- [Optimization scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922973)
- [Parameter sweeps](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [Monte Carlo analysis](https://optics.ansys.com/hc/en-us/articles/360034403194)
- [Script - Parameters sweeps](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
