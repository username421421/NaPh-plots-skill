<div id="fdtdx-device" class="section">

# fdtdx.Device<a href="#fdtdx-device" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Device</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">partial_real_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_real_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_grid_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">color</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">Color(r=1.0,</span> <span class="pre">g=0.8196078431372549,</span> <span class="pre">b=0.8745098039215686)</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_random_real_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">max_random_grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">placement_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">materials</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">param_transforms</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">partial_voxel_grid_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_voxel_real_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">use_etching</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/device.html#Device" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Device" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`OrderableObject`</span>, <span class="pre">`ABC`</span>

Abstract base class for devices with optimizable permittivity distributions.

This class defines the common interface and functionality for both discrete and continuous devices that can be optimized through gradient-based methods.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Device.color" class="reference internal" title="fdtdx.Device.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.Device.grid_shape" class="reference internal" title="fdtdx.Device.grid_shape"><span class="pre"><code class="sourceCode python">grid_shape</code></span></a>

- <a href="#fdtdx.Device.grid_slice" class="reference internal" title="fdtdx.Device.grid_slice"><span class="pre"><code class="sourceCode python">grid_slice</code></span></a>

- <a href="#fdtdx.Device.grid_slice_tuple" class="reference internal" title="fdtdx.Device.grid_slice_tuple"><span class="pre"><code class="sourceCode python">grid_slice_tuple</code></span></a>

- <a href="#fdtdx.Device.materials" class="reference internal" title="fdtdx.Device.materials"><span class="pre"><code class="sourceCode python">materials</code></span></a>

- <a href="#fdtdx.Device.matrix_voxel_grid_shape" class="reference internal" title="fdtdx.Device.matrix_voxel_grid_shape"><span class="pre"><code class="sourceCode python">matrix_voxel_grid_shape</code></span></a>

- <a href="#fdtdx.Device.max_random_grid_offsets" class="reference internal" title="fdtdx.Device.max_random_grid_offsets"><span class="pre"><code class="sourceCode python">max_random_grid_offsets</code></span></a>

- <a href="#fdtdx.Device.max_random_real_offsets" class="reference internal" title="fdtdx.Device.max_random_real_offsets"><span class="pre"><code class="sourceCode python">max_random_real_offsets</code></span></a>

- <a href="#fdtdx.Device.name" class="reference internal" title="fdtdx.Device.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.Device.output_type" class="reference internal" title="fdtdx.Device.output_type"><span class="pre"><code class="sourceCode python">output_type</code></span></a>

- <a href="#fdtdx.Device.param_transforms" class="reference internal" title="fdtdx.Device.param_transforms"><span class="pre"><code class="sourceCode python">param_transforms</code></span></a>

- <a href="#fdtdx.Device.partial_grid_shape" class="reference internal" title="fdtdx.Device.partial_grid_shape"><span class="pre"><code class="sourceCode python">partial_grid_shape</code></span></a>

- <a href="#fdtdx.Device.partial_real_position" class="reference internal" title="fdtdx.Device.partial_real_position"><span class="pre"><code class="sourceCode python">partial_real_position</code></span></a>

- <a href="#fdtdx.Device.partial_real_shape" class="reference internal" title="fdtdx.Device.partial_real_shape"><span class="pre"><code class="sourceCode python">partial_real_shape</code></span></a>

- <a href="#fdtdx.Device.partial_voxel_grid_shape" class="reference internal" title="fdtdx.Device.partial_voxel_grid_shape"><span class="pre"><code class="sourceCode python">partial_voxel_grid_shape</code></span></a>

- <a href="#fdtdx.Device.partial_voxel_real_shape" class="reference internal" title="fdtdx.Device.partial_voxel_real_shape"><span class="pre"><code class="sourceCode python">partial_voxel_real_shape</code></span></a>

- <a href="#fdtdx.Device.placement_order" class="reference internal" title="fdtdx.Device.placement_order"><span class="pre"><code class="sourceCode python">placement_order</code></span></a>

- <a href="#fdtdx.Device.real_shape" class="reference internal" title="fdtdx.Device.real_shape"><span class="pre"><code class="sourceCode python">real_shape</code></span></a>

- <a href="#fdtdx.Device.single_voxel_grid_shape" class="reference internal" title="fdtdx.Device.single_voxel_grid_shape"><span class="pre"><code class="sourceCode python">single_voxel_grid_shape</code></span></a>

- <a href="#fdtdx.Device.single_voxel_real_shape" class="reference internal" title="fdtdx.Device.single_voxel_real_shape"><span class="pre"><code class="sourceCode python">single_voxel_real_shape</code></span></a>

- <a href="#fdtdx.Device.use_etching" class="reference internal" title="fdtdx.Device.use_etching"><span class="pre"><code class="sourceCode python">use_etching</code></span></a>

Methods

- <a href="#fdtdx.Device.apply" class="reference internal" title="fdtdx.Device.apply"><span class="pre"><code class="sourceCode python"><span class="bu">apply</span></code></span></a>

