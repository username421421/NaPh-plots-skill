<div id="fdtdx-connectholesandstructures" class="section">

# fdtdx.ConnectHolesAndStructures<a href="#fdtdx-connectholesandstructures" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">ConnectHolesAndStructures</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">fill_material</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">background_material</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/parameters/discrete.html#ConnectHolesAndStructures" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ConnectHolesAndStructures" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`SameShapeTypeParameterTransform`</span>

Connects floating polymer regions and ensures air holes connect to outside.

This constraint module ensures physical realizability of designs by: 1. Either connecting floating polymer regions to the substrate or removing them 2. Ensuring all air holes are connected to the outside (no trapped air)

The bottom (lower z) is treated as the substrate reference.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.ConnectHolesAndStructures.background_material" class="reference internal" title="fdtdx.ConnectHolesAndStructures.background_material"><span class="pre"><code class="sourceCode python">background_material</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.fill_material" class="reference internal" title="fdtdx.ConnectHolesAndStructures.fill_material"><span class="pre"><code class="sourceCode python">fill_material</code></span></a>

Methods

- <a href="#fdtdx.ConnectHolesAndStructures.aset" class="reference internal" title="fdtdx.ConnectHolesAndStructures.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.get_class_fields" class="reference internal" title="fdtdx.ConnectHolesAndStructures.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.get_input_shape" class="reference internal" title="fdtdx.ConnectHolesAndStructures.get_input_shape"><span class="pre"><code class="sourceCode python">get_input_shape</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.get_output_type" class="reference internal" title="fdtdx.ConnectHolesAndStructures.get_output_type"><span class="pre"><code class="sourceCode python">get_output_type</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.get_public_fields" class="reference internal" title="fdtdx.ConnectHolesAndStructures.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.init_module" class="reference internal" title="fdtdx.ConnectHolesAndStructures.init_module"><span class="pre"><code class="sourceCode python">init_module</code></span></a>

- <a href="#fdtdx.ConnectHolesAndStructures.init_type" class="reference internal" title="fdtdx.ConnectHolesAndStructures.init_type"><span class="pre"><code class="sourceCode python">init_type</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">background_material</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ConnectHolesAndStructures.background_material" class="headerlink" title="Link to this definition">#</a>  
Name of the background material. If none, the material with the lowest permittivity is used. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">fill_material</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ConnectHolesAndStructures.fill_material" class="headerlink" title="Link to this definition">#</a>  
Name of material to use for filling gaps when connecting regions. Required when working with more than 2 materials. Defaults to None.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">get_input_shape</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.get_input_shape" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`...`</span>\]\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">get_output_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.get_output_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`ParameterType`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">init_module</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">materials</span></span>*, *<span class="n"><span class="pre">matrix_voxel_grid_shape</span></span>*, *<span class="n"><span class="pre">single_voxel_size</span></span>*, *<span class="n"><span class="pre">output_shape</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.init_module" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ConnectHolesAndStructures.</span></span><span class="sig-name descname"><span class="pre">init_type</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_type</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ConnectHolesAndStructures.init_type" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
