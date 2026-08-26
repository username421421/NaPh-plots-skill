<div id="fdtdx-uniformplanesource" class="section">

# fdtdx.UniformPlaneSource<a href="#fdtdx-uniformplanesource" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">UniformPlaneSource</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">temporal_profile=SingleFrequencyProfile(phase_shift=#3.141592653589793</span></span>*, *<span class="n"><span class="pre">num_startup_periods=4)</span></span>*, *<span class="n"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">partial_real_shape=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_real_position=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_grid_shape=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">color=Color(r=0.7764705882352941</span></span>*, *<span class="n"><span class="pre">g=0.3176470588235294</span></span>*, *<span class="n"><span class="pre">b=0.00784313725490196)</span></span>*, *<span class="n"><span class="pre">name=None</span></span>*, *<span class="n"><span class="pre">max_random_real_offsets=(0</span></span>*, *<span class="n"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">max_random_grid_offsets=(0</span></span>*, *<span class="n"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">wave_character=null</span></span>*, *<span class="n"><span class="pre">static_amplitude_factor=1.0</span></span>*, *<span class="n"><span class="pre">switch=OnOffSwitch(</span>   <span class="pre">start_time=#None</span></span>*, *<span class="n"><span class="pre">start_after_periods=#None</span></span>*, *<span class="n"><span class="pre">end_time=#None</span></span>*, *<span class="n"><span class="pre">end_after_periods=#None</span></span>*, *<span class="n"><span class="pre">on_for_time=#None</span></span>*, *<span class="n"><span class="pre">on_for_periods=#None</span></span>*, *<span class="n"><span class="pre">period=#None</span></span>*, *<span class="n"><span class="pre">fixed_on_time_steps=#None</span></span>*, *<span class="n"><span class="pre">is_always_off=#False</span></span>*, *<span class="n"><span class="pre">interval=#1</span> <span class="pre">)</span></span>*, *<span class="n"><span class="pre">direction=null</span></span>*, *<span class="n"><span class="pre">azimuth_angle=0.0</span></span>*, *<span class="n"><span class="pre">elevation_angle=0.0</span></span>*, *<span class="n"><span class="pre">max_angle_random_offset=0.0</span></span>*, *<span class="n"><span class="pre">max_vertical_offset=0.0</span></span>*, *<span class="n"><span class="pre">max_horizontal_offset=0.0</span></span>*, *<span class="n"><span class="pre">fixed_E_polarization_vector=None</span></span>*, *<span class="n"><span class="pre">fixed_H_polarization_vector=None</span></span>*, *<span class="n"><span class="pre">normalize_by_energy=True</span></span>*, *<span class="n"><span class="pre">amplitude=1.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/sources/linear_polarization.html#UniformPlaneSource" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.UniformPlaneSource" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`LinearlyPolarizedPlaneSource`</span>

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.UniformPlaneSource.amplitude" class="reference internal" title="fdtdx.UniformPlaneSource.amplitude"><span class="pre"><code class="sourceCode python">amplitude</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.azimuth_angle" class="reference internal" title="fdtdx.UniformPlaneSource.azimuth_angle"><span class="pre"><code class="sourceCode python">azimuth_angle</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.azimuth_radians" class="reference internal" title="fdtdx.UniformPlaneSource.azimuth_radians"><span class="pre"><code class="sourceCode python">azimuth_radians</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.color" class="reference internal" title="fdtdx.UniformPlaneSource.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.direction" class="reference internal" title="fdtdx.UniformPlaneSource.direction"><span class="pre"><code class="sourceCode python">direction</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.elevation_angle" class="reference internal" title="fdtdx.UniformPlaneSource.elevation_angle"><span class="pre"><code class="sourceCode python">elevation_angle</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.elevation_radians" class="reference internal" title="fdtdx.UniformPlaneSource.elevation_radians"><span class="pre"><code class="sourceCode python">elevation_radians</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.fixed_E_polarization_vector" class="reference internal" title="fdtdx.UniformPlaneSource.fixed_E_polarization_vector"><span class="pre"><code class="sourceCode python">fixed_E_polarization_vector</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.fixed_H_polarization_vector" class="reference internal" title="fdtdx.UniformPlaneSource.fixed_H_polarization_vector"><span class="pre"><code class="sourceCode python">fixed_H_polarization_vector</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.grid_shape" class="reference internal" title="fdtdx.UniformPlaneSource.grid_shape"><span class="pre"><code class="sourceCode python">grid_shape</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.grid_slice" class="reference internal" title="fdtdx.UniformPlaneSource.grid_slice"><span class="pre"><code class="sourceCode python">grid_slice</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.grid_slice_tuple" class="reference internal" title="fdtdx.UniformPlaneSource.grid_slice_tuple"><span class="pre"><code class="sourceCode python">grid_slice_tuple</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.horizontal_axis" class="reference internal" title="fdtdx.UniformPlaneSource.horizontal_axis"><span class="pre"><code class="sourceCode python">horizontal_axis</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_angle_random_offset" class="reference internal" title="fdtdx.UniformPlaneSource.max_angle_random_offset"><span class="pre"><code class="sourceCode python">max_angle_random_offset</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_angle_random_offset_radians" class="reference internal" title="fdtdx.UniformPlaneSource.max_angle_random_offset_radians"><span class="pre"><code class="sourceCode python">max_angle_random_offset_radians</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_horizontal_offset" class="reference internal" title="fdtdx.UniformPlaneSource.max_horizontal_offset"><span class="pre"><code class="sourceCode python">max_horizontal_offset</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_horizontal_offset_grid" class="reference internal" title="fdtdx.UniformPlaneSource.max_horizontal_offset_grid"><span class="pre"><code class="sourceCode python">max_horizontal_offset_grid</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_random_grid_offsets" class="reference internal" title="fdtdx.UniformPlaneSource.max_random_grid_offsets"><span class="pre"><code class="sourceCode python">max_random_grid_offsets</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_random_real_offsets" class="reference internal" title="fdtdx.UniformPlaneSource.max_random_real_offsets"><span class="pre"><code class="sourceCode python">max_random_real_offsets</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_vertical_offset" class="reference internal" title="fdtdx.UniformPlaneSource.max_vertical_offset"><span class="pre"><code class="sourceCode python">max_vertical_offset</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.max_vertical_offset_grid" class="reference internal" title="fdtdx.UniformPlaneSource.max_vertical_offset_grid"><span class="pre"><code class="sourceCode python">max_vertical_offset_grid</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.name" class="reference internal" title="fdtdx.UniformPlaneSource.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.normalize_by_energy" class="reference internal" title="fdtdx.UniformPlaneSource.normalize_by_energy"><span class="pre"><code class="sourceCode python">normalize_by_energy</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.partial_grid_shape" class="reference internal" title="fdtdx.UniformPlaneSource.partial_grid_shape"><span class="pre"><code class="sourceCode python">partial_grid_shape</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.partial_real_position" class="reference internal" title="fdtdx.UniformPlaneSource.partial_real_position"><span class="pre"><code class="sourceCode python">partial_real_position</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.partial_real_shape" class="reference internal" title="fdtdx.UniformPlaneSource.partial_real_shape"><span class="pre"><code class="sourceCode python">partial_real_shape</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.propagation_axis" class="reference internal" title="fdtdx.UniformPlaneSource.propagation_axis"><span class="pre"><code class="sourceCode python">propagation_axis</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.real_shape" class="reference internal" title="fdtdx.UniformPlaneSource.real_shape"><span class="pre"><code class="sourceCode python">real_shape</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.static_amplitude_factor" class="reference internal" title="fdtdx.UniformPlaneSource.static_amplitude_factor"><span class="pre"><code class="sourceCode python">static_amplitude_factor</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.switch" class="reference internal" title="fdtdx.UniformPlaneSource.switch"><span class="pre"><code class="sourceCode python">switch</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.temporal_profile" class="reference internal" title="fdtdx.UniformPlaneSource.temporal_profile"><span class="pre"><code class="sourceCode python">temporal_profile</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.vertical_axis" class="reference internal" title="fdtdx.UniformPlaneSource.vertical_axis"><span class="pre"><code class="sourceCode python">vertical_axis</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.wave_character" class="reference internal" title="fdtdx.UniformPlaneSource.wave_character"><span class="pre"><code class="sourceCode python">wave_character</code></span></a>

