<div id="fdtdx-perfectlymatchedlayer" class="section">

# fdtdx.PerfectlyMatchedLayer<a href="#fdtdx-perfectlymatchedlayer" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">PerfectlyMatchedLayer</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">partial_real_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_real_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">partial_grid_shape</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(None,</span> <span class="pre">None,</span> <span class="pre">None)</span></span>*, *<span class="n"><span class="pre">color</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">Color(r=0.21176470588235294,</span> <span class="pre">g=0.21568627450980393,</span> <span class="pre">b=0.21568627450980393)</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">max_random_real_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">max_random_grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">direction</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">alpha_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pml_a_E</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pml_b_E</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">inv_kappa_E</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pml_a_H</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pml_b_H</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">inv_kappa_H</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/perfectly_matched_layer.html#PerfectlyMatchedLayer" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PerfectlyMatchedLayer" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`BaseBoundary`</span>

Implements a Convolutional Perfectly Matched Layer (CPML) boundary condition.

The CPML absorbs outgoing electromagnetic waves with minimal reflection by using a complex coordinate stretching approach. This implementation supports arbitrary axis orientation and both positive/negative directions.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.PerfectlyMatchedLayer.alpha_end" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.alpha_end"><span class="pre"><code class="sourceCode python">alpha_end</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.alpha_order" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.alpha_order"><span class="pre"><code class="sourceCode python">alpha_order</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.alpha_start" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.alpha_start"><span class="pre"><code class="sourceCode python">alpha_start</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.axis" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.axis"><span class="pre"><code class="sourceCode python">axis</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.color" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.color"><span class="pre"><code class="sourceCode python">color</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.descriptive_name" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.descriptive_name"><span class="pre"><code class="sourceCode python">descriptive_name</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.direction" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.direction"><span class="pre"><code class="sourceCode python">direction</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.grid_shape" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.grid_shape"><span class="pre"><code class="sourceCode python">grid_shape</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.grid_slice" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.grid_slice"><span class="pre"><code class="sourceCode python">grid_slice</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.grid_slice_tuple" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.grid_slice_tuple"><span class="pre"><code class="sourceCode python">grid_slice_tuple</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.inv_kappa_E" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.inv_kappa_E"><span class="pre"><code class="sourceCode python">inv_kappa_E</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.inv_kappa_H" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.inv_kappa_H"><span class="pre"><code class="sourceCode python">inv_kappa_H</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.kappa_end" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.kappa_end"><span class="pre"><code class="sourceCode python">kappa_end</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.kappa_order" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.kappa_order"><span class="pre"><code class="sourceCode python">kappa_order</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.kappa_start" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.kappa_start"><span class="pre"><code class="sourceCode python">kappa_start</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.max_random_grid_offsets" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.max_random_grid_offsets"><span class="pre"><code class="sourceCode python">max_random_grid_offsets</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.max_random_real_offsets" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.max_random_real_offsets"><span class="pre"><code class="sourceCode python">max_random_real_offsets</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.name" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.partial_grid_shape" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.partial_grid_shape"><span class="pre"><code class="sourceCode python">partial_grid_shape</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.partial_real_position" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.partial_real_position"><span class="pre"><code class="sourceCode python">partial_real_position</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.partial_real_shape" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.partial_real_shape"><span class="pre"><code class="sourceCode python">partial_real_shape</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.pml_a_E" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.pml_a_E"><span class="pre"><code class="sourceCode python">pml_a_E</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.pml_a_H" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.pml_a_H"><span class="pre"><code class="sourceCode python">pml_a_H</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.pml_b_E" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.pml_b_E"><span class="pre"><code class="sourceCode python">pml_b_E</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.pml_b_H" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.pml_b_H"><span class="pre"><code class="sourceCode python">pml_b_H</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.real_shape" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.real_shape"><span class="pre"><code class="sourceCode python">real_shape</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.sigma_end" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.sigma_end"><span class="pre"><code class="sourceCode python">sigma_end</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.sigma_order" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.sigma_order"><span class="pre"><code class="sourceCode python">sigma_order</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.sigma_start" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.sigma_start"><span class="pre"><code class="sourceCode python">sigma_start</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.thickness" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.thickness"><span class="pre"><code class="sourceCode python">thickness</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.uses_wrap_padding" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.uses_wrap_padding"><span class="pre"><code class="sourceCode python">uses_wrap_padding</code></span></a>

