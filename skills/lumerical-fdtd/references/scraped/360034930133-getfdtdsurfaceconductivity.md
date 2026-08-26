# getfdtdsurfaceconductivity - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034930133-getfdtdsurfaceconductivity  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getfdtdsurfaceconductivity - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 7 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: getfdtdsurfaceconductivity - Script command. Key detected terms: command, fdtd, material, mode, script.

## Key Terms

- command
- fdtd
- material
- mode
- script

## Captured Headings

- getfdtdsurfaceconductivity - Script command

## Official Text Excerpt

> getfdtdsurfaceconductivity - Script command FDTD MODE For materials which use a surface conductivity material model (such as Graphene), this function returns the surface conductivity of the material in the database as it will be used in an actual simulation. For a list of materials which use the surface conductivity model, see Material conductivity models. The conductivity evaluated at the specified frequencies is returned. Note that the fit result depends on the fit parameters, Max coefficients and Tolerance set for the material, thus getfdtdsurfaceconductivity result depends on those parameters as well. | Syntax | Description | out = getfdtdsurfaceconductivity( "materialname", f, fmin, fmax); | Returns the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified frequency f. Similar to getsurfaceconductivity, but you also specify fmin and fmax, the span of frequency range of the simulation. All frequency units are in Hz. | getfdtdsurfaceconductivity("materialname", f,fmin, fmax, component); | Optional argument component can be 1, 2 or 3 to specify the x, y or z component for anisotropic materials. The default ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - Headers: Syntax, Description
  - First row sample: out = getfdtdsurfaceconductivity( "materialname", f, fmin, fmax); | Returns the surface conductivity (in units of S) of the material with the given name. The surface conductivity is returned for the specified frequency f. Similar to getsurf

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [Material conductivity models](https://optics.ansys.com/hc/en-us/articles/360034915113-Material-Conductivity-Models)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [addmaterial](https://optics.ansys.com/hc/en-us/articles/360034930013-addmaterial)
- [setmaterial](https://optics.ansys.com/hc/en-us/articles/360034409654-setmaterial)
- [getsurfaceconductivity](https://optics.ansys.com/hc/en-us/articles/360034409754-getsurfaceconductivity)

## Ansys-Related External Links Found

- None

## External Links Found

- None
