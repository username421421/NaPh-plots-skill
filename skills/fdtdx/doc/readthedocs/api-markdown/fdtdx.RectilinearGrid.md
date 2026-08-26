<div id="fdtdx-rectilineargrid" class="section">

# fdtdx.RectilinearGrid<a href="#fdtdx-rectilineargrid" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">RectilinearGrid</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">x_edges</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">y_edges</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">z_edges</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Realized rectilinear simulation grid described by physical cell edges.

This is the canonical solver-facing grid representation used by fdtdx internals. A uniform grid is represented by equally spaced edge arrays, not by a separate scalar code path. Keeping one realized representation is important for the non-uniform grid migration: placement, PML profiles, mode-solver coordinates, detector weights, and Yee update metrics should all ask the grid for physical distances instead of deriving them from a global <span class="pre">`resolution`</span> value.

The arrays store cell *edges* in metres. For a grid with <span class="pre">`nx`</span> cells along x, <span class="pre">`x_edges`</span> has shape <span class="pre">`(nx`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1,)`</span> and must be strictly increasing. Cell widths, centers, face areas, and volumes are derived from these arrays.

Notes

This class intentionally does not encode automatic mesh generation policy. Future policy objects such as <span class="pre">`AutoGrid`</span> or <span class="pre">`QuasiUniformGrid`</span> should resolve to <span class="pre">`RectilinearGrid`</span> before the solver runs.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.RectilinearGrid.dx" class="reference internal" title="fdtdx.RectilinearGrid.dx"><span class="pre"><code class="sourceCode python">dx</code></span></a>

- <a href="#fdtdx.RectilinearGrid.dy" class="reference internal" title="fdtdx.RectilinearGrid.dy"><span class="pre"><code class="sourceCode python">dy</code></span></a>

- <a href="#fdtdx.RectilinearGrid.dz" class="reference internal" title="fdtdx.RectilinearGrid.dz"><span class="pre"><code class="sourceCode python">dz</code></span></a>

- <a href="#fdtdx.RectilinearGrid.is_uniform" class="reference internal" title="fdtdx.RectilinearGrid.is_uniform"><span class="pre"><code class="sourceCode python">is_uniform</code></span></a>

- <a href="#fdtdx.RectilinearGrid.min_spacing" class="reference internal" title="fdtdx.RectilinearGrid.min_spacing"><span class="pre"><code class="sourceCode python">min_spacing</code></span></a>

- <a href="#fdtdx.RectilinearGrid.min_spacings" class="reference internal" title="fdtdx.RectilinearGrid.min_spacings"><span class="pre"><code class="sourceCode python">min_spacings</code></span></a>

- <a href="#fdtdx.RectilinearGrid.shape" class="reference internal" title="fdtdx.RectilinearGrid.shape"><span class="pre"><code class="sourceCode python">shape</code></span></a>

- <a href="#fdtdx.RectilinearGrid.uniform_spacing" class="reference internal" title="fdtdx.RectilinearGrid.uniform_spacing"><span class="pre"><code class="sourceCode python">uniform_spacing</code></span></a>

- <a href="#fdtdx.RectilinearGrid.x_edges" class="reference internal" title="fdtdx.RectilinearGrid.x_edges"><span class="pre"><code class="sourceCode python">x_edges</code></span></a>

- <a href="#fdtdx.RectilinearGrid.y_edges" class="reference internal" title="fdtdx.RectilinearGrid.y_edges"><span class="pre"><code class="sourceCode python">y_edges</code></span></a>

- <a href="#fdtdx.RectilinearGrid.z_edges" class="reference internal" title="fdtdx.RectilinearGrid.z_edges"><span class="pre"><code class="sourceCode python">z_edges</code></span></a>

Methods

- <a href="#fdtdx.RectilinearGrid.anchor_coordinate" class="reference internal" title="fdtdx.RectilinearGrid.anchor_coordinate"><span class="pre"><code class="sourceCode python">anchor_coordinate</code></span></a>

- <a href="#fdtdx.RectilinearGrid.aset" class="reference internal" title="fdtdx.RectilinearGrid.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.RectilinearGrid.axis_extent" class="reference internal" title="fdtdx.RectilinearGrid.axis_extent"><span class="pre"><code class="sourceCode python">axis_extent</code></span></a>

- <a href="#fdtdx.RectilinearGrid.bounds_for_anchor" class="reference internal" title="fdtdx.RectilinearGrid.bounds_for_anchor"><span class="pre"><code class="sourceCode python">bounds_for_anchor</code></span></a>

- <a href="#fdtdx.RectilinearGrid.bounds_for_center" class="reference internal" title="fdtdx.RectilinearGrid.bounds_for_center"><span class="pre"><code class="sourceCode python">bounds_for_center</code></span></a>

- <a href="#fdtdx.RectilinearGrid.cell_volume" class="reference internal" title="fdtdx.RectilinearGrid.cell_volume"><span class="pre"><code class="sourceCode python">cell_volume</code></span></a>

- <a href="#fdtdx.RectilinearGrid.cell_widths" class="reference internal" title="fdtdx.RectilinearGrid.cell_widths"><span class="pre"><code class="sourceCode python">cell_widths</code></span></a>

- <a href="#fdtdx.RectilinearGrid.centers" class="reference internal" title="fdtdx.RectilinearGrid.centers"><span class="pre"><code class="sourceCode python">centers</code></span></a>

- <a href="#fdtdx.RectilinearGrid.cfl_time_step" class="reference internal" title="fdtdx.RectilinearGrid.cfl_time_step"><span class="pre"><code class="sourceCode python">cfl_time_step</code></span></a>

- <a href="#fdtdx.RectilinearGrid.coord_to_index" class="reference internal" title="fdtdx.RectilinearGrid.coord_to_index"><span class="pre"><code class="sourceCode python">coord_to_index</code></span></a>

- <a href="#fdtdx.RectilinearGrid.custom" class="reference internal" title="fdtdx.RectilinearGrid.custom"><span class="pre"><code class="sourceCode python">custom</code></span></a>

- <a href="#fdtdx.RectilinearGrid.edges" class="reference internal" title="fdtdx.RectilinearGrid.edges"><span class="pre"><code class="sourceCode python">edges</code></span></a>

- <a href="#fdtdx.RectilinearGrid.face_area" class="reference internal" title="fdtdx.RectilinearGrid.face_area"><span class="pre"><code class="sourceCode python">face_area</code></span></a>

- <a href="#fdtdx.RectilinearGrid.get_class_fields" class="reference internal" title="fdtdx.RectilinearGrid.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.RectilinearGrid.get_public_fields" class="reference internal" title="fdtdx.RectilinearGrid.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.RectilinearGrid.length_to_cell_count" class="reference internal" title="fdtdx.RectilinearGrid.length_to_cell_count"><span class="pre"><code class="sourceCode python">length_to_cell_count</code></span></a>

- <a href="#fdtdx.RectilinearGrid.reduce_symmetric" class="reference internal" title="fdtdx.RectilinearGrid.reduce_symmetric"><span class="pre"><code class="sourceCode python">reduce_symmetric</code></span></a>

- <a href="#fdtdx.RectilinearGrid.slice_extent" class="reference internal" title="fdtdx.RectilinearGrid.slice_extent"><span class="pre"><code class="sourceCode python">slice_extent</code></span></a>

- <a href="#fdtdx.RectilinearGrid.subgrid" class="reference internal" title="fdtdx.RectilinearGrid.subgrid"><span class="pre"><code class="sourceCode python">subgrid</code></span></a>

- <a href="#fdtdx.RectilinearGrid.uniform" class="reference internal" title="fdtdx.RectilinearGrid.uniform"><span class="pre"><code class="sourceCode python">uniform</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">dx</span></span><a href="#fdtdx.RectilinearGrid.dx" class="headerlink" title="Link to this definition">#</a>  
Cell widths along x in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">dy</span></span><a href="#fdtdx.RectilinearGrid.dy" class="headerlink" title="Link to this definition">#</a>  
Cell widths along y in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">dz</span></span><a href="#fdtdx.RectilinearGrid.dz" class="headerlink" title="Link to this definition">#</a>  
Cell widths along z in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">is_uniform</span></span><a href="#fdtdx.RectilinearGrid.is_uniform" class="headerlink" title="Link to this definition">#</a>  
Whether all cell widths match a single spacing within numerical tolerance.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">min_spacing</span></span><a href="#fdtdx.RectilinearGrid.min_spacing" class="headerlink" title="Link to this definition">#</a>  
Smallest cell width in the grid.

This value is the conservative spacing used for staged CFL migration. The full non-uniform update should eventually use explicit local metric arrays, but stability remains controlled by the smallest cell.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">min_spacings</span></span><a href="#fdtdx.RectilinearGrid.min_spacings" class="headerlink" title="Link to this definition">#</a>  
Smallest cell width along each axis in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">shape</span></span><a href="#fdtdx.RectilinearGrid.shape" class="headerlink" title="Link to this definition">#</a>  
Number of cells along each axis.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">uniform_spacing</span></span><a href="#fdtdx.RectilinearGrid.uniform_spacing" class="headerlink" title="Link to this definition">#</a>  
Return the scalar spacing for a uniform grid or raise for non-uniform grids.

This compatibility escape hatch should only be used by code that has not yet been migrated to metric-aware helpers. It deliberately raises for non-uniform grids so unsupported paths fail loudly.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">x_edges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.RectilinearGrid.x_edges" class="headerlink" title="Link to this definition">#</a>  
Physical edge coordinates along x in metres, shape <span class="pre">`(nx`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1,)`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">y_edges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.RectilinearGrid.y_edges" class="headerlink" title="Link to this definition">#</a>  
Physical edge coordinates along y in metres, shape <span class="pre">`(ny`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1,)`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">z_edges</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.RectilinearGrid.z_edges" class="headerlink" title="Link to this definition">#</a>  
Physical edge coordinates along z in metres, shape <span class="pre">`(nz`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1,)`</span>.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">anchor_coordinate</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">bounds</span></span>*, *<span class="n"><span class="pre">position</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.anchor_coordinate" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.anchor_coordinate" class="headerlink" title="Link to this definition">#</a>  
Return a physical anchor coordinate inside an interval.

<span class="pre">`position`</span> follows fdtdx object-anchor convention: <span class="pre">`-1`</span> is the lower side, <span class="pre">`0`</span> is the center, and <span class="pre">`+1`</span> is the upper side.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.RectilinearGrid.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">axis_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">bounds</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.axis_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.axis_extent" class="headerlink" title="Link to this definition">#</a>  
Physical length covered by an index interval on one axis.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">bounds_for_anchor</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">size</span></span>*, *<span class="n"><span class="pre">anchor</span></span>*, *<span class="n"><span class="pre">position</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.bounds_for_anchor" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.bounds_for_anchor" class="headerlink" title="Link to this definition">#</a>  
Choose a cell interval whose object anchor is closest to <span class="pre">`anchor`</span>.

Parameters<span class="colon">:</span>  
- **axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Grid axis.

- **size** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Number of cells in the interval.

- **anchor** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Desired physical anchor coordinate in metres.

- **position** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Object-relative anchor position, where <span class="pre">`-1`</span> is lower side, <span class="pre">`0`</span> is center, and <span class="pre">`+1`</span> is upper side.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

Returns<span class="colon">:</span>  
<span class="pre">`(lower,`</span>` `<span class="pre">`upper)`</span> edge indices with <span class="pre">`upper`</span>` `<span class="pre">`-`</span>` `<span class="pre">`lower`</span>` `<span class="pre">`==`</span>` `<span class="pre">`size`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">bounds_for_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">center</span></span>*, *<span class="n"><span class="pre">size</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.bounds_for_center" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.bounds_for_center" class="headerlink" title="Link to this definition">#</a>  
Choose a cell interval whose physical center is closest to <span class="pre">`center`</span>.

Parameters<span class="colon">:</span>  
- **axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Grid axis.

- **center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Desired physical center coordinate in metres.

- **size** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Number of cells in the interval.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

Returns<span class="colon">:</span>  
<span class="pre">`(lower,`</span>` `<span class="pre">`upper)`</span> edge indices with <span class="pre">`upper`</span>` `<span class="pre">`-`</span>` `<span class="pre">`lower`</span>` `<span class="pre">`==`</span>` `<span class="pre">`size`</span>.

Notes

This operation is used by object placement when a physical center position and an already-resolved grid-cell size are known. On a non-uniform grid there is no exact analogue of <span class="pre">`round(x`</span>` `<span class="pre">`/`</span>` `<span class="pre">`dx)`</span>; selecting the closest physical interval center gives deterministic snapping while preserving the requested grid-cell size.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">cell_volume</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.cell_volume" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.cell_volume" class="headerlink" title="Link to this definition">#</a>  
Return per-cell volume weights broadcast to a 3D slice shape.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">cell_widths</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.cell_widths" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.cell_widths" class="headerlink" title="Link to this definition">#</a>  
Return cell widths for <span class="pre">`axis`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">centers</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.centers" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.centers" class="headerlink" title="Link to this definition">#</a>  
Return cell-center coordinates for <span class="pre">`axis`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">cfl_time_step</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">courant_factor</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.cfl_time_step" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.cfl_time_step" class="headerlink" title="Link to this definition">#</a>  
Return the CFL-limited time step for a rectilinear 3D grid.

The stability limit for an orthogonal FDTD grid is controlled by the smallest spacing on each axis:

<span class="pre">`dt`</span>` `<span class="pre">`<=`</span>` `<span class="pre">`courant_factor`</span>` `<span class="pre">`/`</span>` `<span class="pre">`(c`</span>` `<span class="pre">`*`</span>` `<span class="pre">`sqrt(1/dx_min^2`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1/dy_min^2`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1/dz_min^2))`</span>.

For uniform grids this is exactly the existing <span class="pre">`courant_factor/sqrt(3)`</span> behavior. For anisotropic or stretched grids it avoids using one global spacing for all three axes.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">coord_to_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">coord</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.coord_to_index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.coord_to_index" class="headerlink" title="Link to this definition">#</a>  
Map a physical coordinate to a grid edge index.

Parameters<span class="colon">:</span>  
- **axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Grid axis.

- **coord** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Coordinate in metres.

- **snap** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – Snapping rule. <span class="pre">`"nearest"`</span> chooses the closest edge, <span class="pre">`"lower"`</span> chooses the previous edge, and <span class="pre">`"upper"`</span> chooses the next edge.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

Returns<span class="colon">:</span>  
Edge index after applying the requested snapping rule.

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">custom</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">x_edges</span></span>*, *<span class="n"><span class="pre">y_edges</span></span>*, *<span class="n"><span class="pre">z_edges</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.custom" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.custom" class="headerlink" title="Link to this definition">#</a>  
Create a realized rectilinear grid from explicit edge arrays.

This constructor is equivalent to calling <span class="pre">`RectilinearGrid(...)`</span> directly, but it makes the user-facing intent explicit: the caller is supplying the final grid coordinates, not an automatic meshing policy.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">edges</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.edges" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.edges" class="headerlink" title="Link to this definition">#</a>  
Return edge coordinates for <span class="pre">`axis`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">face_area</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.face_area" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.face_area" class="headerlink" title="Link to this definition">#</a>  
Return per-cell face-area weights for a detector plane.

Parameters<span class="colon">:</span>  
- **axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Normal axis of the face.

- **slice_tuple** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\], <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\], <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]\]</span>) – Grid slice containing the detector volume. The normal axis is expected to have width one for a plane detector.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

