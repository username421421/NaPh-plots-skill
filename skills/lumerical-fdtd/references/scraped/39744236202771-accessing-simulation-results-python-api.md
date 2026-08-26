# Accessing Simulation Results – Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/39744236202771-Accessing-Simulation-Results-Python-API  
Area: Python API  
Topic: getresult, getdata, dataset dictionaries, raw arrays  
Discovery depth: 0  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Accessing Simulation Results – Python API` for the topic `getresult, getdata, dataset dictionaries, raw arrays`. It captured 3 heading(s), 13 link(s), 7 code block(s), 1 inline code term(s), and 1 table(s). Main headings: Accessing Simulation Results – Python API, Accessing Datasets, Accessing Raw Data. Key detected terms: command, dataset, fdtd, monitor, python, python-api, script, structure.

## Key Terms

- command
- dataset
- fdtd
- monitor
- python
- python-api
- script
- structure

## Captured Headings

- Accessing Simulation Results – Python API
- Accessing Datasets
- Accessing Raw Data

## Official Text Excerpt

> Accessing Simulation Results – Python API Simulation results are typically stored in datasets simulation or monitor objects Lumerical products. This article will describe how datasets and raw simulation data can be accessed and processed when using the Python API. For more information on how basic datatypes are translated and best practices when transferring data, see the Knowledge Base article Passing Data in Python API, for more information on Lumerical datasets, see the Knowledge Base article Introduction to Lumerical Datasets. Accessing Datasets Datasets are relevant results that have been packaged in a form that makes it possible to readily visualize and explore in Lumerical. These datasets can be passed into the Python workspace using the getresult() method. When datasets are returned into the Python environment, they will be converted into dictionaries, with keys associated with various attributes and parameters. Dictionaries converted from datasets will have a special metadata key 'Lumerical_dataset' which contains identifier values, allows their structure to be preserved when performing a roundtrip back to the Lumerical environment. When passing a dictionary from Python to Lumerical it will be converted ...

## Code Block Inventory

- Code block 1: 19 line(s); first line `from collections import OrderedDict`
- Code block 2: 9 line(s); first line `import lumapi`
- Code block 3: 1 line(s); first line `Transmission result T is type <class 'dict'> with keys dict_keys(['lambda', 'f', 'T', 'Lumerical_dataset'])Time monitor result E is type <class 'dict'> with key`
- Code block 4: 33 line(s); first line `from collections import OrderedDict`
- Code block 5: 1 line(s); first line `unstructured_result is of type <class 'dict'> and contains dict_keys(['area', 'ID', 'x', 'y', 'z', 'connectivity', 'N', 'Lumerical_dataset'])`
- Code block 6: 14 line(s); first line `import lumapi`
- Code block 7: 4 line(s); first line `Frequency field profile data Ex is type with shape (99, 59, 1, 5)`

## Inline Code Inventory

- `connectivity`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - First row sample: Dataset Type | Attribute Dimensions

## Official Links Found

- [Passing Data in Python API](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API)
- [Introduction to Lumerical Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets)
- [getresult()](https://optics.ansys.com/hc/en-us/articles/360034409854)
- [attributes and parameters](https://optics.ansys.com/hc/en-us/articles/360034409554-Introduction-to-Lumerical-datasets#toc_3)
- [pinch()](https://optics.ansys.com/hc/en-us/articles/360034405674)
- [getdata()](https://optics.ansys.com/hc/en-us/articles/360034409834)
- [Python API Overview](https://optics.ansys.com/hc/en-us/articles/360037824513-Python-API-overview)
- [Working with Simulation Objects – Python API](https://optics.ansys.com/hc/en-us/articles/39744946400659-Working-with-Simulation-Objects-Python-API)
- [Script Commands as Methods – Python API](https://optics.ansys.com/hc/en-us/articles/360041579954-Script-commands-as-methods-Python-API)
- [Installation and Getting Started – Python API](https://optics.ansys.com/hc/en-us/articles/39744901602707-Installation-and-Getting-Started-Python-API)
- [Passing Data – Python API](https://optics.ansys.com/hc/en-us/articles/360041401434-Passing-Data-Python-API)

## Ansys-Related External Links Found

- None

## External Links Found

- [numpy arrays](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)
- [squeeze method](https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html)
