# Lumerical Python API Reference

Source URL: https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference  
Area: Python API  
Topic: FDTD, MODE, DEVICE, INTERCONNECT constructors and options  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Lumerical Python API Reference` for the topic `FDTD, MODE, DEVICE, INTERCONNECT constructors and options`. It captured 11 heading(s), 21 link(s), 9 code block(s), 3 inline code term(s), and 3 table(s). Main headings: Lumerical Python API Reference, Lumerical Class, Constructor, Attributes, Methods, SimObject Class, Attributes, Methods. Key detected terms: command, fdtd, geometry, material, mode, port, python, python-api, script.

## Key Terms

- command
- fdtd
- geometry
- material
- mode
- port
- python
- python-api
- script

## Captured Headings

- Lumerical Python API Reference
- Lumerical Class
- Constructor
- Attributes
- Methods
- SimObject Class
- Attributes
- Methods
- SimObjectResults Class
- Attributes
- SimObjectId Class

## Official Text Excerpt

> Lumerical Python API Reference ==Start of tab list========================================= - class Lumerical - class SimObject - class SimObjectResults - class SimObjectId ==End of tab list========================================= ==Start of tab1 content========================================= Lumerical Class The Lumerical class is the common base class for all classes representing interactive sessions with the Lumerical products. Constructor Instantiation The Lumerical class is not intended to be directly instantiated; to create a session for a specific Lumerical product, create an instance of the derived class (FDTD, MODE, DEVICE, and INTERCONNECT) corresponding to the desired product session. |Product|Class |Ansys Lumerical FDTD™|FDTD |Ansys Lumerical MODE™|MODE |Ansys Lumerical Multiphysics™|DEVICE |Ansys Lumerical INTERCONNECT™|INTERCONNECT Example Constructor Signature Parameters | Field | Description |filename| A single string containing either as script filename or a project filename. When the parameter is a project filename, the project will be loaded. When the parameter is a script filename, it will be evaluated. It is recommended to use the keyword arguments script and project over this parameter. See below for more details on keyword arguments. | key | Deprecated parameter, values other than the default should not be entered. ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `fdtd = lumapi.FDTD() #Launches an FDTD session called “fdtd”`
- Code block 2: 1 line(s); first line `class FDTD(filename = None, key = None, hide = False, serverArgs = {}, remoteArgs = {}, **kwargs)class MODE(filename = None, key = None, hide = False, serverArg`
- Code block 3: 5 line(s); first line `fdtd = lumapi.FDTD(filename = fsp_file,`
- Code block 4: 2 line(s); first line `remoteArgs = { "hostname": "192.168.215.129",`
- Code block 5: 1 line(s); first line `fdtd.addrect(x=1e-6,y=0,z=0)`
- Code block 6: 1 line(s); first line `#FDTD Session already openc = 2.99792458e8f_range = np.linspace(c/1100e-9, c/400e-9, 1000)au_index = fdtd.getfdtdindex("Au (Gold) - CRC", f_range, np.min(f_rang`
- Code block 7: 10 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 8: 2 line(s); first line `Attribute Access: rect_obj.x_span =2e-06`
- Code block 9: 6 line(s); first line `fdtd = lumapi.FDTD()`

## Inline Code Inventory

- `-use-solve`
- `fdtd-solutions`
- `platform`

## Table Inventory

- Table 1: 2 column(s), 5 row(s)
  - First row sample: Product | Class
- Table 2: 2 column(s), 6 row(s)
  - Headers: Field, Description
  - First row sample: filename | A single string containing either as script filename or a project filename. When the parameter is a project filename, the project will be loaded. When the parameter is a script filename, it will be evaluated. It is recommended to
- Table 3: 2 column(s), 2 row(s)
  - Headers: Parameter, Description
  - First row sample: project | A single string containing a project filename, including extension. This project will be opened before any scripts specified by the script keyword are run.

## Official Links Found

- [class Lumerical](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [class SimObject](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [class SimObjectResults](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [class SimObjectId](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [Windows](https://optics.ansys.com/hc/en-us/articles/360024812334-Running-simulations-using-the-Windows-command-prompt)
- [Linux](https://optics.ansys.com/hc/en-us/articles/360024974033-Running-simulations-using-terminal-on-Linux)
- [Interop Server](https://optics.ansys.com/hc/en-us/articles/15499581457811-Interop-Server-Remote-API)
- [Lumerical scripting commands](https://optics.ansys.com/hc/en-us/articles/360037228834-Lumerical-scripting-language-By-category)
- [addrect](https://optics.ansys.com/hc/en-us/articles/360034404214-addrect-Script-command)
- [Script Commands as Methods](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [Working with Simulation Objects.](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [close](https://optics.ansys.com/hc/en-us/articles/39746549400723-lumapi-Lumerical-close-Python-API-Method)
- [getObjectById](https://optics.ansys.com/hc/en-us/articles/39747453005715-lumapi-Lumerical-getObjectById-Python-API-Method)
- [getObjectBySelection](https://optics.ansys.com/hc/en-us/articles/39747592765331-lumapi-Lumerical-getObjectBySelection-Python-API-Method)
- [getAllSelectedObjects](https://optics.ansys.com/hc/en-us/articles/39747123391251-lumapi-Lumerical-getAllSelectedObjects-Python-API-Method)
- [eval](https://optics.ansys.com/hc/en-us/articles/360043166434-lumapi-Lumerical-eval-Python-API-Method)
- [getv](https://optics.ansys.com/hc/en-us/articles/39748719848211-lumapi-Lumerical-getv-Python-API-method)
- [putv](https://optics.ansys.com/hc/en-us/articles/39748892700435-lumapi-Lumerical-putv-Python-API-method)
- [Working with Simulation Objects](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [getParent](https://optics.ansys.com/hc/en-us/articles/39748101517075-lumapi-SimObject-getParent-Python-API-Method)
- [getChildren](https://optics.ansys.com/hc/en-us/articles/39748001241491-lumapi-SimObject-getChildren-Python-API-Method)

## Ansys-Related External Links Found

- None

## External Links Found

- None
