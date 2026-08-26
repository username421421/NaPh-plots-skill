<div id="fdtdx-compute-mode" class="section">

# fdtdx.compute_mode<a href="#fdtdx-compute-mode" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_mode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">frequency</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">resolution=None</span></span>*, *<span class="n"><span class="pre">direction='+'</span></span>*, *<span class="n"><span class="pre">mode_index=0</span></span>*, *<span class="n"><span class="pre">filter_pol=None</span></span>*, *<span class="n"><span class="pre">dtype=\<class</span> <span class="pre">'jax.numpy.float32'\></span></span>*, *<span class="n"><span class="pre">bend_radius=None</span></span>*, *<span class="n"><span class="pre">bend_axis=None</span></span>*, *<span class="n"><span class="pre">symmetry=(0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">transverse_coords=None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/modes.html#compute_mode" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_mode" class="headerlink" title="Link to this definition">#</a>  
Compute optical modes of a waveguide cross-section.

This function uses the Tidy3D mode solver to compute the optical modes of a given waveguide cross-section defined by its permittivity distribution.

By default modes are sorted by their effective index. The mode_index argument indexes this sorted list of modes and returns the desired mode. With filter_pol, it is also possible to only index a specific polarization.

Parameters<span class="colon">:</span>  
- **frequency** (*float*) – Operating frequency in Hz

- **inv_permittivities** (*jax.Array*) – 3D array of inverse relative permittivity values

- **inv_permeabilities** (*jax.Array* *\|* *float*) – 3D array of inverse relative permittivity values or single float for uniform permeability distribution.

- **resolution** (*float* *\|* *None*) – Uniform-grid spacing in metres. Required when <span class="pre">`transverse_coords`</span> is not provided (uniform-grid path). Ignored when <span class="pre">`transverse_coords`</span> is given. Defaults to None.

- **direction** (*Literal\["+",* *"-"\]*) – Propagation direction, either “+” or “-“.

- **mode_index** (*int,* *optional*) – Index of the mode to compute. Defaults to 0.

- **filter_pol** (*Literal\["te",* *"tm"\]* *\|* *None,* *optional*)

- **dtype** (*jnp.dtype,* *optional*) – Float dtype of the simulation. Controls whether mode fields are returned as complex64 (float32) or complex128 (float64). Defaults to jnp.float32.

- **bend_radius** (*float* *\|* *None,* *optional*) – Bend radius of the waveguide in meters. Must be set together with bend_axis. When set, the mode solver uses a conformal transformation to account for the bend. Defaults to None (straight waveguide).

- **bend_axis** (*int* *\|* *None,* *optional*) – Physical axis index (0/1/2) pointing from the waveguide toward the center of curvature. Must differ from the propagation axis. Required when bend_radius is set. Defaults to None.

- **symmetry** (*tuple\[int,* *int\],* *optional*) – Symmetry-plane condition at the *min* edge of each transverse axis, in the order of the two non-propagation physical axes (increasing index). <span class="pre">`0`</span> imposes a PEC mirror (electric wall — the tidy3d default), <span class="pre">`1`</span> imposes a PMC mirror (magnetic wall). Use this when the waveguide sits on a symmetry plane of a reduced (half/quarter) domain so the mode solver reproduces the same boundary the FDTD uses there. For a +x-propagating TE mode on a y/z quarter domain with PEC at y=0 and PMC at the z Si-mid plane, pass <span class="pre">`(0,`</span>` `<span class="pre">`1)`</span>. Defaults to <span class="pre">`(0,`</span>` `<span class="pre">`0)`</span> (PEC on both, i.e. no symmetry).

- **transverse_coords** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Optional`</span>\[<span class="pre">`Sequence`</span>\[<span class="pre">`Array`</span>\]\]</span>) – Optional pair of physical edge-coordinate arrays, in metres, for the two axes transverse to propagation. Each array must have one more entry than the corresponding transverse cell count. When provided, the Tidy3D mode solver receives the non-uniform rectilinear grid directly. JAX arrays are accepted; the numpy conversion happens inside the tidy3d callback so the function remains compatible with <span class="pre">`jax.jit`</span>.

Returns<span class="colon">:</span>  
Tuple of E, H field and the effective index as complex-valued jax arrays.

Return type<span class="colon">:</span>  
Tuple\[jax.Array, jax.Array, jax.Array\]

</div>