Methods

- <a href="#fdtdx.UniformPlaneSource.adjust_time_step_by_on_off" class="reference internal" title="fdtdx.UniformPlaneSource.adjust_time_step_by_on_off"><span class="pre"><code class="sourceCode python">adjust_time_step_by_on_off</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.apply" class="reference internal" title="fdtdx.UniformPlaneSource.apply"><span class="pre"><code class="sourceCode python"><span class="bu">apply</span></code></span></a>

- <a href="#fdtdx.UniformPlaneSource.aset" class="reference internal" title="fdtdx.UniformPlaneSource.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.check_overlap" class="reference internal" title="fdtdx.UniformPlaneSource.check_overlap"><span class="pre"><code class="sourceCode python">check_overlap</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.extend_to" class="reference internal" title="fdtdx.UniformPlaneSource.extend_to"><span class="pre"><code class="sourceCode python">extend_to</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.face_to_face_negative_direction" class="reference internal" title="fdtdx.UniformPlaneSource.face_to_face_negative_direction"><span class="pre"><code class="sourceCode python">face_to_face_negative_direction</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.face_to_face_positive_direction" class="reference internal" title="fdtdx.UniformPlaneSource.face_to_face_positive_direction"><span class="pre"><code class="sourceCode python">face_to_face_positive_direction</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.frequency_spectrum" class="reference internal" title="fdtdx.UniformPlaneSource.frequency_spectrum"><span class="pre"><code class="sourceCode python">frequency_spectrum</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.get_class_fields" class="reference internal" title="fdtdx.UniformPlaneSource.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.get_public_fields" class="reference internal" title="fdtdx.UniformPlaneSource.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.is_on_at_time_step" class="reference internal" title="fdtdx.UniformPlaneSource.is_on_at_time_step"><span class="pre"><code class="sourceCode python">is_on_at_time_step</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.place_above" class="reference internal" title="fdtdx.UniformPlaneSource.place_above"><span class="pre"><code class="sourceCode python">place_above</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.place_at_center" class="reference internal" title="fdtdx.UniformPlaneSource.place_at_center"><span class="pre"><code class="sourceCode python">place_at_center</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.place_below" class="reference internal" title="fdtdx.UniformPlaneSource.place_below"><span class="pre"><code class="sourceCode python">place_below</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.place_on_grid" class="reference internal" title="fdtdx.UniformPlaneSource.place_on_grid"><span class="pre"><code class="sourceCode python">place_on_grid</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.place_relative_to" class="reference internal" title="fdtdx.UniformPlaneSource.place_relative_to"><span class="pre"><code class="sourceCode python">place_relative_to</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.plot_time_signal_and_spectrum" class="reference internal" title="fdtdx.UniformPlaneSource.plot_time_signal_and_spectrum"><span class="pre"><code class="sourceCode python">plot_time_signal_and_spectrum</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.same_position" class="reference internal" title="fdtdx.UniformPlaneSource.same_position"><span class="pre"><code class="sourceCode python">same_position</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.same_position_and_size" class="reference internal" title="fdtdx.UniformPlaneSource.same_position_and_size"><span class="pre"><code class="sourceCode python">same_position_and_size</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.same_size" class="reference internal" title="fdtdx.UniformPlaneSource.same_size"><span class="pre"><code class="sourceCode python">same_size</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.sample_time_signal" class="reference internal" title="fdtdx.UniformPlaneSource.sample_time_signal"><span class="pre"><code class="sourceCode python">sample_time_signal</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.set_grid_coordinates" class="reference internal" title="fdtdx.UniformPlaneSource.set_grid_coordinates"><span class="pre"><code class="sourceCode python">set_grid_coordinates</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.size_relative_to" class="reference internal" title="fdtdx.UniformPlaneSource.size_relative_to"><span class="pre"><code class="sourceCode python">size_relative_to</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.update_E" class="reference internal" title="fdtdx.UniformPlaneSource.update_E"><span class="pre"><code class="sourceCode python">update_E</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.update_H" class="reference internal" title="fdtdx.UniformPlaneSource.update_H"><span class="pre"><code class="sourceCode python">update_H</code></span></a>

