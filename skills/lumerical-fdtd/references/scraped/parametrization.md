# Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization)

Source URL: https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html  
Area: Discovered official source  
Topic: Discovered from Introduction to photonic inverse design with lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization)` for the topic `Discovered from Introduction to photonic inverse design with lumopt2`. It captured 12 heading(s), 26 link(s), 12 code block(s), 17 inline code term(s), and 0 table(s). Main headings: Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization), Optimization region [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#optimization-region), Parametric optimization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametric-optimization), Parametrization class [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization-class), Defining parameter mapping [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#defining-parameter-mapping), Bounds and initial values [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#bounds-and-initial-values), Functions not differentiable by autograd [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#functions-not-differentiable-by-autograd), Closed curve class [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#closed-curve-class). Key detected terms: command, fdtd, geometry, group, lumopt, mesh, optimization, plane, port, python, script, structure, symmetry.

## Key Terms

- command
- fdtd
- geometry
- group
- lumopt
- mesh
- optimization
- plane
- port
- python
- script
- structure
- symmetry

## Captured Headings

- Parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization)
- Optimization region [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#optimization-region)
- Parametric optimization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametric-optimization)
- Parametrization class [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization-class)
- Defining parameter mapping [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#defining-parameter-mapping)
- Bounds and initial values [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#bounds-and-initial-values)
- Functions not differentiable by autograd [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#functions-not-differentiable-by-autograd)
- Closed curve class [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#closed-curve-class)
- Closed curve base object [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#closed-curve-base-object)
- Parametrize closed curves [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrize-closed-curves)
- Symmetric parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#symmetric-parametrization)
- Combined parametrization [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#combined-parametrization)

## Official Text Excerpt

> Parametrization # Parametrization is the process of linking properties and geometry of the simulation to the optimization. The lumopt2 module supports parametric optimization in two ways: - Parametrization object: maps optimization parameters to arbitrary Lumerical object properties. - Closed curve object: maps optimization parameters to a special class that defines a closed polygon. Regardless of the parametrization type, you must first define the optimization region. Within this region, the parameters are adjusted. Optimization region # The optimization region defines the bounds within which the geometry of the simulations is varied during optimization. You must ensure that all permutations of the geometry variation stays within the optimization region you define. To define an optimization region, use the``Box class, which takes either the center and span, or min and max values in each dimension. In the definition, you can additionally specify the grid resolution in each dimension using the`dx, dy, dz`arguments. If you do not specify the grid resolution, the optimization region is set up with a default resolution determined by the mesh override simulation object. Parametric optimization # You can conduct ...

## Code Block Inventory

- Code block 1: 4 line(s); first line `1# Define an optimization region centered at the origin with a span of 1 micron in each`
- Code block 2: 7 line(s); first line `1def my_parametrization(params):`
- Code block 3: 7 line(s); first line `1def my_parametrization(params):`
- Code block 4: 7 line(s); first line `1def polygon_parametrization(params):`
- Code block 5: 5 line(s); first line `1parametrization = lmpt.Parametrization(`
- Code block 6: 14 line(s); first line `1def nondiff_func_parametrization(params):`
- Code block 7: 18 line(s); first line `1bend_radius     = 1.0e-6`
- Code block 8: 4 line(s); first line `1n_wg = 3.5 # Silicon waveguide`
- Code block 9: 1 line(s); first line `1closed_curve.plot()`
- Code block 10: 5 line(s); first line `1num_pts_per_curve = 2`
- Code block 11: 1 line(s); first line `1closed_curve.plot()`
- Code block 12: 31 line(s); first line `1num_pts_per_curve = 2                                  # Control vertices per curved segment`

## Inline Code Inventory

- `Box`
- `ClosedCurve`
- `ClosedCurve.make_segments_parametric()`
- `ClosedCurve.plot()`
- `ClosedCurve.set_parametrization_function()`
- `CombinedParametrization`
- `Parametrization`
- `Parametrize`
- `Segment`
- `dx, dy, dz`
- `fdtd.getnamed("my_object_name")`
- `group_name::object_name::property_name`
- `lumopt2.parametrization.closed_curve.EqualSplit`
- `lumopt2.parametrization.closed_curve.ParamVertex`
- `movement`
- `object_name::property_name`
- `use_jac`

## Table Inventory

- No tables detected

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#optimization-region)
- [Box](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.common.Box.html#lumopt2.utils.common.Box)
- [mesh override simulation object](https://optics.ansys.com/hc/en-us/articles/360034901833-Mesh-override-Simulation-Object)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametric-optimization)
- [Parametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.parametrization.Parametrization.html#lumopt2.parametrization.parametrization.Parametrization)
- [ClosedCurve](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrization-class)
- [3x3 pillar example in the getting started section](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/getting_started_simple_metalens.html)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#defining-parameter-mapping)
- [getnamed](https://optics.ansys.com/hc/en-us/articles/360034408574-getnamed-Script-command)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#bounds-and-initial-values)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#functions-not-differentiable-by-autograd)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#closed-curve-class)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#closed-curve-base-object)
- [Segment](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Segment.html#lumopt2.parametrization.closed_curve.Segment)
- [ClosedCurve.plot()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#parametrize-closed-curves)
- [Parametrize](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.Parametrize.html#lumopt2.parametrization.closed_curve.Parametrize)
- [ClosedCurve.make_segments_parametric()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#symmetric-parametrization)
- [ClosedCurve.set_parametrization_function()](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ClosedCurve.html#lumopt2.parametrization.closed_curve.ClosedCurve)
- [lumopt2.parametrization.closed_curve.EqualSplit](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.EqualSplit.html#lumopt2.parametrization.closed_curve.EqualSplit)
- [lumopt2.parametrization.closed_curve.ParamVertex](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.closed_curve.ParamVertex.html#lumopt2.parametrization.closed_curve.ParamVertex)
- [#](https://lumerical.docs.pyansys.com/version/stable/user_guide/lumopt2/parametrization.html#combined-parametrization)
- [CombinedParametrization](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.parametrization.combined_parametrization.CombinedParametrization.html#lumopt2.parametrization.combined_parametrization.CombinedParametrization)

## Ansys-Related External Links Found

- None

## External Links Found

- None
