<div id="fdtdx-closedsurfacephasorpoyntingfluxdetector" class="section">

# fdtdx.ClosedSurfacePhasorPoyntingFluxDetector<a href="#fdtdx-closedsurfacephasorpoyntingfluxdetector" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">\_signed_data=True</span></span>*, *<span class="n"><span class="pre">\*</span></span>*, *<span class="n"><span class="pre">partial_real_shape=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_real_position=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_grid_shape=(None</span></span>*, *<span class="n"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">None)</span></span>*, *<span class="n"><span class="pre">color=Color(r=0.5882352941176471</span></span>*, *<span class="n"><span class="pre">g=0.9764705882352941</span></span>*, *<span class="n"><span class="pre">b=0.4823529411764706)</span></span>*, *<span class="n"><span class="pre">name=None</span></span>*, *<span class="n"><span class="pre">max_random_real_offsets=(0</span></span>*, *<span class="n"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">max_random_grid_offsets=(0</span></span>*, *<span class="n"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">0)</span></span>*, *<span class="n"><span class="pre">dtype=\<class</span> <span class="pre">'jax.numpy.complex64'\></span></span>*, *<span class="n"><span class="pre">exact_interpolation=True</span></span>*, *<span class="n"><span class="pre">inverse=False</span></span>*, *<span class="n"><span class="pre">switch=OnOffSwitch(</span>   <span class="pre">start_time=#None</span></span>*, *<span class="n"><span class="pre">start_after_periods=#None</span></span>*, *<span class="n"><span class="pre">end_time=#None</span></span>*, *<span class="n"><span class="pre">end_after_periods=#None</span></span>*, *<span class="n"><span class="pre">on_for_time=#None</span></span>*, *<span class="n"><span class="pre">on_for_periods=#None</span></span>*, *<span class="n"><span class="pre">period=#None</span></span>*, *<span class="n"><span class="pre">fixed_on_time_steps=#None</span></span>*, *<span class="n"><span class="pre">is_always_off=#False</span></span>*, *<span class="n"><span class="pre">interval=#1</span> <span class="pre">)</span></span>*, *<span class="n"><span class="pre">if_inverse_plot_backwards=True</span></span>*, *<span class="n"><span class="pre">num_video_workers=None</span></span>*, *<span class="n"><span class="pre">plot_interpolation='gaussian'</span></span>*, *<span class="n"><span class="pre">plot_dpi=None</span></span>*, *<span class="n"><span class="pre">wave_characters=null</span></span>*, *<span class="n"><span class="pre">scaling_mode='continuous'</span></span>*, *<span class="n"><span class="pre">dft_subsample=1</span></span>*, *<span class="n"><span class="pre">orientation='outward'</span></span>*, *<span class="n"><span class="pre">axes=None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/detectors/poynting_flux.html#ClosedSurfacePhasorPoyntingFluxDetector" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.PhasorDetector.html#fdtdx.PhasorDetector" class="reference internal" title="fdtdx.objects.detectors.phasor.PhasorDetector"><span class="pre"><code class="sourceCode python">PhasorDetector</code></span></a>

Net time-averaged Poynting flux through a closed box surface (frequency domain).

Frequency-domain analog of <a href="fdtdx.ClosedSurfacePoyntingFluxDetector.html#fdtdx.ClosedSurfacePoyntingFluxDetector" class="reference internal" title="fdtdx.ClosedSurfacePoyntingFluxDetector"><span class="pre"><code class="sourceCode python">ClosedSurfacePoyntingFluxDetector</code></span></a>. It accumulates field phasors and forms the net time-averaged outward flux <span class="pre">`sum_faces`</span>` `<span class="pre">`1/2`</span>` `<span class="pre">`Re(E(w)`</span>` `<span class="pre">`x`</span>` `<span class="pre">`H*(w))`</span>` `<span class="pre">`.`</span>` `<span class="pre">`dA`</span> in <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux"><span class="pre"><code class="sourceCode python">compute_net_flux()</code></span></a>.

Only the **hollow shell** is recorded: for each active axis just the two boundary planes are stored, never the box interior. The persistent detector state is therefore <span class="pre">`O(surface)`</span> rather than <span class="pre">`O(volume)`</span> – the interior phasors would be pure waste since the surface integral reads only the faces.

