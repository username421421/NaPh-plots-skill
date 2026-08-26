# Structure Groups - Simulation object

Source URL: https://optics.ansys.com/hc/en-us/articles/360034382434-Structure-Groups  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Structure Groups - Simulation object` for the topic `Discovered from FDTD product reference manual`. It captured 12 heading(s), 18 link(s), 5 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Structure Groups - Simulation object, Elements of the structure group, Properties tab, Script Tab, Rotations tab, Material tab, Benefits of using structure groups, Parameter Sweeps:. Key detected terms: analysis, command, fdtd, group, material, mode, optimization, port, script, solver, structure, sweep, symmetry.

## Key Terms

- analysis
- command
- fdtd
- group
- material
- mode
- optimization
- port
- script
- solver
- structure
- sweep
- symmetry

## Captured Headings

- Structure Groups - Simulation object
- Elements of the structure group
- Properties tab
- Script Tab
- Rotations tab
- Material tab
- Benefits of using structure groups
- Parameter Sweeps:
- Copying and Pasting (Modularity):
- Simplifies running script files:
- Creating a structure group from a script
- See also

## Official Text Excerpt

> Structure Groups - Simulation object FDTD MODE DGTD CHARGE HEAT FEEM The structure group shown below and located in the associated file is used in the 2D square and triangular photonic crystal (PC) bandstructure calculation examples. Elements of the structure group A structure group consists of two elements: - A group of structure primitives - A setup script to setup or edit the grouped primitives The figure above shows the 2D photonic crystal array structure group from the attached triangular_lattice.fsp file. The structure group consists of an array of rods, whose radius, number, and spacing is set by the setup script. Structure groups are created using the ADD STRUCTURE GROUP option of the Groups button in the main toolbar or the Groups group under the Design tab. If you choose to edit a structure group object, then you will see that there are tabs in the edit dialog box: - The PROPERTIES tab contains input parameters for the script. In the PC structure group, the input parameters are the radius of the rods, the size of the array, the lattice ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `addcircle;set("radius",radius);`
- Code block 2: 1 line(s); first line `addrect;set("x",5e-6);`
- Code block 3: 1 line(s); first line `setnamed("structure group", "group scope effective material","CustomMaterial");`
- Code block 4: 1 line(s); first line `a(i) = linspace(1e-6,6e-6,4) #array of lattice parametersfor(i=1:length(a)) {switchtolayout;#edit structure groupselect("2D photonic crystal array");set("ax",a(`
- Code block 5: 1 line(s); first line `addstructuregroup;set("name","cube");adduserprop("length",2,1e-6);set("construction group",1);# define the setup script by setting the 'script' property.# Note `

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [Design](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface#toc_3)
- [Scripting Language](https://optics.ansys.com/hc/en-us#kb-anchor)
- [runsetup](https://optics.ansys.com/hc/en-us/articles/360034928893-runsetup-Script-command)
- [save](https://optics.ansys.com/hc/en-us/articles/360034410814-save-Script-command)
- [run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command)
- [Structures](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [Analysis groups](https://optics.ansys.com/hc/en-us/articles/360034901893)
- [Arrays of objects](https://optics.ansys.com/hc/en-us/articles/360034901633)
- [addstructuregroup (script command)](https://optics.ansys.com/hc/en-us/articles/360034924093)
- [Rectangular Photonic Crystal Bandstructure](https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure)
- [Triangular, FCC, BCC Photonic Crystal Bandstructure](https://optics.ansys.com/hc/en-us/articles/360041566614-Rectangular-Photonic-Crystal-Bandstructure)
- [Object Library](https://optics.ansys.com/hc/en-us/articles/360034394494)

## Ansys-Related External Links Found

- None

## External Links Found

- None
