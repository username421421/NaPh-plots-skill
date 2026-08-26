<div id="fdtdx-gdslayerobject" class="section">

# fdtdx.GDSLayerObject<a href="#fdtdx-gdslayerobject" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">GDSLayerObject</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">partial_real_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_real_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_grid_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">color</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">Color(r=0.8470588235294118,</span> <span class="pre">g=0.8627450980392157,</span> <span class="pre">b=0.8392156862745098)</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_random_real_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">max_random_grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">placement_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">materials</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">subpixel_smoothing</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">subpixel_full_tensor</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">polygons</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">gds_center</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">material_name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">thickness</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">sidewall_angle</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">90.0</span></span>*, *<span class="n"><span class="pre">reference_plane</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'bottom'</span></span>*, *<span class="n"><span class="pre">fill_supersample</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerObject" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerObject" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`StaticMultiMaterialObject`</span>

A simulation object built from a set of GDS polygons extruded along one axis.

Each instance represents one GDS layer (layer/datatype pair) extruded uniformly along <span class="pre">`axis`</span>. The cross-sectional shape is described by <span class="pre">`polygons`</span>, given in GDS coordinate space (metres). The mapping from GDS space to the local grid is controlled by <span class="pre">`gds_center`</span>, which gives the GDS coordinate that coincides with the x/y centre of the placed object. For example, <span class="pre">`gds_center=(0.0,`</span>` `<span class="pre">`0.0)`</span> maps the GDS origin to the object’s centre, while <span class="pre">`gds_center=(500e-9,`</span>` `<span class="pre">`0.0)`</span> shifts the layout 500 nm to the left.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.GDSLayerObject.axis" class="reference internal" title="fdtdx.GDSLayerObject.axis"><span class="pre"><code class="sourceCode python">axis</code></span></a>

- <a href="#fdtdx.GDSLayerObject.color" class="reference internal" title="fdtdx.GDSLayerObject.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.GDSLayerObject.fill_supersample" class="reference internal" title="fdtdx.GDSLayerObject.fill_supersample"><span class="pre"><code class="sourceCode python">fill_supersample</code></span></a>

- <a href="#fdtdx.GDSLayerObject.gds_center" class="reference internal" title="fdtdx.GDSLayerObject.gds_center"><span class="pre"><code class="sourceCode python">gds_center</code></span></a>

- <a href="#fdtdx.GDSLayerObject.grid_shape" class="reference internal" title="fdtdx.GDSLayerObject.grid_shape"><span class="pre"><code class="sourceCode python">grid_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.grid_slice" class="reference internal" title="fdtdx.GDSLayerObject.grid_slice"><span class="pre"><code class="sourceCode python">grid_slice</code></span></a>

- <a href="#fdtdx.GDSLayerObject.grid_slice_tuple" class="reference internal" title="fdtdx.GDSLayerObject.grid_slice_tuple"><span class="pre"><code class="sourceCode python">grid_slice_tuple</code></span></a>

- <a href="#fdtdx.GDSLayerObject.horizontal_axis" class="reference internal" title="fdtdx.GDSLayerObject.horizontal_axis"><span class="pre"><code class="sourceCode python">horizontal_axis</code></span></a>

- <a href="#fdtdx.GDSLayerObject.material_name" class="reference internal" title="fdtdx.GDSLayerObject.material_name"><span class="pre"><code class="sourceCode python">material_name</code></span></a>

- <a href="#fdtdx.GDSLayerObject.materials" class="reference internal" title="fdtdx.GDSLayerObject.materials"><span class="pre"><code class="sourceCode python">materials</code></span></a>

- <a href="#fdtdx.GDSLayerObject.max_random_grid_offsets" class="reference internal" title="fdtdx.GDSLayerObject.max_random_grid_offsets"><span class="pre"><code class="sourceCode python">max_random_grid_offsets</code></span></a>

- <a href="#fdtdx.GDSLayerObject.max_random_real_offsets" class="reference internal" title="fdtdx.GDSLayerObject.max_random_real_offsets"><span class="pre"><code class="sourceCode python">max_random_real_offsets</code></span></a>

- <a href="#fdtdx.GDSLayerObject.name" class="reference internal" title="fdtdx.GDSLayerObject.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.GDSLayerObject.partial_grid_shape" class="reference internal" title="fdtdx.GDSLayerObject.partial_grid_shape"><span class="pre"><code class="sourceCode python">partial_grid_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.partial_real_position" class="reference internal" title="fdtdx.GDSLayerObject.partial_real_position"><span class="pre"><code class="sourceCode python">partial_real_position</code></span></a>

