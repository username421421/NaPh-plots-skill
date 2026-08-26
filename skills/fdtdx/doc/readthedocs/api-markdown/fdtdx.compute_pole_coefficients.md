<div id="fdtdx-compute-pole-coefficients" class="section">

# fdtdx.compute_pole_coefficients<a href="#fdtdx-compute-pole-coefficients" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_pole_coefficients</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">poles</span></span>*, *<span class="n"><span class="pre">dt</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#compute_pole_coefficients" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_pole_coefficients" class="headerlink" title="Link to this definition">#</a>  
Compute the discrete-time ADE recurrence coefficients of isotropic poles.

Scalar-per-pole variant of <a href="fdtdx.compute_pole_coefficients_per_axis.html#fdtdx.compute_pole_coefficients_per_axis" class="reference internal" title="fdtdx.compute_pole_coefficients_per_axis"><span class="pre"><code class="sourceCode python">compute_pole_coefficients_per_axis()</code></span></a> (see there for the coefficient definitions). Raises <span class="pre">`ValueError`</span> when any pole has per-axis parameters — use the per-axis function for those.

Parameters<span class="colon">:</span>  
- **poles** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<a href="fdtdx.Pole.html#fdtdx.Pole" class="reference internal" title="fdtdx.dispersion.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a>, <span class="pre">`...`</span>\]</span>) – Tuple of isotropic poles (may be empty).

- **dt** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Simulation time step (seconds).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>\]</span>

Returns<span class="colon">:</span>  
Four <span class="pre">`numpy`</span> arrays of shape <span class="pre">`(len(poles),)`</span> with <span class="pre">`c1`</span>, <span class="pre">`c2`</span>, <span class="pre">`c3`</span>, <span class="pre">`c4`</span>. For an empty pole tuple, returns four empty arrays.

</div>
