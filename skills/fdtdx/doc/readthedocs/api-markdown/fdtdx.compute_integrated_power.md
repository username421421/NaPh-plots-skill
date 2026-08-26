<div id="fdtdx-compute-integrated-power" class="section">

# fdtdx.compute_integrated_power<a href="#fdtdx-compute-integrated-power" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_integrated_power</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">area_weights</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/metrics.html#compute_integrated_power" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_integrated_power" class="headerlink" title="Link to this definition">#</a>  
Computes the integrated power (Poynting flux) across a transverse plane.

Parameters<span class="colon">:</span>  
- **E** (*jax.Array*) – Electric field array with component axis first.

- **H** (*jax.Array*) – Magnetic field array with component axis first.

- **axis** (*int*) – Physical propagation axis whose Poynting component is integrated.

- **area_weights** (*jax.Array* *\|* *None,* *optional*) – Optional detector-plane area weights broadcastable to <span class="pre">`E[axis]`</span>. Defaults to None.

Returns<span class="colon">:</span>  
The absolute integrated power.

Return type<span class="colon">:</span>  
jax.Array

</div>