- <a href="#fdtdx.GDSLayerObject.partial_real_shape" class="reference internal" title="fdtdx.GDSLayerObject.partial_real_shape"><span class="pre"><code class="sourceCode python">partial_real_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.placement_order" class="reference internal" title="fdtdx.GDSLayerObject.placement_order"><span class="pre"><code class="sourceCode python">placement_order</code></span></a>

- <a href="#fdtdx.GDSLayerObject.polygons" class="reference internal" title="fdtdx.GDSLayerObject.polygons"><span class="pre"><code class="sourceCode python">polygons</code></span></a>

- <a href="#fdtdx.GDSLayerObject.real_shape" class="reference internal" title="fdtdx.GDSLayerObject.real_shape"><span class="pre"><code class="sourceCode python">real_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.reference_plane" class="reference internal" title="fdtdx.GDSLayerObject.reference_plane"><span class="pre"><code class="sourceCode python">reference_plane</code></span></a>

- <a href="#fdtdx.GDSLayerObject.sidewall_angle" class="reference internal" title="fdtdx.GDSLayerObject.sidewall_angle"><span class="pre"><code class="sourceCode python">sidewall_angle</code></span></a>

- <a href="#fdtdx.GDSLayerObject.subpixel_full_tensor" class="reference internal" title="fdtdx.GDSLayerObject.subpixel_full_tensor"><span class="pre"><code class="sourceCode python">subpixel_full_tensor</code></span></a>

- <a href="#fdtdx.GDSLayerObject.subpixel_smoothing" class="reference internal" title="fdtdx.GDSLayerObject.subpixel_smoothing"><span class="pre"><code class="sourceCode python">subpixel_smoothing</code></span></a>

- <a href="#fdtdx.GDSLayerObject.thickness" class="reference internal" title="fdtdx.GDSLayerObject.thickness"><span class="pre"><code class="sourceCode python">thickness</code></span></a>

- <a href="#fdtdx.GDSLayerObject.vertical_axis" class="reference internal" title="fdtdx.GDSLayerObject.vertical_axis"><span class="pre"><code class="sourceCode python">vertical_axis</code></span></a>

Methods

- <a href="#fdtdx.GDSLayerObject.apply" class="reference internal" title="fdtdx.GDSLayerObject.apply"><span class="pre"><code class="sourceCode python"><span class="bu">apply</span></code></span></a>

- <a href="#fdtdx.GDSLayerObject.aset" class="reference internal" title="fdtdx.GDSLayerObject.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.GDSLayerObject.check_overlap" class="reference internal" title="fdtdx.GDSLayerObject.check_overlap"><span class="pre"><code class="sourceCode python">check_overlap</code></span></a>

- <a href="#fdtdx.GDSLayerObject.extend_to" class="reference internal" title="fdtdx.GDSLayerObject.extend_to"><span class="pre"><code class="sourceCode python">extend_to</code></span></a>

- <a href="#fdtdx.GDSLayerObject.face_to_face_negative_direction" class="reference internal" title="fdtdx.GDSLayerObject.face_to_face_negative_direction"><span class="pre"><code class="sourceCode python">face_to_face_negative_direction</code></span></a>

- <a href="#fdtdx.GDSLayerObject.face_to_face_positive_direction" class="reference internal" title="fdtdx.GDSLayerObject.face_to_face_positive_direction"><span class="pre"><code class="sourceCode python">face_to_face_positive_direction</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_class_fields" class="reference internal" title="fdtdx.GDSLayerObject.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_fill_fraction_for_shape" class="reference internal" title="fdtdx.GDSLayerObject.get_fill_fraction_for_shape"><span class="pre"><code class="sourceCode python">get_fill_fraction_for_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_geometry_size_hint" class="reference internal" title="fdtdx.GDSLayerObject.get_geometry_size_hint"><span class="pre"><code class="sourceCode python">get_geometry_size_hint</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_interface_normal_for_shape" class="reference internal" title="fdtdx.GDSLayerObject.get_interface_normal_for_shape"><span class="pre"><code class="sourceCode python">get_interface_normal_for_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_material_mapping" class="reference internal" title="fdtdx.GDSLayerObject.get_material_mapping"><span class="pre"><code class="sourceCode python">get_material_mapping</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_public_fields" class="reference internal" title="fdtdx.GDSLayerObject.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.GDSLayerObject.get_voxel_mask_for_shape" class="reference internal" title="fdtdx.GDSLayerObject.get_voxel_mask_for_shape"><span class="pre"><code class="sourceCode python">get_voxel_mask_for_shape</code></span></a>

