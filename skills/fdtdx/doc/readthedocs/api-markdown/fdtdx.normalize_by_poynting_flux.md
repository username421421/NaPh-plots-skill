<div id="fdtdx-normalize-by-poynting-flux" class="section">

# fdtdx.normalize_by_poynting_flux<a href="#fdtdx-normalize-by-poynting-flux" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">normalize_by_poynting_flux</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">area_weights</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/metrics.html#normalize_by_poynting_flux" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.normalize_by_poynting_flux" class="headerlink" title="Link to this definition">#</a>  
Normalize fields so the integrated Poynting flux along <span class="pre">`axis`</span> is one.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Electric field array with component axis first.

- **H** (*jax.Array*) – Magnetic field array with component axis first.

- **axis** (*int*) – Physical propagation axis whose Poynting component is integrated.

- **area_weights** (*jax.Array* *\|* *None,* *optional*) – Optional detector-plane area weights broadcastable to <span class="pre">`E[axis]`</span>. Uniform-grid callers may omit this for the historical raw-sum normalization; non-uniform callers should provide weights so refinement alone does not change the normalization.

Returns<span class="colon">:</span>  
Tuple of (normalized E field, normalized H field)

Return type<span class="colon">:</span>  
tuple\[jax.Array, jax.Array\]

</div>
