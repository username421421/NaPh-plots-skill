# Mode source in broadband simulations

Source URL: https://optics.ansys.com/hc/en-us/articles/360034902213-Mode-source-Broadband  
Area: Discovered official source  
Topic: Discovered from FDTD product reference manual  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Mode source in broadband simulations` for the topic `Discovered from FDTD product reference manual`. It captured 7 heading(s), 1 link(s), 0 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Mode source in broadband simulations, Introduction, Broadband Simulation Settings - FDTD, , Number of Frequency Points, Accuracy and Performance Considerations, Example, Broadband Simulation in varFDTD. Key detected terms: convergence, fdtd, import, mode, monitor, plane, port, reflection, script, solver, source, structure.

## Key Terms

- convergence
- fdtd
- import
- mode
- monitor
- plane
- port
- reflection
- script
- solver
- source
- structure

## Captured Headings

- Mode source in broadband simulations
- Introduction
- Broadband Simulation Settings - FDTD
- 
- Number of Frequency Points, Accuracy and Performance Considerations
- Example
- Broadband Simulation in varFDTD

## Official Text Excerpt

> Mode source in broadband simulations FDTD This topic describes how the Mode source operates in broadband time-domain simulations, and how to significantly reduce the injection errors that can occur due to the mode mismatch. Introduction The mode solver of the Mode source uses a frequency domain technique to calculate the modes of a structure. This technique is inherently single frequency and if the default source settings is used, the mode solver calculates the mode profiles at the center frequency of the source. For example, if the source range is 300-600 THz, the mode solver will calculate the modes at 450 THz. If the mode profile is relatively constant as a function of frequency, this works well. However, if the mode profile changes over the specified frequency range, there will be some reflection and scattering at the source injection plane. This can be understood in terms of the mode profile mismatch between the mode that actually exists at that frequency and the mode profile of the center frequency that is being injected. These errors will be most noticeable at the minimum ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - First row sample: Mode source settings | Mode profiles calculated at the frequency points specified in the source settings Actually injected frequency dependent fields in log scale
- Table 2: 2 column(s), 2 row(s)
  - First row sample: Single frequency mode source calculation | Multifrequency mode source calculation

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)

## Ansys-Related External Links Found

- None

## External Links Found

- None