- <a href="#fdtdx.GDSLayerObject.place_above" class="reference internal" title="fdtdx.GDSLayerObject.place_above"><span class="pre"><code class="sourceCode python">place_above</code></span></a>

- <a href="#fdtdx.GDSLayerObject.place_at_center" class="reference internal" title="fdtdx.GDSLayerObject.place_at_center"><span class="pre"><code class="sourceCode python">place_at_center</code></span></a>

- <a href="#fdtdx.GDSLayerObject.place_below" class="reference internal" title="fdtdx.GDSLayerObject.place_below"><span class="pre"><code class="sourceCode python">place_below</code></span></a>

- <a href="#fdtdx.GDSLayerObject.place_on_grid" class="reference internal" title="fdtdx.GDSLayerObject.place_on_grid"><span class="pre"><code class="sourceCode python">place_on_grid</code></span></a>

- <a href="#fdtdx.GDSLayerObject.place_relative_to" class="reference internal" title="fdtdx.GDSLayerObject.place_relative_to"><span class="pre"><code class="sourceCode python">place_relative_to</code></span></a>

- <a href="#fdtdx.GDSLayerObject.same_position" class="reference internal" title="fdtdx.GDSLayerObject.same_position"><span class="pre"><code class="sourceCode python">same_position</code></span></a>

- <a href="#fdtdx.GDSLayerObject.same_position_and_size" class="reference internal" title="fdtdx.GDSLayerObject.same_position_and_size"><span class="pre"><code class="sourceCode python">same_position_and_size</code></span></a>

- <a href="#fdtdx.GDSLayerObject.same_size" class="reference internal" title="fdtdx.GDSLayerObject.same_size"><span class="pre"><code class="sourceCode python">same_size</code></span></a>

- <a href="#fdtdx.GDSLayerObject.set_grid_coordinates" class="reference internal" title="fdtdx.GDSLayerObject.set_grid_coordinates"><span class="pre"><code class="sourceCode python">set_grid_coordinates</code></span></a>

- <a href="#fdtdx.GDSLayerObject.size_relative_to" class="reference internal" title="fdtdx.GDSLayerObject.size_relative_to"><span class="pre"><code class="sourceCode python">size_relative_to</code></span></a>

