<div id="fdtdx-plot-field-slice-component" class="section">

# fdtdx.plot_field_slice_component<a href="#fdtdx-plot-field-slice-component" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">plot_field_slice_component</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">field</span></span>*, *<span class="n"><span class="pre">component_name</span></span>*, *<span class="n"><span class="pre">ax</span></span>*, *<span class="n"><span class="pre">plot_legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/plot_field_slice.html#plot_field_slice_component" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.plot_field_slice_component" class="headerlink" title="Link to this definition">#</a>  
Plots a single component of the electromagnetic field.

Parameters<span class="colon">:</span>  
- **field** (*jnp.ndarray*) – 2D array of shape (w, h) containing field values

- **component_name** (*str*) – Name of the component (e.g., ‘Ex’, ‘Hy’)

- **ax** (*Any*) – Matplotlib axis to plot on

- **plot_legend** (*bool,* *optional*) – Whether to add a colorbar legend

Raises<span class="colon">:</span>  
**ValueError** – If field is not 2D or contains invalid values

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`None`</span></span>

</div>