Methods

- <a href="#fdtdx.PerfectlyMatchedLayer.apply" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.apply"><span class="pre"><code class="sourceCode python"><span class="bu">apply</span></code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.apply_field_reset" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.apply_field_reset"><span class="pre"><code class="sourceCode python">apply_field_reset</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.apply_pad_correction" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.apply_pad_correction"><span class="pre"><code class="sourceCode python">apply_pad_correction</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.apply_post_E_update" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.apply_post_E_update"><span class="pre"><code class="sourceCode python">apply_post_E_update</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.apply_post_H_update" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.apply_post_H_update"><span class="pre"><code class="sourceCode python">apply_post_H_update</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.aset" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.check_overlap" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.check_overlap"><span class="pre"><code class="sourceCode python">check_overlap</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.extend_to" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.extend_to"><span class="pre"><code class="sourceCode python">extend_to</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.face_to_face_negative_direction" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.face_to_face_negative_direction"><span class="pre"><code class="sourceCode python">face_to_face_negative_direction</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.face_to_face_positive_direction" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.face_to_face_positive_direction"><span class="pre"><code class="sourceCode python">face_to_face_positive_direction</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.get_class_fields" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.get_public_fields" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.interface_grid_shape" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.interface_grid_shape"><span class="pre"><code class="sourceCode python">interface_grid_shape</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.interface_slice" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.interface_slice"><span class="pre"><code class="sourceCode python">interface_slice</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.interface_slice_tuple" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.interface_slice_tuple"><span class="pre"><code class="sourceCode python">interface_slice_tuple</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.place_above" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.place_above"><span class="pre"><code class="sourceCode python">place_above</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.place_at_center" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.place_at_center"><span class="pre"><code class="sourceCode python">place_at_center</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.place_below" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.place_below"><span class="pre"><code class="sourceCode python">place_below</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.place_on_grid" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.place_on_grid"><span class="pre"><code class="sourceCode python">place_on_grid</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.place_relative_to" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.place_relative_to"><span class="pre"><code class="sourceCode python">place_relative_to</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.same_position" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.same_position"><span class="pre"><code class="sourceCode python">same_position</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.same_position_and_size" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.same_position_and_size"><span class="pre"><code class="sourceCode python">same_position_and_size</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.same_size" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.same_size"><span class="pre"><code class="sourceCode python">same_size</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.set_grid_coordinates" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.set_grid_coordinates"><span class="pre"><code class="sourceCode python">set_grid_coordinates</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.size_relative_to" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.size_relative_to"><span class="pre"><code class="sourceCode python">size_relative_to</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.step_cpml" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.step_cpml"><span class="pre"><code class="sourceCode python">step_cpml</code></span></a>

- <a href="#fdtdx.PerfectlyMatchedLayer.validate_placement" class="reference internal" title="fdtdx.PerfectlyMatchedLayer.validate_placement"><span class="pre"><code class="sourceCode python">validate_placement</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">alpha_end</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.alpha_end" class="headerlink" title="Link to this definition">#</a>  
Final loss parameter for complex frequency shifting. Defaults to 0.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">alpha_order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.alpha_order" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading. Defaults to 1.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">alpha_start</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.alpha_start" class="headerlink" title="Link to this definition">#</a>  
Initial loss parameter for complex frequency shifting. Defaults to 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">int</span>*<a href="#fdtdx.PerfectlyMatchedLayer.axis" class="headerlink" title="Link to this definition">#</a>  
Principal axis for boundary (0=x, 1=y, 2=z)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">color</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.Color.html#fdtdx.Color" class="reference internal" title="fdtdx.colors.Color"><span class="pre"><code class="sourceCode python">Color</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.color" class="headerlink" title="Link to this definition">#</a>  
RGB color tuple for visualization. defaults to dark grey.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">descriptive_name</span></span><a href="#fdtdx.PerfectlyMatchedLayer.descriptive_name" class="headerlink" title="Link to this definition">#</a>  
Gets a human-readable name describing this PML boundary’s location.

