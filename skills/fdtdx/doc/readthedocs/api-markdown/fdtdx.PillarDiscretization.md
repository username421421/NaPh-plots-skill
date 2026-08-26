<div id="fdtdx-pillardiscretization" class="section">

# fdtdx.PillarDiscretization<a href="#fdtdx-pillardiscretization" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">PillarDiscretization</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">single_polymer_columns</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">distance_metric</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'permittivity_differences_plus_average_permittivity'</span></span>*, *<span class="n"><span class="pre">background_material</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/parameters/discretization.html#PillarDiscretization" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PillarDiscretization" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.ParameterTransformation.html#fdtdx.ParameterTransformation" class="reference internal" title="fdtdx.objects.device.parameters.transform.ParameterTransformation"><span class="pre"><code class="sourceCode python">ParameterTransformation</code></span></a>

Constraint module for mapping pillar structures to allowed configurations.

Maps arbitrary pillar structures to the nearest allowed configurations based on material constraints and geometry requirements. Ensures structures meet fabrication rules like single polymer columns and no trapped air holes.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.PillarDiscretization.axis" class="reference internal" title="fdtdx.PillarDiscretization.axis"><span class="pre"><code class="sourceCode python">axis</code></span></a>

- <a href="#fdtdx.PillarDiscretization.background_material" class="reference internal" title="fdtdx.PillarDiscretization.background_material"><span class="pre"><code class="sourceCode python">background_material</code></span></a>

- <a href="#fdtdx.PillarDiscretization.distance_metric" class="reference internal" title="fdtdx.PillarDiscretization.distance_metric"><span class="pre"><code class="sourceCode python">distance_metric</code></span></a>

- <a href="#fdtdx.PillarDiscretization.single_polymer_columns" class="reference internal" title="fdtdx.PillarDiscretization.single_polymer_columns"><span class="pre"><code class="sourceCode python">single_polymer_columns</code></span></a>

Methods

- <a href="#fdtdx.PillarDiscretization.aset" class="reference internal" title="fdtdx.PillarDiscretization.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.PillarDiscretization.get_class_fields" class="reference internal" title="fdtdx.PillarDiscretization.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.PillarDiscretization.get_input_shape" class="reference internal" title="fdtdx.PillarDiscretization.get_input_shape"><span class="pre"><code class="sourceCode python">get_input_shape</code></span></a>

- <a href="#fdtdx.PillarDiscretization.get_output_type" class="reference internal" title="fdtdx.PillarDiscretization.get_output_type"><span class="pre"><code class="sourceCode python">get_output_type</code></span></a>

- <a href="#fdtdx.PillarDiscretization.get_public_fields" class="reference internal" title="fdtdx.PillarDiscretization.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.PillarDiscretization.init_module" class="reference internal" title="fdtdx.PillarDiscretization.init_module"><span class="pre"><code class="sourceCode python">init_module</code></span></a>

- <a href="#fdtdx.PillarDiscretization.init_type" class="reference internal" title="fdtdx.PillarDiscretization.init_type"><span class="pre"><code class="sourceCode python">init_type</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.PillarDiscretization.axis" class="headerlink" title="Link to this definition">#</a>  
Axis along which to enforce pillar constraints (0=x, 1=y, 2=z).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">background_material</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PillarDiscretization.background_material" class="headerlink" title="Link to this definition">#</a>  
Name of the background material in the materials dictionary of the corresponding device. If None, the material with lowest permittivity is used. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">distance_metric</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'euclidean'`</span><span class="pre">,</span> <span class="pre">`'permittivity_differences_plus_average_permittivity'`</span><span class="pre">\]</span>*<a href="#fdtdx.PillarDiscretization.distance_metric" class="headerlink" title="Link to this definition">#</a>  
Method to compute distances between material distributions:

- “euclidean”: Standard Euclidean distance between permittivity values.

- “permittivity_differences_plus_average_permittivity”: Weighted combination of permittivity differences and average permittivity values, optimized for material distribution comparisons.

Defaults to “permittivity_differences_plus_average_permittivity”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">single_polymer_columns</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span>*<a href="#fdtdx.PillarDiscretization.single_polymer_columns" class="headerlink" title="Link to this definition">#</a>  
If True, restrict to single polymer columns.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">get_input_shape</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.get_input_shape" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`...`</span>\]\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">get_output_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.get_output_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`ParameterType`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">init_module</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">materials</span></span>*, *<span class="n"><span class="pre">matrix_voxel_grid_shape</span></span>*, *<span class="n"><span class="pre">single_voxel_size</span></span>*, *<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/parameters/discretization.html#PillarDiscretization.init_module" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PillarDiscretization.init_module" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PillarDiscretization.</span></span><span class="sig-name descname"><span class="pre">init_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PillarDiscretization.init_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