- <a href="#fdtdx.UniformPlaneSource.validate_placement" class="reference internal" title="fdtdx.UniformPlaneSource.validate_placement"><span class="pre"><code class="sourceCode python">validate_placement</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">amplitude</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.UniformPlaneSource.amplitude" class="headerlink" title="Link to this definition">#</a>  
the amplitude of the uniform source

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">azimuth_angle</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.azimuth_angle" class="headerlink" title="Link to this definition">#</a>  
the azimuth angle

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">azimuth_radians</span></span><a href="#fdtdx.UniformPlaneSource.azimuth_radians" class="headerlink" title="Link to this definition">#</a>  
Convert azimuth angle from degrees to radians.

Returns<span class="colon">:</span>  
Azimuth angle in radians.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Color</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.UniformPlaneSource.color" class="headerlink" title="Link to this definition">#</a>  
color of the object

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">direction</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal\['+',</span> <span class="pre">'-'\]</span>*<a href="#fdtdx.UniformPlaneSource.direction" class="headerlink" title="Link to this definition">#</a>  
Direction of propagation (‘+’ or ‘-’ along propagation axis).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">elevation_angle</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.elevation_angle" class="headerlink" title="Link to this definition">#</a>  
the elevation angle

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">elevation_radians</span></span><a href="#fdtdx.UniformPlaneSource.elevation_radians" class="headerlink" title="Link to this definition">#</a>  
Convert elevation angle from degrees to radians.

