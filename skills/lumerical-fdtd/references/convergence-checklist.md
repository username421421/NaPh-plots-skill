# Convergence And Review Checklist

Use this file before trusting or reporting an FDTD result. Primary official source: [Convergence testing process for FDTD simulations](https://optics.ansys.com/hc/en-us/articles/360034915833-Convergence-testing-process-for-FDTD-simulations), with supporting guidance from solver, mesh, PML, source, and monitor documentation.

## Scope and execution

This checklist governs acceptance of scientific results. It does not require
rerunning validated campaigns for documentation or logging changes and does not
authorize compute. Reuse evidence only when it applies to the current geometry,
materials, source, grid, monitors, and metric. Identify missing evidence and
obtain the workspace's required run confirmation before new solves or exports.
Set a budget and termination ceiling for proposed sweeps; reaching a limit is
not convergence. Report which checks were performed, reused, or remain pending.

## Convergence Workflow

1. Define the reported metric before tuning the simulation: transmission at target wavelength, resonance wavelength/Q, Purcell factor, directivity, S-parameter, color coordinate, etc.
2. Establish a baseline project that runs and exports the metric reproducibly.
3. Sweep one numerical control at a time: mesh accuracy, local mesh override, PML distance, PML layers/profile, simulation time/auto shutoff, source placement, monitor placement, material fit.
4. Record metric change, runtime, and memory.
5. Choose the cheapest settings whose metric is stable within tolerance.
6. Re-run final settings from a clean project builder, not from hand-edited GUI state.

## Solver And Boundary Checks

- Does every object have a descriptive name?
- Are all positions, spans, wavelengths, and times in SI units?
- Is the Lumerical version/API path explicit and current for this workspace?
- Is the FDTD region large enough that PML does not perturb near fields?
- Are PML profile/layers appropriate for grazing incidence or structures through PML?
- Are periodic/Bloch boundaries used only where geometry and fields justify them?
- If symmetry is used, has a full-domain or less-symmetric comparison been run?

## Mesh Checks

- Is global mesh accuracy low enough for iteration and high enough for the final claim?
- Are mesh overrides limited to critical regions?
- Are thin layers and high-index gaps represented by enough cells?
- Are conformal/staircase/precise-volume choices justified?
- Are reference and perturbed simulations using consistent mesh where differences are compared?
- Is mesh order explicit for overlapping geometry?

## Source Checks

- Are global source limits set once and overridden only intentionally?
- Is the source far enough from scatterers/PML to inject the intended field?
- For angled injection, are Bloch/BFAST/periodic assumptions valid over the band?
- For mode sources, is the mode cross section large enough and the selected mode logged?
- For dipoles, does source orientation match symmetry and reported quantity?
- For TFSF, is the scattering object fully inside the total-field region and away from source boundaries?

## Monitor Checks

- Are monitors recording only needed dimensions, components, and frequency points?
- Are reflection/transmission monitors placed away from source artifacts and near-field contamination?
- Is normalization physically meaningful for the source type?
- Are time monitors used for high-Q or long-decay structures?
- Are far-field projection monitors enclosing the needed radiation in a homogeneous region?
- Are result keys inspected before assuming dataset structure?

## Automation Checks

- Does the script start from `newproject()` and `deleteall()` or a known template?
- Are material fallbacks explicit?
- Are saved `.fsp` paths deterministic?
- Are result exports reproducible without GUI clicks?
- Are failed runs logged with enough metadata to debug?
- Is there a short script or notebook that regenerates the reported plot/table from raw monitor data?
