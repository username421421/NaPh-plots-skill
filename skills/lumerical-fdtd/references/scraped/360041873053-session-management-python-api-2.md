# Session Management - Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/360041873053-Session-management-Python-API  
Area: Discovered official source  
Topic: Discovered from Installation and Getting Started - Python API  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Session Management - Python API` for the topic `Discovered from Installation and Getting Started - Python API`. It captured 8 heading(s), 11 link(s), 9 code block(s), 1 inline code term(s), and 1 table(s). Main headings: Session Management - Python API, Starting a Local Session, Starting a Remote Session using the Interop Server, Advanced session management, Wrapping the session in a function, Using the "with" context manager, Passing in Command Line Arguments, Closing the session. Key detected terms: command, fdtd, import, mode, port, python, python-api, script, sweep.

## Key Terms

- command
- fdtd
- import
- mode
- port
- python
- python-api
- script
- sweep

## Captured Headings

- Session Management - Python API
- Starting a Local Session
- Starting a Remote Session using the Interop Server
- Advanced session management
- Wrapping the session in a function
- Using the "with" context manager
- Passing in Command Line Arguments
- Closing the session

## Official Text Excerpt

> Session Management - Python API Starting a Local Session The Python API interacts with Lumerical products through sessions. The simplest way to create a session is by calling the relevant constructor for the Lumerical product and storing it in an object. These constructors construct objects derived from the Lumerical class. Example Parameters | Product | Derived Class |Ansys Lumerical FDTD™|FDTD |Ansys Lumerical MODE™|MODE |Ansys Lumerical Multiphysics™|DEVICE |Ansys Lumerical INTERCONNECT™|INTERCONNECT Multiple sessions can also be created. Sessions may be for the same product. Example Each of the product's constructor supports various parameters and keyword arguments. For more information, see the Lumerical Python API Reference. Example Starting a Remote Session using the Interop Server Since the 2023 R1.2 release, the Python API can be used remotely on a Linux machine running the interop server (see Interop Server - Remote API to configure and run the interop server). To use the remote API, an additional parameter is required when starting a session, to specify the IP address and port to use to connect to the interop server. This port must be the starting ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `fdtd = lumapi.FDTD()`
- Code block 2: 1 line(s); first line `mode1 = lumapi.MODE()mode2 = lumapi.MODE()device = lumapi.DEVICE()`
- Code block 3: 1 line(s); first line `# loads and runs script.lsf while hiding the application windowinc = lumapi.INTERCONNECT(filename="script.lsf", hide=True)`
- Code block 4: 1 line(s); first line `remoteArgs = { "hostname": "192.168.215.129","port": 8989 }fdtd = lumapi.FDTD(hide=True, remoteArgs=remoteArgs)`
- Code block 5: 4 line(s); first line `def myFunction(someOptionalParameter):`
- Code block 6: 6 line(s); first line `with lumapi.FDTD(hide=True) as fdtd:`
- Code block 7: 4 line(s); first line `fdtd = lumapi.FDTD(serverArgs = {`
- Code block 8: 1 line(s); first line `fdtd-solutions -threads 2 -platform offscreen -use-solve`
- Code block 9: 1 line(s); first line `inc.close() #inc is the name of the active session`

## Inline Code Inventory

- `serverArgs`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Product, Derived Class
  - First row sample: Ansys Lumerical FDTD™ | FDTD

## Official Links Found

- [Lumerical class.](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [Lumerical Python API Reference](https://optics.ansys.com/hc/en-us/articles/38660003331859-Lumerical-Python-API-Reference)
- [Interop Server - Remote API](https://optics.ansys.com/hc/en-us/articles/15499581457811)
- [Passing data](https://optics.ansys.com/hc/en-us/articles/360041401434)
- [Working with Simulation Objects](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Windows](https://optics.ansys.com/hc/en-us/articles/360024812334-Running-simulations-using-the-Windows-command-prompt)
- [Linux](https://optics.ansys.com/hc/en-us/articles/360024974033-Running-simulations-using-terminal-on-Linux)
- [Python API Overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Working with Simulation Objects – Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods – Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-Commands-as-Methods-Python-API)
- [Installation and Getting Started – Python API](https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- None