Returns<span class="colon">:</span>  
Elevation angle in radians.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">fixed_E_polarization_vector</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.UniformPlaneSource.fixed_E_polarization_vector" class="headerlink" title="Link to this definition">#</a>  
the electric polarization vector

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">fixed_H_polarization_vector</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.UniformPlaneSource.fixed_H_polarization_vector" class="headerlink" title="Link to this definition">#</a>  
the magnetic polarization vector

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">grid_shape</span></span><a href="#fdtdx.UniformPlaneSource.grid_shape" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">grid_slice</span></span><a href="#fdtdx.UniformPlaneSource.grid_slice" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">grid_slice_tuple</span></span><a href="#fdtdx.UniformPlaneSource.grid_slice_tuple" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">horizontal_axis</span></span><a href="#fdtdx.UniformPlaneSource.horizontal_axis" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_angle_random_offset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.max_angle_random_offset" class="headerlink" title="Link to this definition">#</a>  
the max angle random offset

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_angle_random_offset_radians</span></span><a href="#fdtdx.UniformPlaneSource.max_angle_random_offset_radians" class="headerlink" title="Link to this definition">#</a>  
Convert maximum random angle offset from degrees to radians.

Returns<span class="colon">:</span>  
Maximum random angle offset in radians.

Return type<span class="colon">:</span>  
float

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_horizontal_offset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.max_horizontal_offset" class="headerlink" title="Link to this definition">#</a>  
the max horizontal offset

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_horizontal_offset_grid</span></span><a href="#fdtdx.UniformPlaneSource.max_horizontal_offset_grid" class="headerlink" title="Link to this definition">#</a>  
Return the maximum horizontal random offset in source-center units.

Returns<span class="colon">:</span>  
On uniform grids this is the legacy grid-index offset. On non-uniform grids source centers are represented in physical transverse coordinates, so the returned value is the requested physical offset in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_random_grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[int,</span> <span class="pre">int,</span> <span class="pre">int\]</span>*<a href="#fdtdx.UniformPlaneSource.max_random_grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in grid coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_random_real_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span>*<a href="#fdtdx.UniformPlaneSource.max_random_real_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in real coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_vertical_offset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.max_vertical_offset" class="headerlink" title="Link to this definition">#</a>  
the max vertical offset

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">max_vertical_offset_grid</span></span><a href="#fdtdx.UniformPlaneSource.max_vertical_offset_grid" class="headerlink" title="Link to this definition">#</a>  
Return the maximum vertical random offset in source-center units.

Returns<span class="colon">:</span>  
On uniform grids this is the legacy grid-index offset. On non-uniform grids source centers are represented in physical transverse coordinates, so the returned value is the requested physical offset in metres.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.UniformPlaneSource.name" class="headerlink" title="Link to this definition">#</a>  
Unique identifier for the object. Automatically enforced to be unique through the UniqueName validator. The user can also set a name manually.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">normalize_by_energy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.UniformPlaneSource.normalize_by_energy" class="headerlink" title="Link to this definition">#</a>  
whether to normalize the polarization vector

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">partial_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialGridShape3D</span>*<a href="#fdtdx.UniformPlaneSource.partial_grid_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in grid coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">partial_real_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.UniformPlaneSource.partial_real_position" class="headerlink" title="Link to this definition">#</a>  
The object’s position in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">partial_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.UniformPlaneSource.partial_real_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">propagation_axis</span></span><a href="#fdtdx.UniformPlaneSource.propagation_axis" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">real_shape</span></span><a href="#fdtdx.UniformPlaneSource.real_shape" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by this object’s placed grid slice.

