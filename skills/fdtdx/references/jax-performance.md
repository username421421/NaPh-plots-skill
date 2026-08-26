# JAX, Backends, Memory, and Differentiation

## Contents

- [Environment and backend](#environment-and-backend)
- [JIT workflow](#jit-workflow)
- [Memory rules](#memory-rules)
- [Randomness and static shapes](#randomness-and-static-shapes)
- [Sharding and multiple devices](#sharding-and-multiple-devices)
- [Automatic differentiation](#automatic-differentiation)

## Environment and backend

Run `python scripts/fdtdx_doctor.py --project <project>` before expensive work. Confirm that the imported FDTDX is the intended editable/install path and that `jax.devices()` reports the expected backend.

- FDTDX supports Python 3.11 through 3.14.
- Choose `SimulationConfig(backend=...)` consistently with the JAX arrays' devices.
- On Linux, install the JAX accelerator wheel matching the machine/driver. Do not infer CUDA support from `nvidia-smi` alone.
- Native Windows normally uses CPU JAX; use WSL/Linux for official CUDA wheels.
- Tests may force `JAX_PLATFORMS=cpu` before importing JAX to prevent CPU-buffer/CUDA-sharding mismatches.

## JIT workflow

Keep the simulation function pure:

```python
def simulate(params, arrays, objects, config, key):
    transform_key, simulation_key = jax.random.split(key)
    arrays, objects, _ = fdtdx.apply_params(arrays, objects, params, transform_key)
    _, arrays = fdtdx.run_fdtd(arrays, objects, config, simulation_key, show_progress=False)
    return arrays

compiled = jax.jit(simulate).lower(params, arrays, objects, config, key).compile()
result = compiled(params, arrays, objects, config, key)
```

Compile only after placement resolves object slices and the concrete grid. Separate compilation time from repeated execution time. A changed shape, static field, dtype, boundary/Bloch vector, detector structure, or object tree can trigger recompilation.

Use `donate_argnames=["arrays"]` only when the caller will never reuse the donated arrays.

## Memory rules

- Inspect `pytreeclass.tree_summary(arrays)` after placement.
- Field storage scales with grid cells, components, dtype, dispersion states, PML states, detectors, recorders, and checkpoints.
- `EnergyDetector(as_slices=True)` limits video storage; full-volume and frequent detector recording can dominate memory.
- Reversible gradients reduce trajectory storage but may need checkpoints for lossy/dispersive reconstruction accuracy.
- Checkpointed gradients trade recomputation for memory.
- JAX commonly preallocates accelerator memory. Tune `XLA_PYTHON_CLIENT_PREALLOCATE` or allocator settings only when needed and record them.

## Randomness and static shapes

- Split PRNG keys before independent stochastic operations; do not reuse the same key by accident.
- JAX arrays are immutable; use `.at[...]` or TreeClass `.aset(...)` functional updates.
- Array shapes must remain static inside compiled control flow.
- Use JAX control-flow primitives for data-dependent loops/branches.
- Keep file I/O, plotting, logging side effects, and Python mutation outside JIT unless an API explicitly supports callbacks.

## Sharding and multiple devices

Read `doc/tests/unit/core/jax/test_sharding.py` and the sharding source before changing distribution logic.

- The sharded dimension must be divisible by the device count.
- Avoid choosing a singleton dimension; use the library fallback or redesign the layout.
- Buffers, NamedSharding, and selected backend must refer to compatible devices.
- Verify per-device shapes, memory, and numerical parity against one device.
- There is no bundled real multi-GPU end-to-end physics benchmark; measure correctness and scaling on the target machine.

## Automatic differentiation

`GradientConfig` supports:

- `method="reversible"` with a `Recorder`; optional `num_checkpoints_reversible` bounds reconstruction drift.
- `method="checkpointed"` with `num_checkpoints`.

Use the architecture in `doc/examples/optimize_ceviche_corner.py`, then add the gradient checks from `references/convergence-validation.md`. Reversible differentiation through lossy/dispersive simulations deserves direct comparison with checkpointed gradients or finite differences.
