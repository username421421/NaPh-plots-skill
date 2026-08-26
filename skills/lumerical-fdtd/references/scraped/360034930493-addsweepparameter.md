# addsweepparameter - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930493-addsweepparameter  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addsweepparameter - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 21 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: addsweepparameter - Script command. Key detected terms: analysis, command, fdtd, mode, optimization, s-parameter, script, sweep, symmetry.

## Key Terms

- analysis
- command
- fdtd
- mode
- optimization
- s-parameter
- script
- sweep
- symmetry

## Captured Headings

- addsweepparameter - Script command

## Official Text Excerpt

> addsweepparameter - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Adds a parameter to a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. | Syntax | Description | addsweepparameter("name", "parameter"); | Adds a parameter to a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "parameter" could be a string (i.e. create a parameter with default values. eg. ::model::rectangle::index) or a struct which counld contain parameter, type, start, stop, unit, etc. Returns the parameter name. Example This example shows how to add a parameter to an existing optimization. This piece of script command is taken from the example file sweep_AR_coating_example_script.lsf in the example page Optimization scripting commands. This example shows how to add a parameter sweep which sweeps 5 values of a thickness parameter. This example shows how to add an S-parameter sweep and set up the rows of the S-matrix mapping table manually. This script can be used with the example in S-parameter matrix sweep and it generates the same table without using the "auto symmetry" option for mapping between rows. This manual mapping is not ...

## Code Block Inventory

- Code block 1: 15 line(s); first line `# add a sweep`
- Code block 2: 14 line(s); first line `addsweep(0);setsweep("sweep","name","thickness_sweep");`
- Code block 3: 50 line(s); first line `##ADD SWEEP##deletesweep("s-parameter sweep"); # if a sweep task named s-parameter sweep already exists, remove it`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: addsweepparameter("name", "parameter"); | Adds a parameter to a parameter sweep/optimization/Monte Carlo/S-parameter sweep item. "name" is the absolute name of an analysis item. "parameter" could be a string (i.e. create a parameter with de

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Optimization scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922973-Optimization-scripting-commands)
- [S-parameter matrix sweep](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [copysweep](https://optics.ansys.com/hc/en-us/articles/360034930373-copysweep)
- [pastesweep](https://optics.ansys.com/hc/en-us/articles/360034930393-pastesweep)
- [addsweep](https://optics.ansys.com/hc/en-us/articles/360034404254-addsphere)
- [insertsweep](https://optics.ansys.com/hc/en-us/articles/360034930433-insertsweep)
- [getsweep](https://optics.ansys.com/hc/en-us/articles/360034930453-getsweep)
- [setsweep](https://optics.ansys.com/hc/en-us/articles/360034930473-setsweep-Script-command)
- [addsweepresult](https://optics.ansys.com/hc/en-us/articles/360034410034-addsweepresult)
- [removesweepparameter](https://optics.ansys.com/hc/en-us/articles/360034930513-removesweepparameter)
- [removesweepresult](https://optics.ansys.com/hc/en-us/articles/360034930533-removesweepresult)
- [Sweep scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922893-Sweep-scripting-commands)
- [Monte Carlo scripting commands](https://optics.ansys.com/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)

## Ansys-Related External Links Found

- None

## External Links Found

- None