- <a href="#fdtdx.GDSLayerObject.validate_placement" class="reference internal" title="fdtdx.GDSLayerObject.validate_placement"><span class="pre"><code class="sourceCode python">validate_placement</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a href="#fdtdx.GDSLayerObject.axis" class="headerlink" title="Link to this definition">#</a>  
The extrusion axis (0=x, 1=y, 2=z).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Color</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.GDSLayerObject.color" class="headerlink" title="Link to this definition">#</a>  
the color of the material

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">fill_supersample</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a href="#fdtdx.GDSLayerObject.fill_supersample" class="headerlink" title="Link to this definition">#</a>  
Number of sub-samples per axis used to estimate the in-plane fill fraction for sub-pixel smoothing (see <a href="#fdtdx.GDSLayerObject.get_fill_fraction_for_shape" class="reference internal" title="fdtdx.GDSLayerObject.get_fill_fraction_for_shape"><span class="pre"><code class="sourceCode python">get_fill_fraction_for_shape()</code></span></a>). Higher values give a more accurate fill fraction / interface normal at a quadratic cost in this (CPU-side, one-time) rasterization step.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">gds_center</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float\]</span>*<a href="#fdtdx.GDSLayerObject.gds_center" class="headerlink" title="Link to this definition">#</a>  
GDS coordinate (horizontal, vertical) in metres that coincides with the x/y centre of the placed object.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">grid_shape</span></span><a href="#fdtdx.GDSLayerObject.grid_shape" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">grid_slice</span></span><a href="#fdtdx.GDSLayerObject.grid_slice" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">grid_slice_tuple</span></span><a href="#fdtdx.GDSLayerObject.grid_slice_tuple" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">horizontal_axis</span></span><a href="#fdtdx.GDSLayerObject.horizontal_axis" class="headerlink" title="Link to this definition">#</a>  
Cross-section axis that is not the extrusion axis and not the vertical axis.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">material_name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.GDSLayerObject.material_name" class="headerlink" title="Link to this definition">#</a>  
Key into the materials dictionary used for this object.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">materials</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">dict\[str,</span> <span class="pre">Material\]</span>*<a href="#fdtdx.GDSLayerObject.materials" class="headerlink" title="Link to this definition">#</a>  
the static material

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">max_random_grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[int,</span> <span class="pre">int,</span> <span class="pre">int\]</span>*<a href="#fdtdx.GDSLayerObject.max_random_grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in grid coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">max_random_real_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span>*<a href="#fdtdx.GDSLayerObject.max_random_real_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in real coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.GDSLayerObject.name" class="headerlink" title="Link to this definition">#</a>  
Unique identifier for the object. Automatically enforced to be unique through the UniqueName validator. The user can also set a name manually.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">partial_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialGridShape3D</span>*<a href="#fdtdx.GDSLayerObject.partial_grid_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in grid coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">partial_real_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.GDSLayerObject.partial_real_position" class="headerlink" title="Link to this definition">#</a>  
The object’s position in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">partial_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.GDSLayerObject.partial_real_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">placement_order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a href="#fdtdx.GDSLayerObject.placement_order" class="headerlink" title="Link to this definition">#</a>  
Field placeholder for autoinit.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">polygons</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence\[np.ndarray\]</span>*<a href="#fdtdx.GDSLayerObject.polygons" class="headerlink" title="Link to this definition">#</a>  
Sequence of (N, 2) vertex arrays for each polygon, in GDS metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">real_shape</span></span><a href="#fdtdx.GDSLayerObject.real_shape" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by this object’s placed grid slice.

The value is derived from <span class="pre">`SimulationConfig.grid`</span> when available. That keeps object geometry tied to physical edge coordinates instead of a global scalar resolution. During early placement, before a concrete grid has been attached to the config, the legacy uniform-resolution fallback is still used for compatibility.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">reference_plane</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal\['bottom',</span> <span class="pre">'middle',</span> <span class="pre">'top'\]</span>*<a href="#fdtdx.GDSLayerObject.reference_plane" class="headerlink" title="Link to this definition">#</a>  
<span class="pre">`"bottom"`</span>, <span class="pre">`"middle"`</span> or <span class="pre">`"top"`</span>.

