# Analysis Groups - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382454-Analysis-Groups  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Analysis Groups - Simulation object` for the topic `Discovered from FDTD`. It captured 9 heading(s), 13 link(s), 3 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Analysis Groups - Simulation object, Using Analysis Groups, Example:, Setup - Variables, Setup - Script, Analysis - Variables, Analysis - Script, Results. Key detected terms: analysis, command, dataset, far, fdtd, group, import, mode, monitor, optimization, plane, port, script, source, structure, sweep.

## Key Terms

- analysis
- command
- dataset
- far
- fdtd
- group
- import
- mode
- monitor
- optimization
- plane
- port
- script
- source
- structure
- sweep
- transmission

## Captured Headings

- Analysis Groups - Simulation object
- Using Analysis Groups
- Example:
- Setup - Variables
- Setup - Script
- Analysis - Variables
- Analysis - Script
- Results
- See also

## Official Text Excerpt

> Analysis Groups - Simulation object FDTD MODE Analysis objects allow you to group monitors (similar to structure groups) and to analyze that monitor data. For example, a set of monitors can be grouped together to form a closed box. From the raw monitor data, the group can calculate quantities like cross sections and far field projections. The files in this section were created using FDTD, but the same set up can be created using MODE Solution's propagator. Lumerical provides many built in analysis groups in our object library. Please press this button to open the online library of analysis groups, or see object library for more details. Analysis groups are container objects that can contain any simulation object and associated script functions which can be used to customize data analysis. For example, an absorption monitor group can be created with a power monitor, an index monitor, and the script function that calculates absorption from these objects. One can also automate an optimization/parameter sweep procedure using an analysis group made of structures/simulation regions/sources/monitors, and use the script function to update each ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `set("object","parameter",value);         # to set the values of the group parametersrunanalysis;   # to run the analysis routinesgetdata();     # to obtain raw `
- Code block 2: 1 line(s); first line `getresults;  # get packaged dataset`
- Code block 3: 1 line(s); first line `setnamed("trans_box","plot results",0);runanalysis;Pabs = getresult("trans_box","T");?Pabs;?Pabs.T;?Pabs.f;visualize(Pabs);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [object library](https://optics.ansys.com/hc/en-us/articles/360034394494)
- [Scripting Language](https://optics.ansys.com/hc/en-us#kb-anchor)
- [runsetup](https://optics.ansys.com/hc/en-us/articles/360034928893-runsetup-Script-command)
- [save](https://optics.ansys.com/hc/en-us/articles/360034410814-save-Script-command)
- [run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command)
- [selectall](https://optics.ansys.com/hc/en-us/articles/360034408354-selectall-Script-command)
- [Monitors and analysis groups,](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [addanalysisgroup (script command)](https://optics.ansys.com/hc/en-us/articles/360034404074)
- [Structure groups,](https://optics.ansys.com/hc/en-us/articles/360034382434)
- [Object Library](https://optics.ansys.com/hc/en-us/articles/360034394494)

## Ansys-Related External Links Found

- None

## External Links Found

- [Datasets](https://kb.lumerical.com/ref_scripts_datasets.html)