Returns<span class="colon">:</span>  
Area weights broadcast to the detector’s 3D slice shape.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.RectilinearGrid.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.RectilinearGrid.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">length_to_cell_count</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">length</span></span>*, *<span class="n"><span class="pre">snap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'nearest'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.length_to_cell_count" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.length_to_cell_count" class="headerlink" title="Link to this definition">#</a>  
Convert a physical length to a number of cells from the lower domain edge.

This helper preserves the old uniform-grid behavior when <span class="pre">`snap`</span> is <span class="pre">`"nearest"`</span>. For non-uniform placement, <span class="pre">`"upper"`</span> is usually the safer rule because it chooses enough cells to cover the requested metric size from the lower domain edge.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">reduce_symmetric</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">symmetry</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.reduce_symmetric" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.reduce_symmetric" class="headerlink" title="Link to this definition">#</a>  
Return the grid reduced onto the kept (upper) half along each symmetric axis.

Used by <span class="pre">`place_objects`</span> when <span class="pre">`config.symmetry`</span> is set on a non-uniform grid: the simulation runs on the reduced (half/quarter/octant) domain and the result is unfolded afterwards. For every axis with <span class="pre">`symmetry[a]`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`0`</span> this keeps the upper-half edges <span class="pre">`edges(a)[n`</span>` `<span class="pre">`//`</span>` `<span class="pre">`2:]`</span> (absolute coordinates preserved — the FDTD metrics depend only on cell widths, which are translation-invariant). Non-symmetric axes are returned unchanged.