A face pair on an axis of size one cancels, so the default <span class="pre">`axes`</span> (every axis with more than one cell) reduces to a 4-face surface for a quasi-2D setup and a 6-face surface in full 3D, exactly like the time-domain version.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.axes" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.axes"><span class="pre"><code class="sourceCode python">axes</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.color" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.components" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.components"><span class="pre"><code class="sourceCode python">components</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dft_subsample" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dft_subsample"><span class="pre"><code class="sourceCode python">dft_subsample</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dtype" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dtype"><span class="pre"><code class="sourceCode python">dtype</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.exact_interpolation" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.exact_interpolation"><span class="pre"><code class="sourceCode python">exact_interpolation</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_shape" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_shape"><span class="pre"><code class="sourceCode python">grid_shape</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice"><span class="pre"><code class="sourceCode python">grid_slice</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice_tuple" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice_tuple"><span class="pre"><code class="sourceCode python">grid_slice_tuple</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.if_inverse_plot_backwards" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.if_inverse_plot_backwards"><span class="pre"><code class="sourceCode python">if_inverse_plot_backwards</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.inverse" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.inverse"><span class="pre"><code class="sourceCode python">inverse</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_grid_offsets" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_grid_offsets"><span class="pre"><code class="sourceCode python">max_random_grid_offsets</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_real_offsets" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_real_offsets"><span class="pre"><code class="sourceCode python">max_random_real_offsets</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.name" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_time_steps_recorded" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_time_steps_recorded"><span class="pre"><code class="sourceCode python">num_time_steps_recorded</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_video_workers" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_video_workers"><span class="pre"><code class="sourceCode python">num_video_workers</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.orientation" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.orientation"><span class="pre"><code class="sourceCode python">orientation</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_grid_shape" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_grid_shape"><span class="pre"><code class="sourceCode python">partial_grid_shape</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_position" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_position"><span class="pre"><code class="sourceCode python">partial_real_position</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_shape" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_shape"><span class="pre"><code class="sourceCode python">partial_real_shape</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot"><span class="pre"><code class="sourceCode python">plot</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_dpi" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_dpi"><span class="pre"><code class="sourceCode python">plot_dpi</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_interpolation" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_interpolation"><span class="pre"><code class="sourceCode python">plot_interpolation</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.real_shape" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.real_shape"><span class="pre"><code class="sourceCode python">real_shape</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.reduce_volume" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.reduce_volume"><span class="pre"><code class="sourceCode python">reduce_volume</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.scaling_mode" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.scaling_mode"><span class="pre"><code class="sourceCode python">scaling_mode</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.switch" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.switch"><span class="pre"><code class="sourceCode python">switch</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.wave_characters" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.wave_characters"><span class="pre"><code class="sourceCode python">wave_characters</code></span></a>

Methods

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.apply" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.apply"><span class="pre"><code class="sourceCode python"><span class="bu">apply</span></code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.aset" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.check_overlap" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.check_overlap"><span class="pre"><code class="sourceCode python">check_overlap</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux"><span class="pre"><code class="sourceCode python">compute_net_flux</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.draw_plot" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.draw_plot"><span class="pre"><code class="sourceCode python">draw_plot</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.extend_to" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.extend_to"><span class="pre"><code class="sourceCode python">extend_to</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_negative_direction" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_negative_direction"><span class="pre"><code class="sourceCode python">face_to_face_negative_direction</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_positive_direction" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_positive_direction"><span class="pre"><code class="sourceCode python">face_to_face_positive_direction</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_class_fields" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_public_fields" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.init_state" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.init_state"><span class="pre"><code class="sourceCode python">init_state</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_above" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_above"><span class="pre"><code class="sourceCode python">place_above</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_at_center" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_at_center"><span class="pre"><code class="sourceCode python">place_at_center</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_below" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_below"><span class="pre"><code class="sourceCode python">place_below</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_on_grid" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_on_grid"><span class="pre"><code class="sourceCode python">place_on_grid</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_relative_to" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_relative_to"><span class="pre"><code class="sourceCode python">place_relative_to</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position"><span class="pre"><code class="sourceCode python">same_position</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position_and_size" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position_and_size"><span class="pre"><code class="sourceCode python">same_position_and_size</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_size" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_size"><span class="pre"><code class="sourceCode python">same_size</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.set_grid_coordinates" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.set_grid_coordinates"><span class="pre"><code class="sourceCode python">set_grid_coordinates</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.size_relative_to" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.size_relative_to"><span class="pre"><code class="sourceCode python">size_relative_to</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.update" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.update"><span class="pre"><code class="sourceCode python">update</code></span></a>

