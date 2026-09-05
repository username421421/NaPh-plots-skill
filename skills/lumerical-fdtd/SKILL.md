---
name: lumerical-fdtd
description: Build, review, and debug Ansys Lumerical FDTD simulations and lumapi/PyLumerical automation, including solver physics, exact properties, and result extraction.
---

# Lumerical FDTD

Preserve the campaign's Lumerical release, interpreter, API path/style, and material
choices. Use local official-documentation captures first; verify against the selected
runtime or matching official sources if evidence is missing, incompatible, or live
verification is requested. Captures are snapshots, not proof of runtime support.
Do not open extra application sessions when metadata/source suffices.

## Resolve the affected API directly

Paths are relative to this skill. Choose one relevant reference/section below,
then search its linked captured page for exact arguments, property names, object
types, and result keys. Broaden only when unresolved; do not load every index.

```text
rg -n -m 8 "<command-or-property>" references/<selected-reference>.md
```

Use matches to locate the complete relevant section. Do not infer an API contract
from a truncated snippet. Reuse a compatible campaign or official example rather
than redesigning an existing workflow.

| Need | Reference |
| --- | --- |
| Bundled `lumapi`: sessions, script methods, data/results | `references/python-api.md` |
| `ansys.lumerical.core`: constructors/handles, autodiscovery, `serverArgs`, `lumopt2` | Relevant heading of `references/pylumerical.md`; shared API only if needed |
| Domain, materials, time/shutoff, global spectrum | `references/fdtd-setup.md` |
| Mesh/conformal/overlap order | `references/mesh.md` |
| PML, Bloch/periodic, symmetry/parity/unfolding | `references/boundaries-symmetry.md` |
| Plane/beam, mode, dipole, TFSF, ports | `references/sources.md` |
| DFT/time/mode monitors, normalization, far field, result axes | `references/monitors-results.md` |
| New builder or object-property audit | Relevant rows in `references/api-audit.md` |
| Closest official example/command | `references/examples-and-commands.md` |
| Scientific acceptance | `references/convergence-checklist.md` |

If direct routing fails, search `references/keyword-index.md` or
`references/corpus-index.md`; use `references/link-graph.md` for related pages.
Captured pages live under `references/scraped/`.

## Implement and verify

For changed physics/APIs/results, identify a compatible example, audit affected
commands/properties, then briefly record chosen approach, reference, assumptions,
and convergence risks before coding. Full builders use the detailed audit;
local documentation/path/logging edits reuse unchanged evidence.

Use exact property names including spaces. Use `OrderedDict` when object type or
mode must precede dependent properties. Verify dataset keys/axes and normalization;
do not guess result structure. Preserve source, monitor, boundary, mesh, resource,
output, and overwrite settings unless their changes are authorized.

Follow the workspace execution contract before solves, sweeps, optimization,
exports, or expensive extraction. Scientific acceptance needs applicable convergence
evidence, not automatic extra runs. Report performed/reused/pending checks and
uncertainty; use the smallest relevant verification for the change.

`scripts/scrape_lumerical_docs.py` refreshes the corpus only when needed; it is not
a normal package-usage step.
