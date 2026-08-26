# Accessing simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-simulation-results)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html  
Area: PyLumerical  
Topic: getresult, getdata, datasets, raw arrays  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Accessing simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-simulation-results)` for the topic `getresult, getdata, datasets, raw arrays`. It captured 3 heading(s), 11 link(s), 7 code block(s), 4 inline code term(s), and 1 table(s). Main headings: Accessing simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-simulation-results), Accessing datasets [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-datasets), Accessing raw data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-raw-data). Key detected terms: command, dataset, fdtd, monitor, pylumerical, python, script, structure.

## Key Terms

- command
- dataset
- fdtd
- monitor
- pylumerical
- python
- script
- structure

## Captured Headings

- Accessing simulation results [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-simulation-results)
- Accessing datasets [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-datasets)
- Accessing raw data [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-raw-data)

## Official Text Excerpt

> Accessing simulation results # Simulation results are typically stored in datasets simulation or monitor objects Lumerical products. This article describes how you can access and process datasets and raw simulation data when using the PyLumerical. For more information on how PyLumerical translates basic data types and best practices when transferring data, see the article on Passing data, for more information on Lumerical datasets, see the Lumerical Knowledge Base article Introduction to lumerical datasets. Accessing datasets # Lumerical products package relevant results in datasets so that you can readily visualize and explore them. You can use the getresult method to retrieve these datasets into the Python workspace. PyLumerical retrieves datasets as dictionaries, with keys associated with various attributes and parameters. Dictionaries converted from datasets have a special metadata key`Lumerical_dataset`which contains identifier values, this key preserves their structure when performing a roundtrip back to the Lumerical environment. When passing a dictionary from Python to Lumerical, PyLumerical converts it into a generic structure, unless it has the metadata element. Attributes and parameters are both stored as``numpy.ndarray. Parameters are 1-D arrays that acts as ...

## Code Block Inventory

- Code block 1: 19 line(s); first line `1from collections import OrderedDict`
- Code block 2: 8 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 3: 2 line(s); first line `1Transmission result T is type <class 'dict'> with keys dict_keys(['lambda', 'f', 'T', 'Lumerical_dataset'])`
- Code block 4: 33 line(s); first line `1from collections import OrderedDict`
- Code block 5: 1 line(s); first line `1unstructured_result is of type <class 'dict'> and contains dict_keys(['area', 'ID', 'x', 'y', 'z', 'connectivity', 'N', 'Lumerical_dataset'])`
- Code block 6: 14 line(s); first line `1import ansys.lumerical.core as lumapi`
- Code block 7: 4 line(s); first line `1Frequency field profile data Ex is type with shape (99, 59, 1, 5)`

## Inline Code Inventory

- `Lumerical_dataset`
- `connectivity`
- `numpy.ndarray`
- `numpy.squeeze()`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - Headers: Dataset Type, Attribute Dimensions
  - First row sample: Matrix Dataset | Dimensions depend on type of attribute: Scalar attribute: [ \(N_{p1}\) ; \(N_{p2}\) ; … ; \(N_{pn}\) ] Vector attribute: [ \(N_{p1}\) ; \(N_{p2}\) ; … ; \(N_{pn}\) ; 3 ] where \(N_{p_i}\) is the length of the \(i\) th param

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-simulation-results)
- [Passing data](https://lumerical.docs.pyansys.com/version/stable/user_guide/passing_data.html)
- [Introduction to lumerical datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-datasets)
- [getresult](https://optics.ansys.com/hc/en-us/articles/360034409854)
- [attributes and parameters](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets#toc_3)
- [pinch](https://optics.ansys.com/hc/en-us/articles/360034405674)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/accessing_simulation_results.html#accessing-raw-data)
- [getdata](https://optics.ansys.com/hc/en-us/articles/360034409834)

## Ansys-Related External Links Found

- None

## External Links Found

- [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [numpy.squeeze()](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html#numpy.squeeze)
