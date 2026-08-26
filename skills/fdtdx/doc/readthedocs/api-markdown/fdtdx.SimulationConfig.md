<div id="fdtdx-simulationconfig" class="section">

# fdtdx.SimulationConfig<a href="#fdtdx-simulationconfig" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">SimulationConfig</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">time=null</span></span>*, *<span class="n"><span class="pre">grid=null</span></span>*, *<span class="n"><span class="pre">backend='gpu'</span></span>*, *<span class="n"><span class="pre">dtype=\<class</span> <span class="pre">'jax.numpy.float32'\></span></span>*, *<span class="n"><span class="pre">use_complex_fields=None</span></span>*, *<span class="n"><span class="pre">courant_factor=0.99</span></span>*, *<span class="n"><span class="pre">symmetry=(0</span></span>*, *<span class="n"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">gradient_config=None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/config.html#SimulationConfig" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SimulationConfig" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Configuration settings for FDTD simulations.

This class contains all the parameters needed to configure and run an FDTD simulation, including spatial and temporal discretization, hardware backend, and gradient computation settings.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.SimulationConfig.backend" class="reference internal" title="fdtdx.SimulationConfig.backend"><span class="pre"><code class="sourceCode python">backend</code></span></a>

- <a href="#fdtdx.SimulationConfig.courant_factor" class="reference internal" title="fdtdx.SimulationConfig.courant_factor"><span class="pre"><code class="sourceCode python">courant_factor</code></span></a>

- <a href="#fdtdx.SimulationConfig.courant_number" class="reference internal" title="fdtdx.SimulationConfig.courant_number"><span class="pre"><code class="sourceCode python">courant_number</code></span></a>

- <a href="#fdtdx.SimulationConfig.dtype" class="reference internal" title="fdtdx.SimulationConfig.dtype"><span class="pre"><code class="sourceCode python">dtype</code></span></a>

- <a href="#fdtdx.SimulationConfig.gradient_config" class="reference internal" title="fdtdx.SimulationConfig.gradient_config"><span class="pre"><code class="sourceCode python">gradient_config</code></span></a>

- <a href="#fdtdx.SimulationConfig.grid" class="reference internal" title="fdtdx.SimulationConfig.grid"><span class="pre"><code class="sourceCode python">grid</code></span></a>

- <a href="#fdtdx.SimulationConfig.has_nonuniform_grid" class="reference internal" title="fdtdx.SimulationConfig.has_nonuniform_grid"><span class="pre"><code class="sourceCode python">has_nonuniform_grid</code></span></a>

- <a href="#fdtdx.SimulationConfig.has_symmetry" class="reference internal" title="fdtdx.SimulationConfig.has_symmetry"><span class="pre"><code class="sourceCode python">has_symmetry</code></span></a>

- <a href="#fdtdx.SimulationConfig.invertible_optimization" class="reference internal" title="fdtdx.SimulationConfig.invertible_optimization"><span class="pre"><code class="sourceCode python">invertible_optimization</code></span></a>

- <a href="#fdtdx.SimulationConfig.max_travel_distance" class="reference internal" title="fdtdx.SimulationConfig.max_travel_distance"><span class="pre"><code class="sourceCode python">max_travel_distance</code></span></a>

- <a href="#fdtdx.SimulationConfig.only_forward" class="reference internal" title="fdtdx.SimulationConfig.only_forward"><span class="pre"><code class="sourceCode python">only_forward</code></span></a>

- <a href="#fdtdx.SimulationConfig.resolved_grid" class="reference internal" title="fdtdx.SimulationConfig.resolved_grid"><span class="pre"><code class="sourceCode python">resolved_grid</code></span></a>

- <a href="#fdtdx.SimulationConfig.symmetry" class="reference internal" title="fdtdx.SimulationConfig.symmetry"><span class="pre"><code class="sourceCode python">symmetry</code></span></a>

- <a href="#fdtdx.SimulationConfig.time" class="reference internal" title="fdtdx.SimulationConfig.time"><span class="pre"><code class="sourceCode python">time</code></span></a>

- <a href="#fdtdx.SimulationConfig.time_step_duration" class="reference internal" title="fdtdx.SimulationConfig.time_step_duration"><span class="pre"><code class="sourceCode python">time_step_duration</code></span></a>

