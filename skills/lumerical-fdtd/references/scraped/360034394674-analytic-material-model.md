# Tips and simple example for using the analytic material model in FDTD

Source URL: https://optics.ansys.com/hc/en-us/articles/360034394674-Analytic-Material-Model  
Area: Discovered official source  
Topic: Discovered from FDTD  
Discovery depth: 2  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Tips and simple example for using the analytic material model in FDTD` for the topic `Discovered from FDTD`. It captured 5 heading(s), 4 link(s), 0 code block(s), 0 inline code term(s), and 1 table(s). Main headings: Tips and simple example for using the analytic material model in FDTD, Simple example, FDTD example, MODE example, See also. Key detected terms: fdtd, import, material, mode, port.

## Key Terms

- fdtd
- import
- material
- mode
- port

## Captured Headings

- Tips and simple example for using the analytic material model in FDTD
- Simple example
- FDTD example
- MODE example
- See also

## Official Text Excerpt

> Tips and simple example for using the analytic material model in FDTD FDTD MODE This section describes the Analytic material model. Simple example Suppose we have two materials: material A has a refractive index of na and material B has a refractive index of nb. These two materials can be combined to produce a composite material. The refractive index of this composite material is simply the weighted average a of the refractive index of the two base materials, as shown in the following formula. $$index=n_a\alpha+n_b(1-\alpha)$$ This type of material model can be implemented in the material database using the Analytic material model. This model makes it possible to define a material via an analytic function. In this case, our function has three variables: the index of materials A and B, and the fraction of material A in the mixture. The variables of the analytic model have fixed names, such as x1, x2, x3 and so on. Therefore, we must write the formula as: $$index=x_1x_3+x_2(1-x_3)$$ where \( x_1=n_a, x_2=n_b, x_3=\alpha \) FDTD example It is important to understand that the analytic ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note : The predefined variables that can be used in the equations for "real" and "imaginary" are: f: the frequency in the specified frequency units l0: the free space wavelength in the specified length units w: 2 * \( \pi \) *f in the speci

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [setmaterial](https://optics.ansys.com/hc/en-us/articles/360034409654)

## Ansys-Related External Links Found

- [Importing arbitrary dispersive models](https://innovationspace.ansys.com/forum/forums/topic/ansys-insight-importing-arbitrary-dispersive-models/)

## External Links Found

- None