Type<span class="colon">:</span>  
Face that keeps the nominal footprint

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">sidewall_angle</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.GDSLayerObject.sidewall_angle" class="headerlink" title="Link to this definition">#</a>  
Sidewall angle in **degrees** between the wall and the substrate (foundry convention). <span class="pre">`90.0`</span> extrudes a vertical wall; other values produce a trapezoidal cross-section by eroding (angle <span class="pre">`<`</span>` `<span class="pre">`90`</span>) or dilating (angle <span class="pre">`>`</span>` `<span class="pre">`90`</span>) each z-slice laterally by an offset <span class="pre">`offset(z)`</span>` `<span class="pre">`=`</span>` `<span class="pre">`(z`</span>` `<span class="pre">`-`</span>` `<span class="pre">`z_ref)`</span>` `<span class="pre">`*`</span>` `<span class="pre">`tan(90deg`</span>` `<span class="pre">`-`</span>` `<span class="pre">`sidewall_angle)`</span> measured from <span class="pre">`reference_plane`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">subpixel_full_tensor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.GDSLayerObject.subpixel_full_tensor" class="headerlink" title="Link to this definition">#</a>  
Selects the smoothing tensor representation when <span class="pre">`subpixel_smoothing`</span> is on. <span class="pre">`False`</span> (default) keeps only the DIAGONAL of the Farjadpour tensor (<span class="pre">`eps_ii`</span>` `<span class="pre">`=`</span>` `<span class="pre">`eps_bar`</span>` `<span class="pre">`-`</span>` `<span class="pre">`(eps_bar`</span>` `<span class="pre">`-`</span>` `<span class="pre">`eps_h)*n_i**2`</span>), allocating a cheap 3-component array that runs on the elementwise Yee update. This is EXACT for axis-aligned interfaces (their normal lies on one axis, so the off-diagonal terms vanish) and is the recommended production path for Manhattan geometries. <span class="pre">`True`</span> allocates the full 9-component tensor (keeps the off-diagonal <span class="pre">`-(eps_bar`</span>` `<span class="pre">`-`</span>` `<span class="pre">`eps_h)*n_i*n_j`</span> terms), which is more accurate for tilted interfaces (slanted sidewalls, diagonal edges) but ~3x heavier per step and forces the anisotropic update kernel. Ignored when <span class="pre">`subpixel_smoothing`</span> is False.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">subpixel_smoothing</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.GDSLayerObject.subpixel_smoothing" class="headerlink" title="Link to this definition">#</a>  
Enable sub-pixel (sub-cell) dielectric smoothing for this object. When <span class="pre">`True`</span> the assembler replaces the binary voxel occupancy with an analytic fill-fraction and builds a smoothed, anisotropic (full 3x3 tensor) effective permittivity at interface cells following Farjadpour et al. (Meep): arithmetic mean of <span class="pre">`eps`</span> for the field components tangential to the interface and harmonic mean of <span class="pre">`eps`</span> for the component normal to it. This removes the first-order staircasing error of the Yee grid at strong dielectric jumps (2nd-order accuracy). Forces the whole simulation to allocate an anisotropic permittivity tensor (3-component diagonal by default, or a full 9-component tensor when <span class="pre">`subpixel_full_tensor`</span> is set). Requires the object to provide a fractional <span class="pre">`get_fill_fraction_for_shape`</span> (the default falls back to the binary mask, which still yields a valid but only cell-wide normal). See issue \#373.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">thickness</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.GDSLayerObject.thickness" class="headerlink" title="Link to this definition">#</a>  
Extrusion thickness in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">vertical_axis</span></span><a href="#fdtdx.GDSLayerObject.vertical_axis" class="headerlink" title="Link to this definition">#</a>  
Second cross-section axis perpendicular to the extrusion axis.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">apply</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.apply" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">check_overlap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.check_overlap" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">extend_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.extend_to" class="headerlink" title="Link to this definition">#</a>  
Creates a SizeExtensionConstraint that extends this object along a specified axis until it reaches another object or the simulation boundary. The extension can be in either positive or negative direction.

Parameters<span class="colon">:</span>  
- **other** (*str* *\|* *None*) – Target object to extend to, or None to extend to simulation boundary

- **axis** (*int*) – Which axis to extend along (0, 1, or 2)

- **direction** (*Literal\["+",* *"-"\]*) – Direction to extend in (‘+’ or ‘-‘)

- **other_position** (*float* *\|* *None,* *optional*) – Relative position on target object (-1 to 1) to extend to. If None, defaults to the corresponding side (-1 for ‘+’ direction, 1 for ‘-’ direction). Defaults to None.

- **offset** (*float,* *optional*) – Additional offset in meters to apply after extension. Ignored when extending to simulation boundary. Defaults to zero.

- **grid_offset** (*int,* *optional*) – Additional offset in Yee-grid voxels to apply after extension. Ignored when extending to simulation boundary. Defaults to zero.

Returns<span class="colon">:</span>  
Constraint defining how the object extends

Return type<span class="colon">:</span>  
<a href="fdtdx.SizeExtensionConstraint.html#fdtdx.SizeExtensionConstraint" class="reference internal" title="fdtdx.SizeExtensionConstraint">SizeExtensionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">face_to_face_negative_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.face_to_face_negative_direction" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that places this object facing another object in the negative direction of specified axes. The objects will touch at their facing boundaries unless margins are specified.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int*) – Either a single integer or a tuple describing which axes to align on

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional margins in meters between the facing surfaces. Must have same length as axes. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional margins in Yee-grid voxels between the facing surfaces. Must have same length as axes. If None, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Position constraint aligning objects face-to-face in negative direction

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">face_to_face_positive_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.face_to_face_positive_direction" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that places this object facing another object in the positive direction of specified axes. The objects will touch at their facing boundaries unless margins are specified.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int*) – Either a single integer or a tuple describing which axes to align on

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional margins in meters between the facing surfaces. Must have same length as axes. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional margins in Yee-grid voxels between the facing surfaces. Must have same length as axes. If None, no margin is used. Defaults to None

