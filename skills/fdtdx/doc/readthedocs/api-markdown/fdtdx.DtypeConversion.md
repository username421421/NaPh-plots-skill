<div id="fdtdx-dtypeconversion" class="section">

# fdtdx.DtypeConversion<a href="#fdtdx-dtypeconversion" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">DtypeConversion</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">dtype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">exclude_filter</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/modules.html#DtypeConversion" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DtypeConversion" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`CompressionModule`</span>

Compression module that converts data types of field values.

This module changes the data type of field values while preserving their shape, useful for reducing memory usage or meeting precision requirements.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.DtypeConversion.dtype" class="reference internal" title="fdtdx.DtypeConversion.dtype"><span class="pre"><code class="sourceCode python">dtype</code></span></a>

- <a href="#fdtdx.DtypeConversion.exclude_filter" class="reference internal" title="fdtdx.DtypeConversion.exclude_filter"><span class="pre"><code class="sourceCode python">exclude_filter</code></span></a>

Methods

- <a href="#fdtdx.DtypeConversion.aset" class="reference internal" title="fdtdx.DtypeConversion.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.DtypeConversion.compress" class="reference internal" title="fdtdx.DtypeConversion.compress"><span class="pre"><code class="sourceCode python">compress</code></span></a>

- <a href="#fdtdx.DtypeConversion.decompress" class="reference internal" title="fdtdx.DtypeConversion.decompress"><span class="pre"><code class="sourceCode python">decompress</code></span></a>

- <a href="#fdtdx.DtypeConversion.get_class_fields" class="reference internal" title="fdtdx.DtypeConversion.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.DtypeConversion.get_public_fields" class="reference internal" title="fdtdx.DtypeConversion.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.DtypeConversion.init_shapes" class="reference internal" title="fdtdx.DtypeConversion.init_shapes"><span class="pre"><code class="sourceCode python">init_shapes</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">dtype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dtype`</span>*<a href="#fdtdx.DtypeConversion.dtype" class="headerlink" title="Link to this definition">#</a>  
Target data type for conversion.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">exclude_filter</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Sequence`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">\]</span>*<a href="#fdtdx.DtypeConversion.exclude_filter" class="headerlink" title="Link to this definition">#</a>  
List of field names to exclude from conversion.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.DtypeConversion.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">compress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/modules.html#DtypeConversion.compress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DtypeConversion.compress" class="headerlink" title="Link to this definition">#</a>  
Compress field values at the current time step.

Parameters<span class="colon">:</span>  
- **values** (*dict\[str,* *jax.Array\]*) – Dictionary mapping field names to their values.

- **state** (<a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState"><em>RecordingState</em></a>) – Current recording state.

- **key** (*jax.Array*) – Random key for stochastic operations.

Returns<span class="colon">:</span>  
Tuple containing:  
- Dictionary of compressed field values

- Updated recording state

Return type<span class="colon">:</span>  
tuple\[dict\[str, jax.Array\], <a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState">RecordingState</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">decompress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/modules.html#DtypeConversion.decompress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DtypeConversion.decompress" class="headerlink" title="Link to this definition">#</a>  
Decompress field values back to their original form.

Parameters<span class="colon">:</span>  
- **values** (*dict\[str,* *jax.Array\]*) – Dictionary mapping field names to their compressed values.

- **state** (<a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState"><em>RecordingState</em></a>) – Current recording state.

- **key** (*jax.Array*) – Random key for stochastic operations.

Returns<span class="colon">:</span>  
Dictionary mapping field names to their decompressed values.

Return type<span class="colon">:</span>  
dict\[str, jax.Array\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.DtypeConversion.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.DtypeConversion.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DtypeConversion.</span></span><span class="sig-name descname"><span class="pre">init_shapes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_shape_dtypes</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/modules.html#DtypeConversion.init_shapes" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DtypeConversion.init_shapes" class="headerlink" title="Link to this definition">#</a>  
Initialize shapes and sizes for the compression module.

Parameters<span class="colon">:</span>  
**input_shape_dtypes** (*dict\[str,* *jax.ShapeDtypeStruct\]*) – Dictionary mapping field names to their input shapes/dtypes.

Returns<span class="colon">:</span>  
Tuple containing:  
- Self: Updated instance of the compression module

- Dictionary mapping field names to their output shapes/dtypes

- Dictionary mapping field names to their state shapes/dtypes

Return type<span class="colon">:</span>  
tuple\[Self, dict\[str, jax.ShapeDtypeStruct\], dict\[str, jax.ShapeDtypeStruct\]\]

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