Returns<span class="colon">:</span>  
Description like “min_x” or “max_z” indicating position

Return type<span class="colon">:</span>  
str

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">direction</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">Literal\['+',</span> <span class="pre">'-'\]</span>*<a href="#fdtdx.PerfectlyMatchedLayer.direction" class="headerlink" title="Link to this definition">#</a>  
Direction along axis (“+” or “-“)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">grid_shape</span></span><a href="#fdtdx.PerfectlyMatchedLayer.grid_shape" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">grid_slice</span></span><a href="#fdtdx.PerfectlyMatchedLayer.grid_slice" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">grid_slice_tuple</span></span><a href="#fdtdx.PerfectlyMatchedLayer.grid_slice_tuple" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">inv_kappa_E</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.inv_kappa_E" class="headerlink" title="Link to this definition">#</a>  
Inverse of the kappa stretching parameter array for the Electric field.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">inv_kappa_H</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.inv_kappa_H" class="headerlink" title="Link to this definition">#</a>  
Inverse of the kappa stretching parameter array for the Magnetic field.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">kappa_end</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.kappa_end" class="headerlink" title="Link to this definition">#</a>  
Final kappa stretching coefficient. Defaults to 0.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">kappa_order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.kappa_order" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading. Defaults to 1.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">kappa_start</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.kappa_start" class="headerlink" title="Link to this definition">#</a>  
Initial kappa stretching coefficient. Defaults to 0.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">max_random_grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[int,</span> <span class="pre">int,</span> <span class="pre">int\]</span>*<a href="#fdtdx.PerfectlyMatchedLayer.max_random_grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in grid coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">max_random_real_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">tuple\[float,</span> <span class="pre">float,</span> <span class="pre">float\]</span>*<a href="#fdtdx.PerfectlyMatchedLayer.max_random_real_offsets" class="headerlink" title="Link to this definition">#</a>  
Maximum random offset values that can be applied to the object’s position in real coordinates for each axis (x, y, z). Defaults to (0, 0, 0) for no random offset.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">str</span>*<a href="#fdtdx.PerfectlyMatchedLayer.name" class="headerlink" title="Link to this definition">#</a>  
Unique identifier for the object. Automatically enforced to be unique through the UniqueName validator. The user can also set a name manually.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">partial_grid_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialGridShape3D</span>*<a href="#fdtdx.PerfectlyMatchedLayer.partial_grid_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in grid coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">partial_real_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.PerfectlyMatchedLayer.partial_real_position" class="headerlink" title="Link to this definition">#</a>  
The object’s position in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">partial_real_shape</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">PartialRealShape3D</span>*<a href="#fdtdx.PerfectlyMatchedLayer.partial_real_shape" class="headerlink" title="Link to this definition">#</a>  
The object’s shape in real-world coordinates. Defaults to UNDEFINED_SHAPE_3D if not specified.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">pml_a_E</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.pml_a_E" class="headerlink" title="Link to this definition">#</a>  
CPML ‘a’ coefficient array for Electric field updates.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">pml_a_H</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.pml_a_H" class="headerlink" title="Link to this definition">#</a>  
CPML ‘a’ coefficient array for Magnetic field updates.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">pml_b_E</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.pml_b_E" class="headerlink" title="Link to this definition">#</a>  
CPML ‘b’ coefficient array for Electric field updates.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">pml_b_H</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.pml_b_H" class="headerlink" title="Link to this definition">#</a>  
CPML ‘b’ coefficient array for Magnetic field updates.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">real_shape</span></span><a href="#fdtdx.PerfectlyMatchedLayer.real_shape" class="headerlink" title="Link to this definition">#</a>  
Physical side lengths covered by this object’s placed grid slice.

