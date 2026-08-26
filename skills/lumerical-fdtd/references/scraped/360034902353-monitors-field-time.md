# Field time monitor - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902353-Monitors-Field-time  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Field time monitor - Simulation object` for the topic `Discovered from FDTD`. It captured 6 heading(s), 8 link(s), 1 code block(s), 0 inline code term(s), and 5 table(s). Main headings: Field time monitor - Simulation object, General tab, Geometry tab, Data to record, Advanced tab, Results returned. Key detected terms: analysis, boundary, command, fdtd, geometry, material, mesh, mode, monitor, pml, port, script, structure, transmission.

## Key Terms

- analysis
- boundary
- command
- fdtd
- geometry
- material
- mesh
- mode
- monitor
- pml
- port
- script
- structure
- transmission

## Captured Headings

- Field time monitor - Simulation object
- General tab
- Geometry tab
- Data to record
- Advanced tab
- Results returned

## Official Text Excerpt

> Field time monitor - Simulation object FDTD MODE These monitors provide time-domain information for field components over the course of the simulation. Time-domain monitors can consist of point, line, or area monitors to capture this information over different spatial extents within the FDTD and varFDTD simulation regions. For the purposes of extracting line widths of resonant structures through Fourier analysis, point time monitors with a down sample time of 1 are sufficient. Memory and computational requirements: Generally, time monitors don't have a large effect on the simulation time. However, they can require large amounts of memory when recording data over a large spatial domain. When possible, use 1D rather than 2D or 3D monitors. Similarly, you can reduce the duration of time where data is recorded. Temporal down sampling is also used to minimize the amount of data collected. Finally, it is possible to control which field components are recorded on the Data to record tab. General tab The general tab for the time domain monitor includes options to edit the amount of data, and time period over which data ...

## Code Block Inventory

- Code block 1: 26 line(s); first line `# this code can be used to manually calculate the`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: WARNING : This tab includes options which should only be changed if you are quite familiar with the meshing algorithm and techniques used.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note : Spatial interpolation - NONE setting Disabling the spatial interpolation is a very advanced feature. Only expert users that are very familiar with the FDTD method should consider using this feature. Most standard analysis functions (
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note : Sampling Rate When calculating the spectrum the frequency resolution is equal to the size of the FFT window divided by the sampling rate. FDTD will use zero-padding so the spacing between frequency points is N\SAMPLING RATE where N=2
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note : Manual calculation of SPECTRUM result The following code can be used to manually calculate the spectrum data (eg. if it is necessary to adjust the frequency range of the data). # this code can be used to manually calculate the # spec
- Table 5: 1 column(s), 1 row(s)
  - First row sample: Note : Plugin material - storage fields For point monitors inside an object that uses a plugin material, the data in the storage fields can be found in the rawdata returned by the monitor (see below).

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [mesh settings tab](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [fft - Script command,](https://optics.ansys.com/hc/en-us/articles/360034926133)
- [czt - Script command.](https://optics.ansys.com/hc/en-us/articles/360034926173)
- [findresonances](https://optics.ansys.com/hc/en-us/articles/360034925953)
- [Parseval's theorem](https://optics.ansys.com/hc/en-us/articles/360034394274)
- [plugin material](https://optics.ansys.com/hc/en-us/articles/360034394734)

## Ansys-Related External Links Found

- None

## External Links Found

- None
