<div id="fdtdx-linearreconstructeveryk" class="section">

# fdtdx.LinearReconstructEveryK<a href="#fdtdx-linearreconstructeveryk" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">LinearReconstructEveryK</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">k</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">start_recording_after</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`TimeStepFilter`</span>

Time step filter that performs linear reconstruction between sampled steps.

This filter saves field values every k time steps and uses linear interpolation to reconstruct values at intermediate time steps.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.LinearReconstructEveryK.k" class="reference internal" title="fdtdx.LinearReconstructEveryK.k"><span class="pre"><code class="sourceCode python">k</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.start_recording_after" class="reference internal" title="fdtdx.LinearReconstructEveryK.start_recording_after"><span class="pre"><code class="sourceCode python">start_recording_after</code></span></a>

Methods

- <a href="#fdtdx.LinearReconstructEveryK.aset" class="reference internal" title="fdtdx.LinearReconstructEveryK.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.compress" class="reference internal" title="fdtdx.LinearReconstructEveryK.compress"><span class="pre"><code class="sourceCode python">compress</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.decompress" class="reference internal" title="fdtdx.LinearReconstructEveryK.decompress"><span class="pre"><code class="sourceCode python">decompress</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.get_class_fields" class="reference internal" title="fdtdx.LinearReconstructEveryK.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.get_public_fields" class="reference internal" title="fdtdx.LinearReconstructEveryK.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.indices_to_decompress" class="reference internal" title="fdtdx.LinearReconstructEveryK.indices_to_decompress"><span class="pre"><code class="sourceCode python">indices_to_decompress</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.init_shapes" class="reference internal" title="fdtdx.LinearReconstructEveryK.init_shapes"><span class="pre"><code class="sourceCode python">init_shapes</code></span></a>

- <a href="#fdtdx.LinearReconstructEveryK.time_to_array_index" class="reference internal" title="fdtdx.LinearReconstructEveryK.time_to_array_index"><span class="pre"><code class="sourceCode python">time_to_array_index</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">k</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.LinearReconstructEveryK.k" class="headerlink" title="Link to this definition">#</a>  
Number of time steps between saved values.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">start_recording_after</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.LinearReconstructEveryK.start_recording_after" class="headerlink" title="Link to this definition">#</a>  
Time step to start recording from. Defaults to zero.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.LinearReconstructEveryK.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">compress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">time_idx</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK.compress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK.compress" class="headerlink" title="Link to this definition">#</a>  
Compress field values at a given time step.

Parameters<span class="colon">:</span>  
- **values** (*dict\[str,* *jax.Array\]*) – Dictionary mapping field names to their values.

- **state** (<a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState"><em>RecordingState</em></a>) – Current recording state.

- **time_idx** (*jax.Array*) – Current time step index.

- **key** (*jax.Array*) – Random key for stochastic operations.

Returns<span class="colon">:</span>  
Tuple containing:  
- Dictionary of compressed field values

- Updated recording state

Return type<span class="colon">:</span>  
tuple\[dict\[str, jax.Array\], <a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState">RecordingState</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">decompress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">arr_indices</span></span>*, *<span class="n"><span class="pre">time_idx</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK.decompress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK.decompress" class="headerlink" title="Link to this definition">#</a>  
Decompress field values to reconstruct data for a time step.

Parameters<span class="colon">:</span>  
- **values** (*list\[dict\[str,* *jax.Array\]\]*) – List of dictionaries containing array values needed for reconstruction.

- **state** (<a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState"><em>RecordingState</em></a>) – Current recording state.

- **arr_indices** (*jax.Array*) – Array indices needed for reconstruction.

- **time_idx** (*jax.Array*) – Time step index to reconstruct. scalar value.

- **key** (*jax.Array*) – Random key for stochastic operations.

Returns<span class="colon">:</span>  
Dictionary of reconstructed field values.

Return type<span class="colon">:</span>  
dict\[str, jax.Array\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.LinearReconstructEveryK.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.LinearReconstructEveryK.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">indices_to_decompress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_idx</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK.indices_to_decompress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK.indices_to_decompress" class="headerlink" title="Link to this definition">#</a>  
Get array indices needed to reconstruct data for a given time step.

Parameters<span class="colon">:</span>  
**time_idx** (*jax.Array*) – Time step index to reconstruct.

Returns<span class="colon">:</span>  
Array of indices needed to reconstruct the data for this time step.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">init_shapes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_shape_dtypes</span></span>*, *<span class="n"><span class="pre">time_steps_max</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK.init_shapes" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK.init_shapes" class="headerlink" title="Link to this definition">#</a>  
Initialize shapes and sizes for the time step filter.

Parameters<span class="colon">:</span>  
- **input_shape_dtypes** (*dict\[str,* *jax.ShapeDtypeStruct\]*) – Dictionary mapping field names to their shape/dtype information.

- **time_steps_max** (*int*) – Maximum number of time steps in the simulation.

Returns<span class="colon">:</span>  
A tuple containing:  
- Updated filter instance

- Size of array for storing filtered data

- Dictionary of data shapes/dtypes

- Dictionary of state shapes/dtypes

Return type<span class="colon">:</span>  
tuple\[Self, int, dict\[str, jax.ShapeDtypeStruct\], dict\[str, jax.ShapeDtypeStruct\]\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LinearReconstructEveryK.</span></span><span class="sig-name descname"><span class="pre">time_to_array_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_idx</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/time_filter.html#LinearReconstructEveryK.time_to_array_index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LinearReconstructEveryK.time_to_array_index" class="headerlink" title="Link to this definition">#</a>  
Convert a time step index to its corresponding array index.

Parameters<span class="colon">:</span>  
**time_idx** (*int*) – Time step index to convert.

Returns<span class="colon">:</span>  
The corresponding array index if the time step is not filtered,  
or -1 if the time step is filtered out.

Return type<span class="colon">:</span>  
int

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