Returns<span class="colon">:</span>  
Position constraint aligning objects face-to-face in positive direction

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_fill_fraction_for_shape</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerObject.get_fill_fraction_for_shape" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerObject.get_fill_fraction_for_shape" class="headerlink" title="Link to this definition">#</a>  
Analytic per-cell fill fraction of the extruded (optionally trapezoidal) polygon, in <span class="pre">`[0,`</span>` `<span class="pre">`1]`</span>.

The fraction is the product of an in-plane footprint coverage and the z-extent coverage:

- <span class="pre">`f_xy`</span> — the in-plane fraction of each cell covered by the polygon footprint, estimated by super-sampling <span class="pre">`polygon_to_mask_at_points()`</span> on an <span class="pre">`N`</span>` `<span class="pre">`x`</span>` `<span class="pre">`N`</span> grid inside every cell; and

- <span class="pre">`f_z`</span> — the fraction of each z-cell overlapped by the layer’s physical z-extent <span class="pre">`[z_base,`</span>` `<span class="pre">`z_base`</span>` `<span class="pre">`+`</span>` `<span class="pre">`thickness]`</span> (partial coverage at the top and bottom faces).

When <span class="pre">`sidewall_angle`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`90`</span> the footprint shrinks/grows with height, so <span class="pre">`f_xy`</span> is recomputed per z-slice on the laterally offset polygon (<span class="pre">`offset(z)`</span>` `<span class="pre">`=`</span>` `<span class="pre">`(z`</span>` `<span class="pre">`-`</span>` `<span class="pre">`z_ref)`</span>` `<span class="pre">`*`</span>` `<span class="pre">`tan(90deg`</span>` `<span class="pre">`-`</span>` `<span class="pre">`angle)`</span>, matching <span class="pre">`_extrude_with_sidewall()`</span>), giving a sub-cell-accurate trapezoidal profile whose interface normal (recovered from the fill gradient) tilts with the wall. For a vertical wall, or when the total lateral taper stays below half a cell (the common sub-cell case), the cheaper separable <span class="pre">`f_xy(x,`</span>` `<span class="pre">`y)`</span>` `<span class="pre">`*`</span>` `<span class="pre">`f_z(z)`</span> form on the nominal footprint is used — it is identical there.

Returns<span class="colon">:</span>  
Float array of shape <span class="pre">`self.grid_shape`</span> with values in <span class="pre">`[0,`</span>` `<span class="pre">`1]`</span>.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_geometry_size_hint</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerObject.get_geometry_size_hint" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerObject.get_geometry_size_hint" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span> \| <span class="pre">`None`</span>, <span class="pre">`float`</span> \| <span class="pre">`None`</span>, <span class="pre">`float`</span> \| <span class="pre">`None`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_interface_normal_for_shape</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.get_interface_normal_for_shape" class="headerlink" title="Link to this definition">#</a>  
Return a per-cell unit interface normal derived from the fill-fraction gradient.

The normal is <span class="pre">`n`</span>` `<span class="pre">`=`</span>` `<span class="pre">`-grad(fill)`</span>` `<span class="pre">`/`</span>` `<span class="pre">`|grad(fill)|`</span> (the sign is irrelevant downstream because only the symmetric outer product <span class="pre">`n`</span>` `<span class="pre">`⊗`</span>` `<span class="pre">`n`</span> is used). The gradient is taken with the object’s physical cell pitch on each axis, so the direction is geometrically correct on anisotropic grids. Cells away from an interface (<span class="pre">`|grad(fill)|`</span>` `<span class="pre">`~`</span>` `<span class="pre">`0`</span>) get a zero normal, which makes the smoothed tensor collapse back to the isotropic bulk value. Computed in NumPy at initialisation (static geometry, not a traced quantity).

Returns<span class="colon">:</span>  
Float array of shape <span class="pre">`(3,`</span>` `<span class="pre">`*self.grid_shape)`</span> with the per-cell unit normal.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_material_mapping</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerObject.get_material_mapping" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerObject.get_material_mapping" class="headerlink" title="Link to this definition">#</a>  
Return an integer array filled with the index of <span class="pre">`material_name`</span> in the sorted material list.

Returns<span class="colon">:</span>  
Integer array of shape <span class="pre">`self.grid_shape`</span> where every voxel has the same value — the position of <span class="pre">`material_name`</span> in the sorted material name list.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">get_voxel_mask_for_shape</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSLayerObject.get_voxel_mask_for_shape" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSLayerObject.get_voxel_mask_for_shape" class="headerlink" title="Link to this definition">#</a>  
Compute a 3-D boolean mask for the extruded polygon shape.