Two conditions must hold on each symmetric axis so that mirroring the kept half exactly reconstructs the full domain:

- an even cell count, so the split lands on a cell edge, and

- mirror-symmetric cell widths about the center (<span class="pre">`dx[i]`</span>` `<span class="pre">`==`</span>` `<span class="pre">`dx[n`</span>` `<span class="pre">`-`</span>` `<span class="pre">`1`</span>` `<span class="pre">`-`</span>` `<span class="pre">`i]`</span>), so the discarded lower half is the exact mirror of the kept half.

Parameters<span class="colon">:</span>  
**symmetry** (*tuple\[int,* *int,* *int\]*) – Per-axis symmetry condition <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>; <span class="pre">`0`</span> means no reduction on that axis (any nonzero value reduces it).

Returns<span class="colon">:</span>  
The reduced grid (a new instance; the original is unchanged).

Return type<span class="colon">:</span>  
<a href="#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.RectilinearGrid">RectilinearGrid</a>

Raises<span class="colon">:</span>  
**ValueError** – If a symmetric axis has an odd (or \< 2) cell count, or cell widths that are not mirror-symmetric about the center.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">slice_extent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">slice_tuple</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.slice_extent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.slice_extent" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by a 3D grid slice.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">subgrid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.subgrid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.subgrid" class="headerlink" title="Link to this definition">#</a>  
Convenience wrapper to get the sub-grid of a placed fdtdx.SimulationObject given its grid_slice

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">RectilinearGrid.</span></span><span class="sig-name descname"><span class="pre">uniform</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">shape</span></span>*, *<span class="n"><span class="pre">spacing</span></span>*, *<span class="n"><span class="pre">origin</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/grid.html#RectilinearGrid.uniform" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RectilinearGrid.uniform" class="headerlink" title="Link to this definition">#</a>  
Create a realized rectilinear grid for a uniform grid.

