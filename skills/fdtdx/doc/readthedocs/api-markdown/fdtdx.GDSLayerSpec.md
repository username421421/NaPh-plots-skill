<div id="fdtdx-gdslayerspec" class="section">

# fdtdx.GDSLayerSpec<a href="#fdtdx-gdslayerspec" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">GDSLayerSpec</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gds_layer</span></span>*, *<span class="n"><span class="pre">material_name</span></span>*, *<span class="n"><span class="pre">thickness</span></span>*, *<span class="n"><span class="pre">gds_datatype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">z_base</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">etch_by</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">sidewall_angle</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">90.0</span></span>*, *<span class="n"><span class="pre">reference_plane</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'bottom'</span></span>*, *<span class="n"><span class="pre">subpixel_smoothing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">subpixel_full_tensor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">fill_supersample</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8</span></span>*, *<span class="n"><span class="pre">color</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">Color(r=0.8470588235294118,</span> <span class="pre">g=0.8627450980392157,</span> <span class="pre">b=0.8392156862745098)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerSpec" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerSpec" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`object`</span>

Specification for a single GDS layer to be imported as a simulation object.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.GDSLayerSpec.color" class="reference internal" title="fdtdx.GDSLayerSpec.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.etch_by" class="reference internal" title="fdtdx.GDSLayerSpec.etch_by"><span class="pre"><code class="sourceCode python">etch_by</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.fill_supersample" class="reference internal" title="fdtdx.GDSLayerSpec.fill_supersample"><span class="pre"><code class="sourceCode python">fill_supersample</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.gds_datatype" class="reference internal" title="fdtdx.GDSLayerSpec.gds_datatype"><span class="pre"><code class="sourceCode python">gds_datatype</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.name" class="reference internal" title="fdtdx.GDSLayerSpec.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.reference_plane" class="reference internal" title="fdtdx.GDSLayerSpec.reference_plane"><span class="pre"><code class="sourceCode python">reference_plane</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.sidewall_angle" class="reference internal" title="fdtdx.GDSLayerSpec.sidewall_angle"><span class="pre"><code class="sourceCode python">sidewall_angle</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.subpixel_full_tensor" class="reference internal" title="fdtdx.GDSLayerSpec.subpixel_full_tensor"><span class="pre"><code class="sourceCode python">subpixel_full_tensor</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.subpixel_smoothing" class="reference internal" title="fdtdx.GDSLayerSpec.subpixel_smoothing"><span class="pre"><code class="sourceCode python">subpixel_smoothing</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.z_base" class="reference internal" title="fdtdx.GDSLayerSpec.z_base"><span class="pre"><code class="sourceCode python">z_base</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.gds_layer" class="reference internal" title="fdtdx.GDSLayerSpec.gds_layer"><span class="pre"><code class="sourceCode python">gds_layer</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.material_name" class="reference internal" title="fdtdx.GDSLayerSpec.material_name"><span class="pre"><code class="sourceCode python">material_name</code></span></a>

