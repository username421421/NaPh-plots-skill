# Frequency-domain monitor - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902393-Frequency-domain-monitor-Simulation-object  
Area: Monitors  
Topic: DFT monitor memory, output fields/power, interpolation  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Frequency-domain monitor - Simulation object` for the topic `DFT monitor memory, output fields/power, interpolation`. It captured 7 heading(s), 6 link(s), 0 code block(s), 0 inline code term(s), and 4 table(s). Main headings: Frequency-domain monitor - Simulation object, General tab, Geometry tab, Data to record, Spectral averaging and apodization tab, Advanced tab, Results returned. Key detected terms: analysis, boundary, far, far-field, fdtd, geometry, import, material, mesh, mode, monitor, normalization, plane, pml, port, script.

## Key Terms

- analysis
- boundary
- far
- far-field
- fdtd
- geometry
- import
- material
- mesh
- mode
- monitor
- normalization
- plane
- pml
- port
- script
- solver
- source
- structure
- transmission

## Captured Headings

- Frequency-domain monitor - Simulation object
- General tab
- Geometry tab
- Data to record
- Spectral averaging and apodization tab
- Advanced tab
- Results returned

## Official Text Excerpt

> Frequency-domain monitor - Simulation object FDTD MODE Frequency-domain field monitors (DFT monitors) collect the field profile in the frequency domain from simulation results across some spatial region within the simulation in the FDTD, varFDTD solvers. | Tips: Memory and computation time Frequency domain field monitors can require large amounts of memory when recording data over a large spatial domain. When possible, use 1D or 2D rather than 3D monitors. Similarly, try to minimize the number of frequency points recorded. It is also possible to use spatial downsampling to record less spatial resolution. Finally, it is possible to control which field components are recorded on the Data to record tab. If you are only interested in the power flux, you can select the OUTPUT POWER and disable everything else. Generally, frequency monitors don't have a large effect on the simulation time, except when recording a very large amount of data. To determine the effect on the simulation speed, simply disable the monitor and re-run the simulation. General tab Simulation type: Record the type of simulation data, default setting is ALL Override ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Tips : Memory and computation time Frequency domain field monitors can require large amounts of memory when recording data over a large spatial domain. When possible, use 1D or 2D rather than 3D monitors. Similarly, try to minimize the numb
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note : Apodization functions FULL apodization involves windowing the time-domain data on both the start and end side. The resulting “windowed” data is then processed to produce frequency-domain information. START apodization involves window
- Table 3: 1 column(s), 1 row(s)
  - First row sample: WARNING: This tab includes options that should only be changed if you are quite familiar with the meshing algorithm and techniques used.
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note : Spatial interpolation - NONE setting Disabling the spatial interpolation is a very advanced feature. Only expert users that are very familiar with the FDTD method should consider using this feature. Most standard analysis functions (

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [apodization](https://optics.ansys.com/hc/en-us/articles/360034902473)
- [box of monitors](https://optics.ansys.com/hc/en-us/articles/360034915613-Far-field-projections-from-a-box-of-monitors)
- [Simple far-field projection example](https://optics.ansys.com/hc/en-us/articles/360034914733)
- [Parseval's theorem](https://optics.ansys.com/hc/en-us/articles/360034394274)

## Ansys-Related External Links Found

- None

## External Links Found

- None
