# lumopt2.fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#lumopt2-fom)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `lumopt2.fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#lumopt2-fom)` for the topic `Discovered from lumopt2 API reference`. It captured 3 heading(s), 8 link(s), 2 code block(s), 0 inline code term(s), and 0 table(s). Main headings: lumopt2.fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#lumopt2-fom), Classes [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#classes), Examples [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#examples). Key detected terms: lumopt, mode, monitor, optimization, port, structure, transmission.

## Key Terms

- lumopt
- mode
- monitor
- optimization
- port
- structure
- transmission

## Captured Headings

- lumopt2.fom [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#lumopt2-fom)
- Classes [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#classes)
- Examples [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#examples)

## Official Text Excerpt

> lumopt2.fom # The figure of merit module defines the objective functions for optimization. Figure of merit (FOM) module for inverse design optimization. This module provides classes for defining and computing figures of merit based on simulation results from field and port monitors. The FOM determines what is being optimized in the inverse design problem. Classes # Fom Factory function that returns FieldFom or PortFom based on monitor types. BaseFom Base class providing shared FOM infrastructure (advanced use). FieldFom FOM calculator for field-based (DFT monitor) simulations. PortFom FOM calculator for port-based (waveguide mode) simulations. FieldResults Container for field monitor simulation results. PortResults Container for port monitor simulation results. Examples # Port transmission optimization (using factory): Field intensity optimization (using factory): fom.fom Factory function to create the correct FoM subclass based on the simulation result. lumopt2.fom.fom fom.field_fom FoM calculator for field region results. lumopt2.fom.field_fom fom.port_fom FoM calculator for port results. lumopt2.fom.port_fom fom.base_fom Base class providing shared FoM infrastructure. lumopt2.fom.base_fom fom.simulation_results Containers for simulation results from field region and ports. lumopt2.fom.simulation_results

## Code Block Inventory

- Code block 1: 5 line(s); first line `>>> from lumopt2.fom import Fom, PortResults`
- Code block 2: 4 line(s); first line `>>> from lumopt2.fom import Fom, FieldResults`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#lumopt2-fom)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#classes)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/index.html#examples)
- [lumopt2.fom.fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/fom.html)
- [lumopt2.fom.field_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/field_fom.html)
- [lumopt2.fom.port_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/port_fom.html)
- [lumopt2.fom.base_fom](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/base_fom.html)
- [lumopt2.fom.simulation_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/fom/simulation_results.html)

## Ansys-Related External Links Found

- None

## External Links Found

- None