The grid is centered at <span class="pre">`center`</span> by default, so edge arrays span <span class="pre">`[center[a]`</span>` `<span class="pre">`-`</span>` `<span class="pre">`shape[a]`</span>` `<span class="pre">`*`</span>` `<span class="pre">`spacing`</span>` `<span class="pre">`/`</span>` `<span class="pre">`2,`</span>` `<span class="pre">`center[a]`</span>` `<span class="pre">`+`</span>` `<span class="pre">`shape[a]`</span>` `<span class="pre">`*`</span>` `<span class="pre">`spacing`</span>` `<span class="pre">`/`</span>` `<span class="pre">`2]`</span> along each axis. Negative and positive coordinates are used symmetrically around the center of the simulation domain.

Passing an explicit <span class="pre">`origin`</span> (lower-corner coordinate) overrides <span class="pre">`center`</span> and restores the legacy lower-corner behaviour. This is used internally by <span class="pre">`UniformGrid.resolve`</span> after it has already computed the lower corner from the center.

Parameters<span class="colon">:</span>  
- **shape** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>) – Number of cells in <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>.

- **spacing** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Uniform cell width in metres.

- **center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – Physical coordinate of the domain center. Defaults to <span class="pre">`(0,`</span>` `<span class="pre">`0,`</span>` `<span class="pre">`0)`</span> so the domain spans equally into negative and positive coordinates.

- **origin** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\] \| <span class="pre">`None`</span></span>) – Physical coordinate of the **lower** domain corner. When provided this takes priority over <span class="pre">`center`</span>.

Returns<span class="colon">:</span>  
A grid whose edge arrays are equally spaced and centered on <span class="pre">`center`</span> (or anchored at <span class="pre">`origin`</span> when given).

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