- <a href="#fdtdx.Device.aset" class="reference internal" title="fdtdx.Device.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.Device.check_overlap" class="reference internal" title="fdtdx.Device.check_overlap"><span class="pre"><code class="sourceCode python">check_overlap</code></span></a>

- <a href="#fdtdx.Device.extend_to" class="reference internal" title="fdtdx.Device.extend_to"><span class="pre"><code class="sourceCode python">extend_to</code></span></a>

- <a href="#fdtdx.Device.face_to_face_negative_direction" class="reference internal" title="fdtdx.Device.face_to_face_negative_direction"><span class="pre"><code class="sourceCode python">face_to_face_negative_direction</code></span></a>

- <a href="#fdtdx.Device.face_to_face_positive_direction" class="reference internal" title="fdtdx.Device.face_to_face_positive_direction"><span class="pre"><code class="sourceCode python">face_to_face_positive_direction</code></span></a>

- <a href="#fdtdx.Device.get_class_fields" class="reference internal" title="fdtdx.Device.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.Device.get_public_fields" class="reference internal" title="fdtdx.Device.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.Device.init_params" class="reference internal" title="fdtdx.Device.init_params"><span class="pre"><code class="sourceCode python">init_params</code></span></a>

- <a href="#fdtdx.Device.place_above" class="reference internal" title="fdtdx.Device.place_above"><span class="pre"><code class="sourceCode python">place_above</code></span></a>

- <a href="#fdtdx.Device.place_at_center" class="reference internal" title="fdtdx.Device.place_at_center"><span class="pre"><code class="sourceCode python">place_at_center</code></span></a>

- <a href="#fdtdx.Device.place_below" class="reference internal" title="fdtdx.Device.place_below"><span class="pre"><code class="sourceCode python">place_below</code></span></a>

- <a href="#fdtdx.Device.place_on_grid" class="reference internal" title="fdtdx.Device.place_on_grid"><span class="pre"><code class="sourceCode python">place_on_grid</code></span></a>

- <a href="#fdtdx.Device.place_relative_to" class="reference internal" title="fdtdx.Device.place_relative_to"><span class="pre"><code class="sourceCode python">place_relative_to</code></span></a>

- <a href="#fdtdx.Device.same_position" class="reference internal" title="fdtdx.Device.same_position"><span class="pre"><code class="sourceCode python">same_position</code></span></a>

- <a href="#fdtdx.Device.same_position_and_size" class="reference internal" title="fdtdx.Device.same_position_and_size"><span class="pre"><code class="sourceCode python">same_position_and_size</code></span></a>

- <a href="#fdtdx.Device.same_size" class="reference internal" title="fdtdx.Device.same_size"><span class="pre"><code class="sourceCode python">same_size</code></span></a>

- <a href="#fdtdx.Device.set_grid_coordinates" class="reference internal" title="fdtdx.Device.set_grid_coordinates"><span class="pre"><code class="sourceCode python">set_grid_coordinates</code></span></a>

- <a href="#fdtdx.Device.size_relative_to" class="reference internal" title="fdtdx.Device.size_relative_to"><span class="pre"><code class="sourceCode python">size_relative_to</code></span></a>

- <a href="#fdtdx.Device.validate_placement" class="reference internal" title="fdtdx.Device.validate_placement"><span class="pre"><code class="sourceCode python">validate_placement</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.Color.html#fdtdx.Color" class="reference internal" title="fdtdx.colors.Color"><span class="pre"><code class="sourceCode python">Color</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.Device.color" class="headerlink" title="Link to this definition">#</a>  
Color of the object when plotted. Defaults to XKCD_LIGHT_PINK.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">grid_shape</span></span><a href="#fdtdx.Device.grid_shape" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">grid_slice</span></span><a href="#fdtdx.Device.grid_slice" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">grid_slice_tuple</span></span><a href="#fdtdx.Device.grid_slice_tuple" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">materials</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <a href="fdtdx.Material.html#fdtdx.Material" class="reference internal" title="fdtdx.materials.Material"><span class="pre"><code class="sourceCode python">Material</code></span></a><span class="pre">\]</span>*<a href="#fdtdx.Device.materials" class="headerlink" title="Link to this definition">#</a>  
Dictionary of materials to be used in the device.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">matrix_voxel_grid_shape</span></span><a href="#fdtdx.Device.matrix_voxel_grid_shape" class="headerlink" title="Link to this definition">#</a>  
Calculate the shape of the voxel matrix in grid coordinates.

Returns<span class="colon">:</span>  
Tuple of (x,y,z) dimensions representing how many voxels fit in each direction  
of the grid shape when divided by the single voxel shape.

