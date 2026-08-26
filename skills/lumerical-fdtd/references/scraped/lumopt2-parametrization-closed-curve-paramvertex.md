# ParamVertex [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#paramvertex)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `ParamVertex [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#paramvertex)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 10 link(s), 0 code block(s), 9 inline code term(s), and 1 table(s). Main headings: ParamVertex [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#paramvertex). Key detected terms: lumopt, mode, port.

## Key Terms

- lumopt
- mode
- port

## Captured Headings

- ParamVertex [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#paramvertex)

## Official Text Excerpt

> ParamVertex # class lumopt2.parametrization.closed_curve. ParamVertex (idx: int, movement: str = 'manual', value: float = None, delta_x: float = None, delta_y: float = None) # Specification for a parametric vertex adjustment. Supports two modes of operation: 1. Manual mode (default): Specify delta_x and/or delta_y directly 2. Directional mode: Specify movement direction and value Attributes: idx``int 1-based index of the vertex to parametrize. movement``str,`optional` Movement direction mode. Options: - ‘manual’ (default): Use delta_x and delta_y directly - ‘normal’: Move along outward normal direction by value - ‘tangent’: Move along tangent direction by value - ‘x-axis’: Move along x-axis by value - ‘y-axis’: Move along y-axis by value value``float,`optional` Movement amount (used when movement != ‘manual’). Positive values move outward for ‘normal’, forward for ‘tangent’. delta_x``float,`optional` Manual adjustment in x direction (used when movement == ‘manual’). delta_y``float,`optional` Manual adjustment in y direction (used when movement == ‘manual’). Examples Manual mode: >>> ParamVertex(idx=2, delta_x=100e-9, delta_y=50e-9) Normal direction: >>> ParamVertex(idx=2, movement=’normal’, value=params[0]) X-axis only: >>> ParamVertex(idx=3, movement=’x-axis’, value=params[1]) Attributes | ``ParamVertex.delta_x | | ``ParamVertex.delta_y | | ``ParamVertex.movement | | ``ParamVertex.value | | ``ParamVertex.idx |

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `ParamVertex.delta_x`
- `ParamVertex.delta_y`
- `ParamVertex.idx`
- `ParamVertex.movement`
- `ParamVertex.value`
- `float`
- `int`
- `optional`
- `str`

## Table Inventory

- Table 1: 2 column(s), 5 row(s)
  - First row sample: ParamVertex.delta_x | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#paramvertex)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#lumopt2.parametrization.closed_curve.ParamVertex)
- [ParamVertex.delta_x](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.delta_x.html#lumopt2.parametrization.closed_curve.ParamVertex.delta_x)
- [ParamVertex.delta_y](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.delta_y.html#lumopt2.parametrization.closed_curve.ParamVertex.delta_y)
- [ParamVertex.movement](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.movement.html#lumopt2.parametrization.closed_curve.ParamVertex.movement)
- [ParamVertex.value](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.value.html#lumopt2.parametrization.closed_curve.ParamVertex.value)
- [ParamVertex.idx](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.idx.html#lumopt2.parametrization.closed_curve.ParamVertex.idx)

## Ansys-Related External Links Found

- None

## External Links Found

- [int](https://docs.python.org/3/library/functions.html#int)
- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [float](https://docs.python.org/3/library/functions.html#float)
