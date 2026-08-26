<div id="fdtdx-compute-pole-coefficients-per-axis" class="section">

# fdtdx.compute_pole_coefficients_per_axis<a href="#fdtdx-compute-pole-coefficients-per-axis" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_pole_coefficients_per_axis</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">poles</span></span>*, *<span class="n"><span class="pre">dt</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#compute_pole_coefficients_per_axis" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_pole_coefficients_per_axis" class="headerlink" title="Link to this definition">#</a>  
Compute the per-axis discrete-time ADE recurrence coefficients.

For each pole and grid axis, returns <span class="pre">`(c1,`</span>` `<span class="pre">`c2,`</span>` `<span class="pre">`c3,`</span>` `<span class="pre">`c4)`</span> with (<span class="pre">`D`</span>` `<span class="pre">`=`</span>` `<span class="pre">`1`</span>` `<span class="pre">`+`</span>` `<span class="pre">`gamma`</span>` `<span class="pre">`dt`</span>` `<span class="pre">`/`</span>` `<span class="pre">`2`</span>)

<div class="math notranslate nohighlight">

\\c_1 = \frac{2 - \omega_0^2 \Delta t^2}{D}, \quad c_2 = -\frac{1 - \gamma \Delta t / 2}{D}, \quad c_3 = \frac{a \Delta t^2 - b \Delta t}{D}, \quad c_4 = \frac{b \Delta t}{D},\\

</div>

where <span class="pre">`a`</span>` `<span class="pre">`=`</span>` `<span class="pre">`coupling_sq`</span> is the <span class="pre">`E`</span> coupling and <span class="pre">`b`</span>` `<span class="pre">`=`</span>` `<span class="pre">`coupling_edot`</span> is the <span class="pre">`dE/dt`</span> coupling. The recurrence uses a forward difference for the <span class="pre">`dE/dt`</span> term so it stays compatible with the reversible time stepping:

<span class="math notranslate nohighlight">\\p_p^{n+1} = c_1 p_p^n + c_2 p_p^{n-1} + c_3 E^n + c_4 E^{n+1}\\</span>.

For isotropic poles the three axis columns are identical. For Lorentz and Drude poles <span class="pre">`b`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0`</span>, so <span class="pre">`c4`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0`</span> and <span class="pre">`c3`</span> reduces to the classic <span class="math notranslate nohighlight">\\K \Delta t^2 / D\\</span>.

Parameters<span class="colon">:</span>  
- **poles** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<a href="fdtdx.Pole.html#fdtdx.Pole" class="reference internal" title="fdtdx.dispersion.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a>, <span class="pre">`...`</span>\]</span>) – Tuple of poles (may be empty).

- **dt** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Simulation time step (seconds).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>\]</span>

Returns<span class="colon">:</span>  
Four <span class="pre">`numpy`</span> arrays of shape <span class="pre">`(len(poles),`</span>` `<span class="pre">`3)`</span> with <span class="pre">`c1`</span>, <span class="pre">`c2`</span>, <span class="pre">`c3`</span>, <span class="pre">`c4`</span> per pole and axis. For an empty pole tuple, returns four <span class="pre">`(0,`</span>` `<span class="pre">`3)`</span> arrays.

</div>