The value is derived from <span class="pre">`SimulationConfig.grid`</span> when available. That keeps object geometry tied to physical edge coordinates instead of a global scalar resolution. During early placement, before a concrete grid has been attached to the config, the legacy uniform-resolution fallback is still used for compatibility.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">sigma_end</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.sigma_end" class="headerlink" title="Link to this definition">#</a>  
Final sigma value. Defaults to 1.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">sigma_order</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.sigma_order" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading. Defaults to 3.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">sigma_start</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.PerfectlyMatchedLayer.sigma_start" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value. Defaults to 0.0 if not provided.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">thickness</span></span><a href="#fdtdx.PerfectlyMatchedLayer.thickness" class="headerlink" title="Link to this definition">#</a>  
Gets the thickness of the PML layer in grid points.

Returns<span class="colon">:</span>  
Number of grid points in the PML along its axis

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">uses_wrap_padding</span></span><a href="#fdtdx.PerfectlyMatchedLayer.uses_wrap_padding" class="headerlink" title="Link to this definition">#</a>  
Whether this boundary’s axis should use wrap (periodic) padding.

Returns True for boundaries that connect opposite sides of the domain (periodic, Bloch). Returns False for terminating boundaries (PEC, PMC, PML).

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">apply</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">key</span></span>*, *<span class="n"><span class="pre">inv_permittivities</span></span>*, *<span class="n"><span class="pre">inv_permeabilities</span></span>*, *<span class="n"><span class="pre">dispersive_c1</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c2</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c3</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.apply" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">apply_field_reset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">fields</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/perfectly_matched_layer.html#PerfectlyMatchedLayer.apply_field_reset" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PerfectlyMatchedLayer.apply_field_reset" class="headerlink" title="Link to this definition">#</a>  
Zero all field components within the PML region.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">apply_pad_correction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">padded_fields</span></span>*, *<span class="n"><span class="pre">volume_shape</span></span>*, *<span class="n"><span class="pre">resolution</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.apply_pad_correction" class="headerlink" title="Link to this definition">#</a>  
Apply boundary-specific correction to padded fields.

Called after basic wrap/constant padding. Default is a no-op. Subclasses like BlochBoundary override this to apply phase shifts to ghost cells.

Parameters<span class="colon">:</span>  
- **padded_fields** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – Padded field array of shape (3, Nx+2, Ny+2, Nz+2)

- **volume_shape** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>) – Full simulation volume shape (Nx, Ny, Nz)

- **resolution** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Grid resolution in meters

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

Returns<span class="colon">:</span>  
Padded fields with boundary-specific corrections applied

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">apply_post_E_update</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.apply_post_E_update" class="headerlink" title="Link to this definition">#</a>  
Apply boundary-specific enforcement after E field update.

Called after each E field update (forward and reverse). Default is a no-op. Subclasses like PEC override this to zero tangential E components.

Parameters<span class="colon">:</span>  
**E** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – Electric field array of shape (3, Nx, Ny, Nz)

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

Returns<span class="colon">:</span>  
E field with boundary conditions enforced

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">apply_post_H_update</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">H</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.apply_post_H_update" class="headerlink" title="Link to this definition">#</a>  
Apply boundary-specific enforcement after H field update.

Called after each H field update (forward and reverse). Default is a no-op. Subclasses like PMC override this to zero tangential H components.

Parameters<span class="colon">:</span>  
**H** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – Magnetic field array of shape (3, Nx, Ny, Nz)

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>

