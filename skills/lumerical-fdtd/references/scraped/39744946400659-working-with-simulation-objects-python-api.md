# Working with Simulation Objects – Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API  
Area: Python API  
Topic: Object construction, ordered properties, linked properties, handles  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Working with Simulation Objects – Python API` for the topic `Object construction, ordered properties, linked properties, handles`. It captured 11 heading(s), 7 link(s), 10 code block(s), 5 inline code term(s), and 0 table(s). Main headings: Working with Simulation Objects – Python API, Creating Simulation Objects, Assigning Properties with an Ordered Dict, Assigning Properties with Keyword Arguments, Assigning Properties with “set”, Linked Properties, Manipulating Simulation Objects, Direct Attribute Access. Key detected terms: command, fdtd, geometry, import, lumapi, monitor, port, python, python-api, script, source, structure.

## Key Terms

- command
- fdtd
- geometry
- import
- lumapi
- monitor
- port
- python
- python-api
- script
- source
- structure

## Captured Headings

- Working with Simulation Objects – Python API
- Creating Simulation Objects
- Assigning Properties with an Ordered Dict
- Assigning Properties with Keyword Arguments
- Assigning Properties with “set”
- Linked Properties
- Manipulating Simulation Objects
- Direct Attribute Access
- Dict-Like Access
- Duplicate Names
- Parent and Children Objects

## Official Text Excerpt

> Working with Simulation Objects – Python API At a basic level, simulation objects can be interacted with in the same way the Lumerical Script Language can be used to interact with the object. However, specific Pythonic approaches can also be used to interact with them. This article describes unique ways to interact with simulation objects, such as structures, sources, and monitors, using the Python API. For more information on how to use script commands in the Python API, see the Knowledge Base article on Script Commands as Methods. Creating Simulation Objects When adding a simulation object into Lumerical products using the lumapi, the values of properties at creation can be set like using a constructor in programming. There are multiple ways of assigning the properties of objects when you create them. Assigning Properties with an Ordered Dict A Python`dict`can also be used as a constructor to the object by assigning it to the attribute properties. In Python,`dict`ordering is not guaranteed, so if there are properties that depend on other properties, an ordered`dict`is necessary. For example, in the below line of ...

## Code Block Inventory

- Code block 1: 6 line(s); first line `from collections import OrderedDict`
- Code block 2: 5 line(s); first line `props = {"name": "power",`
- Code block 3: 2 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 4: 4 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 5: 3 line(s); first line `with lumapi.FDTD() as fdtd:`
- Code block 6: 1 line(s); first line `rect1.x_span=2e-06 #Note that this is different than what was set earlier from the x_span argument`
- Code block 7: 3 line(s); first line `rectangle = fdtd.addrect(x = 2e-6, y = 0.0, z = 0.0)`
- Code block 8: 3 line(s); first line `rectangle = fdtd.addrect(x = 2e-6, y = 0.0, z = 0.0)`
- Code block 9: 11 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 10: 12 line(s); first line `#Create 3 rectangles and list their names`

## Inline Code Inventory

- `dict`
- `x`
- `x max`
- `x min`
- `x span`

## Table Inventory

- No tables detected

## Official Links Found

- [Script Commands as Methods](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set-Script-command)
- [setnamed](https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed-Script-command)
- [Python API Overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Working with Simulation Objects – Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods – Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [Installation and Getting Started – Python API](https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- None
