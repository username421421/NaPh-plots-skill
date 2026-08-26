<div id="fdtdx-compute-energy" class="section">

# fdtdx.compute_energy<a href="#fdtdx-compute-energy" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">inv_permittivity</span></span>*, *<span class="n"><span class="pre">inv_permeability</span></span>*, *<span class="n"><span class="pre">axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/metrics.html#compute_energy" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_energy" class="headerlink" title="Link to this definition">#</a>  
Computes the total electromagnetic energy density of the field.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Electric field array with shape (3, nx, ny, nz)

- **H** (*jax.Array*) – Magnetic field array with shape (3, nx, ny, nz)

- **inv_permittivity** (*jax.Array* *\|* *float*) – Inverse permittivity. Shape (3, nx, ny, nz) for anisotropic or scalar

- **inv_permeability** (*jax.Array* *\|* *float*) – Inverse permeability. Shape (3, nx, ny, nz) for anisotropic or scalar

- **axis** (*int,* *optional*) – Axis index of the X,Y,Z component for the E and H field. Defaults to 0.

Returns<span class="colon">:</span>  
Total energy density array with shape (nx, ny, nz)

Return type<span class="colon">:</span>  
jax.Array

</div>
