# tdrimportdataset - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/52496768733331-tdrimportdataset-Script-command  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `tdrimportdataset - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 2 heading(s), 12 link(s), 2 code block(s), 1 inline code term(s), and 2 table(s). Main headings: tdrimportdataset - Script command, Wrapper functions. Key detected terms: command, dataset, fdtd, geometry, import, mesh, mode, port, script, script-command, structure.

## Key Terms

- command
- dataset
- fdtd
- geometry
- import
- mesh
- mode
- port
- script
- script-command
- structure

## Captured Headings

- tdrimportdataset - Script command
- Wrapper functions

## Official Text Excerpt

> tdrimportdataset - Script command FDTD MODE CHARGE HEAT Imports a dataset from a Sentaurus TDR file into a corresponding currently selected Lumerical simulation object. This script command only supports the following objects, attempting to import into any other object will result in an error. - FDTD: np Density and Temperature Index Perturbation - Multiphysics: Import doping, Import heat distribution, Import temperature distribution Note: The results in imported objects cannot be visualized directly due to the IP protection of the content in tdr files. In FDTD and MODE, you can run a short simulation and visualize the index result that includes perturbations. In Multiphysics, you can run meshing to visualize the imported doping profile or run a short simulation to visualize doping and other imported datasets. |Syntax|Description |out = tdrimportdataset(“file_name”, dataset_name, opt);| Imports a dataset from a TDR file into a selected object. The arguments are as follows: - file_name: A string pointing to a TDR file containing the dataset you wish to import. - dataset_name: A cell array containing names of datasets to import in the format “state name/quantity name/region ...

## Code Block Inventory

- Code block 1: 15 line(s); first line `# Wrap tdrimportdataset around a function to first add the right grid attribute`
- Code block 2: 13 line(s); first line `function addDoping(tdrFileName, tdrDsName, type, opt) {`

## Inline Code Inventory

- `state_0/X/Silicon`

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = tdrimportdataset(“file_name”, dataset_name, opt); | Imports a dataset from a TDR file into a selected object. The arguments are as follows: file_name: A string pointing to a TDR file containing the dataset you wish to import. dataset_
- Table 2: 2 column(s), 4 row(s)
  - Headers: Field, Description
  - First row sample: X_rename | This maps the TDR dataset name to the attribute name in the Lumerical dataset that is imported into the selected Lumerical simulation object. For example, if the TDR dataset is state_0/X/Silicon , and you set this quantity, the c

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [np Density and Temperature Index Perturbation](https://optics.ansys.com/hc/en-us/articles/360034901753-np-Density-and-Temperature-Index-Perturbation-Simulation-object)
- [Import doping](https://optics.ansys.com/hc/en-us/articles/360034398054-Import-doping-region-Simulation-object)
- [Import heat distribution,](https://optics.ansys.com/hc/en-us/articles/360034398114-Import-heat-distribution-Simulation-object)
- [Import temperature distribution](https://optics.ansys.com/hc/en-us/articles/360034918753-Import-temperature-distribution-Simulation-object)
- [tdraddregion](https://optics.ansys.com/hc/en-us/articles/49705410349971-tdraddregion-Script-command)
- [Synopsys Sentaurus™ interoperability – import from and export to TDR files](https://optics.ansys.com/hc/en-us/articles/49705353405459-Synopsys-Sentaurus-interoperability-import-from-and-export-to-TDR-files)
- [tdrinfo](https://optics.ansys.com/hc/en-us/articles/49705705300243-tdrinfo-Script-command)
- [tdrwritedataset](https://optics.ansys.com/hc/en-us/articles/49705814878355-tdrwritedataset-Script-command)

## Ansys-Related External Links Found

- None

## External Links Found

- None
