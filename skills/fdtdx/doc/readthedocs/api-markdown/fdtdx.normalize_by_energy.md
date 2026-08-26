<div id="fdtdx-normalize-by-energy" class="section">

# fdtdx.normalize_by_energy<a href="#fdtdx-normalize-by-energy" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">normalize_by_energy</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">inv_permittivity</span></span>*, *<span class="n"><span class="pre">inv_permeability</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/metrics.html#normalize_by_energy" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.normalize_by_energy" class="headerlink" title="Link to this definition">#</a>  
Normalizes electromagnetic fields by their total energy.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Electric field array with shape (3, nx, ny, nz)

- **H** (*jax.Array*) – Magnetic field array with shape (3, nx, ny, nz)

- **inv_permittivity** (*jax.Array* *\|* *float*) – Inverse of the electric permittivity array

- **inv_permeability** (*jax.Array* *\|* *float*) – Inverse of the magnetic permeability array

Returns<span class="colon">:</span>  
Tuple of (normalized E field, normalized H field)

Return type<span class="colon">:</span>  
tuple\[jax.Array, jax.Array\]

</div>