Return type<span class="colon">:</span>  
tuple\[int, int, int\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">max_random_grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`int`</span><span class="pre">\]</span>*<a href="#fdtdx.Device.max_random_grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in grid coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">max_random_real_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.Device.max_random_real_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in real coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.Device.name" class="headerlink" title="Link to this definition">#</a>  
Unique identifier for the object. Automatically enforced to be unique through the UniqueName validator. The user can also set a name manually.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">output_type</span></span><a href="#fdtdx.Device.output_type" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">param_transforms</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Sequence`</span><span class="pre">\[</span><a href="fdtdx.ParameterTransformation.html#fdtdx.ParameterTransformation" class="reference internal" title="fdtdx.objects.device.parameters.transform.ParameterTransformation"><span class="pre"><code class="sourceCode python">ParameterTransformation</code></span></a><span class="pre">\]</span>*<a href="#fdtdx.Device.param_transforms" class="headerlink" title="Link to this definition">#</a>  
A Sequence of parameter transformation to be applied to the parameters when mapping them to simulation materials.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">partial_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\]\]</span>*<a href="#fdtdx.Device.partial_grid_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in grid coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">partial_real_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\]\]</span>*<a href="#fdtdx.Device.partial_real_position" class="headerlink" title="Link to this definition">#</a>  
The object’s position in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">partial_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\]\]</span>*<a href="#fdtdx.Device.partial_real_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">partial_voxel_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\]\]</span>*<a href="#fdtdx.Device.partial_voxel_grid_shape" class="headerlink" title="Link to this definition">#</a>  
Size of the material voxels used within the device in metrical units (meter). Note that this is independent of the simulation voxel size. Defaults to undefined shape. For all three axes, either the voxel grid or real shape needs to be defined.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">partial_voxel_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\],</span> <span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">\]\]</span>*<a href="#fdtdx.Device.partial_voxel_real_shape" class="headerlink" title="Link to this definition">#</a>  
Size of the material voxels used within the device in simulation voxels. Defaults to undefined shape. For all three axes, either the voxel grid or real shape needs to be defined.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">placement_order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.Device.placement_order" class="headerlink" title="Link to this definition">#</a>  
Field placeholder for autoinit.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">real_shape</span></span><a href="#fdtdx.Device.real_shape" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by this object’s placed grid slice.

The value is derived from <span class="pre">`SimulationConfig.grid`</span> when available. That keeps object geometry tied to physical edge coordinates instead of a global scalar resolution. During early placement, before a concrete grid has been attached to the config, the legacy uniform-resolution fallback is still used for compatibility.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">single_voxel_grid_shape</span></span><a href="#fdtdx.Device.single_voxel_grid_shape" class="headerlink" title="Link to this definition">#</a>  
Get the shape of a single voxel in grid coordinates.

Returns<span class="colon">:</span>  
Tuple of (x,y,z) dimensions for one voxel.

Return type<span class="colon">:</span>  
tuple\[int, int, int\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">single_voxel_real_shape</span></span><a href="#fdtdx.Device.single_voxel_real_shape" class="headerlink" title="Link to this definition">#</a>  
Calculate the representative physical size of one design voxel.

Returns<span class="colon">:</span>  
Tuple of <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> dimensions in metres.

Notes

On uniform simulation grids this is the exact size of each design voxel. On non-uniform grids, devices are currently supported only when design voxels are specified by simulation-cell counts. The returned physical size is then the average design-voxel extent over the placed device, suitable for transforms that need a representative scale. True physical-size design voxels still require a resampling layer and are rejected during placement.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">use_etching</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span>*<a href="#fdtdx.Device.use_etching" class="headerlink" title="Link to this definition">#</a>  
Determines the material placement behavior. If False, the device fully populates its defined 3D space using its material permittivities. If True, it acts as an etch, either leaving the space unmodified or replacing it with a single material (e.g., air) based on the parameters.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">apply</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.apply" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">check_overlap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.check_overlap" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">extend_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.extend_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">face_to_face_negative_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.face_to_face_negative_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">face_to_face_positive_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.face_to_face_positive_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Device.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Device.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">init_params</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/device.html#Device.init_params" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Device.init_params" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\] \| <span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">place_above</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.place_above" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">place_at_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.place_at_center" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">place_below</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.place_below" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">place_on_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice_tuple</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/device.html#Device.place_on_grid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Device.place_on_grid" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">place_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">own_positions</span></span>*, *<span class="n"><span class="pre">other_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.place_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">same_position</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.same_position" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">same_position_and_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.same_position_and_size" class="headerlink" title="Link to this definition">#</a>  
Creates both position and size constraints to make this object match another object’s position and size. This is a convenience wrapper combining place_at_center() and same_size().

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match. Defaults to all axes (0, 1, 2).

Returns<span class="colon">:</span>  
Position and size constraints for matching objects

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>, <a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">same_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.same_size" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">set_grid_coordinates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.set_grid_coordinates" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">size_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">proportions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.size_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Device.</span></span><span class="sig-name descname"><span class="pre">validate_placement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Device.validate_placement" class="headerlink" title="Link to this definition">#</a>  
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
