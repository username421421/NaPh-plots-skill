# Using and understanding Mode Expansion Monitors

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902433-Using-and-understanding-Mode-Expansion-Monitors  
Area: Monitors  
Topic: Mode expansion analysis best practices  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Using and understanding Mode Expansion Monitors` for the topic `Mode expansion analysis best practices`. It captured 8 heading(s), 14 link(s), 0 code block(s), 0 inline code term(s), and 4 table(s). Main headings: Using and understanding Mode Expansion Monitors, What is mode expansion?, How to set up mode expansion monitors, What do the results mean?, Interpreting the results, Parameter extraction, Related publications, See also. Key detected terms: analysis, command, fdtd, grating, import, mesh, mode, monitor, normalization, plane, port, reflection, s-parameter, script, solver, source.

## Key Terms

- analysis
- command
- fdtd
- grating
- import
- mesh
- mode
- monitor
- normalization
- plane
- port
- reflection
- s-parameter
- script
- solver
- source
- structure
- sweep
- symmetry
- transmission

## Captured Headings

- Using and understanding Mode Expansion Monitors
- What is mode expansion?
- How to set up mode expansion monitors
- What do the results mean?
- Interpreting the results
- Parameter extraction
- Related publications
- See also

## Official Text Excerpt

> Using and understanding Mode Expansion Monitors FDTD MODE Mode expansion monitor simulation objects allow you to analyze the fraction of power transmitted into any mode(s) of a non-absorbing waveguide or fiber. This page provides additional information to allow users to get the most accurate results from their simulations. See the Mode expansion monitor page for an overview of these objects and lists all input and output properties. Note that if performing parameter extraction using FDTD, using ports and the S-parameter sweep tool is preferable since the port objects can act as both sources and monitors and return S-parameters as a result. What is mode expansion? Consider a waveguide/fiber that supports a set of forward-propagating modes, \( \varphi_{m}^{\text{forward }}\) (with \(\mathbf{E}_{m}^{\text{forward}} \) and \( \mathbf{H}_{m}^{\text{forward}}\) ), and backward-propagating modes, \( \varphi_{m}^{\text{backward }}\) (with \(\mathbf{E}_{m}^{\text{backward}} \) and \( \mathbf{H}_{m}^{\text{backward}}\) ). If a complete basis state of modes is known, any input field can be expanded using these modes: $$ \mathbf{E}_{in}=\sum_{m}\left(a_{m} \mathbf{E}_{m}^{forward}+b_{m} \mathbf{E}_{m}^{\text{backward}} \right) $$ $$\mathbf{H}_{in}=\sum_{m}\left(a_{m} \mathbf{H}_{m}^{forward}+b_{m} \mathbf{H}_{m}^{\text{backward}} \right) $$ \(a_{m} \) and \( b_{m} \) represent the complex transmission coefficient of the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Grid dispersion These equations only apply to the ideal case. In practice, since an FDTD simulation uses a mesh, a correction step is necessary to account for the grid dispersion from this discrete mesh. This correction factor is take
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Power orthogonality Strictly speaking, the power orthogonality condition using the conjugated cross product above is true for the bound modes of non-absorbing waveguides. A more general orthogonality relation, valid for both absorbing
- Table 3: 2 column(s), 8 row(s)
  - First row sample: Ttotal | the total transmission of the input profile. This will be the same as the result obtained with the transmission script command. It's important to notice that the Transmission values are normalized to the power injected by the sourc
- Table 4: 1 column(s), 1 row(s)
  - First row sample: Note: No results returned If no results are returned in the mode expansion monitor, the most likely cause is that no "Monitors for expansion" have been selected, or that they are of the wrong type (ex. if they do not have the right dimensio

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Mode expansion monitor](https://optics.ansys.com/hc/en-us/articles/360034902413)
- [ports](https://optics.ansys.com/hc/en-us/articles/360034382554)
- [S-parameter sweep tool](https://optics.ansys.com/hc/en-us/articles/360034403214)
- [expand2](https://optics.ansys.com/hc/en-us/articles/360034406414)
- [Mode Expansion](https://optics.ansys.com/hc/en-us/articles/360034902413)
- [Mode Expansion](https://optics.ansys.com/hc/en-us/articles/360034902433)
- [sourcepower](https://optics.ansys.com/hc/en-us/articles/360034925313)
- [port](https://optics.ansys.com/hc/en-us/articles/360034382554)
- [addmodeexpansion,](https://optics.ansys.com/hc/en-us/articles/360034924573)
- [setexpansion,](https://optics.ansys.com/hc/en-us/articles/360034408974)
- [removeexpansion](https://optics.ansys.com/hc/en-us/articles/360034408994)

## Ansys-Related External Links Found

- None

## External Links Found

- [Inverse design of grating coupler,](https://apps.lumerical.com/inverse-design-grating-coupler.html)
