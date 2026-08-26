# getmeshcontours - Script command

Source URL: https://optics.ansys.com/hc/en-us/articles/360034929973-getmeshcontours  
Area: Discovered official source  
Topic: Discovered from Lumerical scripting language alphabetical list  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `getmeshcontours - Script command` for the topic `Discovered from Lumerical scripting language alphabetical list`. It captured 1 heading(s), 11 link(s), 1 code block(s), 0 inline code term(s), and 1 table(s). Main headings: getmeshcontours - Script command. Key detected terms: boundary, command, dataset, fdtd, mesh, mode, script, structure.

## Key Terms

- boundary
- command
- dataset
- fdtd
- mesh
- mode
- script
- structure

## Captured Headings

- getmeshcontours - Script command

## Official Text Excerpt

> getmeshcontours - Script command FDTD MODE DGTD CHARGE HEAT FEEM INTERCONNECT Gets information about the contours between different domains in an unstructured (finite-element) dataset. The dataset must contain the "ID" attribute (a unique identified for each domain in the finite-element mesh generated in Ansys Lumerical Multiphysics™). |Syntax|Description |A = getmeshcontours(dataset);| Returns information about the contours between different domains of the unstructured dataset named "dataset". The output is provided as a cell array. Each entry is a struct with three fields: ID: An integer ID that is unique for that contour. adjacent: Two integers representing the IDs of the adjacent domains. elements: For 2D, Nx2 array and for 3D, Nx3 array of integers that are the indexes to the vertices for each face on the boundary. Examples The script commands below will get the contour information for the "grid" dataset (available after calculating the finite-element mesh). See Also Datasets, unstructureddataset, mesh, getresult

## Code Block Inventory

- Code block 1: 9 line(s); first line `mesh("CHARGE");  # calculate the mesh in Lumerical Multiphysics using the CHARGE solver`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 2 column(s), 1 row(s)
  - Headers: Syntax, Description
  - First row sample: A = getmeshcontours(dataset); | Returns information about the contours between different domains of the unstructured dataset named "dataset". The output is provided as a cell array. Each entry is a struct with three fields: ID: An integer I

## Official Links Found

- [FDTD](https://optics.ansys.com/hc/en-us/articles/360033154434)
- [MODE](https://optics.ansys.com/hc/en-us/articles/360020687354)
- [DGTD](https://optics.ansys.com/hc/en-us/articles/360037744173)
- [CHARGE](https://optics.ansys.com/hc/en-us/articles/360037184494)
- [HEAT](https://optics.ansys.com/hc/en-us/articles/360037224694)
- [FEEM](https://optics.ansys.com/hc/en-us/articles/360037744633)
- [INTERCONNECT](https://optics.ansys.com/hc/en-us/articles/360037304774)
- [Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets)
- [unstructureddataset](https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset)
- [mesh](https://optics.ansys.com/hc/en-us/articles/360034410654-mesh)
- [getresult](https://optics.ansys.com/hc/en-us/articles/360034409854-getresult)

## Ansys-Related External Links Found

- None

## External Links Found

- None