Returns<span class="colon">:</span>  
H field with boundary conditions enforced

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">check_overlap</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.check_overlap" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">extend_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.extend_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">face_to_face_negative_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.face_to_face_negative_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">face_to_face_positive_direction</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.face_to_face_positive_direction" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">interface_grid_shape</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.interface_grid_shape" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">interface_slice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.interface_slice" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`slice`</span>, <span class="pre">`slice`</span>, <span class="pre">`slice`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">interface_slice_tuple</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.interface_slice_tuple" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\], <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\], <span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>\]\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">place_above</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.place_above" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">place_at_center</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.place_at_center" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">place_below</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.place_below" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">place_on_grid</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">grid_slice_tuple</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/perfectly_matched_layer.html#PerfectlyMatchedLayer.place_on_grid" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PerfectlyMatchedLayer.place_on_grid" class="headerlink" title="Link to this definition">#</a>  
Place the PML on the grid and calculate any remaining defaults.

This is called after initialization, so grid_shape and config are available.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">place_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">own_positions</span></span>*, *<span class="n"><span class="pre">other_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.place_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">same_position</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">own_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">other_positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.same_position" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">same_position_and_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.same_position_and_size" class="headerlink" title="Link to this definition">#</a>  
Creates both position and size constraints to make this object match another object’s position and size. This is a convenience wrapper combining place_at_center() and same_size().

Parameters<span class="colon">:</span>  
- **other** (<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>) – Another object in the simulation scene

- **axes** (*tuple\[int,* *...\]* *\|* *int,* *optional*) – Either a single integer or a tuple describing which axes to match. Defaults to all axes (0, 1, 2).

Returns<span class="colon">:</span>  
Position and size constraints for matching objects

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>, <a href="fdtdx.SizeConstraint.html#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint">SizeConstraint</a>\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">same_size</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">1,</span> <span class="pre">2)</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.same_size" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">set_grid_coordinates</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.set_grid_coordinates" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">size_relative_to</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">other</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">proportions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.size_relative_to" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">step_cpml</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">d_field_1</span></span>*, *<span class="n"><span class="pre">d_field_2</span></span>*, *<span class="n"><span class="pre">psi_1</span></span>*, *<span class="n"><span class="pre">psi_2</span></span>*, *<span class="n"><span class="pre">is_curl_E</span></span>*, *<span class="n"><span class="pre">simulate_boundaries</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/perfectly_matched_layer.html#PerfectlyMatchedLayer.step_cpml" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PerfectlyMatchedLayer.step_cpml" class="headerlink" title="Link to this definition">#</a>  
Performs localized CPML correction for the two derivatives along this boundary’s axis.

Uses Auxiliary Differential Equations (ADEs) to update the psi arrays and applies the complex coordinate stretching corrections to the spatial derivatives.

Parameters<span class="colon">:</span>  
- **d_field_1** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – The first spatial derivative array needing PML correction.

- **d_field_2** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – The second spatial derivative array needing PML correction.

- **psi_1** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – The accumulator array (psi) corresponding to the first derivative.

- **psi_2** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span></span>) – The accumulator array (psi) corresponding to the second derivative.

- **is_curl_E** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Flag determining whether to use H-field coefficients (True, when computing curl(E) to update H) or E-field coefficients (False, when computing curl(H) to update E).

- **simulate_boundaries** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Flag to toggle whether the boundary memory variables (psi) should actually be updated in this step.

Returns<span class="colon">:</span>  
A tuple containing: - corr_1: The PML-corrected first spatial derivative. - corr_2: The PML-corrected second spatial derivative. - psi_1_new: The updated accumulator array for the first derivative. - psi_2_new: The updated accumulator array for the second derivative.

Return type<span class="colon">:</span>  
tuple\[jax.Array, jax.Array, jax.Array, jax.Array\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PerfectlyMatchedLayer.</span></span><span class="sig-name descname"><span class="pre">validate_placement</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.PerfectlyMatchedLayer.validate_placement" class="headerlink" title="Link to this definition">#</a>  
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
