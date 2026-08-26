<div id="fdtdx-uniformgrid" class="section">

# fdtdx.UniformGrid<a href="#fdtdx-uniformgrid" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">UniformGrid</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">spacing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Unresolved policy for a uniform rectilinear grid.

<span class="pre">`UniformGrid`</span> is user intent, not the solver mesh itself. It records the physical cell spacing while the final simulation shape may still be unknown. Object placement resolves this policy to a concrete <span class="pre">`RectilinearGrid`</span> once the volume shape is known.

Keeping uniform spacing here avoids a second scalar discretization source on <span class="pre">`SimulationConfig`</span>. Uniform grids and explicitly non-uniform grids both enter the solver through the same realized <span class="pre">`RectilinearGrid`</span> structure.

The grid origin is at the **center** of the simulation domain. Edge arrays therefore span <span class="pre">`[-N/2`</span>` `<span class="pre">`*`</span>` `<span class="pre">`spacing,`</span>` `<span class="pre">`+N/2`</span>` `<span class="pre">`*`</span>` `<span class="pre">`spacing]`</span> along each axis, giving the domain symmetric negative and positive coordinates. <span class="pre">`center`</span> shifts this physical center away from the geometric origin when non-zero.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.UniformGrid.center" class="reference internal" title="fdtdx.UniformGrid.center"><span class="pre"><code class="sourceCode python">center</code></span></a>

- <a href="#fdtdx.UniformGrid.is_uniform" class="reference internal" title="fdtdx.UniformGrid.is_uniform"><span class="pre"><code class="sourceCode python">is_uniform</code></span></a>

- <a href="#fdtdx.UniformGrid.min_spacing" class="reference internal" title="fdtdx.UniformGrid.min_spacing"><span class="pre"><code class="sourceCode python">min_spacing</code></span></a>

- <a href="#fdtdx.UniformGrid.spacing" class="reference internal" title="fdtdx.UniformGrid.spacing"><span class="pre"><code class="sourceCode python">spacing</code></span></a>

- <a href="#fdtdx.UniformGrid.uniform_spacing" class="reference internal" title="fdtdx.UniformGrid.uniform_spacing"><span class="pre"><code class="sourceCode python">uniform_spacing</code></span></a>

Methods

- <a href="#fdtdx.UniformGrid.anchor_coordinate" class="reference internal" title="fdtdx.UniformGrid.anchor_coordinate"><span class="pre"><code class="sourceCode python">anchor_coordinate</code></span></a>

- <a href="#fdtdx.UniformGrid.aset" class="reference internal" title="fdtdx.UniformGrid.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.UniformGrid.axis_extent" class="reference internal" title="fdtdx.UniformGrid.axis_extent"><span class="pre"><code class="sourceCode python">axis_extent</code></span></a>

- <a href="#fdtdx.UniformGrid.bounds_for_anchor" class="reference internal" title="fdtdx.UniformGrid.bounds_for_anchor"><span class="pre"><code class="sourceCode python">bounds_for_anchor</code></span></a>

- <a href="#fdtdx.UniformGrid.bounds_for_center" class="reference internal" title="fdtdx.UniformGrid.bounds_for_center"><span class="pre"><code class="sourceCode python">bounds_for_center</code></span></a>

- <a href="#fdtdx.UniformGrid.cell_volume" class="reference internal" title="fdtdx.UniformGrid.cell_volume"><span class="pre"><code class="sourceCode python">cell_volume</code></span></a>

- <a href="#fdtdx.UniformGrid.coord_to_index" class="reference internal" title="fdtdx.UniformGrid.coord_to_index"><span class="pre"><code class="sourceCode python">coord_to_index</code></span></a>

- <a href="#fdtdx.UniformGrid.face_area" class="reference internal" title="fdtdx.UniformGrid.face_area"><span class="pre"><code class="sourceCode python">face_area</code></span></a>

