# Untitled

Source URL: https://lumerical.docs.pyansys.com/version/stable/_static/simulation_examples/lumopt2_3x3pillar/metalens_3x3.py  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Untitled` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 0 heading(s), 0 link(s), 0 code block(s), 0 inline code term(s), and 0 table(s). Main headings: no captured headings. Key detected terms: fdtd, import, lumopt, monitor, optimization, port, source.

## Key Terms

- fdtd
- import
- lumopt
- monitor
- optimization
- port
- source

## Captured Headings

- No headings extracted

## Official Text Excerpt

> import os import numpy as np import ansys.lumerical.core.lumopt2 as lmpt # Set working directory to current path cwd_path = os.path.dirname(__file__) os.chdir(cwd_path) ## OPTIMIZATION REGION ## optimization_region = lmpt.Box(x_span=1e-6, y_span=1e-6, z_min=1e-6, z_max=1e-6 + 750e-9, dx=0.025e-6, dy=0.025e-6, dz=0.025e-6) ## PARAMETRIZATION ## num_cyl = 3 * 3 bounds = [(0.05e-6, 0.1e-6)] * num_cyl def param_func(params): return {f"cyl{idx}::radius": value for idx, value in enumerate(params)} parametrization = lmpt.Parametrization(func=param_func, bounds=bounds, optimization_region=optimization_region) ## INITIAL PARAMETERS ## params = np.ones(num_cyl) * 0.075e-6 ## FIGURE OF MERIT ## # Sum of field intensity at 'focus' normalized by sum of field intensity at 'norm' intensity_focus = lmpt.FieldResults(monitor_name="focus", metric="intensity", wavelengths=940e-9) intensity_norm = lmpt.FieldResults(monitor_name="norm", metric="intensity", wavelengths=940e-9) def custom_fct(result_list): return result_list[0] / result_list[1] fom = lmpt.Fom([intensity_focus, intensity_norm], fct=custom_fct) ## PROJECT CONFIGURATION ## project = lmpt.Project( setup=os.path.join(cwd_path, "metalens_3x3.fsp"), parametrization=parametrization, fom=fom, fdtd_session=lmpt.FdtdSession(show_fdtd_cad=False), runner=lmpt.LocalRunner(resource="GPU"), ) ## VALIDATION ## project.visualize_fom(params=params) # Test Figure of Merit ## OPTIMIZATION ## optimizer = lmpt.ScipyOptimizer(bounds=bounds, max_iter=15, gtol=1e-9) visualizer = lmpt.GraphicalVisualizer() optimization = lmpt.Optimization(project, optimizer, visualizer) optimization.run(initial_params=params)

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- None

## Ansys-Related External Links Found

- None

## External Links Found

- None
