# gpuspecs – Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/34669049884947-gpuspecs-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `gpuspecs – Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 3 link(s), 2 code block(s), 0 inline code term(s), and 2 table(s). Main headings: gpuspecs – Script command. Key detected terms: command, fdtd, script, script-command, source, structure.

## Key Terms

- command
- fdtd
- script
- script-command
- source
- structure

## Captured Headings

- gpuspecs – Script command

## Official Text Excerpt

> gpuspecs – Script command FDTD Obtains specifications of all GPUs in the system and return as a cell array. Each element of the cell array represents a physical GPU installed in the system, and contains a structure with fields showing its specifications. | Syntax | Description | gpuspecs; | Returns a cell array representing all installed GPUs in the system, elements to each cell are structs that show individual specifications. Details of each struct are shown below. Each structure in the cell array will have the following fields | Field | Description |availableDeviceMemoryKb|Available Video RAM (VRAM) of the GPU in Kilobytes (KB). |bus|Index for the bus of the device |deviceSMCount|Number of streaming microprocessors in the GPU. |deviceTotalMemoryKb|Total VRAM of the GPU in KB. |deviceUUID|Unique Identifier for the GPU. |domain|The Peripheral Component Interconnect (PCI) domain of the device. |maxLinkSpeedMBPS|Maximum link speed of the GPU’s PCI express (PCIe) interface in MPBS. |maxlinkWidth|Maximum link width of the GPU and its PCIe interface. |memoryBusWidth|Memory bus width of the GPU in Megabytes-per-second (MBPS). |nvmlDeviceIndex|Index of GPU for Resource Configuration. |userReadableDeviceName|Human-readable name for the GPU. Example ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `gpus_cell = gpuspecs; #save cell array of all GPU specs in gpus_cell?gpus_cell{1}.deviceIndex;result:0`
- Code block 2: 1 line(s); first line `?gpus_cell{1}.deviceSMCount;result:16`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: gpuspecs; | Returns a cell array representing all installed GPUs in the system, elements to each cell are structs that show individual specifications. Details of each struct are shown below.
- Table 2: 2 column(s), 11 row(s)
  - Headers: Field, Description
  - First row sample: availableDeviceMemoryKb | Available Video RAM (VRAM) of the GPU in Kilobytes (KB).

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)
- [FDTD on GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)

## Ansys-Related External Links Found

- None

## External Links Found

- None
