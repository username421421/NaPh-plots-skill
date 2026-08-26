# Working with simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#working-with-simulation-objects)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html  
Area: PyLumerical  
Topic: Object construction, OrderedDict, keyword args, object handles, duplicate names  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Working with simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#working-with-simulation-objects)` for the topic `Object construction, OrderedDict, keyword args, object handles, duplicate names`. It captured 11 heading(s), 16 link(s), 9 code block(s), 6 inline code term(s), and 0 table(s). Main headings: Working with simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#working-with-simulation-objects), Creating simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#creating-simulation-objects), Assigning properties with an ordered dict [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-an-ordered-dict), Assigning properties with keyword arguments [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-keyword-arguments), Assigning properties with “set” [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-set), Linked properties [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#linked-properties), Manipulating simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#manipulating-simulation-objects), Direct attribute access [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#direct-attribute-access). Key detected terms: command, fdtd, geometry, import, monitor, port, pylumerical, python, script, source, structure.

## Key Terms

- command
- fdtd
- geometry
- import
- monitor
- port
- pylumerical
- python
- script
- source
- structure

## Captured Headings

- Working with simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#working-with-simulation-objects)
- Creating simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#creating-simulation-objects)
- Assigning properties with an ordered dict [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-an-ordered-dict)
- Assigning properties with keyword arguments [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-keyword-arguments)
- Assigning properties with “set” [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-set)
- Linked properties [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#linked-properties)
- Manipulating simulation objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#manipulating-simulation-objects)
- Direct attribute access [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#direct-attribute-access)
- Dict-like access [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#dict-like-access)
- Duplicate names [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#duplicate-names)
- Parent and children objects [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#parent-and-children-objects)

## Official Text Excerpt

> Working with simulation objects # At a basic level, you can interact with simulation objects in the same way as when you use the Lumerical Script Language. However, Lumerical scripting language interacts primarily with the currently selected object, which may not be clear from the Python code alone. Therefore, PyLumerical also provides you with ways to interact with all objects that fits better with the Python coding style. This article describes various ways to interact with simulation objects, such as structures, sources, and monitors. For more information on how to use script commands in PyLumerical, see the article on Script commands as methods. Creating simulation objects # When adding a simulation object into Lumerical products using PyLumerical, you can set the values of properties at creation. There are multiple ways of assigning the properties of objects when you create them. Assigning properties with an ordered dict # You can also use a Python``dict as a constructor to the object by assigning it to the attribute properties. In Python,``dict ordering isn’t guaranteed, so if there are properties that depend on other ...

## Code Block Inventory

- Code block 1: 6 line(s); first line `1from collections import OrderedDict`
- Code block 2: 2 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 3: 4 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 4: 3 line(s); first line `1with lumapi.FDTD() as fdtd:`
- Code block 5: 1 line(s); first line `1rect1.x_span=2e-06 # Note that this is different than what was set earlier from the x_span argument`
- Code block 6: 3 line(s); first line `1rectangle = fdtd.addrect(x = 2e-6, y = 0.0, z = 0.0)`
- Code block 7: 3 line(s); first line `1rectangle = fdtd.addrect(x = 2e-6, y = 0.0, z = 0.0)`
- Code block 8: 11 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 9: 12 line(s); first line `1# Create 3 rectangles and list their names`

## Inline Code Inventory

- `collections.OrderedDict`
- `dict`
- `x`
- `x max`
- `x min`
- `x span`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#working-with-simulation-objects)
- [Script commands as methods](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#creating-simulation-objects)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-an-ordered-dict)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-keyword-arguments)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#assigning-properties-with-set)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set-Script-command)
- [setnamed](https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed-Script-command)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#linked-properties)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#manipulating-simulation-objects)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#direct-attribute-access)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#dict-like-access)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#duplicate-names)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html#parent-and-children-objects)

## Ansys-Related External Links Found

- None

## External Links Found

- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
- [collections.OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
