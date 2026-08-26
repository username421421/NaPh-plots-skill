# Integrating power in far field projections

Source URL: https://optics.ansys.com/hc/en-us/articles/360034914813-Far-field-projections-Power-integration-on-hemisphere  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Integrating power in far field projections` for the topic `Discovered from FDTD`. It captured 2 heading(s), 2 link(s), 2 code block(s), 0 inline code term(s), and 3 table(s). Main headings: Integrating power in far field projections, Power Integrals. Key detected terms: far, far-field, fdtd, grating, mode, monitor, normalization, plane, port, script, source, transmission.

## Key Terms

- far
- far-field
- fdtd
- grating
- mode
- monitor
- normalization
- plane
- port
- script
- source
- transmission

## Captured Headings

- Integrating power in far field projections
- Power Integrals

## Official Text Excerpt

> Integrating power in far field projections FDTD The section explains how to integrate the far fields on the default hemispherical surface. This is typically done to calculate the amount of far field power within some range of angles. Note: The descriptions and examples of the far field projection calculation on the following pages are primarily intended for users of FDTD. For users interested in calculating far field projections with MODE, these descriptions are basically still correct, although some subtle differences do exist. Power Integrals In general, we want to integrate power over a given solid angle in the far field. There are 2 ways this can be done - We integrate the fraction of total electric field intensity (|E|2) over the solid angle that we are interested in, and multiply by the normalized power transmission through the monitor in the near field. $$\text{far field fraction}=\frac{\int_{cone}\mid\mathbf{E}\mid^2}{\int_{hemisphere}\mid\mathbf{E}\mid^2}\\ \text{Power norm}=\text{far field fraction}*\text{near field power transmission}$$ - We calculate the Poynting vector in the far field and integrate the power over a given solid angle. We then normalize to the original source power. In ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `# choose the half angle over which we will integratehalf_angle = 30; #in degrees`
- Code block 2: 1 line(s); first line `> solver_far_field2;The half angle is: 30 degrees at (theta,phi)=(0,0)  The normalized transmission by Method 1 is: 45.6613 %  The normalized transmission by Me`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 3 column(s), 3 row(s)
  - Headers: Cone half angle (degrees), Normalized transmission in cone by method 1 (%), Normalized transmission in cone by method 2 (%)
  - First row sample: 29 | 38.4055 | 37.4377
- Table 2: 1 column(s), 1 row(s)
  - First row sample: NOTE: Far field integration The function farfield3dintegrate makes integrating far field data very easy.
- Table 3: 1 column(s), 1 row(s)
  - First row sample: NOTE: Integration with non-default far field refractive index. Additional normalization is required when using a non-default far field refractive index. See the far field refractive index page or contact Lumerical support for additional inf

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [far field refractive index](https://optics.ansys.com/hc/en-us/articles/360034395194)

## Ansys-Related External Links Found

- None

## External Links Found

- None
