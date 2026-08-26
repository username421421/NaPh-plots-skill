<div id="fdtdx-arraycontainer" class="section">

# fdtdx.ArrayContainer<a href="#fdtdx-arraycontainer" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">ArrayContainer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fields</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">detector_states</span></span>*, *<span class="n"><span class="pre">recording_state</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">magnetic_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_inv_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">initial_inv_permittivities</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ArrayContainer" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ArrayContainer" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Container for simulation field arrays and states.

This class holds the electromagnetic field arrays and various state information needed during FDTD simulation. It includes the E and H fields, material properties, and states for boundaries, detectors and recordings.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.ArrayContainer.detector_states" class="reference internal" title="fdtdx.ArrayContainer.detector_states"><span class="pre"><code class="sourceCode python">detector_states</code></span></a>

- <a href="#fdtdx.ArrayContainer.dispersive_c1" class="reference internal" title="fdtdx.ArrayContainer.dispersive_c1"><span class="pre"><code class="sourceCode python">dispersive_c1</code></span></a>

- <a href="#fdtdx.ArrayContainer.dispersive_c2" class="reference internal" title="fdtdx.ArrayContainer.dispersive_c2"><span class="pre"><code class="sourceCode python">dispersive_c2</code></span></a>

- <a href="#fdtdx.ArrayContainer.dispersive_c3" class="reference internal" title="fdtdx.ArrayContainer.dispersive_c3"><span class="pre"><code class="sourceCode python">dispersive_c3</code></span></a>

- <a href="#fdtdx.ArrayContainer.dispersive_c4" class="reference internal" title="fdtdx.ArrayContainer.dispersive_c4"><span class="pre"><code class="sourceCode python">dispersive_c4</code></span></a>

- <a href="#fdtdx.ArrayContainer.dispersive_inv_c2" class="reference internal" title="fdtdx.ArrayContainer.dispersive_inv_c2"><span class="pre"><code class="sourceCode python">dispersive_inv_c2</code></span></a>

- <a href="#fdtdx.ArrayContainer.electric_conductivity" class="reference internal" title="fdtdx.ArrayContainer.electric_conductivity"><span class="pre"><code class="sourceCode python">electric_conductivity</code></span></a>

- <a href="#fdtdx.ArrayContainer.fields" class="reference internal" title="fdtdx.ArrayContainer.fields"><span class="pre"><code class="sourceCode python">fields</code></span></a>

- <a href="#fdtdx.ArrayContainer.initial_inv_permittivities" class="reference internal" title="fdtdx.ArrayContainer.initial_inv_permittivities"><span class="pre"><code class="sourceCode python">initial_inv_permittivities</code></span></a>

- <a href="#fdtdx.ArrayContainer.inv_permeabilities" class="reference internal" title="fdtdx.ArrayContainer.inv_permeabilities"><span class="pre"><code class="sourceCode python">inv_permeabilities</code></span></a>

- <a href="#fdtdx.ArrayContainer.inv_permittivities" class="reference internal" title="fdtdx.ArrayContainer.inv_permittivities"><span class="pre"><code class="sourceCode python">inv_permittivities</code></span></a>

- <a href="#fdtdx.ArrayContainer.magnetic_conductivity" class="reference internal" title="fdtdx.ArrayContainer.magnetic_conductivity"><span class="pre"><code class="sourceCode python">magnetic_conductivity</code></span></a>

- <a href="#fdtdx.ArrayContainer.recording_state" class="reference internal" title="fdtdx.ArrayContainer.recording_state"><span class="pre"><code class="sourceCode python">recording_state</code></span></a>

Methods

