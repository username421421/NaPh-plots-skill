# Session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#session-management)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html  
Area: PyLumerical  
Topic: Product sessions, context managers, serverArgs, close behavior  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#session-management)` for the topic `Product sessions, context managers, serverArgs, close behavior`. It captured 7 heading(s), 13 link(s), 8 code block(s), 1 inline code term(s), and 1 table(s). Main headings: Session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#session-management), Starting a local session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#starting-a-local-session), Advanced session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#advanced-session-management), Wrapping the session in a function [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#wrapping-the-session-in-a-function), Using the “with” context manager [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#using-the-with-context-manager), Passing in command line arguments [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#passing-in-command-line-arguments), Closing the session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#closing-the-session). Key detected terms: command, fdtd, mode, port, pylumerical, python, script, sweep.

## Key Terms

- command
- fdtd
- mode
- port
- pylumerical
- python
- script
- sweep

## Captured Headings

- Session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#session-management)
- Starting a local session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#starting-a-local-session)
- Advanced session management [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#advanced-session-management)
- Wrapping the session in a function [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#wrapping-the-session-in-a-function)
- Using the “with” context manager [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#using-the-with-context-manager)
- Passing in command line arguments [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#passing-in-command-line-arguments)
- Closing the session [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#closing-the-session)

## Official Text Excerpt

> Session management # Starting a local session # The Python API interacts with Lumerical products through sessions. The simplest way to create a session is by calling the relevant constructor for the Lumerical product and storing it in an object. These constructors construct objects derived from the Lumerical class. Example Parameters | Product | Derived Class | Ansys Lumerical FDTD™ | FDTD | Ansys Lumerical MODE™ | MODE | Ansys Lumerical Multiphysics™ | DEVICE | Ansys Lumerical INTERCONNECT™ | INTERCONNECT You can also create multiple sessions, even if they’re for the same product. Example Each of the product’s constructor supports various parameters and keyword arguments. For more information, see API reference. Example Advanced session management # Wrapping the session in a function # You can wrap Lumerical sessions in a function to simplify setup. This is useful when you need multiple sessions where some parameters are constant while others change. For example, when sweeping over parameters. For more information on how Lumerical sessions return results, see Passing data and Working with simulation objects. Example Using the “with” context manager # ...

## Code Block Inventory

- Code block 1: 3 line(s); first line `1# Starting a local Lumerical FDTD session`
- Code block 2: 4 line(s); first line `1# Starting two Lumerical MODE sessions one Lumerical Multiphysics session`
- Code block 3: 3 line(s); first line `1# Loads and runs script.lsf while hiding the application`
- Code block 4: 9 line(s); first line `1def myFunction(gaussianParameters=dict()):`
- Code block 5: 6 line(s); first line `1with lumapi.FDTD(hide=True) as fdtd:`
- Code block 6: 5 line(s); first line `1fdtd = lumapi.FDTD(serverArgs = {`
- Code block 7: 1 line(s); first line `1fdtd-solutions -threads 2 -platform offscreen -use-solve`
- Code block 8: 1 line(s); first line `1inc.close() # inc is the name of the active session`

## Inline Code Inventory

- `serverArgs`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Product, Derived Class
  - First row sample: Ansys Lumerical FDTD™ | FDTD

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#session-management)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#starting-a-local-session)
- [Lumerical class](https://lumerical.docs.pyansys.com/version/stable/api/interface_class.html)
- [API reference](https://lumerical.docs.pyansys.com/version/stable/api/index.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#advanced-session-management)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#wrapping-the-session-in-a-function)
- [Passing data](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html)
- [Working with simulation objects](https://lumerical.docs.pyansys.com/version/stable/user_guide/working_with_simulation_objects.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#using-the-with-context-manager)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#passing-in-command-line-arguments)
- [Windows](https://optics.ansys.com/hc/en-us/articles/360024812334-Running-simulations-using-the-Windows-command-prompt)
- [Linux](https://optics.ansys.com/hc/en-us/articles/360024974033-Running-simulations-using-terminal-on-Linux)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/session_management.html#closing-the-session)

## Ansys-Related External Links Found

- None

## External Links Found

- None
