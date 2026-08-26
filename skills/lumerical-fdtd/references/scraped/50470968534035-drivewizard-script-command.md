# drivewizard - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/50470968534035-drivewizard-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `drivewizard - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 10 link(s), 1 code block(s), 0 inline code term(s), and 2 table(s). Main headings: drivewizard - Script command. Key detected terms: command, fdtd, geometry, import, mode, port, script, script-command, source, structure.

## Key Terms

- command
- fdtd
- geometry
- import
- mode
- port
- script
- script-command
- source
- structure

## Captured Headings

- drivewizard - Script command

## Official Text Excerpt

> drivewizard - Script command FDTD MODE DGTD CHARGE HEAT FEEM Activates specific wizards with a settings structure. This command is only available on Linux. |Syntax|Description |drivewizard(“wizard_name”, wizard_settings);| Activate the wizard given by “wizard_name” with the settings specified by wizard_settings. The only supported wizard_name is “layout geometry wizard”. The wizard_settings structure must follow the structure given by getwizardinputs. The tables below show the mandatory fields of the wizard_settings structure for each available wizard. Layout Geometry Wizard The layout geometry wizard is only available on Linux, and is used for importing component layout from Cadence Virtuoso or Synopsys OptoCompiler™. |Field|Description |layout_tool| A structure containing information for the source page of the layout geometry wizard. Fields of the structure must follow the list below: - “source”: A string containing the platform for geometry import. Either “optocompiler” or “virtuoso” is supported. - “libconfig”: The location of the library file as a string for the selected source. |geometry_source| A structure containing information for the geometry source page of the layout geometry wizard. Fields of the structure must follow the list below: - “library”: Name of ...

## Code Block Inventory

- Code block 1: 13 line(s); first line `lgWizardInputs = {`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: drivewizard(“wizard_name”, wizard_settings); | Activate the wizard given by “wizard_name” with the settings specified by wizard_settings. The only supported wizard_name is “layout geometry wizard”. The wizard_settings structure must follow 
- Table 2: 2 column(s), 3 row(s)
  - Headers: Field, Description
  - First row sample: layout_tool | A structure containing information for the source page of the layout geometry wizard. Fields of the structure must follow the list below: “source”: A string containing the platform for geometry import. Either “optocompiler” or

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [Cadence Virtuoso](https://optics.ansys.com/hc/en-us/articles/4412939657107-Cadence-Virtuoso-Layout-Integration)
- [Synopsys OptoCompiler™](https://optics.ansys.com/hc/en-us/articles/47076085200787-Lumerical-OptoCompiler-integration)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [getwizardinputs](https://optics.ansys.com/hc/en-us/articles/50997486765331-getwizardinputs-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