- <a href="#fdtdx.UniformGrid.get_class_fields" class="reference internal" title="fdtdx.UniformGrid.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.UniformGrid.get_public_fields" class="reference internal" title="fdtdx.UniformGrid.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.UniformGrid.length_to_cell_count" class="reference internal" title="fdtdx.UniformGrid.length_to_cell_count"><span class="pre"><code class="sourceCode python">length_to_cell_count</code></span></a>

- <a href="#fdtdx.UniformGrid.resolve" class="reference internal" title="fdtdx.UniformGrid.resolve"><span class="pre"><code class="sourceCode python">resolve</code></span></a>

- <a href="#fdtdx.UniformGrid.slice_extent" class="reference internal" title="fdtdx.UniformGrid.slice_extent"><span class="pre"><code class="sourceCode python">slice_extent</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">center</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.UniformGrid.center" class="headerlink" title="Link to this definition">#</a>  
Physical coordinate of the domain center in metres. Defaults to (0, 0, 0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">is_uniform</span></span><a href="#fdtdx.UniformGrid.is_uniform" class="headerlink" title="Link to this definition">#</a>  
Uniform policies always represent equal cell widths.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">min_spacing</span></span><a href="#fdtdx.UniformGrid.min_spacing" class="headerlink" title="Link to this definition">#</a>  
Smallest cell width implied by this policy.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">spacing</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.UniformGrid.spacing" class="headerlink" title="Link to this definition">#</a>  
Physical cell spacing in metres. Must be positive.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">uniform_spacing</span></span><a href="#fdtdx.UniformGrid.uniform_spacing" class="headerlink" title="Link to this definition">#</a>  
Scalar cell width in metres.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">anchor_coordinate</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">bounds</span></span>*, *<span class="n"><span class="pre">position</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.anchor_coordinate" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.anchor_coordinate" class="headerlink" title="Link to this definition">#</a>  
Return a physical anchor coordinate inside a uniform interval.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformGrid.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">axis_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">bounds</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.axis_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.axis_extent" class="headerlink" title="Link to this definition">#</a>  
Physical length covered by an index interval on one axis.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">bounds_for_anchor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">size</span></span>*, *<span class="n"><span class="pre">anchor</span></span>*, *<span class="n"><span class="pre">position</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.bounds_for_anchor" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.bounds_for_anchor" class="headerlink" title="Link to this definition">#</a>  
Choose a uniform-grid interval from an object anchor.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">bounds_for_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">center</span></span>*, *<span class="n"><span class="pre">size</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.bounds_for_center" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.bounds_for_center" class="headerlink" title="Link to this definition">#</a>  
Convert a physical center and grid size to edge bounds.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">cell_volume</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.cell_volume" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.cell_volume" class="headerlink" title="Link to this definition">#</a>  
Return per-cell volumes for a slice on this uniform policy.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">coord_to_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">coord</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.coord_to_index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.coord_to_index" class="headerlink" title="Link to this definition">#</a>  
Map a physical coordinate to a uniform-grid edge index.

Because unresolved policies do not yet know <span class="pre">`shape`</span>, this helper uses a center-relative basis: <span class="pre">`coord`</span> is interpreted relative to <span class="pre">`self.center[axis]`</span> and the returned index is a center-relative edge offset. Use <a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid.coord_to_index" class="reference internal" title="fdtdx.RectilinearGrid.coord_to_index"><span class="pre"><code class="sourceCode python">RectilinearGrid.coord_to_index()</code></span></a> on the resolved grid when you need absolute edge indices.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">face_area</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.face_area" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.face_area" class="headerlink" title="Link to this definition">#</a>  
Return per-face areas for a slice on this uniform policy.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.UniformGrid.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.UniformGrid.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">length_to_cell_count</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">length</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.length_to_cell_count" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.length_to_cell_count" class="headerlink" title="Link to this definition">#</a>  
Convert a physical length to a uniform-grid cell count.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">resolve</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">shape</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.resolve" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.resolve" class="headerlink" title="Link to this definition">#</a>  
Return a concrete solver grid for <span class="pre">`shape`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformGrid.</span></span><span class="sig-name descname"><span class="pre">slice_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#UniformGrid.slice_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformGrid.slice_extent" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by a 3D grid slice.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
