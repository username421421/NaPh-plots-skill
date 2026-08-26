# ClosedCurveCubicSegment [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#closedcurvecubicsegment)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ClosedCurveCubicSegment [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#closedcurvecubicsegment)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 10 link(s), 0 code block(s), 8 inline code term(s), and 1 table(s). Main headings: ClosedCurveCubicSegment [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#closedcurvecubicsegment). Key detected terms: lumopt, optimization.

## Key Terms

- lumopt
- optimization

## Captured Headings

- ClosedCurveCubicSegment [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#closedcurvecubicsegment)

## Official Text Excerpt

> ClosedCurveCubicSegment # class lumopt2.parametrization.closed_curve. ClosedCurveCubicSegment (start_vertex_idx: int, end_vertex_idx: int, fixed_start_tangent: ndarray|None = None, fixed_end_tangent: ndarray|None = None, n_vertices_lumerical_polygon: int = 50) # A cubic Bezier curve segment. Parameters: start_vertex_idx``int Index of the starting vertex (1-based). end_vertex_idx``int Index of the ending vertex (1-based). fixed_start_tangent`Optional```[np.ndarray],`optional` Fixed tangent vector at start vertex (default: None). fixed_end_tangent`Optional```[np.ndarray],`optional` Fixed tangent vector at end vertex (default: None). n_vertices_lumerical_polygon``int,`optional` Number of discrete points (default: 50). Methods | ``ClosedCurveCubicSegment.evaluate (vertices, ...) | Evaluate cubic Bezier curve (possibly subdivided with control points). | ``ClosedCurveCubicSegment.get_control_points (...) | Get the intermediate control point positions for visualization. | ``ClosedCurveCubicSegment.get_num_params () | Get number of optimization parameters for this segment. | ``ClosedCurveCubicSegment.set_parametric (...) | Make this segment parametric for optimization.

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `ClosedCurveCubicSegment.evaluate`
- `ClosedCurveCubicSegment.get_control_points`
- `ClosedCurveCubicSegment.get_num_params`
- `ClosedCurveCubicSegment.set_parametric`
- `Optional`
- `int`
- `np.ndarray`
- `optional`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - First row sample: ClosedCurveCubicSegment.evaluate (vertices, ...) | Evaluate cubic Bezier curve (possibly subdivided with control points).

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#closedcurvecubicsegment)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment)
- [ClosedCurveCubicSegment.evaluate](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.evaluate.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.evaluate)
- [ClosedCurveCubicSegment.get_control_points](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.get_control_points.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.get_control_points)
- [ClosedCurveCubicSegment.get_num_params](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.get_num_params.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.get_num_params)
- [ClosedCurveCubicSegment.set_parametric](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.set_parametric.html#lumopt2.parametrization.closed_curve.ClosedCurveCubicSegment.set_parametric)

## Ansys-Related External Links Found

- None

## External Links Found

- [int](https://docs.python.org/3/library/functions.html#int)
- [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
- [None](https://docs.python.org/3/library/constants.html#None)
- [np.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)
