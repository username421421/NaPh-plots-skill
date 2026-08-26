<div id="fdtdx-standardtoplusoneminusonerange" class="section">

# fdtdx.StandardToPlusOneMinusOneRange<a href="#fdtdx-standardtoplusoneminusonerange" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">StandardToPlusOneMinusOneRange</span></span><a href="../_modules/fdtdx/objects/device/parameters/continuous.html#StandardToPlusOneMinusOneRange" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.StandardToPlusOneMinusOneRange" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.StandardToCustomRange.html#fdtdx.StandardToCustomRange" class="reference internal" title="fdtdx.objects.device.parameters.continuous.StandardToCustomRange"><span class="pre"><code class="sourceCode python">StandardToCustomRange</code></span></a>

Maps standard \[0,1\] range to \[-1,1\] range.

Special case of StandardToCustomRange that maps to \[-1,1\] range. Used for symmetric value ranges around zero.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.max_value" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.max_value"><span class="pre"><code class="sourceCode python">max_value</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.min_value" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.min_value"><span class="pre"><code class="sourceCode python">min_value</code></span></a>

Methods

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.aset" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.get_class_fields" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.get_input_shape" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.get_input_shape"><span class="pre"><code class="sourceCode python">get_input_shape</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.get_output_type" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.get_output_type"><span class="pre"><code class="sourceCode python">get_output_type</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.get_public_fields" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.init_module" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.init_module"><span class="pre"><code class="sourceCode python">init_module</code></span></a>

- <a href="#fdtdx.StandardToPlusOneMinusOneRange.init_type" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange.init_type"><span class="pre"><code class="sourceCode python">init_type</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">max_value</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.StandardToPlusOneMinusOneRange.max_value" class="headerlink" title="Link to this definition">#</a>  
Maximum value of target range. Defaults to one.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">min_value</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.StandardToPlusOneMinusOneRange.min_value" class="headerlink" title="Link to this definition">#</a>  
Minimum value of target range. Defaults to zero.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">get_input_shape</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.get_input_shape" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`...`</span>\]\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">get_output_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.get_output_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`ParameterType`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">init_module</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">materials</span></span>*, *<span class="n"><span class="pre">matrix_voxel_grid_shape</span></span>*, *<span class="n"><span class="pre">single_voxel_size</span></span>*, *<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.init_module" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">StandardToPlusOneMinusOneRange.</span></span><span class="sig-name descname"><span class="pre">init_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.StandardToPlusOneMinusOneRange.init_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
