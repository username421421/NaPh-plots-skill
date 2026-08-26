<div id="fdtdx-quasiuniformgrid" class="section">

# fdtdx.QuasiUniformGrid<a href="#fdtdx-quasiuniformgrid" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">QuasiUniformGrid</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">dx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">dy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">dz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Unresolved policy for a rectilinear grid with independent per-axis spacings.

<span class="pre">`QuasiUniformGrid`</span> generalises <span class="pre">`UniformGrid`</span> to allow different cell widths along x, y, and z while keeping each axis internally uniform. This is sometimes called a *quasi-uniform* or *anisotropic-uniform* mesh: the grid is rectilinear and axis-aligned, but the aspect ratio is not 1 : 1 : 1.

Like <span class="pre">`UniformGrid`</span>, this is user intent rather than the solver mesh. Calling <a href="#fdtdx.QuasiUniformGrid.resolve" class="reference internal" title="fdtdx.QuasiUniformGrid.resolve"><span class="pre"><code class="sourceCode python">resolve()</code></span></a> converts the policy to a concrete <span class="pre">`RectilinearGrid`</span> once the simulation shape is known. The resulting grid is centered at <span class="pre">`center`</span> so that coordinates span symmetrically into both negative and positive values along every axis.

Example:

<div class="highlight-default notranslate">

<div class="highlight">

    grid = QuasiUniformGrid(dx=10e-9, dy=10e-9, dz=20e-9)
    resolved = grid.resolve(shape=(100, 100, 50))
    # x, y edges span [-500 nm, +500 nm]; z edges span [-500 nm, +500 nm]

</div>

</div>

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.QuasiUniformGrid.center" class="reference internal" title="fdtdx.QuasiUniformGrid.center"><span class="pre"><code class="sourceCode python">center</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.dx" class="reference internal" title="fdtdx.QuasiUniformGrid.dx"><span class="pre"><code class="sourceCode python">dx</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.dy" class="reference internal" title="fdtdx.QuasiUniformGrid.dy"><span class="pre"><code class="sourceCode python">dy</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.dz" class="reference internal" title="fdtdx.QuasiUniformGrid.dz"><span class="pre"><code class="sourceCode python">dz</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.is_uniform" class="reference internal" title="fdtdx.QuasiUniformGrid.is_uniform"><span class="pre"><code class="sourceCode python">is_uniform</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.min_spacing" class="reference internal" title="fdtdx.QuasiUniformGrid.min_spacing"><span class="pre"><code class="sourceCode python">min_spacing</code></span></a>

Methods

- <a href="#fdtdx.QuasiUniformGrid.aset" class="reference internal" title="fdtdx.QuasiUniformGrid.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.axis_extent" class="reference internal" title="fdtdx.QuasiUniformGrid.axis_extent"><span class="pre"><code class="sourceCode python">axis_extent</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.axis_spacing" class="reference internal" title="fdtdx.QuasiUniformGrid.axis_spacing"><span class="pre"><code class="sourceCode python">axis_spacing</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.cell_volume" class="reference internal" title="fdtdx.QuasiUniformGrid.cell_volume"><span class="pre"><code class="sourceCode python">cell_volume</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.coord_to_index" class="reference internal" title="fdtdx.QuasiUniformGrid.coord_to_index"><span class="pre"><code class="sourceCode python">coord_to_index</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.face_area" class="reference internal" title="fdtdx.QuasiUniformGrid.face_area"><span class="pre"><code class="sourceCode python">face_area</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.get_class_fields" class="reference internal" title="fdtdx.QuasiUniformGrid.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.get_public_fields" class="reference internal" title="fdtdx.QuasiUniformGrid.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.length_to_cell_count" class="reference internal" title="fdtdx.QuasiUniformGrid.length_to_cell_count"><span class="pre"><code class="sourceCode python">length_to_cell_count</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.resolve" class="reference internal" title="fdtdx.QuasiUniformGrid.resolve"><span class="pre"><code class="sourceCode python">resolve</code></span></a>

- <a href="#fdtdx.QuasiUniformGrid.slice_extent" class="reference internal" title="fdtdx.QuasiUniformGrid.slice_extent"><span class="pre"><code class="sourceCode python">slice_extent</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">center</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.QuasiUniformGrid.center" class="headerlink" title="Link to this definition">#</a>  
Physical coordinate of the domain center in metres. Defaults to (0, 0, 0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">dx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.QuasiUniformGrid.dx" class="headerlink" title="Link to this definition">#</a>  
Cell width along x in metres. Must be positive.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">dy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.QuasiUniformGrid.dy" class="headerlink" title="Link to this definition">#</a>  
Cell width along y in metres. Must be positive.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">dz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.QuasiUniformGrid.dz" class="headerlink" title="Link to this definition">#</a>  
Cell width along z in metres. Must be positive.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">is_uniform</span></span><a href="#fdtdx.QuasiUniformGrid.is_uniform" class="headerlink" title="Link to this definition">#</a>  
True only when all three spacings are equal.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">min_spacing</span></span><a href="#fdtdx.QuasiUniformGrid.min_spacing" class="headerlink" title="Link to this definition">#</a>  
Smallest cell width across all three axes in metres.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.QuasiUniformGrid.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">axis_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">bounds</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.axis_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.axis_extent" class="headerlink" title="Link to this definition">#</a>  
Physical length covered by an index interval on one axis.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">axis_spacing</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.axis_spacing" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.axis_spacing" class="headerlink" title="Link to this definition">#</a>  
Return the cell width for a single axis.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">cell_volume</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.cell_volume" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.cell_volume" class="headerlink" title="Link to this definition">#</a>  
Return per-cell volume weights broadcast to a 3D slice shape.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">coord_to_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">coord</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.coord_to_index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.coord_to_index" class="headerlink" title="Link to this definition">#</a>  
Map a physical coordinate to a grid edge index along <span class="pre">`axis`</span>.

Coordinates are measured from <span class="pre">`self.center[axis]`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">face_area</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.face_area" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.face_area" class="headerlink" title="Link to this definition">#</a>  
Return per-face area weights for a detector plane normal to <span class="pre">`axis`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.QuasiUniformGrid.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.QuasiUniformGrid.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">length_to_cell_count</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">length</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.length_to_cell_count" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.length_to_cell_count" class="headerlink" title="Link to this definition">#</a>  
Convert a physical length to a cell count along <span class="pre">`axis`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">resolve</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">shape</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.resolve" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.resolve" class="headerlink" title="Link to this definition">#</a>  
Return a concrete <span class="pre">`RectilinearGrid`</span> for <span class="pre">`shape`</span>.

Edge arrays are built independently for each axis using the per-axis spacing and the requested number of cells. The domain is centered at <span class="pre">`self.center`</span>.

Parameters<span class="colon">:</span>  
**shape** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>) – Number of cells in <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a></span>

Returns<span class="colon">:</span>  
A <span class="pre">`RectilinearGrid`</span> whose edge arrays are piecewise-uniform (one constant spacing per axis) and span symmetrically around <span class="pre">`self.center`</span>.

Raises<span class="colon">:</span>  
**ValueError** – If any axis has an odd cell count. The center-origin convention requires even cell counts on every axis so the domain center always lands on a cell edge. An odd count silently shifts which Yee component sits at object boundaries, changing the effective simulated length by one cell.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">QuasiUniformGrid.</span></span><span class="sig-name descname"><span class="pre">slice_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#QuasiUniformGrid.slice_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.QuasiUniformGrid.slice_extent" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by a 3D grid slice.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
