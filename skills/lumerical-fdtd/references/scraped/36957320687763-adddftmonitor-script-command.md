# adddftmonitor - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/36957320687763-adddftmonitor-Script-command  
Area: Script command  
Topic: Add frequency-domain monitor  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `adddftmonitor - Script command` for the topic `Add frequency-domain monitor`. It captured 1 heading(s), 4 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: adddftmonitor - Script command. Key detected terms: command, mesh, monitor, script, script-command.

## Key Terms

- command
- mesh
- monitor
- script
- script-command

## Captured Headings

- adddftmonitor - Script command

## Official Text Excerpt

> adddftmonitor - Script command Adds a frequency domain field profile monitor to the simulation environment. This monitor will snap to the nearest mesh cell to record the data by default. To record data exactly where the monitor is placed, change the “spatial interpolation” settings under “Advanced” in the object properties to “specified position”. Specifics regarding each spatial interpolation option can be found in the Knowledge Base article on Frequeny-domain monitor. | Syntax | Description |adddftmonitor;| Adds a field profile monitor to the simulation environment. This function does not return any data. |adddftmonitor(struct_data);| Adds a field profile monitor and set its property using a struct containing "property" and value pairs. See the struct script command page for an example. This function does not return any data. The following script commands will add a 2D z-normal frequency domain field profile monitor to the simulation region and set its dimension. See Also List of commands, set

## Code Block Inventory

- Code block 1: 1 line(s); first line `adddftmonitor;set("name","field_profile");set("monitor type",7); # 2D z-normalset("x",0);set("x span",5e-6);set("y",0);set("y span",5e-6);set("z",0);`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: adddftmonitor; | Adds a field profile monitor to the simulation environment. This function does not return any data.

## Official Links Found

- [Frequeny-domain monitor](https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-Profile-and-Power-monitor-Simulation-object)
- [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)

## Ansys-Related External Links Found

- None

## External Links Found

- None
