# ClosedCurve [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#closedcurve)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html  
Area: Discovered official source  
Topic: Discovered from Getting started with lumopt2: simple metalens  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ClosedCurve [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#closedcurve)` for the topic `Discovered from Getting started with lumopt2: simple metalens`. It captured 1 heading(s), 27 link(s), 0 code block(s), 28 inline code term(s), and 2 table(s). Main headings: ClosedCurve [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#closedcurve). Key detected terms: fdtd, geometry, lumopt, material, mesh, optimization, structure.

## Key Terms

- fdtd
- geometry
- lumopt
- material
- mesh
- optimization
- structure

## Captured Headings

- ClosedCurve [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#closedcurve)

## Official Text Excerpt

> ClosedCurve # class lumopt2.parametrization.closed_curve. ClosedCurve (path, index: float|str, z_min: float, z_max: float, optimization_region: Box = None, num_pts_per_vertices: int = 50, dp: float = None) # A Beziergon - a polygon where edges can be linear or cubic Bezier curves. All curves are C1-continuous with their neighbors. Parameters: path``list List of (vertex, segment_type, n_vertices_lumerical_polygon[optional]) tuples. index`Union```[float,``str] Refractive index of the geometry or material name. z_min``float Minimum z-coordinate. z_max``float Maximum z-coordinate. optimization_region`Box`,`optional` Box defining optimization region (default: None). num_pts_per_vertices``int,`optional` Default number of points per segment (default: 50). dp``float,`optional` Perturbation size for finite difference gradient calculation (default: None, meaning it will be automatically determined). Methods | ``ClosedCurve.compute_gradient_from_fields (...) | Compute the gradient for a ClosedCurve parametrization. | ``ClosedCurve.compute_opt_params_direct_to_permittivity_jacobian (...) | Compute d_eps/dp, the (sparse) Jacobian of the permittivity wrt optimization parameters ('p'). | ``ClosedCurve.compute_parametrization_jacobian (params) | Compute the Jacobian of the parametrization function. | ``ClosedCurve.compute_params_to_lumerical_jacobian (params) | Compute Jacobian from optimization parameters to Lumerical parameters. | ``ClosedCurve.compute_polygon_jacobian (params) | Compute the Jacobian of the discretized polygon vertices. | ``ClosedCurve.create_optimization_structures (...) | Add optimization structure to FDTD simulation. | ``ClosedCurve.discretize_polygon (params) | Discretize the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `Box`
- `ClosedCurve.bounds`
- `ClosedCurve.compute_gradient_from_fields`
- `ClosedCurve.compute_opt_params_direct_to_permittivity_jacobian`
- `ClosedCurve.compute_parametrization_jacobian`
- `ClosedCurve.compute_params_to_lumerical_jacobian`
- `ClosedCurve.compute_polygon_jacobian`
- `ClosedCurve.create_optimization_structures`
- `ClosedCurve.discretize_polygon`
- `ClosedCurve.find_segments_connecting`
- `ClosedCurve.get_bounding_box`
- `ClosedCurve.get_bounds`
- `ClosedCurve.get_initial_params`
- `ClosedCurve.make_segments_parametric`
- `ClosedCurve.make_vertex_parametric`
- `ClosedCurve.plot`
- `ClosedCurve.set_parametrization_function`
- `ClosedCurve.split_segments`
- `ClosedCurve.store_mesh_info`
- `ClosedCurve.update_structure`
- `ClosedCurve.visualize`
- `Union`
- `float`
- `int`
- `list`
- `optional`
- `str`
- `structure`

## Table Inventory

- Table 1: 2 column(s), 19 row(s)
  - First row sample: ClosedCurve.compute_gradient_from_fields (...) | Compute the gradient for a ClosedCurve parametrization.
- Table 2: 2 column(s), 1 row(s)
  - First row sample: ClosedCurve.bounds | Parameter bounds for optimization.

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#closedcurve)
- [Box](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.Box.html#lumopt2.utils.common.Box)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [ClosedCurve.compute_gradient_from_fields](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.compute_gradient_from_fields.html#lumopt2.parametrization.closed_curve.ClosedCurve.compute_gradient_from_fields)
- [ClosedCurve.compute_opt_params_direct_to_permittivity_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.compute_opt_params_direct_to_permittivity_jacobian.html#lumopt2.parametrization.closed_curve.ClosedCurve.compute_opt_params_direct_to_permittivity_jacobian)
- [ClosedCurve.compute_parametrization_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.compute_parametrization_jacobian.html#lumopt2.parametrization.closed_curve.ClosedCurve.compute_parametrization_jacobian)
- [ClosedCurve.compute_params_to_lumerical_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.compute_params_to_lumerical_jacobian.html#lumopt2.parametrization.closed_curve.ClosedCurve.compute_params_to_lumerical_jacobian)
- [ClosedCurve.compute_polygon_jacobian](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.compute_polygon_jacobian.html#lumopt2.parametrization.closed_curve.ClosedCurve.compute_polygon_jacobian)
- [ClosedCurve.create_optimization_structures](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.create_optimization_structures.html#lumopt2.parametrization.closed_curve.ClosedCurve.create_optimization_structures)
- [ClosedCurve.discretize_polygon](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.discretize_polygon.html#lumopt2.parametrization.closed_curve.ClosedCurve.discretize_polygon)
- [ClosedCurve.find_segments_connecting](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.find_segments_connecting.html#lumopt2.parametrization.closed_curve.ClosedCurve.find_segments_connecting)
- [ClosedCurve.get_bounding_box](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.get_bounding_box.html#lumopt2.parametrization.closed_curve.ClosedCurve.get_bounding_box)
- [ClosedCurve.get_bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.get_bounds.html#lumopt2.parametrization.closed_curve.ClosedCurve.get_bounds)
- [ClosedCurve.get_initial_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.get_initial_params.html#lumopt2.parametrization.closed_curve.ClosedCurve.get_initial_params)
- [ClosedCurve.make_segments_parametric](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.make_segments_parametric.html#lumopt2.parametrization.closed_curve.ClosedCurve.make_segments_parametric)
- [ClosedCurve.make_vertex_parametric](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.make_vertex_parametric.html#lumopt2.parametrization.closed_curve.ClosedCurve.make_vertex_parametric)
- [ClosedCurve.plot](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.plot.html#lumopt2.parametrization.closed_curve.ClosedCurve.plot)
- [ClosedCurve.set_parametrization_function](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.set_parametrization_function.html#lumopt2.parametrization.closed_curve.ClosedCurve.set_parametrization_function)
- [ClosedCurve.split_segments](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.split_segments.html#lumopt2.parametrization.closed_curve.ClosedCurve.split_segments)
- [ClosedCurve.store_mesh_info](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.store_mesh_info.html#lumopt2.parametrization.closed_curve.ClosedCurve.store_mesh_info)
- [ClosedCurve.update_structure](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.update_structure.html#lumopt2.parametrization.closed_curve.ClosedCurve.update_structure)
- [ClosedCurve.visualize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.visualize.html#lumopt2.parametrization.closed_curve.ClosedCurve.visualize)
- [ClosedCurve.bounds](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.bounds.html#lumopt2.parametrization.closed_curve.ClosedCurve.bounds)

## Ansys-Related External Links Found

- None

## External Links Found

- [float](https://docs.python.org/3/library/functions.html#float)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [int](https://docs.python.org/3/library/functions.html#int)
- [list](https://docs.python.org/3/library/stdtypes.html#list)
