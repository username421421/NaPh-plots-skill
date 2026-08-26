# gnddisconnectedelectricalports – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/52495523728659-gnddisconnectedelectricalports-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `gnddisconnectedelectricalports – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 8 link(s), 6 code block(s), 0 inline code term(s), and 1 table(s). Main headings: gnddisconnectedelectricalports – Script command. Key detected terms: analysis, command, group, mode, port, script, script-command, source.

## Key Terms

- analysis
- command
- group
- mode
- port
- script
- script-command
- source

## Captured Headings

- gnddisconnectedelectricalports – Script command

## Official Text Excerpt

> gnddisconnectedelectricalports – Script command INTERCONNECT Automatically grounds all disconnected input and bidirectional electrical ports in the current group scope. It creates a single Ground Source element and a Node element, then connects all disconnected input and bidirectional electrical ports through the node. Bidirectional electrical ports have a port converter added before connecting to ground. You can only use this command in design mode. An error is returned if used in analysis mode. Warning: You must ensure that the grounding of disconnected electrical ports is intentional and appropriate for your simulation setup. We recommend you review each grounded element and port to verify that grounding of these connections does not adversely impact simulation results. |Syntax|Description |out = gnddisconnectedelectricalports;| Grounds all disconnected input and bidirectional electrical ports in the current group scope. Returns a struct describing which ports were connected, or an empty struct and a warning if no disconnected elements were found. The returned struct contains the following: - Field names of the returned struct describes elements where a disconnected electrical port exists - Field values of the returned struct is ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `out= gnddisconnectedelectricalports;`
- Code block 2: 1 line(s); first line `?out;`
- Code block 3: 3 line(s); first line `Struct with fields:`
- Code block 4: 4 line(s); first line `?out.AM_1;`
- Code block 5: 1 line(s); first line `disconnect("AM_1","modulation");`
- Code block 6: 4 line(s); first line `select("GND_disconnectedelectricalports");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = gnddisconnectedelectricalports; | Grounds all disconnected input and bidirectional electrical ports in the current group scope. Returns a struct describing which ports were connected, or an empty struct and a warning if no disconnecte

## Official Links Found

- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Ground Source element](https://optics.ansys.com/hc/en-us/articles/360036233174-Ground-Source-GND-INTERCONNECT-Element)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [connect](https://optics.ansys.com/hc/en-us/articles/360034929313-connect-Script-command)
- [disconnect](https://optics.ansys.com/hc/en-us/articles/360034408954-disconnect-Script-command)
- [delete](https://optics.ansys.com/hc/en-us/articles/360034928573-delete-Script-command)
- [addelement](https://optics.ansys.com/hc/en-us/articles/360034404694-addelement-Script-command)
- [switchtodesign](https://optics.ansys.com/hc/en-us/articles/360034924013-switchtodesign-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