When <span class="pre">`sidewall_angle`</span> is 90 deg the polygon footprint is extruded vertically and every z-slice is identical. Otherwise each z-slice is offset laterally by <span class="pre">`(z_center`</span>` `<span class="pre">`-`</span>` `<span class="pre">`z_ref)`</span>` `<span class="pre">`*`</span>` `<span class="pre">`tan(90deg`</span>` `<span class="pre">`-`</span>` `<span class="pre">`sidewall_angle)`</span> (erosion for an angle \< 90, dilation for an angle \> 90), giving a trapezoidal cross-section that approximates <span class="pre">`Tidy3D.PolySlab`</span> with the equivalent angle / <span class="pre">`reference_plane`</span>. The per-slice offset is applied in physical (metre) units via a Euclidean distance transform; on a non-uniform cross-section grid it uses a constant per-axis pitch (the minimum cell width), which is an approximation.

<div class="admonition note">

Note

Only <span class="pre">`axis=2`</span> (z-extrusion) is supported. GDS layouts encode x/y coordinates only, so extruding along x or y would require a z-coordinate that does not exist in the GDS file.

</div>

Returns<span class="colon">:</span>  
Boolean array of shape <span class="pre">`self.grid_shape`</span>.

Return type<span class="colon">:</span>  
jax.Array

Raises<span class="colon">:</span>  
**ValueError** – If <span class="pre">`self.axis`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`2`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">place_above</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.place_above" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that places this object above another object along the z-axis. This is a convenience wrapper around face_to_face_positive_direction() for axis 2 (z-axis).

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional vertical margins in meters between objects. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional vertical margins in Yee-grid voxels between objects. If None, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Position constraint placing this object above the other

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">place_at_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.place_at_center" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that centers this object relative to another object along specified axes. This is a convenience wrapper around place_relative_to() with default positions at the center (0).

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to center on. Defaults to all axes (0, 1, 2).

- **own_positions** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Relative positions on this object (-1 to 1). If None, uses center (0). Defaults to None.

- **other_positions** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Relative positions on other object (-1 to 1). If None, uses center (0). Defaults to None.

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional margins in meters between objects. Must have same length as axes. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional margins in Yee-grid voxels between objects. Must have same length as axes. If None, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Position constraint centering objects relative to each other

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">place_below</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.place_below" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that places this object below another object along the z-axis. This is a convenience wrapper around face_to_face_negative_direction() for axis 2 (z-axis).

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional vertical margins in meters between objects. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional vertical margins in Yee-grid voxels between objects. If None, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Position constraint placing this object below the other

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">place_on_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice_tuple</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.place_on_grid" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">place_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">own_positions</span></span>*, *<span class="n"><span class="pre">other_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.place_relative_to" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionalConstraint between two objects. The constraint is defined by anchor points on both objects, which are constrained to be at the same position. Anchors are defined in relative coordinates, i.e. a position of -1 is the left object boundary in the respective axis and a position of +1 the right boundary.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int*) – Eiter a single integer or a tuple describing the axes of the constraints

- **own_positions** (*tuple\[float,* *...\]* *\|* *float*) – The positions of the own anchor in the axes. Must have the same lengths as axes

- **other_positions** (*tuple\[float,* *...\]* *\|* *float*) – The positions of the other objects’ anchor in the axes. Must have the same lengths as axes

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – The margins between the anchors of both objects in meters. Must have the same lengths as axes. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – The margins between the anchors of both objects in Yee-grid voxels. Must have the same lengths as axes. If none, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Positional constraint between this object and the other

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">same_position</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.same_position" class="headerlink" title="Link to this definition">#</a>  
Creates a PositionConstraint that places this object at the same position as another object. This is a convenience wrapper around place_at_center() for more intuitive naming.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match position on. Defaults to all axes (0, 1, 2).

- **own_positions** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Relative positions on this object (-1 to 1). If None, uses center (0). Defaults to None.

- **other_positions** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Relative positions on other object (-1 to 1). If None, uses center (0). Defaults to None.

- **margins** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional margins in meters between objects. Must have same length as axes. If None, no margin is used. Defaults to None.

- **grid_margins** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional margins in Yee-grid voxels between objects. Must have same length as axes. If None, no margin is used. Defaults to None.

Returns<span class="colon">:</span>  
Position constraint placing objects at the same position

