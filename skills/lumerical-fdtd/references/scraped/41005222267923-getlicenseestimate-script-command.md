# getlicenseestimate – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/41005222267923-getlicenseestimate-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getlicenseestimate – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 13 link(s), 2 code block(s), 0 inline code term(s), and 2 table(s). Main headings: getlicenseestimate – Script command. Key detected terms: command, fdtd, group, mode, script, script-command, solver, source, structure, sweep.

## Key Terms

- command
- fdtd
- group
- mode
- script
- script-command
- solver
- source
- structure
- sweep

## Captured Headings

- getlicenseestimate – Script command

## Official Text Excerpt

> getlicenseestimate – Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Checks how many licenses is required to run a given resource and returns the result. | Syntax | Description |out = getlicenseestimate(“solver”, “resource”);|Returns a structure outlining the feature license and amount of license required dictated by a given solver specified and the resource. The resource parameter should either be a string indicating the row number in the Resource Configuration window (starting at 1), or a string indicating the name of the resource. If duplicate names are present, the first one is returned. The output structures are specified below. The returned structure is specified below. | Field | Description |feature|The name of the license feature required as specified by the List of licensed features by product. |sharedlicense|Only returned for standard licenses. Indicates whether the selected resource can use standard license sharing. The result is 0 if standard license sharing cannot be used, and 1 if it can be. |single|Indicates the required licenses for a single simulation ran on the selected resource as a string. For standard license, a number is ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `#Obtain output structurelic_struct=getlicenseestimate("FDTD","1"); ?lic_struct.feature; #This returns lum_fdtd_solve, the FDTD license feature needed?lic_struct`
- Code block 2: 1 line(s); first line `lic_struct=getlicenseestimate("FDTD","Local Host"); ?lic_struct.feature; #This returns ‘1 lumerical_solve’, meaning that 1 lumerical_solve license feature is ne`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = getlicenseestimate(“solver”, “resource”); | Returns a structure outlining the feature license and amount of license required dictated by a given solver specified and the resource. The resource parameter should either be a string indic
- Table 2: 2 column(s), 5 row(s)
  - Headers: Field, Description
  - First row sample: feature | The name of the license feature required as specified by the List of licensed features by product.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [List of licensed features by product.](https://optics.ansys.com/hc/en-us/articles/360052724713-List-of-licensed-features-by-product)
- [gpuspecs](https://optics.ansys.com/hc/en-us/articles/34669049884947-gpuspecs-Script-command)
- [Ansys optics solve, accelerator, and Ansys HPC license consumption,](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)
- [,](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [getlicenseestimateallactiveresources](https://optics.ansys.com/hc/en-us/articles/41005384196627-getlicenseestimateallactiveresources-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
