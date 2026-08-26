# queryanalysisprop - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360042187894-queryanalysisprop-Script-command  
Area: Discovered official source  
Topic: Discovered from Script Commands as Methods - Python API  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `queryanalysisprop - Script command` for the topic `Discovered from Script Commands as Methods - Python API`. It captured 1 heading(s), 6 link(s), 3 code block(s), 0 inline code term(s), and 1 table(s). Main headings: queryanalysisprop - Script command. Key detected terms: analysis, command, fdtd, group, script, script-command.

## Key Terms

- analysis
- command
- fdtd
- group
- script
- script-command

## Captured Headings

- queryanalysisprop - Script command

## Official Text Excerpt

> queryanalysisprop - Script command FDTD Return analysis-script property names and the numeric code for their types from an analysis group. | Syntax | Description | out = queryanalysisprop("AnalysisGroup") | Returns a list of the property names and types to a struct "out" from the Analysis Variables in a selected analysis group. Examples The following script gives the first two property names and their types of the analysis group "Qanalysis" to the "out" struct: The result is: One can also use a loop to get all the results: Please refer adduserprop for more details of the data types. See Also adduserprop, querynamed , queryuserprop , queryanalysisresult

## Code Block Inventory

- Code block 1: 1 line(s); first line `select("Qanalysis");out = queryanalysisprop("Qanalysis");?out.name{1};?out.name{2};?out.type{1};?out.type{2};`
- Code block 2: 1 line(s); first line `t startf max34`
- Code block 3: 1 line(s); first line `for(n=1:length(out.name)){?out.name{n};?out.type{n};}t start3f max4make plots0f min4`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: out = queryanalysisprop("AnalysisGroup") | Returns a list of the property names and types to a struct "out" from the Analysis Variables in a selected analysis group.

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [adduserprop](https://optics.ansys.com/hc/en-us/articles/360034928733)
- [querynamed](https://optics.ansys.com/hc/en-us/articles/360042115274)
- [,](https://optics.ansys.com/knowledge/articles/360042678353)
- [queryuserprop](https://optics.ansys.com/hc/en-us/articles/360042665193)
- [queryanalysisresult](https://optics.ansys.com/hc/en-us/articles/360042678353)

## Ansys-Related External Links Found

- None

## External Links Found

- None