- <a href="#fdtdx.SimulationConfig.time_steps_total" class="reference internal" title="fdtdx.SimulationConfig.time_steps_total"><span class="pre"><code class="sourceCode python">time_steps_total</code></span></a>

- <a href="#fdtdx.SimulationConfig.use_complex_fields" class="reference internal" title="fdtdx.SimulationConfig.use_complex_fields"><span class="pre"><code class="sourceCode python">use_complex_fields</code></span></a>

Methods

- <a href="#fdtdx.SimulationConfig.aset" class="reference internal" title="fdtdx.SimulationConfig.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.SimulationConfig.get_class_fields" class="reference internal" title="fdtdx.SimulationConfig.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.SimulationConfig.get_public_fields" class="reference internal" title="fdtdx.SimulationConfig.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.SimulationConfig.resolve_grid" class="reference internal" title="fdtdx.SimulationConfig.resolve_grid"><span class="pre"><code class="sourceCode python">resolve_grid</code></span></a>

- <a href="#fdtdx.SimulationConfig.uniform_spacing" class="reference internal" title="fdtdx.SimulationConfig.uniform_spacing"><span class="pre"><code class="sourceCode python">uniform_spacing</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">backend</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'gpu'`</span><span class="pre">,</span> <span class="pre">`'tpu'`</span><span class="pre">,</span> <span class="pre">`'cpu'`</span><span class="pre">,</span> <span class="pre">`'METAL'`</span><span class="pre">\]</span>*<a href="#fdtdx.SimulationConfig.backend" class="headerlink" title="Link to this definition">#</a>  
Computation backend (‘gpu’, ‘tpu’, ‘cpu’ or ‘METAL’). Defaults to “gpu”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">courant_factor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.SimulationConfig.courant_factor" class="headerlink" title="Link to this definition">#</a>  
0.99).

