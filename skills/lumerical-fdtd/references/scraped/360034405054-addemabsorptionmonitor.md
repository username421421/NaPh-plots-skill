# addemabsorptionmonitor - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034405054-addemabsorptionmonitor  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `addemabsorptionmonitor - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 6 link(s), 2 code block(s), 0 inline code term(s), and 2 table(s). Main headings: addemabsorptionmonitor - Script command. Key detected terms: command, monitor, plane, port, script, solver, source.

## Key Terms

- command
- monitor
- plane
- port
- script
- solver
- source

## Captured Headings

- addemabsorptionmonitor - Script command

## Official Text Excerpt

> addemabsorptionmonitor - Script command DGTD Adds an absorption monitor to the 'DGTD' solver in Ansys Lumerical Multiphysics™. The monitor reports the power absorbed within the monitor volume. A DGTD solver region must be present in the objects tree for this command to work. |Syntax|Description |addemabsorptionmonitor;| Adds an absorption monitor to the 'DGTD' solver. This function does not return any data. |addemabsorptionmonitor(struct_data);| Adds an absorption monitor and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. Example 1 The following script commands will add an absorption monitor to the 'DGTD' solver already present in the objects tree and print all available properties of the monitor. Example 2 The following script commands will add an absorption monitor to the 'DGTD' solver, change its name, set its frequency span to be the same as the source, and assign it to a solid named "nanoparticle". |NOTE: The script above assumes that there is already a solid named "nanoparticle" and a source named "plane_wave" present in the ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `addemabsorptionmonitor;`
- Code block 2: 6 line(s); first line `addemabsorptionmonitor;`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: addemabsorptionmonitor; | Adds an absorption monitor to the 'DGTD' solver. This function does not return any data.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: NOTE: The script above assumes that there is already a solid named "nanoparticle" and a source named "plane_wave" present in the objects tree.

## Official Links Found

- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [absorption monitor](https://optics.ansys.com/hc/en-us/articles/360034918573)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [adddgtdsolver](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
- [addemfieldmonitor](https://optics.ansys.com/hc/en-us/articles/360034405054-addemabsorptionmonitor)
- [addemfieldtimemonitor](https://optics.ansys.com/hc/en-us/articles/360034925053-addemfieldtimemonitor)

## Ansys-Related External Links Found

- None

## External Links Found

- None
