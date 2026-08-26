# Solving bent waveguides in FDE and FEEM

Source URL: https://optics.ansys.com/hc/en-us/articles/360034917253-Bent-waveguide-solver  
Area: Discovered official source  
Topic: Discovered from MODE  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Solving bent waveguides in FDE and FEEM` for the topic `Discovered from MODE`. It captured 7 heading(s), 5 link(s), 0 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Solving bent waveguides in FDE and FEEM, Bent waveguide physics, Bend radius setting, Minimum bend radius, Bend orientation setting (FDE only), FDE Solver in other orientations (XZ, YZ, or 1D solvers), See also. Key detected terms: analysis, boundary, import, mode, plane, pml, port, script, solver.

## Key Terms

- analysis
- boundary
- import
- mode
- plane
- pml
- port
- script
- solver

## Captured Headings

- Solving bent waveguides in FDE and FEEM
- Bent waveguide physics
- Bend radius setting
- Minimum bend radius
- Bend orientation setting (FDE only)
- FDE Solver in other orientations (XZ, YZ, or 1D solvers)
- See also

## Official Text Excerpt

> Solving bent waveguides in FDE and FEEM MODE This page discusses the physics of bent waveguides and provides details on the more complicated aspects of using the bent waveguide solver. With the exception of the Bend orientation setting section, which only applies to the FDE solver, the content on this page applies to both the FDE and FEEM solvers. Bent waveguide physics In a straight waveguide, the FDE/FEEM engine solves Maxwell's equations by looking for solutions in the form shown below: $$E(x,y,z)=E_j(x,y)e^{i\beta_jz}$$ where \(\beta_j\) is the propagation constant of the \(j_{th}\) mode. It is a property of the mode and has units of inverse length. The effective index is generally used rather than propagation constant and it is defined by: $$\beta_j=k_0n_{eff,j}$$ where \(k_0 = \omega / c\) is the wavevector in free space. Maxwell's equations are solved in a Cartesian coordinate system with the appropriate boundary conditions. In a bent waveguide, the eigenmode solver will solve for modes of the form $$E(\rho,\theta,y)=E_j(\rho,y)e^{i\widetilde{\beta_j}\theta}$$ where \(\widetilde{\beta_j}\) depicts the angular propagation constant of the \(j_{th}\) mode and has units of inverse radian, and ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note: Loss values The bend can lead to radiative losses, which can be measured by using Perfectly Matched Layer (PML) boundary conditions to absorb the radiation from the waveguide. The loss values reported by the solver are the net loss of
- Table 2: 1 column(s), 1 row(s)
  - First row sample: Note: Bent waveguide location before 2019A-R2 In versions of the software before 2019A-R2 (v7.13.1809) the bend location was fixed to be at the center of simulation region including the boundary conditions. This definition matches with the 
- Table 3: 1 column(s), 1 row(s)
  - First row sample: Note: Solver algorithm compatibility Bent waveguide solver is not available with "H transverse" solver algorithm.

## Official Links Found

- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Bend orientation setting](https://optics.ansys.com/hc/en-us/articles/360034917253-Bent-waveguide-solver#h_01FDAYGG1AYJ79CXXP1VH0HBGS)
- [MODE - Finite Difference Eigenmode (FDE) solver introduction](https://optics.ansys.com/hc/en-us/articles/360034917233)
- [FDE solver analysis - Modal Analysis Tab](https://optics.ansys.com/hc/en-us/articles/360034917353)
- [FEEM solver - Simulation object](https://optics.ansys.com/hc/en-us/articles/360034918393)

## Ansys-Related External Links Found

- None

## External Links Found

- None