- <a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.validate_placement" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.validate_placement"><span class="pre"><code class="sourceCode python">validate_placement</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">axes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.axes" class="headerlink" title="Link to this definition">#</a>  
Axes whose two faces contribute to the surface integral. <span class="pre">`None`</span> (default) uses every axis with a grid extent greater than one.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Color</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.color" class="headerlink" title="Link to this definition">#</a>  
RGB color for plotting. Defaults to light green.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">components</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Sequence`</span><span class="pre">\[</span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'Ex'`</span><span class="pre">,</span> <span class="pre">`'Ey'`</span><span class="pre">,</span> <span class="pre">`'Ez'`</span><span class="pre">,</span> <span class="pre">`'Hx'`</span><span class="pre">,</span> <span class="pre">`'Hy'`</span><span class="pre">,</span> <span class="pre">`'Hz'`</span><span class="pre">\]\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.components" class="headerlink" title="Link to this definition">#</a>  
Always all six field components – both E and H are needed for the Poynting flux. Not user-configurable.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">dft_subsample</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span> <span class="pre">\|</span> <span class="pre">Literal\['auto'\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dft_subsample" class="headerlink" title="Link to this definition">#</a>  
Subsampling stride for the phasor DFT. Only every stride-th active time step is recorded, with the kept samples rescaled to match every-step recording. If set to “auto”, the stride is derived from the highest recorded frequency and the time step duration. Defaults to 1, which records every active time step.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">dtype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">jnp.dtype</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.dtype" class="headerlink" title="Link to this definition">#</a>  
Data type for detector arrays, defaults to float32.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">exact_interpolation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.exact_interpolation" class="headerlink" title="Link to this definition">#</a>  
Whether to use exact field interpolation. Defaults to True.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">grid_shape</span></span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_shape" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">grid_slice</span></span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">grid_slice_tuple</span></span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.grid_slice_tuple" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">if_inverse_plot_backwards</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.if_inverse_plot_backwards" class="headerlink" title="Link to this definition">#</a>  
Plot inverse data in reverse time order.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">inverse</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">bool</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.inverse" class="headerlink" title="Link to this definition">#</a>  
Whether to record fields in inverse time order. Defaults to false.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">max_random_grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[int,</span> <span class="pre">int,</span> <span class="pre">int\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in grid coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">max_random_real_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.max_random_real_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in real coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.name" class="headerlink" title="Link to this definition">#</a>  
Unique identifier for the object. Automatically enforced to be unique through the UniqueName validator. The user can also set a name manually.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">num_time_steps_recorded</span></span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_time_steps_recorded" class="headerlink" title="Link to this definition">#</a>  
Gets the total number of time steps that will be recorded.

Returns<span class="colon">:</span>  
Number of time steps where detector will record data.

Return type<span class="colon">:</span>  
int

Raises<span class="colon">:</span>  
**Exception** – If detector is not yet initialized.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">num_video_workers</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.num_video_workers" class="headerlink" title="Link to this definition">#</a>  
Number of workers for video generation. If None (default), then no multiprocessing is used. Note that the combination of multiprocessing and matplotlib is known to produce problems and can cause the entire system to freeze. It does make the video generation much faster though.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">orientation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'outward'`</span><span class="pre">,</span> <span class="pre">`'inward'`</span><span class="pre">\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.orientation" class="headerlink" title="Link to this definition">#</a>  
<span class="pre">`"outward"`</span> (default) counts net power leaving the box as positive. <span class="pre">`"inward"`</span> flips the sign (net power entering, e.g. absorbed power).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">partial_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialGridShape3D</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_grid_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in grid coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">partial_real_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_position" class="headerlink" title="Link to this definition">#</a>  
The object’s position in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">partial_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.partial_real_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">plot</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot" class="headerlink" title="Link to this definition">#</a>  
Raw phasor auto-plotting is not meaningful; consume the <span class="pre">`compute_net_flux`</span> result instead.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">plot_dpi</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span> <span class="pre">\|</span> <span class="pre">None</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_dpi" class="headerlink" title="Link to this definition">#</a>  
DPI resolution for plots. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">plot_interpolation</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.plot_interpolation" class="headerlink" title="Link to this definition">#</a>  
Interpolation method for plots. Defualts to “gaussian”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">real_shape</span></span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.real_shape" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by this object’s placed grid slice.

The value is derived from <span class="pre">`SimulationConfig.grid`</span> when available. That keeps object geometry tied to physical edge coordinates instead of a global scalar resolution. During early placement, before a concrete grid has been attached to the config, the legacy uniform-resolution fallback is still used for compatibility.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">reduce_volume</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.reduce_volume" class="headerlink" title="Link to this definition">#</a>  
Storage is per-face and handled explicitly, so the base volume reduction is disabled.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">scaling_mode</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal\['continuous',</span> <span class="pre">'pulse'\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.scaling_mode" class="headerlink" title="Link to this definition">#</a>  
Scaling of the resulting phasor. In continuous mode, the result is scaled by a factor of 2 / N, where N is the number of time steps recorded. This allows accurate reconstruction of a continuous signal. In pulse mode, the result is not scaled.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">switch</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">OnOffSwitch</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.switch" class="headerlink" title="Link to this definition">#</a>  
This switch controls the time steps that the detector is on, i.e. records data. Defaults to all time steps.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">wave_characters</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Sequence\[WaveCharacter\]</span>*<a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.wave_characters" class="headerlink" title="Link to this definition">#</a>  
WaveCharacters to analyze.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">apply</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.apply" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">check_overlap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.check_overlap" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">compute_net_flux</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">state</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/detectors/poynting_flux.html#ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.compute_net_flux" class="headerlink" title="Link to this definition">#</a>  
Net time-averaged Poynting flux through the closed surface at every wavelength.

