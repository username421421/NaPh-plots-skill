# runoptimization - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034407794-runoptimization  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `runoptimization - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 4 heading(s), 1 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: runoptimization - Script command, The following script line optimizes the thermal noise for a PIN Photodetector for target, The following script line searches the minimum cutoff frequency for a LP Bessel Filter, The following script line searches the maximum cutoff frequency for a LP Bessel Filter. Key detected terms: command, optimization, script.

## Key Terms

- command
- optimization
- script

## Captured Headings

- runoptimization - Script command
- The following script line optimizes the thermal noise for a PIN Photodetector for target
- The following script line searches the minimum cutoff frequency for a LP Bessel Filter
- The following script line searches the maximum cutoff frequency for a LP Bessel Filter

## Official Text Excerpt

> runoptimization - Script command INTERCONNECT Optimizes a property from a chosen element under specified condition. | Syntax | Description | x=runoptimization(element, property, min, max, analyzer, result, ’target’, target, tolerance=1e-9, iterations=2000) | Optimizes property from element until a target for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values. | x=runoptimization(element, property, min, max, analyzer, result, ’minimize’, tolerance=1e-9, iterations=2000) | Optimizes property from element until a minimum value for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values. | x=runoptimization(element, property, min, max, analyzer, result, ’maximize’, tolerance=1e-9, iterations=2000) | Optimizes property from element until a maximum value for an analyzer result is reached. Function returns an array with two columns, the firs column contains the property values and the second column contains the result values. Example The following script line optimizes the thermal noise for a PIN Photodetector for target The following script line searches ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `x=runoptimization("PIN Photodetector","thermal noise",1e-20,1e-17,"Eye Diagram","measurement/Q factor","target",6,1e-2);`
- Code block 2: 1 line(s); first line `x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/log of BER","minimize");`
- Code block 3: 1 line(s); first line `x=runoptimization("LP Bessel Filter","cutoff frequency",1e+09,1e+10,"Eye Diagram","measurement/Q factor","maximize");`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Syntax, Description
  - First row sample: x=runoptimization(element, property, min, max, analyzer, result, ’target’, target, tolerance=1e-9, iterations=2000) | Optimizes property from element until a target for an analyzer result is reached. Function returns an array with two colum

## Official Links Found

- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)

## Ansys-Related External Links Found

- None

## External Links Found

- None