Return type<span class="colon">:</span>  
<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">same_position_and_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.same_position_and_size" class="headerlink" title="Link to this definition">#</a>  
Creates both position and size constraints to make this object match another object’s position and size. This is a convenience wrapper combining place_at_center() and same_size().

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match. Defaults to all axes (0, 1, 2).

Returns<span class="colon">:</span>  
Position and size constraints for matching objects

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>, <a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">same_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.same_size" class="headerlink" title="Link to this definition">#</a>  
Creates a SizeConstraint that makes this object the same size as another object along specified axes. This is a convenience wrapper around size_relative_to() with proportions set to 1.0.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes should have the same size. Defaults to all axes (0, 1, 2).

- **offsets** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional size offsets in meters to apply. Must have same length as axes. If None, no offset is used. Defaults to None.

- **grid_offsets** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional size offsets in Yee-grid voxels to apply. Must have same length as axes. If None, no offset is used. Defaults to None.

Returns<span class="colon">:</span>  
Size constraint ensuring equal sizes between objects

Return type<span class="colon">:</span>  
<a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">set_grid_coordinates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.set_grid_coordinates" class="headerlink" title="Link to this definition">#</a>  
Creates a GridCoordinateConstraint that forces specific sides of this object to align with given grid coordinates. Used for precise positioning in the discretized simulation space.

Parameters<span class="colon">:</span>  
- **axes** (*tuple\[int,* *...\]* *\|* *int*) – Either a single integer or a tuple describing which axes to constrain

- **sides** (*tuple\[Literal\["+",* *"-"\],* *...\]* *\|* *Literal\["+",* *"-"\]*) – Either a single string or a tuple of strings (‘+’ or ‘-’) indicating which side of each axis to constrain. Must have same length as axes.

- **coordinates** (*tuple\[int,* *...\]* *\|* *int*) – Either a single integer or a tuple of integers specifying the grid coordinates to align with. Must have same length as axes.

Returns<span class="colon">:</span>  
Constraint forcing alignment with specific grid coordinates

Return type<span class="colon">:</span>  
<a href="fdtdx.GridCoordinateConstraint.html#fdtdx.GridCoordinateConstraint" class="reference internal" title="fdtdx.GridCoordinateConstraint">GridCoordinateConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">size_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">proportions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.size_relative_to" class="headerlink" title="Link to this definition">#</a>  
Creates a SizeConstraint between two objects. The constraint defines the size of this object relative to another object, allowing for proportional scaling and offsets in specified axes.

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int*) – Either a single integer or a tuple describing which axes of this object to constrain.

- **other_axes** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Either a single integer or a tuple describing which axes of the other object to reference. If None, uses the same axes as specified in ‘axes’. Defaults to None.

- **proportions** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Scale factors to apply to the other object’s dimensions. Must have same length as axes. If None, uses 1.0 (same size). Defaults to None.

- **offsets** (*tuple\[float,* *...\]* *\|* *float* *\|* *None,* *optional*) – Additional size offsets in meters to apply after scaling. Must have same length as axes. If None, no offset is used. Defaults to None.

- **grid_offsets** (*tuple\[int,* *...\]* *\|* *int* *\|* *None,* *optional*) – Additional size offsets in Yee-grid voxels to apply after scaling. Must have same length as axes. If None, no offset is used. Defaults to None.

Returns<span class="colon">:</span>  
Size constraint between this object and the other

Return type<span class="colon">:</span>  
<a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSLayerObject.</span></span><span class="sig-name descname"><span class="pre">validate_placement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GDSLayerObject.validate_placement" class="headerlink" title="Link to this definition">#</a>  
Validate this object against the fully-resolved object container.

Called once by <span class="pre">`place_objects()`</span> after every object has been placed and the container built, giving cross-object checks (e.g. a source verifying the boundaries around it) a place to run. Returns a list of human-readable error messages; an empty list means the placement is valid. The default implementation performs no checks.

Parameters<span class="colon">:</span>  
**objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – The fully-resolved container of all placed objects (exposes <span class="pre">`.volume`</span>, <span class="pre">`.boundary_objects`</span>, <span class="pre">`.sources`</span>, …).

Returns<span class="colon">:</span>  
Error messages describing invalid placement, or <span class="pre">`[]`</span>.

Return type<span class="colon">:</span>  
list\[str\]

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
