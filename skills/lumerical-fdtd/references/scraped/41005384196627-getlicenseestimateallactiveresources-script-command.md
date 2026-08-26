# getlicenseestimateallactiveresources – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/41005384196627-getlicenseestimateallactiveresources-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getlicenseestimateallactiveresources – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 10 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: getlicenseestimateallactiveresources – Script command. Key detected terms: command, fdtd, mode, script, script-command, solver, source, sweep.

## Key Terms

- command
- fdtd
- mode
- script
- script-command
- solver
- source
- sweep

## Captured Headings

- getlicenseestimateallactiveresources – Script command

## Official Text Excerpt

> getlicenseestimateallactiveresources – Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Obtain the number of licenses needed to run a parameter sweep on all active resources. | Syntax | Description |out = getlicenseestimateallactiveresources(“solver”, “resource_type”);| Returns a string indicating the number of licenses required to run parameter sweep on all active resources specified by the resource_type parameter. If none is specified, defaults to “CPU”: - For FDTD, the parameter can either be “CPU” or “GPU”. - For all other solvers, the parameter can only be “CPU”. Example Two FDTD CPU resources are set up with enterprise license. The first resource has process = 16, threads =1, and capacity =4. The second resource has process = 8, threads =1, and capacity = 3. See Also Ansys optics solve, accelerator, and Ansys HPC license consumption, getlicenseestimate, islicensestandard

## Code Block Inventory

- Code block 1: 1 line(s); first line `?getlicenseestimateallactiveresources("FDTD","CPU"); #Returns ‘1 lumerical_solve AND (104 anshpc OR 9 anshpc_pack),’ indicating the number of HPC packs needed t`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = getlicenseestimateallactiveresources(“solver”, “resource_type”); | Returns a string indicating the number of licenses required to run parameter sweep on all active resources specified by the resource_type parameter. If none is specifi

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [getlicenseestimate](https://optics.ansys.com/hc/en-us/articles/41005222267923-getlicenseestimate-Script-command)
- [islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
