# Creating parameter sweeps using a script

Source URL: https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Creating parameter sweeps using a script` for the topic `Discovered from FDTD`. It captured 5 heading(s), 12 link(s), 6 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Creating parameter sweeps using a script, Creating the parameter sweep project, Running the parameter sweep, Viewing the results, See also. Key detected terms: analysis, command, dataset, fdtd, mode, optimization, script, sweep.

## Key Terms

- analysis
- command
- dataset
- fdtd
- mode
- optimization
- script
- sweep

## Captured Headings

- Creating parameter sweeps using a script
- Creating the parameter sweep project
- Running the parameter sweep
- Viewing the results
- See also

## Official Text Excerpt

> Creating parameter sweeps using a script FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT This page describes how to generate and run a sweep using script commands. The script commands used in this example could also be applied to optimization and yield analysis. To generate and run the sweep using script commands, user can open the sweep_AR_coating_example_script.fsp file and follow the three steps listed below; or, open and run the script file sweep_AR_coating_example_script.lsf. Creating the parameter sweep project The following commands are used to generate and superficially define a new sweep named "thickness_sweep_script". When the sweep is superficially generated, the parameters can then be defined and added to it. The following commands define the name, type, range and the path of the parameter "thickness". This command adds the parameter "thickness" to the sweep "thickness_sweep_script". When the parameter is successfully added, the sweep will appear in the "Optimizations and Sweeps" tab as shown below. The next step is to add the results that we want to measure into the sweep. The commands listed below define and add the results "R" and "T" ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# add a new sweep and set basic propertiesaddsweep;setsweep("sweep", "name", "thickness_sweep_script");setsweep("thickness_sweep_script", "type", "Ranges");sets`
- Code block 2: 1 line(s); first line `# define the parameter thicknesspara = struct;para.Name = "thickness";para.Parameter = "::model::AR structure::thickness";para.Type = "Length";para.Start = 0.05`
- Code block 3: 1 line(s); first line `# add the parameter thickness to the sweepaddsweepparameter("thickness_sweep_script", para);`
- Code block 4: 1 line(s); first line `# define resultsresult_1 = struct;result_1.Name = "R";result_1.Result = "::model::R::T";result_2 = struct;result_2.Name = "T";result_2.Result = "::model::T::T";`
- Code block 5: 1 line(s); first line `# run the sweeprunsweep("thickness_sweep_script");`
- Code block 6: 1 line(s); first line `# save & view the resultsR = getsweepresult("thickness_sweep_script", "R");T = getsweepresult("thickness_sweep_script", "T");plot(R.thickness*1e9, R.T, "AR thic`

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
- [runsweep - Script command](https://optics.ansys.com/hc/en-us/articles/360034931413-runsweep-Script-command)
- [Parameter sweeps](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [Optimization](https://optics.ansys.com/hc/en-us/articles/360034922953)
- [Yield analysis](https://optics.ansys.com/hc/en-us/articles/360034403194)
- [List of script commands](https://optics.ansys.com/hc/en-us/articles/360037228834)

## Ansys-Related External Links Found

- None

## External Links Found

- None