Parameters<span class="colon">:</span>  
**state** (*DetectorState*) – Detector state holding the per-face phasors.

Returns<span class="colon">:</span>  
Real net flux of shape <span class="pre">`(num_freqs,)`</span>. Positive means net power leaving the box for <span class="pre">`orientation="outward"`</span>.

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">draw_plot</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">progress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">cmap</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'default'</span></span>*, *<span class="n"><span class="pre">aspect</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'equal'</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.draw_plot" class="headerlink" title="Link to this definition">#</a>  
Generates plots or videos from recorded detector data.

Creates visualizations based on dimensionality of recorded data and detector configuration. Supports 1D line plots, 2D heatmaps, and video generation for time-varying data.

Parameters<span class="colon">:</span>  
- **state** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`ndarray`</span>\]</span>) – dict\[str, np.ndarray\]: Dictionary containing recorded field data arrays.

- **progress** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Progress`</span> \| <span class="pre">`None`</span></span>) – Progress \| None, optional: Optional progress bar for video generation.

- **cmap** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – str = “default”: Color map for the detector plots. “default” is turbo for unsigned data and RdBu_r for signed data.

- **aspect** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Literal`</span>\[<span class="pre">`'auto'`</span>, <span class="pre">`'equal'`</span>\]</span>) – Literal\[“auto”, “equal”\]: Size aspect of the detector plots. “equal” (default) uses the same scale for all axes. “auto” adjusts each axis’s scale to fit the figure size.

Returns<span class="colon">:</span>  
Dictionary mapping plot names to either  
matplotlib Figure objects or paths to generated video files.

Return type<span class="colon">:</span>  
dict\[str, Figure \| str\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">extend_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.extend_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">face_to_face_negative_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_negative_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">face_to_face_positive_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.face_to_face_positive_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">init_state</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.init_state" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">place_above</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_above" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">place_at_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_at_center" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">place_below</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_below" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">place_on_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice_tuple</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/detectors/poynting_flux.html#ClosedSurfacePhasorPoyntingFluxDetector.place_on_grid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_on_grid" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">place_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">own_positions</span></span>*, *<span class="n"><span class="pre">other_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.place_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">same_position</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">same_position_and_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_position_and_size" class="headerlink" title="Link to this definition">#</a>  
Creates both position and size constraints to make this object match another object’s position and size. This is a convenience wrapper combining place_at_center() and same_size().

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match. Defaults to all axes (0, 1, 2).

Returns<span class="colon">:</span>  
Position and size constraints for matching objects

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>, <a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">same_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.same_size" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">set_grid_coordinates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.set_grid_coordinates" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">size_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">proportions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.size_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">update</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">inv_permittivity</span></span>*, *<span class="n"><span class="pre">inv_permeability</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/detectors/poynting_flux.html#ClosedSurfacePhasorPoyntingFluxDetector.update" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.update" class="headerlink" title="Link to this definition">#</a>  
Updates detector state with current field values.

Note that fields and materials arrive already restricted to this detector’s <span class="pre">`grid_slice`</span> and, when <span class="pre">`exact_interpolation`</span> is set, already co-located onto the E_z Yee point, so implementations must not slice <span class="pre">`grid_slice`</span> again.

Parameters<span class="colon">:</span>  
- **time_step** (*jax.Array*) – Current simulation time step.

- **E** (*jax.Array*) – Electric field array.

- **H** (*jax.Array*) – Magnetic field array.

- **state** (*DetectorState*) – Current detector state.

- **inv_permittivity** (*jax.Array*) – Inverse permittivity array.

- **inv_permeability** (*jax.Array* *\|* *float*) – Inverse permeability array.

Returns<span class="colon">:</span>  
Updated detector state.

Return type<span class="colon">:</span>  
DetectorState

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ClosedSurfacePhasorPoyntingFluxDetector.</span></span><span class="sig-name descname"><span class="pre">validate_placement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector.validate_placement" class="headerlink" title="Link to this definition">#</a>  
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
