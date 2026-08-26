# Running parameter sweeps without the CAD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034922933-Running-parameter-sweeps-without-the-CAD  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Running parameter sweeps without the CAD` for the topic `Discovered from FDTD`. It captured 5 heading(s), 14 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Running parameter sweeps without the CAD, Step 1: Adjust model parameters and save a new fsp file for each parameter value, Step 2: Run the simulations, Step 3: Load the results, See also. Key detected terms: analysis, command, fdtd, mode, optimization, script, source, sweep.

## Key Terms

- analysis
- command
- fdtd
- mode
- optimization
- script
- source
- sweep

## Captured Headings

- Running parameter sweeps without the CAD
- Step 1: Adjust model parameters and save a new fsp file for each parameter value
- Step 2: Run the simulations
- Step 3: Load the results
- See also

## Official Text Excerpt

> Running parameter sweeps without the CAD FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT This section describes an alternative way to run parameter sweeps on a separate network (i.e. an external cluster). If your full license is installed on one network (i.e. your office) and your extra engine licenses are installed on an external cluster, then the Job Manager feature of FDTD can't be used. Instead, you will use the full license on your local computer to generate a set of simulation files. These files are then transferred to the cluster. Very often, these jobs will be submitted to the clusters job scheduler. See the Running simulations section for more information on running simulations from the command line (i.e without using the Lumerical Job Manager). When the simulations are finished, the files are transferred back to the local desktop computer. You can then reload the data files and extract the requested information. - Adjust model parameters and save a set of fsp files (a fsp file for each parameter value). - Run all the simulations - Load the simulation files and ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Re-running the parameter sweep Once the sweep is run, a new set of fsp files are saved to a folder. If the sweep is run again, then a set of fsp files will be saved to overwrite the previous files. To avoid overwriting the fsp files, 

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Running simulations](https://optics.ansys.com/hc/en-us/sections/360004588574)
- [Parameter sweeps](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [Resource configuration](https://optics.ansys.com/hc/en-us/articles/360025161033)
- [Running from the command line using MPI for your operating system,](https://optics.ansys.com/hc/en-us/sections/360004588574)
- [Job scheduler submission scripts (SGE, Slurm, Torque)](https://optics.ansys.com/hc/en-us/articles/360039028654)
- [Run a parameter sweep](https://optics.ansys.com/hc/en-us/articles/360034922873)
- [Running simulations on your cluster](https://optics.ansys.com/hc/en-us/articles/360026165714)

## Ansys-Related External Links Found

- None

## External Links Found

- None
