# Creating new sampled data materials in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034915093-Creating-Sampled-Data-Materials  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Creating new sampled data materials in FDTD` for the topic `Discovered from FDTD product reference manual`. It captured 13 heading(s), 12 link(s), 3 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Creating new sampled data materials in FDTD, Adding a new material from a .txt data file, 1. Create wavelength/frequency vs index/permittivity text file., 2. Open the Material Database and click the Add button., 3. Click on the Import Data button to import the material data from the text file., 4. Specify the column ordering, 5.Automated error checking, Adding a new material from a .yml data file. Key detected terms: command, fdtd, import, material, mode, port, script, source.

## Key Terms

- command
- fdtd
- import
- material
- mode
- port
- script
- source

## Captured Headings

- Creating new sampled data materials in FDTD
- Adding a new material from a .txt data file
- 1. Create wavelength/frequency vs index/permittivity text file.
- 2. Open the Material Database and click the Add button.
- 3. Click on the Import Data button to import the material data from the text file.
- 4. Specify the column ordering
- 5.Automated error checking
- Adding a new material from a .yml data file
- Adding a new material with a script
- Check the material fit
- Anisotropic materials
- III-V Semiconductor Optical Materials
- See also

## Official Text Excerpt

> Creating new sampled data materials in FDTD FDTD MODE This section describes how to import experimental material data into the Material database, and how to check the material fit with the Material Explorer. The Sampled 2D Data or Sampled 3D Data material type should be used when creating materials from measured data. Alternative video source in Mandarin, click here Adding a new material from a .txt data file 1. Create wavelength/frequency vs index/permittivity text file. Save the experimental data in a 3 column text file, as shown below, and in the text file below. The first column of the material files should contain the wavelength or frequency, and the second and third columns should contain the corresponding real and imaginary parts of the refractive index (n,k) or permittivity when specifying a Sampled 3D Data type material. When specifying a Sampled 2D Data type material, the second and third columns should contain the corresponding real and imaginary parts of the conductivity or resistivity. In this example, we will illustrate a Sampled 3D Data material with refractive index data over wavelength. 2. ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `420  5.08894  0.237724440  4.78731  0.169323460  4.57592  0.130235480  4.4202   0.0933521500  4.29748  0.0728287520  4.19996  0.0568346540  4.11973  0.047231256`
- Code block 2: 1 line(s); first line `# this file is part of refractiveindex.info database# refractiveindex.info database is in the public domain# copyright and related rights waived via CC0 1.0REFE`
- Code block 3: 1 line(s); first line `400 5.57 0.387 2.785 0.1935 1.85667 0.129420 5.08894 0.237724 2.54447 0.118862 1.69631 0.0792415440 4.78731 0.169323 2.39366 0.0846613 1.59577 0.0564409460 4.57`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [setmaterial](https://optics.ansys.com/hc/en-us/articles/360034409654)
- [Modify material fits](https://optics.ansys.com/hc/en-us/articles/360034915053)

## Ansys-Related External Links Found

- [Importing arbitrary dispersive models](https://innovationspace.ansys.com/forum/forums/topic/ansys-insight-importing-arbitrary-dispersive-models/)

## External Links Found

- [here](http://v.youku.com/v_show/id_XOTU1OTQ0MDQw.html)
- [list of available YAML files](https://refractiveindex.info)
- [Importing arbitrary dispersive models](https://kx.lumerical.com/t/importing-arbitrary-dispersive-models/32076)
- [III-V Semiconductor Optical Material Data Tool](https://support.lumerical.com/hc/en-us/articles/4411081333011)
- [Getting material data from the database](https://kx.lumerical.com/t/how-to-get-material-data-from-material-database/31906)
- [Creating lossless materials](https://kx.lumerical.com/t/creating-lossless-materials/32273)
- [Creating 2D conductivity from permittivity data](https://kx.lumerical.com/t/creating-2d-conductivity-from-permittivity-data/32089)