- <a href="#fdtdx.ArrayContainer.aset" class="reference internal" title="fdtdx.ArrayContainer.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.ArrayContainer.get_class_fields" class="reference internal" title="fdtdx.ArrayContainer.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.ArrayContainer.get_public_fields" class="reference internal" title="fdtdx.ArrayContainer.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.ArrayContainer.reset" class="reference internal" title="fdtdx.ArrayContainer.reset"><span class="pre"><code class="sourceCode python">reset</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">detector_states</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`Array`</span><span class="pre">\]\]</span>*<a href="#fdtdx.ArrayContainer.detector_states" class="headerlink" title="Link to this definition">#</a>  
Dictionary mapping detector names to their states.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">dispersive_c1</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.dispersive_c1" class="headerlink" title="Link to this definition">#</a>  
Per-cell dispersive recurrence coefficient c1. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span> with <span class="pre">`num_components`</span> 1 (isotropic dispersion, broadcast over the field components) or 3 (per-axis / diagonally anisotropic dispersion). <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">dispersive_c2</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.dispersive_c2" class="headerlink" title="Link to this definition">#</a>  
Per-cell dispersive recurrence coefficient c2. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>, <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3)`</span>. <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">dispersive_c3</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.dispersive_c3" class="headerlink" title="Link to this definition">#</a>  
Per-cell dispersive recurrence coefficient c3. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>, <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3)`</span>. <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">dispersive_c4</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.dispersive_c4" class="headerlink" title="Link to this definition">#</a>  
Per-cell dispersive recurrence coefficient c4 (the <span class="pre">`dE/dt`</span> / CCPR coupling to <span class="pre">`E^{n+1}`</span>). Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>, <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3)`</span>. <span class="pre">`None`</span> unless at least one CCPR pole with non-zero <span class="pre">`coupling_edot`</span> is present; Lorentz/Drude-only sims leave it <span class="pre">`None`</span> and skip the CCPR update path.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">dispersive_inv_c2</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.dispersive_inv_c2" class="headerlink" title="Link to this definition">#</a>  
Per-cell cached <span class="pre">`1`</span>` `<span class="pre">`/`</span>` `<span class="pre">`c2`</span> with non-dispersive cells set to 0. Lets the reverse-time ADE update avoid a <span class="pre">`jnp.where`</span> + division per step. Derived from <span class="pre">`dispersive_c2`</span>; never differentiated independently. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>, <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3)`</span>. <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">electric_conductivity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.electric_conductivity" class="headerlink" title="Link to this definition">#</a>  
field for electric conductivity terms. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">fields</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.FieldState.html#fdtdx.FieldState" class="reference internal" title="fdtdx.fdtd.container.FieldState"><span class="pre"><code class="sourceCode python">FieldState</code></span></a>*<a href="#fdtdx.ArrayContainer.fields" class="headerlink" title="Link to this definition">#</a>  
Dynamic electromagnetic fields (E, H and PML auxiliaries).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">initial_inv_permittivities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.initial_inv_permittivities" class="headerlink" title="Link to this definition">#</a>  
Backup of inverse permittivity values array. Only used when etching a device.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">inv_permeabilities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`float`</span>*<a href="#fdtdx.ArrayContainer.inv_permeabilities" class="headerlink" title="Link to this definition">#</a>  
Inverse permeability values array.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">inv_permittivities</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.ArrayContainer.inv_permittivities" class="headerlink" title="Link to this definition">#</a>  
Inverse permittivity values array.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">magnetic_conductivity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  
field for magnetic conductivity terms. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">recording_state</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.interfaces.state.RecordingState"><span class="pre"><code class="sourceCode python">RecordingState</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ArrayContainer.recording_state" class="headerlink" title="Link to this definition">#</a>  
Optional state for recording simulation data.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ArrayContainer.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ArrayContainer.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ArrayContainer.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ArrayContainer.</span></span><span class="sig-name descname"><span class="pre">reset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">reset_detector_states</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">reset_recording_state</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ArrayContainer.reset" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ArrayContainer.reset" class="headerlink" title="Link to this definition">#</a>  
Return a reset copy of this array container.

Dynamic field arrays are zeroed while material arrays and conductivity arrays are preserved. Detector states are reset by default because they accumulate time-dependent measurements. Recording state is preserved by default so partial simulations can continue writing to the same buffers.

Parameters<span class="colon">:</span>  
- **reset_detector_states** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Whether to zero all detector state arrays. Defaults to True.

- **reset_recording_state** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Whether to zero recording data and state arrays when a recording state is present. Defaults to False.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a></span>

Returns<span class="colon">:</span>  
A new ArrayContainer with reset dynamic state.

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
