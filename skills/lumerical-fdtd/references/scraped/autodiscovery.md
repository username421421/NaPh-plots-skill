# Autodiscovery [#](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html#autodiscovery)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html  
Area: PyLumerical  
Topic: Lumerical install autodiscovery and manual path fallback  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Autodiscovery [#](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html#autodiscovery)` for the topic `Lumerical install autodiscovery and manual path fallback`. It captured 1 heading(s), 3 link(s), 0 code block(s), 12 inline code term(s), and 1 table(s). Main headings: Autodiscovery [#](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html#autodiscovery). Key detected terms: import, lumopt, port, pylumerical, python.

## Key Terms

- import
- lumopt
- port
- pylumerical
- python

## Captured Headings

- Autodiscovery [#](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html#autodiscovery)

## Official Text Excerpt

> Autodiscovery # PyLumerical requires Lumerical 2022 R1 or later to run. The autodiscovery function first attempts to find the installation location using the following methods: - Environment variable: PyLumerical checks the`LUMERICAL_HOME`environment variable for the installation path. If found, this path is used. - Windows registry: On Windows, PyLumerical checks the registry for the installation path of Lumerical products. - Default installation paths: If the registry lookup fails, or if you are using Linux, PyLumerical checks the default installation paths: - On Windows, with the Lumerical standalone installer:`C:\Program Files\Lumerical\` - On Windows, with the Ansys automated installer:`C:\Program Files\Ansys Inc\` - On Linux, with the Lumerical standalone installer:`/opt/lumerical/` - On Linux, with the Ansys automated installer:`~/Ansys/ansys_inc/` When PyLumerical finds an installation path, it configures the interop path. If bundled`lumopt2`is present, PyLumerical enables`import lumopt2`and`import ansys.lumerical.core.lumopt2`directly without exposing unrelated modules from`<install>/api/python`. If PyLumerical can’t find the installation path automatically, it returns a warning. Set`LUMERICAL_HOME`before import and start a new Python session. Manual`sys.path`overrides for`lumopt2`are unsupported. The autodiscovery helpers below run automatically when you import PyLumerical: | ``ansys.lumerical.core.autodiscovery.locate_lumerical_install () | Locate the installation directory and interop ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `/opt/lumerical/`
- `<install>/api/python`
- `C:\Program Files\Ansys Inc\`
- `C:\Program Files\Lumerical\`
- `LUMERICAL_HOME`
- `ansys.lumerical.core.autodiscovery.get_lumerical_api_python_path`
- `ansys.lumerical.core.autodiscovery.locate_lumerical_install`
- `import ansys.lumerical.core.lumopt2`
- `import lumopt2`
- `lumopt2`
- `sys.path`
- `~/Ansys/ansys_inc/`

## Table Inventory

- Table 1: 2 column(s), 2 row(s)
  - First row sample: ansys.lumerical.core.autodiscovery.locate_lumerical_install () | Locate the installation directory and interop library directory for Lumerical software.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/autodiscovery.html#autodiscovery)
- [ansys.lumerical.core.autodiscovery.locate_lumerical_install](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.autodiscovery.locate_lumerical_install.html#ansys.lumerical.core.autodiscovery.locate_lumerical_install)
- [ansys.lumerical.core.autodiscovery.get_lumerical_api_python_path](https://lumerical.docs.pyansys.com/version/stable/api/_autosummary/ansys.lumerical.core.autodiscovery.get_lumerical_api_python_path.html#ansys.lumerical.core.autodiscovery.get_lumerical_api_python_path)

## Ansys-Related External Links Found

- None

## External Links Found

- None
