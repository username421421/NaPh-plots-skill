# FDTD solver - Simulation Object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object  
Area: Solver  
Topic: Region geometry, mesh type, boundary conditions, advanced settings, status  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `FDTD solver - Simulation Object` for the topic `Region geometry, mesh type, boundary conditions, advanced settings, status`. It captured 24 heading(s), 12 link(s), 2 code block(s), 2 inline code term(s), and 3 table(s). Main headings: FDTD solver - Simulation Object, General tab, Geometry tab, Mesh settings tab, Mesh type, Mesh Refinement, Time Step:, Minimum mesh step settings. Key detected terms: bfast, bloch, boundary, command, convergence, dipole, fdtd, geometry, import, material, mesh, mode, monitor, normalization, periodic, plane.

## Key Terms

- bfast
- bloch
- boundary
- command
- convergence
- dipole
- fdtd
- geometry
- import
- material
- mesh
- mode
- monitor
- normalization
- periodic
- plane
- pml
- port
- reflection
- script
- solver
- source
- structure
- symmetry
- transmission

## Captured Headings

- FDTD solver - Simulation Object
- General tab
- Geometry tab
- Mesh settings tab
- Mesh type
- Mesh Refinement
- Time Step:
- Minimum mesh step settings
- Boundary conditions tab
- Supported Boundary Conditions FDTD/MODE
- Boundary condition options
- 
- Advanced options
- Simulation bandwidth
- Mesh settings
- Miscellaneous
- Auto shutoff
- Parallel engine options
- Checkpoint options
- BFAST settings
- Results returned
- Grid
- Simulation status
- Simulation benchmark

## Official Text Excerpt

> FDTD solver - Simulation Object FDTD General tab - DIMENSION: The dimension of the simulation region (2D or 3D). - BACKGROUND INDEX: The refractive index of the surrounding, background medium in the simulation region. - SIMULATION TIME: The maximum duration of the simulation to be performed. The actual simulation may be shorter if the autoshutoff criteria are satisfied before this maximum simulation time is exceeded. - SIMULATION TEMPERATURE (K): The simulation temperature, for simulations that include temperature dependent objects. Geometry tab - X, Y, Z: The center position of the simulation region - X MIN, X MAX: X min, X max position - Y MIN, Y MAX: Y min, Y max position - Z MIN, Z MAX: Z min, Z max position - X SPAN, Y SPAN, Z SPAN: X, Y, Z span of the simulation region Mesh settings tab Mesh type Four types of mesh generation algorithms are available, as described below - Auto non-uniform (default): A non-uniform mesh is automatically generated based on the mesh accuracy slider bar. It is strongly recommended to start with a mesh accuracy ...

## Code Block Inventory

- Code block 1: 2 line(s); first line `# Specifies points starting from 0. Result will be mirrored and points will be at -0.2um, -0.1um, 0um, 0.1um, 0.2um.`
- Code block 2: 1 line(s); first line `stat = getresult("FDTD","status");`

## Inline Code Inventory

- `setnamed`
- `user specified mesh x/y/z`

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: if you choose BFAST plane wave source , the Bloch BCs will be automatically overridden and use its built-in boundary conditions.
- Table 2: 1 column(s), 1 row(s)
  - First row sample: WARNING: This tab includes options that should only be changed if you are quite familiar with the meshing algorithm and techniques used.
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: These results can be copied to the script workspace using the function getresult with "FDTD" as the monitor name. For example:

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Mesh refinement options](https://optics.ansys.com/hc/en-us/articles/360034382614)
- [PML](https://optics.ansys.com/hc/en-us/articles/360034382674)
- [default setting](https://optics.ansys.com/hc/en-us/articles/360034901873)
- [Periodic](https://optics.ansys.com/hc/en-us/articles/360034382734)
- [Bloch (FDTD/varFDTD)](https://optics.ansys.com/hc/en-us/articles/360034382714)
- [BFAST plane wave source](https://optics.ansys.com/hc/en-us/articles/360034902273)
- [Choosing between symmetric and anti-symmetric BCs](https://optics.ansys.com/hc/en-us/articles/360034382694)
- [PML boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382674)
- [extending structures through PML](https://optics.ansys.com/hc/en-us/articles/360034382414)
- [on the GPU](https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU)
- [getresult](https://optics.ansys.com/hc/en-us/articles/360034409854)

## Ansys-Related External Links Found

- None

## External Links Found

- None
