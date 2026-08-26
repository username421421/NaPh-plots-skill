# Script commands as methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#script-commands-as-methods)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html  
Area: PyLumerical  
Topic: Lumerical script commands, constructors, custom functions, unsupported methods  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Script commands as methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#script-commands-as-methods)` for the topic `Lumerical script commands, constructors, custom functions, unsupported methods`. It captured 8 heading(s), 40 link(s), 16 code block(s), 6 inline code term(s), and 0 table(s). Main headings: Script commands as methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#script-commands-as-methods), Built-in scripting commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#built-in-scripting-commands), Overview [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#overview), Constructor script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#constructor-script-commands), Importing custom script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#importing-custom-script-commands), Non-constructor script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#non-constructor-script-commands), Unsupported methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#unsupported-methods), Local documentation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#local-documentation). Key detected terms: command, fdtd, gaussian, import, mode, monitor, plane, port, pylumerical, python, script, script-command, source, transmission.

## Key Terms

- command
- fdtd
- gaussian
- import
- mode
- monitor
- plane
- port
- pylumerical
- python
- script
- script-command
- source
- transmission

## Captured Headings

- Script commands as methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#script-commands-as-methods)
- Built-in scripting commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#built-in-scripting-commands)
- Overview [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#overview)
- Constructor script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#constructor-script-commands)
- Importing custom script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#importing-custom-script-commands)
- Non-constructor script commands [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#non-constructor-script-commands)
- Unsupported methods [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#unsupported-methods)
- Local documentation [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#local-documentation)

## Official Text Excerpt

> Script commands as methods # At the most basic level, you can use PyLumerical to directly invoke Lumerical script commands and interact with the product as the Lumerical Scripting Language would. This article describes the basic use case for using scripting commands as methods, and common best practices. Built-in scripting commands # Overview # You can use almost all script commands in the Lumerical Scripting Language as methods on your session object in Python. The PyLumerical methods and the Lumerical script commands share the same name, and you can call them directly on the session object once you create it. For more information on the Lumerical Scripting Language, please see: - Lumerical Scripting Learning Track on Ansys Innovation Courses (AIC) - Lumerical Scripting Language - Alphabetical list - Lumerical Scripting Language - By category Two simple examples are show below. The first example uses Lumerical commands getfdtdindex and stackrt in conjunction with typical math and plotting libraries in Python to simulate and visualize the transmission of a gold thin film illuminated by a plane wave. The second example sets up ...

## Code Block Inventory

- Code block 1: 23 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 2: 44 line(s); first line `1import os,sys`
- Code block 3: 8 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 4: 6 line(s); first line `1from collections import OrderedDict # Ensure OrderedDict is imported`
- Code block 5: 2 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 6: 7 line(s); first line `1function helloWorld(){`
- Code block 7: 3 line(s); first line `1function customMultiply(a,b){`
- Code block 8: 6 line(s); first line `1with lumapi.FDTD(script = ["MyFunctions.lsf", "MyFunctions2.lsf"]) as fdtd:`
- Code block 9: 3 line(s); first line `1helloworld`
- Code block 10: 4 line(s); first line `1fdtd.addfdtd()`
- Code block 11: 2 line(s); first line `1fdtd.addfdtd()`
- Code block 12: 12 line(s); first line `1function constructFDTDandRect(x_input,y_input,z_input){`
- Code block 13: 6 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 14: 4 line(s); first line `1fdtd = lumapi.FDTD()`
- Code block 15: 5 line(s); first line `1# First, create an FDTD object`
- Code block 16: 17 line(s); first line `1Help on method addfdtd in module lumapi:`

## Inline Code Inventory

- `ansys.lumerical.core.DEVICE.eval()`
- `ansys.lumerical.core.FDTD.eval()`
- `ansys.lumerical.core.INTERCONNECT.eval()`
- `ansys.lumerical.core.MODE.eval()`
- `x span`
- `x_span`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#script-commands-as-methods)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#built-in-scripting-commands)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#overview)
- [Lumerical Scripting Language - Alphabetical list](https://optics.ansys.com/hc/en-us/articles/360034923553)
- [Lumerical Scripting Language - By category](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [getfdtdindex](https://optics.ansys.com/hc/en-us/articles/360034409694-getfdtdindex-Script-command)
- [stackrt](https://optics.ansys.com/hc/en-us/articles/360034406254-stackrt-Script-command)
- [Installation and getting started for PyLumerical](https://lumerical.docs.pyansys.com/version/stable/getting_started/index.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#constructor-script-commands)
- [addrect](https://optics.ansys.com/hc/en-us/articles/360034404214-addrect-Script-command)
- [addfdtd](https://optics.ansys.com/hc/en-us/articles/360034924173-addfdtd-Script-command)
- [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set-Script-command)
- [setnamed](https://optics.ansys.com/hc/en-us/articles/360034928793-setnamed-Script-command)
- [Working with simulation objects](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#importing-custom-script-commands)
- [script keyword argument](https://lumerical.docs.pyansys.com/version/stable/api/interface_class.html)
- [ansys.lumerical.core.FDTD.eval()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.FDTD.eval.html#ansys.lumerical.core.FDTD.eval)
- [ansys.lumerical.core.MODE.eval()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.MODE.eval.html#ansys.lumerical.core.MODE.eval)
- [ansys.lumerical.core.DEVICE.eval()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.DEVICE.eval.html#ansys.lumerical.core.DEVICE.eval)
- [ansys.lumerical.core.INTERCONNECT.eval()](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.INTERCONNECT.eval.html#ansys.lumerical.core.INTERCONNECT.eval)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#non-constructor-script-commands)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#unsupported-methods)
- [*](https://optics.ansys.com/hc/en-us/articles/360034930833)
- [/](https://optics.ansys.com/hc/en-us/articles/360034930853)
- [+](https://optics.ansys.com/hc/en-us/articles/360034410254)
- [-](https://optics.ansys.com/hc/en-us/articles/360034930873)
- [^](https://optics.ansys.com/hc/en-us/articles/360034410274)
- [>=](https://optics.ansys.com/hc/en-us/articles/360034930933)
- [<](https://optics.ansys.com/hc/en-us/articles/360034410334)
- [>](https://optics.ansys.com/hc/en-us/articles/360034930953)
- [&](https://optics.ansys.com/hc/en-us/articles/360034930973)
- [and](https://optics.ansys.com/hc/en-us/articles/360034410354)
- [|](https://optics.ansys.com/hc/en-us/articles/360034410374)
- [or](https://optics.ansys.com/hc/en-us/articles/360034930993)
- [!](https://optics.ansys.com/hc/en-us/articles/360034931013)
- [~](https://optics.ansys.com/hc/en-us/articles/360034931033)
- [? (print, display)](https://optics.ansys.com/hc/en-us/articles/360034410434)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/script_commands_as_methods.html#local-documentation)
- [Alphabetical List of Script Commands](https://optics.ansys.com/hc/en-us/articles/360034923553)

## Ansys-Related External Links Found

- [Lumerical Scripting Learning Track on Ansys Innovation Courses (AIC)](https://innovationspace.ansys.com/product/ansys-lumerical-scripting/)

## External Links Found

- None
