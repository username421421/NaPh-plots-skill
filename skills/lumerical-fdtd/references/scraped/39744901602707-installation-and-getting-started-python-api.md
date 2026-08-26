# Installation and Getting Started – Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API  
Area: Python API  
Topic: Import paths, embedded Python, external Python setup  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Installation and Getting Started – Python API` for the topic `Import paths, embedded Python, external Python setup`. It captured 5 heading(s), 14 link(s), 10 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Installation and Getting Started – Python API, System Requirements, Installation and Importing Modules, Using Python API with the CAD Script Editor, Using Python API with External Editor. Key detected terms: command, import, lumapi, port, python, python-api, script.

## Key Terms

- command
- import
- lumapi
- port
- python
- python-api
- script

## Captured Headings

- Installation and Getting Started – Python API
- System Requirements
- Installation and Importing Modules
- Using Python API with the CAD Script Editor
- Using Python API with External Editor

## Official Text Excerpt

> Installation and Getting Started – Python API The Lumerical Python API is a powerful interoperability tool that integrates Lumerical tools with the Python language, allowing you to develop complex automated workflows and perform advanced data processing operations. In this article, installation of the Lumerical Python API is explained. System Requirements - Lumerical product version 2019a R3 or later - Gnome or Mate terminal for supported Linux systems - The Gnome or Mate desktop environment is required if running from the Lumerical CAD/GUI. - A Lumerical GUI license – a GUI license is required as the Python API interfaces with the Lumerical GUI Installation and Importing Modules The Python API can be used either with the built-in script editor to the Lumerical CAD, or with an external Python editor. Using Python API with the CAD Script Editor All Lumerical products since 2019a R3 are shipped with a basic Python 3 distribution, and Python can be directly edited and executed with the built-in CAD script editor. To add a Python file, you can click on the arrow beside the “New Lumerical Script” ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `import lumapi`
- Code block 2: 1 line(s); first line `C:\\Program Files\\Lumerical\\[[verpath]]\\api\\python\\`
- Code block 3: 1 line(s); first line `C:\\Program Files\\Ansys Inc\\[[verpath]]\\Lumerical\\api\\python\\`
- Code block 4: 1 line(s); first line `/opt/lumerical/[[verpath]]/api/python/`
- Code block 5: 1 line(s); first line `~/Ansys/ansys_inc/[[verpath]]/Lumerical/api/python/`
- Code block 6: 1 line(s); first line `import sys, os#default path for current release sys.path.append("C:\\Program Files\\Lumerical\\[[verpath]]\\api\\python\\") #lumapi directorysys.path.append(os.`
- Code block 7: 1 line(s); first line `import sys, os#default path for current release sys.path.append("/opt/lumerical/[[verpath]]/api/python/") sys.path.append(os.path.dirname(__file__)) #Current di`
- Code block 8: 1 line(s); first line `import importlib.util#default path for current release spec_win = importlib.util.spec_from_file_location('lumapi', 'C:\\Program Files\\Lumerical\\[[verpath]]\\a`
- Code block 9: 1 line(s); first line `import importlib.util#default path for current release spec_lin = importlib.util.spec_from_file_location('lumapi', "/opt/lumerical/[[verpath]]/api/python/lumapi`
- Code block 10: 1 line(s); first line `import lumapi`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [supported Linux systems](https://optics.ansys.com/hc/en-us/articles/16391565007379-System-Requirements)
- [Lumerical Installer](https://optics.ansys.com/hc/en-us/articles/360024508974-Windows-installation-guide)
- [Ansys Automated Installer](https://optics.ansys.com/hc/en-us/articles/36966860625171-Installing-Lumerical-Using-the-Ansys-Automated-Installer)
- [RedHat/Rocky Linux](https://optics.ansys.com/hc/en-us/articles/360020603053-RHEL-CentOS-Linux-installation-guide)
- [SUSE Linux Enterprise Server](https://optics.ansys.com/hc/en-us/articles/4402705320211-SUSE-Linux-Enterprise-Server-installation-guide)
- [Ubuntu](https://optics.ansys.com/hc/en-us/articles/1500005392522-Ubuntu-Linux-installation-guide)
- [Session Management](https://optics.ansys.com/hc/en-us/articles/360041873053-Session-management-Python-API)
- [Working with Simulation Objects](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [Python API Overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Session Management – Python API](https://optics.ansys.com/hc/en-us/articles/360041873053-Session-management-Python-API)
- [Working with Simulation Objects – Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods – Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- [modifying Python’s search path](https://docs.python.org/3.3/install/index.html#inst-search-path)
