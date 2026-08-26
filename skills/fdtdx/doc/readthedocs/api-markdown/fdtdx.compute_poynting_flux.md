<div id="fdtdx-compute-poynting-flux" class="section">

# fdtdx.compute_poynting_flux<a href="#fdtdx-compute-poynting-flux" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_poynting_flux</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/metrics.html#compute_poynting_flux" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_poynting_flux" class="headerlink" title="Link to this definition">#</a>  
Calculates the Poynting vector (energy flux) from E and H fields.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Electric field array with shape (3, nx, ny, nz)

- **H** (*jax.Array*) – Magnetic field array with shape (3, nx, ny, nz)

- **axis** (*int,* *optional*) – Axis for computing the poynting flux. Defaults to 0.

Returns<span class="colon">:</span>  
Poynting vector array with shape (3, nx, ny, nz) representing energy flux in each direction

Return type<span class="colon">:</span>  
jax.Array

</div>
