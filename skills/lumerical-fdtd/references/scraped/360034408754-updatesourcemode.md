# updatesourcemode - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034408754-updatesourcemode  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `updatesourcemode - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 15 link(s), 1 code block(s), 0 inline code term(s), and 3 table(s). Main headings: updatesourcemode - Script command. Key detected terms: command, fdtd, mesh, mode, port, script, solver, source.

## Key Terms

- command
- fdtd
- mesh
- mode
- port
- script
- solver
- source

## Captured Headings

- updatesourcemode - Script command

## Official Text Excerpt

> updatesourcemode - Script command FDTD MODE Updates the mode profile of selected mode source. If there is no mode profile stored in the source, then the mode with the highest effective index will be selected. If a mode is already stored in the source, then the mode with the best overlap with the old mode will be selected. Note that the mode source must be selected before running this command. | Syntax | Description | ?updatesourcemode; | Updates mode profile of the selected Mode source. Returns the fraction of electromagnetic fields that overlap between the old and the new mode | ?updatesourcemode(mode_number); | Updates the mode source and selects the desired mode number. For example, updatesourcemode(1); will calculate the fundamental mode. Please note that making this call will force a recalculation of a mode, even if the same mode has previously been calculated. In addition, making this call will force the mode selection method to become "user select". This optional argument was introduced in FDTD 8.6.3 and MODE 6.5.3. | NOTE: Saving simulation files before using updatesourcemode If you have ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `# update the source mode profileselect("source");updatesourcemode;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: ?updatesourcemode; | Updates mode profile of the selected Mode source. Returns the fraction of electromagnetic fields that overlap between the old and the new mode
- Table 2: 1 column(s), 1 row(s)
  - First row sample: NOTE: Saving simulation files before using updatesourcemode If you have a script file which updates the simulation mesh, then you should use the save script command before updating the source mode. This will ensure that the mesh has been up
- Table 3: 1 column(s), 1 row(s)
  - First row sample: NOTE: overlap The fraction of electromagnetic fields that overlap between the two modes is given by the expression below. It is also the fraction of power from mode2 that can propagate in mode1. For more information, please see overlap scri

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [save script command](https://optics.ansys.com/hc/en-us/articles/360034410814-save)
- [overlap script command](https://optics.ansys.com/hc/en-us/articles/360034405254-overlap)
- [Manipulating objects](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [addmode](https://optics.ansys.com/hc/en-us/articles/360034924353-addmode)
- [clearsourcedata](https://optics.ansys.com/hc/en-us/articles/360034929093-clearsourcedata)
- [clearmodedata](https://optics.ansys.com/hc/en-us/articles/360034408774-clearmodedata)
- [getresult](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult)
- [overlap](https://optics.ansys.com/hc/en-us/articles/360034405254-overlap)
- [expand](https://optics.ansys.com/hc/en-us/articles/360034926653-expand)
- [seteigensolver](https://optics.ansys.com/hc/en-us/articles/360034929113-seteigensolver)
- [geteigensolver](https://optics.ansys.com/hc/en-us/articles/360034408794-geteigensolver)
- [updatemode](https://optics.ansys.com/hc/en-us/articles/360034929073-updatemodes)
- [updateportmodes](https://optics.ansys.com/hc/en-us/articles/360034409174-updateportmodes)

## Ansys-Related External Links Found

- None

## External Links Found

- None
