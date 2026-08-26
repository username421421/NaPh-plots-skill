# Using an equation to define the spatial field profile of a source in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034383054-Custom-source-profile-from-an-equation  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Using an equation to define the spatial field profile of a source in FDTD` for the topic `Discovered from FDTD product reference manual`. It captured 5 heading(s), 5 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Using an equation to define the spatial field profile of a source in FDTD, Defining the field profile, Adding the source to your simulation, Measure the profile with a monitor, See also. Key detected terms: boundary, dataset, fdtd, import, monitor, normalization, plane, port, reflection, script, solver, source, symmetry.

## Key Terms

- boundary
- dataset
- fdtd
- import
- monitor
- normalization
- plane
- port
- reflection
- script
- solver
- source
- symmetry

## Captured Headings

- Using an equation to define the spatial field profile of a source in FDTD
- Defining the field profile
- Adding the source to your simulation
- Measure the profile with a monitor
- See also

## Official Text Excerpt

> Using an equation to define the spatial field profile of a source in FDTD FDTD This topic explains how the Import source can be used to inject an arbitrary field profile into your simulation. In this example, the script can create an approximately radially polarized or azimuthally polarized beam. Defining the field profile Download the associated files. Open usr_custom_source.fsp and run the script file usr_custom_source.lsf. The script calculates the electric and magnetic fields at the source injection plane. The default settings in the script file will create a radially polarized beam, but you can modify the value of the "pol" variable in the script to specify an azimuthally polarized beam instead. | Warning: The field profile calculated in this script is greatly simplified equation for a radial polarized beam that is intended for demonstration purpose only. Adding the source to your simulation The script then packages the data into a dataset and loads that data into the Import source using the importdataset function. The data is also saved to a .mat file that can be later loaded into the Import ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Warning : The field profile calculated in this script is greatly simplified equation for a radial polarized beam that is intended for demonstration purpose only.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note : Symmetric boundary conditions for custom field profiles Symmetry boundary conditions can be used whenever the EM fields have a plane of symmetry through the middle of the simulation region. For more information see Choosing between s

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114)
- [Choosing between symmetric and anti-symmetric BCs](https://optics.ansys.com/hc/en-us/articles/360034382694)
- [Custom source profile from monitor data](https://optics.ansys.com/hc/en-us/articles/360034383034)
- [Importing arbitrary source fields into an EME solver port](https://optics.ansys.com/hc/en-us/articles/360034396394)

## Ansys-Related External Links Found

- None

## External Links Found

- None