Type<span class="colon">:</span>  
Safety factor for the Courant condition (default

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">courant_number</span></span><a href="#fdtdx.SimulationConfig.courant_number" class="headerlink" title="Link to this definition">#</a>  
Calculate the Courant number for the simulation.

The Courant number is a dimensionless quantity that determines stability of the FDTD simulation. It represents the ratio of the physical propagation speed to the numerical propagation speed.

Returns<span class="colon">:</span>  
The Courant number, scaled by the courant_factor and normalized  
for 3D simulations.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">dtype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dtype`</span>*<a href="#fdtdx.SimulationConfig.dtype" class="headerlink" title="Link to this definition">#</a>  
Data type for numerical computations. Defaults to jnp.float32.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">gradient_config</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.GradientConfig.html#fdtdx.GradientConfig" class="reference internal" title="fdtdx.config.GradientConfig"><span class="pre"><code class="sourceCode python">GradientConfig</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.SimulationConfig.gradient_config" class="headerlink" title="Link to this definition">#</a>  
Optional configuration for gradient computation.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">grid</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.UniformGrid.html#fdtdx.UniformGrid" class="reference internal" title="fdtdx.core.grid.UniformGrid"><span class="pre"><code class="sourceCode python">UniformGrid</code></span></a> <span class="pre">\|</span> <a href="fdtdx.QuasiUniformGrid.html#fdtdx.QuasiUniformGrid" class="reference internal" title="fdtdx.core.grid.QuasiUniformGrid"><span class="pre"><code class="sourceCode python">QuasiUniformGrid</code></span></a> <span class="pre">\|</span> <a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a>*<a href="#fdtdx.SimulationConfig.grid" class="headerlink" title="Link to this definition">#</a>  
Spatial grid configuration.

<span class="pre">`UniformGrid`</span> is an unresolved policy used while the final volume shape is still being inferred. <span class="pre">`RectilinearGrid`</span> is the realized solver grid with explicit physical edge coordinates. Placement resolves policies to <span class="pre">`RectilinearGrid`</span> so compiled FDTD code has exactly one metric source.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">has_nonuniform_grid</span></span><a href="#fdtdx.SimulationConfig.has_nonuniform_grid" class="headerlink" title="Link to this definition">#</a>  
Whether the realized solver grid is non-uniform.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">has_symmetry</span></span><a href="#fdtdx.SimulationConfig.has_symmetry" class="headerlink" title="Link to this definition">#</a>  
Whether any axis requests mirror symmetry.

Returns<span class="colon">:</span>  
True if at least one entry of <a href="#fdtdx.SimulationConfig.symmetry" class="reference internal" title="fdtdx.SimulationConfig.symmetry"><span class="pre"><code class="sourceCode python">symmetry</code></span></a> is nonzero, meaning the  
domain will be reduced and a PEC/PMC wall placed on the symmetry plane(s).

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">invertible_optimization</span></span><a href="#fdtdx.SimulationConfig.invertible_optimization" class="headerlink" title="Link to this definition">#</a>  
Check if invertible optimization is enabled.

Invertible optimization uses time-reversibility of Maxwell’s equations to compute gradients with reduced memory requirements compared to checkpointing-based methods.

Returns<span class="colon">:</span>  
True if gradient computation uses invertible differentiation  
(recorder is specified), False otherwise.

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">max_travel_distance</span></span><a href="#fdtdx.SimulationConfig.max_travel_distance" class="headerlink" title="Link to this definition">#</a>  
Calculate the maximum distance light can travel during the simulation.

This represents the theoretical maximum distance that light could travel through the simulation volume, useful for determining if the simulation time is sufficient for light to traverse the entire domain.

Returns<span class="colon">:</span>  
Maximum travel distance in meters, based on the speed of light  
and total simulation time.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">only_forward</span></span><a href="#fdtdx.SimulationConfig.only_forward" class="headerlink" title="Link to this definition">#</a>  
Check if the simulation is forward-only (no gradient computation).

Forward-only simulations don’t compute gradients and are used when only the forward propagation of electromagnetic fields is needed, without optimization.

Returns<span class="colon">:</span>  
True if no gradient configuration is specified, False otherwise.

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">resolved_grid</span></span><a href="#fdtdx.SimulationConfig.resolved_grid" class="headerlink" title="Link to this definition">#</a>  
Return the concrete solver grid, or <span class="pre">`None`</span> if not yet resolved.

<span class="pre">`UniformGrid`</span> has no edge arrays until the simulation shape is known. Callers that need coordinates, areas, or volumes should use this property and fall back to <span class="pre">`uniform_spacing`</span> when it returns <span class="pre">`None`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">symmetry</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`int`</span><span class="pre">\]</span>*<a href="#fdtdx.SimulationConfig.symmetry" class="headerlink" title="Link to this definition">#</a>  
Per-axis mirror symmetry of the simulation, in the order (x, y, z). Each entry is one of <span class="pre">`{-1,`</span>` `<span class="pre">`0,`</span>` `<span class="pre">`+1}`</span>: <span class="pre">`0`</span> = no symmetry on this axis (default), <span class="pre">`-1`</span> = PEC (electric-wall) mirror on the axis center plane, <span class="pre">`+1`</span> = PMC (magnetic-wall) mirror on the axis center plane. When any entry is nonzero, <a href="fdtdx.place_objects.html#fdtdx.place_objects" class="reference internal" title="fdtdx.place_objects"><span class="pre"><code class="sourceCode python">fdtdx.place_objects()</code></span></a> automatically reduces the domain to the symmetric half/quarter/octant (keeping the upper half along each symmetric axis), clips every object onto that reduced grid, inserts the PEC/PMC wall on the symmetry plane, and forwards the matching per-axis condition to the mode solver. The FDTD then runs on the reduced domain; call <a href="fdtdx.unfold_fields.html#fdtdx.unfold_fields" class="reference internal" title="fdtdx.unfold_fields"><span class="pre"><code class="sourceCode python">fdtdx.unfold_fields()</code></span></a> / <a href="fdtdx.unfold_detector_states.html#fdtdx.unfold_detector_states" class="reference internal" title="fdtdx.unfold_detector_states"><span class="pre"><code class="sourceCode python">fdtdx.unfold_detector_states()</code></span></a> afterwards to reconstruct the full-domain arrays. This is additive and independent of manually specifying PEC/PMC as ordinary boundaries via <a href="fdtdx.BoundaryConfig.html#fdtdx.BoundaryConfig" class="reference internal" title="fdtdx.BoundaryConfig"><span class="pre"><code class="sourceCode python">fdtdx.BoundaryConfig</code></span></a>. Each symmetric axis must resolve to an **even** number of grid cells (so the domain splits exactly down the middle and the unfolded result matches the full domain cell-for-cell); otherwise <a href="fdtdx.place_objects.html#fdtdx.place_objects" class="reference internal" title="fdtdx.place_objects"><span class="pre"><code class="sourceCode python">fdtdx.place_objects()</code></span></a> raises a <span class="pre">`ValueError`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">time</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.SimulationConfig.time" class="headerlink" title="Link to this definition">#</a>  
Total simulation time in seconds.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">time_step_duration</span></span><a href="#fdtdx.SimulationConfig.time_step_duration" class="headerlink" title="Link to this definition">#</a>  
Calculate the duration of a single time step.

The time step duration is determined by the Courant condition to ensure numerical stability. Realized rectilinear grids use their smallest per-axis spacings. Unresolved uniform grids use their configured scalar spacing; unresolved quasi-uniform grids use their smallest per-axis spacing as a conservative CFL bound.

Returns<span class="colon">:</span>  
Time step duration in seconds, calculated using the Courant  
condition and spatial resolution.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">time_steps_total</span></span><a href="#fdtdx.SimulationConfig.time_steps_total" class="headerlink" title="Link to this definition">#</a>  
Calculate the total number of time steps for the simulation.

Determines how many discrete time steps are needed to simulate the specified total simulation time, based on the time step duration.

Returns<span class="colon">:</span>  
Total number of time steps needed to reach the specified  
simulation time.

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">use_complex_fields</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.SimulationConfig.use_complex_fields" class="headerlink" title="Link to this definition">#</a>  
Whether to use complex-valued field arrays. None (default): auto-detect based on boundary conditions (e.g. Bloch). True: force complex fields (complex64 if dtype=float32, complex128 if dtype=float64). False: force real fields (raises error if Bloch boundaries are present).

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SimulationConfig.aset" class="headerlink" title="Link to this definition">#</a>  
Sets an attribute of this class. In contrast to the classical .at\[\].set(), this method updates the class attribute directly and does not only operate on jax pytree leaf nodes. Instead, replaces the full attribute with the new value.

The attribute can either be the attribute name of this class, or for nested classes it can also be the attribute name of a class, which itself is an attribute of this class. The syntax for this operation could look like this: “a-\>b-\>\[0\]-\>\[‘name’\]”. Here, the current class has an attribute a, which has an attribute b, which is a list, which we index at index 0, which is an element of type dictionary, which we index using the dictionary key ‘name’.

Note that dictionary keys cannot contain square brackets or single quotes (even if they are escaped).

Parameters<span class="colon">:</span>  
- **attr_name** (*str*) – Name of attribute to set

- **val** (*Any*) – Value to set the attribute to

- **create_new_ok** (*bool,* *optional*) – If false (default), throw an error if the attribute does not exist. If true, creates a new attribute if the attribute name does not exist yet.

Returns<span class="colon">:</span>  
Updated instance with new attribute value

Return type<span class="colon">:</span>  
Self

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.SimulationConfig.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.SimulationConfig.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">resolve_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/config.html#SimulationConfig.resolve_grid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SimulationConfig.resolve_grid" class="headerlink" title="Link to this definition">#</a>  
Return a concrete solver grid.

Parameters<span class="colon">:</span>  
**shape** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\] \| <span class="pre">`None`</span></span>) – Required when <span class="pre">`grid`</span> is an unresolved <span class="pre">`UniformGrid`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a></span>

Returns<span class="colon">:</span>  
A concrete <span class="pre">`RectilinearGrid`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SimulationConfig.</span></span><span class="sig-name descname"><span class="pre">uniform_spacing</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/config.html#SimulationConfig.uniform_spacing" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SimulationConfig.uniform_spacing" class="headerlink" title="Link to this definition">#</a>  
Return the uniform grid spacing.

<span class="pre">`UniformGrid`</span> can answer this before placement. <span class="pre">`RectilinearGrid`</span> answers only when all spacings are equal and raises for non-uniform meshes, making unsupported scalar assumptions explicit.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
