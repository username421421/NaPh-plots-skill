# Mesh Strategy

Use this file for mesh accuracy, mesh overrides, mesh refinement modes, mesh order, and convergence. Primary official sources: [Mesh override - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034901833-Mesh-override-Simulation-Object), [Understanding Mesh Refinement and Conformal Mesh in FDTD](https://optics.ansys.com/hc/en-us/articles/360034382594-Understanding-Mesh-Refinement-and-Conformal-Mesh-in-FDTD), [Selecting the best mesh refinement option](https://optics.ansys.com/hc/en-us/articles/360034382614-Selecting-the-best-mesh-refinement-option-in-the-FDTD-simulation-object), [Getting the mesh size](https://optics.ansys.com/hc/en-us/articles/360034382574-Getting-the-mesh-size), [Using the non-uniform mesh](https://optics.ansys.com/hc/en-us/articles/360034382634-Using-the-non-uniform-mesh), and [Mesh Order](https://optics.ansys.com/hc/en-us/articles/360034915233-Mesh-Order).

## Default Workflow

1. Start with automatic meshing and moderate `mesh accuracy` for topology, object placement, and workflow debugging.
2. Add mesh overrides only around small gaps, high-index boundaries, thin layers, resonant hot spots, and monitors whose interpolation error matters.
3. Run convergence on the reported metric, not on field plots alone.
4. Increase mesh accuracy and/or decrease override step size until the metric change is below the required tolerance.
5. Keep final mesh choices documented in the script.

Source: [Convergence testing process](https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing-process-for-FDTD-simulations).

## Automatic Mesh Accuracy

`mesh accuracy` controls the automatic non-uniform mesh. Higher values improve resolution and cost more memory/time. Do not choose the final value by habit. Use:

- `mesh accuracy` 1-2 for fast geometry/API iteration.
- `mesh accuracy` 2-3 for initial physical sweeps.
- Higher accuracy or local overrides for final results after convergence testing.

## Mesh Overrides

Use `addmesh` for local resolution control. Keep overrides as small as possible and align spans to the geometry they protect.

```python
fdtd.addmesh(properties=OrderedDict([
    ("name", "mesh_gap_10nm"),
    ("x", 0.0),
    ("x span", 500 * NM),
    ("y", 0.0),
    ("y span", 500 * NM),
    ("z", 110 * NM),
    ("z span", 260 * NM),
    ("override x mesh", 1),
    ("override y mesh", 1),
    ("override z mesh", 1),
    ("dx", 10 * NM),
    ("dy", 10 * NM),
    ("dz", 5 * NM),
]))
```

Use anisotropic spacing when physics is anisotropic: thin films often need small `dz` more than small `dx/dy`; narrow waveguide gaps may need small transverse spacing but not along the propagation axis.

Mesh override regions can use equivalent index or structure-based behavior in the GUI/object settings. Treat those options as part of the physical model and include them in convergence notes. Source: [Mesh override - Simulation Object](https://optics.ansys.com/hc/en-us/articles/360034901833-Mesh-override-Simulation-Object).

## Conformal And Refinement Modes

Conformal mesh reduces staircasing error at material interfaces compared with a pure staircase approximation. It is especially important for curved interfaces, slanted sidewalls, and high-index contrast where the interface location strongly changes the field. Source: [Understanding Mesh Refinement and Conformal Mesh in FDTD](https://optics.ansys.com/hc/en-us/articles/360034382594-Understanding-Mesh-Refinement-and-Conformal-Mesh-in-FDTD).

Use the mesh refinement option that matches the problem:

- Conformal variants: usually preferred for dielectric interfaces and curved geometry.
- Staircase: useful for debugging, compatibility checks, or cases where conformal behavior is not desired.
- Precise volume average or inverse-design-friendly options: consider for adjoint/inverse-design workflows where material interpolation and gradients matter.

Source: [Selecting the best mesh refinement option](https://optics.ansys.com/hc/en-us/articles/360034382614-Selecting-the-best-mesh-refinement-option-in-the-FDTD-simulation-object).

## Getting The Mesh Size

For debugging, query or visualize mesh size before running expensive sweeps. The official "Getting the mesh size" guidance is useful when you need to confirm the actual discretization produced by automatic meshing and overrides. Source: [Getting the mesh size](https://optics.ansys.com/hc/en-us/articles/360034382574-Getting-the-mesh-size).

In automation, prefer logging the intended mesh settings plus a screenshot or exported mesh diagnostic for critical final runs. If using script commands to query mesh arrays, keep the query code next to the convergence script.

## Mesh Order

When geometry overlaps, mesh order determines which material wins in overlapping cells. Use explicit mesh order for imported data, thin metal layers, or objects that intentionally overlap with substrate/cladding. Source: [Mesh Order](https://optics.ansys.com/hc/en-us/articles/360034915233-Mesh-Order).

## Cost Controls

- Avoid global high mesh accuracy when a local override would resolve the critical feature.
- Disable unnecessary field components and monitor sampling while doing mesh sweeps.
- Keep override spans stable between reference and device simulations.
- Record memory/runtime when changing mesh so speedups are not confused with physical convergence.

## Mesh Convergence Checklist

- Does the final metric change acceptably when `mesh accuracy` is increased?
- Does the metric change acceptably when each local override is refined?
- Are thin layers represented by multiple cells in the sensitive dimension?
- Are high-index boundaries resolved in the dimensions that dominate field gradients?
- Are mesh overrides outside PML unless intentionally testing PML interaction?
- Are reference and perturbed simulations using consistent mesh where a difference is being measured?
