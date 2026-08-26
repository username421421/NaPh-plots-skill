<div id="fdtdx-plot-field-slice" class="section">

# fdtdx.plot_field_slice<a href="#fdtdx-plot-field-slice" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">plot_field_slice</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">axs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/plot_field_slice.html#plot_field_slice" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.plot_field_slice" class="headerlink" title="Link to this definition">#</a>  
Creates a visualization of electromagnetic field components.

Generates a 2x3 subplot showing all six components of the electromagnetic field (Ex, Ey, Ez, Hx, Hy, Hz) in a single figure.

Parameters<span class="colon">:</span>  
- **E** (*jnp.ndarray*) – Electric field array of shape (3, nx, ny, nz) or (3, w, h)

- **H** (*jnp.ndarray*) – Magnetic field array of shape (3, nx, ny, nz) or (3, w, h)

- **filename** (*str* *\|* *Path* *\|* *None,* *optional*) – If provided, saves the plot to this file

- **axs** (*Any* *\|* *None,* *optional*) – Optional matplotlib axes to plot on. If None, creates new figure

- **plot_legend** (*bool,* *optional*) – Whether to add colorbar legends

Returns<span class="colon">:</span>  
The generated figure object

Return type<span class="colon">:</span>  
Figure

Raises<span class="colon">:</span>  
**ValueError** – If arrays have incorrect shapes or contain invalid values

<div class="admonition note">

Note

For 4D inputs (3, nx, ny, nz), exactly one of nx, ny, nz must be 1. The function will automatically squeeze out the singleton dimension.

</div>

</div>
