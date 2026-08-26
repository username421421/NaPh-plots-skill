# Boundaries And Symmetry

Use this file for PML, periodic, Bloch, symmetric, and anti-symmetric boundary conditions. Primary official sources: [PML boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382674-PML-boundary-conditions-in-FDTD-and-MODE), [Periodic boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382734-Periodic-boundary-conditions-in-FDTD-and-MODE), [Bloch boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382714-Bloch-boundary-conditions-in-FDTD-and-MODE), and [Symmetric and anti-symmetric BCs](https://optics.ansys.com/hc/en-us/articles/360034382694-Symmetric-and-anti-symmetric-BCs-in-FDTD-and-MODE).

## PML

Use PML for open radiation boundaries. Keep it far enough from scattering objects, resonant near fields, and evanescent tails that absorption does not perturb the result. Source: [PML boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382674-PML-boundary-conditions-in-FDTD-and-MODE).

PML profile choice:

- Standard/default: normal open-boundary use.
- Steep angle: use for strong grazing-angle content, periodic angled incidence, or plane waves near tangential propagation.
- Stabilized: use when dispersive/material structures extend into PML or when simulations diverge due to PML interaction.

Increase PML layers when reflections contaminate the metric or when steep-angle/stabilized profiles need more thickness. Validate by moving PML farther away and increasing layers until the metric stabilizes.

## Periodic Boundaries

Use periodic boundaries when the geometry and electromagnetic fields repeat with no phase shift across the boundary. The simulation span should equal the unit-cell pitch along that axis. Do not use periodic boundaries on an axis where fields are not physically periodic. Source: [Periodic boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382734-Periodic-boundary-conditions-in-FDTD-and-MODE).

Common periodic setup:

```python
fdtd.setnamed("FDTD", "x min bc", "Periodic")
fdtd.setnamed("FDTD", "x max bc", "Periodic")
fdtd.setnamed("FDTD", "y min bc", "Periodic")
fdtd.setnamed("FDTD", "y max bc", "Periodic")
fdtd.setnamed("FDTD", "z min bc", "PML")
fdtd.setnamed("FDTD", "z max bc", "PML")
```

## Bloch Boundaries

Use Bloch boundaries when the structure is periodic but the fields have a phase shift across the unit cell, such as angled incidence in a periodic array. Bloch fields are generally complex. Source: [Bloch boundary conditions](https://optics.ansys.com/hc/en-us/articles/360034382714-Bloch-boundary-conditions-in-FDTD-and-MODE).

For broadband angled injection, check whether the angle is frequency dependent and whether BFAST or other official angled-source methods are needed. Source: [Understanding injection angles in broadband simulations](https://optics.ansys.com/hc/en-us/articles/360034382894-Understanding-injection-angles-in-broadband-simulations).

## Symmetry And Anti-Symmetry

Use symmetric or anti-symmetric boundaries only when both the geometry and the excited field parity match. Official guidance emphasizes validating symmetry setups against a full-domain or less-symmetric simulation before trusting production results. Source: [Symmetric and anti-symmetric BCs](https://optics.ansys.com/hc/en-us/articles/360034382694-Symmetric-and-anti-symmetric-BCs-in-FDTD-and-MODE).

Practical rule:

- Symmetric boundary means tangential electric-field parity is even for the retained half-space.
- Anti-symmetric boundary means tangential electric-field parity is odd for the retained half-space.
- Source polarization and source position determine whether a symmetry plane is valid.
- If a source is off the symmetry plane or has mixed polarization/parity, do not use that symmetry.

Local helper pattern:

```python
def apply_xy_symmetry(fdtd, *, x_sym=None, y_sym=None):
    if x_sym is not None:
        fdtd.setnamed("FDTD", "x min bc", x_sym)
        fdtd.setnamed("FDTD", "x max bc", "PML")
    if y_sym is not None:
        fdtd.setnamed("FDTD", "y min bc", y_sym)
        fdtd.setnamed("FDTD", "y max bc", "PML")
```

Use explicit strings from Lumerical, usually `"Symmetric"` and `"Anti-Symmetric"`.

## Monitor Behavior With Symmetry

Symmetry can reduce simulated volume, but monitor interpretation still needs the physical full-domain meaning:

- Power integrals may need symmetry factors depending on monitor placement and quantity.
- Far-field or directivity analysis should be checked carefully because the simulated monitor surface may represent only part of the physical surface.
- Field plots on the simulated domain do not automatically prove full-domain parity is correct.

For important metrics, run a comparison:

1. Full domain or one less symmetry plane.
2. Same mesh strategy and source/monitor definitions.
3. Same reported metric and normalization.
4. Difference below the required tolerance before using symmetry for sweeps.

## Boundary Selection Table

| Physical situation | Boundary choice |
| --- | --- |
| Isolated scatterer or finite device in open space | PML on open axes |
| Infinite periodic normal-incidence unit cell | Periodic on periodic axes, PML on propagation axis |
| Periodic angled incidence | Bloch or official angled-injection method, PML on propagation axis |
| Mirror-symmetric geometry and source parity | Symmetric or anti-symmetric on valid symmetry plane |
| Waveguide crossing simulation edge | Use ports/mode source/monitors or extend domain; do not rely on arbitrary PML placement without convergence |