- <a href="#fdtdx.GDSLayerSpec.thickness" class="reference internal" title="fdtdx.GDSLayerSpec.thickness"><span class="pre"><code class="sourceCode python">thickness</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.Color.html#fdtdx.Color" class="reference internal" title="fdtdx.colors.Color"><span class="pre"><code class="sourceCode python">Color</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">Color(r=0.8470588235294118,</span> <span class="pre">g=0.8627450980392157,</span> <span class="pre">b=0.8392156862745098)</span>*<a href="#fdtdx.GDSLayerSpec.color" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">etch_by</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`int`</span><span class="pre">\],</span> <span class="pre">`...`</span><span class="pre">\]</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">()</span>*<a href="#fdtdx.GDSLayerSpec.etch_by" class="headerlink" title="Link to this definition">#</a>  
Tuple of (layer, datatype) pairs whose polygons are subtracted from this layer via a boolean NOT operation before voxelization. Useful for etched features such as via holes.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">fill_supersample</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">8</span>*<a href="#fdtdx.GDSLayerSpec.fill_supersample" class="headerlink" title="Link to this definition">#</a>  
Number of sub-samples per axis used to estimate the in-plane fill fraction when <span class="pre">`subpixel_smoothing`</span> is on. See <span class="pre">`fill_supersample`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">gds_datatype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a href="#fdtdx.GDSLayerSpec.gds_datatype" class="headerlink" title="Link to this definition">#</a>  
GDS datatype number (default 0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span> <span class="pre">\|</span> <span class="pre">`None`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">None</span>*<a href="#fdtdx.GDSLayerSpec.name" class="headerlink" title="Link to this definition">#</a>  
Optional name for the resulting object. Auto-generates <span class="pre">`"gds_{layer}_{datatype}"`</span> if None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">reference_plane</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'bottom'`</span><span class="pre">,</span> <span class="pre">`'middle'`</span><span class="pre">,</span> <span class="pre">`'top'`</span><span class="pre">\]</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'bottom'</span>*<a href="#fdtdx.GDSLayerSpec.reference_plane" class="headerlink" title="Link to this definition">#</a>  
Which face keeps the nominal polygon footprint when <span class="pre">`sidewall_angle`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`90`</span>. <span class="pre">`"bottom"`</span> (default) keeps the base footprint and tapers the top inward for an angle <span class="pre">`<`</span>` `<span class="pre">`90`</span>; <span class="pre">`"top"`</span> keeps the top footprint; <span class="pre">`"middle"`</span> keeps the mid-height footprint and splits the taper symmetrically. Mirrors <span class="pre">`PolySlab.reference_plane`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">sidewall_angle</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">90.0</span>*<a href="#fdtdx.GDSLayerSpec.sidewall_angle" class="headerlink" title="Link to this definition">#</a>  
Sidewall angle in **degrees**, measured between the sidewall and the substrate plane, the way foundry PDKs specify it. <span class="pre">`90.0`</span> (default) is a perfectly vertical wall. An angle <span class="pre">`<`</span>` `<span class="pre">`90`</span> tilts the wall so the cross-section *shrinks* toward the top (regular trapezoid / positive-resist etch, e.g. 89 deg); an angle <span class="pre">`>`</span>` `<span class="pre">`90`</span> makes it *grow* toward the top (re-entrant / undercut profile). Must satisfy <span class="pre">`0`</span>` `<span class="pre">`<`</span>` `<span class="pre">`sidewall_angle`</span>` `<span class="pre">`<`</span>` `<span class="pre">`180`</span>. (Relation to the Tidy3D <span class="pre">`PolySlab`</span> convention: <span class="pre">`polyslab_angle_rad`</span>` `<span class="pre">`=`</span>` `<span class="pre">`deg2rad(90`</span>` `<span class="pre">`-`</span>` `<span class="pre">`sidewall_angle)`</span>.)

<div class="admonition note">

Note

For <span class="pre">`sidewall_angle`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`90`</span> the *binary* voxelization (<a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject.get_voxel_mask_for_shape" class="reference internal" title="fdtdx.GDSLayerObject.get_voxel_mask_for_shape"><span class="pre"><code class="sourceCode python">GDSLayerObject.get_voxel_mask_for_shape()</code></span></a>) **staircases** the trapezoidal profile on the z-grid: each z-slice is eroded/dilated to a whole number of cells, so the wall is approximated by discrete steps rather than a continuous slope. Enabling <span class="pre">`subpixel_smoothing`</span> removes this staircasing: the fill fraction is then computed per z-slice on the laterally offset footprint, giving a sub-cell-accurate slanted face whose interface normal tilts with the wall (issue \#373).

</div>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">subpixel_full_tensor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a href="#fdtdx.GDSLayerSpec.subpixel_full_tensor" class="headerlink" title="Link to this definition">#</a>  
Keep the full 9-component smoothing tensor (accurate for tilted sidewalls, ~3x heavier) instead of the default cheap 3-component diagonal. See <span class="pre">`subpixel_full_tensor`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">subpixel_smoothing</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">False</span>*<a href="#fdtdx.GDSLayerSpec.subpixel_smoothing" class="headerlink" title="Link to this definition">#</a>  
Enable sub-pixel dielectric smoothing for this layer (see <span class="pre">`subpixel_smoothing`</span>). When <span class="pre">`True`</span> the layer is voxelised with an analytic fill fraction (supersampled footprint x fractional z-coverage of the top/bottom faces) and the assembler builds a 2nd-order-accurate anisotropic effective permittivity at the interface cells. Removes the staircasing of both the in-plane polygon edges and the horizontal layer faces on the Yee grid. Defaults to a cheap 3-component diagonal tensor (exact for axis-aligned interfaces); set <span class="pre">`subpixel_full_tensor`</span> for the full 9-component tensor.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">z_base</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0.0</span>*<a href="#fdtdx.GDSLayerSpec.z_base" class="headerlink" title="Link to this definition">#</a>  
Distance from the simulation volume bottom face to the base of this layer, in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">gds_layer</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.GDSLayerSpec.gds_layer" class="headerlink" title="Link to this definition">#</a>  
GDS layer number.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">material_name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.GDSLayerSpec.material_name" class="headerlink" title="Link to this definition">#</a>  
Key into the materials dictionary to use for this layer.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerSpec.</span></span><span class="sig-name descname"><span class="pre">thickness</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.GDSLayerSpec.thickness" class="headerlink" title="Link to this definition">#</a>  
Layer thickness in metres.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