The value is derived from <span class="pre">`SimulationConfig.grid`</span> when available. That keeps object geometry tied to physical edge coordinates instead of a global scalar resolution. During early placement, before a concrete grid has been attached to the config, the legacy uniform-resolution fallback is still used for compatibility.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">static_amplitude_factor</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">float</span>*<a href="#fdtdx.UniformPlaneSource.static_amplitude_factor" class="headerlink" title="Link to this definition">#</a>  
the static amplitude factor

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">switch</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">OnOffSwitch</span>*<a href="#fdtdx.UniformPlaneSource.switch" class="headerlink" title="Link to this definition">#</a>  
the on-off switch

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">temporal_profile</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">TemporalProfile</span>*<a href="#fdtdx.UniformPlaneSource.temporal_profile" class="headerlink" title="Link to this definition">#</a>  
the temporal profile, uses single frequency

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">vertical_axis</span></span><a href="#fdtdx.UniformPlaneSource.vertical_axis" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">wave_character</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">WaveCharacter</span>*<a href="#fdtdx.UniformPlaneSource.wave_character" class="headerlink" title="Link to this definition">#</a>  
the wave-character

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">adjust_time_step_by_on_off</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_step</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.adjust_time_step_by_on_off" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">apply</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.apply" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">check_overlap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.check_overlap" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">extend_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.extend_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">face_to_face_negative_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.face_to_face_negative_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">face_to_face_positive_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.face_to_face_positive_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">frequency_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.frequency_spectrum" class="headerlink" title="Link to this definition">#</a>  
Return the one-sided FFT magnitude of this source’s sampled time signal.

This is intended for analyzing or visualizing its frequency spectrum.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">is_on_at_time_step</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_step</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.is_on_at_time_step" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">place_above</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.place_above" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">place_at_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.place_at_center" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">place_below</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.place_below" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">place_on_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice_tuple</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.place_on_grid" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">place_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">own_positions</span></span>*, *<span class="n"><span class="pre">other_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.place_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">plot_time_signal_and_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.plot_time_signal_and_spectrum" class="headerlink" title="Link to this definition">#</a>  
Plot this source’s sampled time signal and one-sided frequency spectrum.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">same_position</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.same_position" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">same_position_and_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.same_position_and_size" class="headerlink" title="Link to this definition">#</a>  
Creates both position and size constraints to make this object match another object’s position and size. This is a convenience wrapper combining place_at_center() and same_size().

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match. Defaults to all axes (0, 1, 2).

Returns<span class="colon">:</span>  
Position and size constraints for matching objects

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>, <a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">same_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.same_size" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">sample_time_signal</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.sample_time_signal" class="headerlink" title="Link to this definition">#</a>  
Sample this source’s time signal for plotting or analysis.

The returned signal uses the FDTD time grid from the supplied config, or from self.\_config if the source has already been placed.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">set_grid_coordinates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.set_grid_coordinates" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">size_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">proportions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.size_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">update_E</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">inverse</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.update_E" class="headerlink" title="Link to this definition">#</a>  
Update the electric field component.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Current electric field array.

- **inv_permittivities** (*jax.Array*) – Inverse permittivity values.

- **inv_permeabilities** (*jax.Array* *\|* *float*) – Inverse permeability values.

- **time_step** (*jax.Array*) – Current simulation time step.

- **inverse** (*bool*) – Whether to perform inverse update for backpropagation.

Returns<span class="colon">:</span>  
Updated electric field array.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">update_H</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">inverse</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.update_H" class="headerlink" title="Link to this definition">#</a>  
Update the magnetic field component.

Parameters<span class="colon">:</span>  
- **H** (*jax.Array*) – Current magnetic field array.

- **inv_permittivities** (*jax.Array*) – Inverse permittivity values.

- **inv_permeabilities** (*jax.Array* *\|* *float*) – Inverse permeability values.

- **time_step** (*jax.Array*) – Current simulation time step.

- **inverse** (*bool*) – Whether to perform inverse update for backpropagation.

Returns<span class="colon">:</span>  
Updated magnetic field array.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">UniformPlaneSource.</span></span><span class="sig-name descname"><span class="pre">validate_placement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.UniformPlaneSource.validate_placement" class="headerlink" title="Link to this definition">#</a>  
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
