<div id="fdtdx-unfold-source-mode" class="section">

# fdtdx.unfold_source_mode<a href="#fdtdx-unfold-source-mode" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">unfold_source_mode</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">source</span></span>*, *<span class="n"><span class="pre">config</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/symmetry.html#unfold_source_mode" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.unfold_source_mode" class="headerlink" title="Link to this definition">#</a>  
Reconstruct the full-domain <span class="pre">`(E,`</span>` `<span class="pre">`H)`</span> mode profile a mode source injects.

A <a href="fdtdx.ModePlaneSource.html#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.ModePlaneSource"><span class="pre"><code class="sourceCode python">ModePlaneSource</code></span></a> solves and stores its mode on the *reduced* cross-section (<span class="pre">`source._E`</span> / <span class="pre">`source._H`</span>, real, shape <span class="pre">`(3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span> with a singleton on the propagation axis). This mirrors that profile back to the full transverse cross-section with the correct per-component parity. Only the two transverse axes are unfolded — the propagation axis is never a symmetry plane for a mode source (its mode plane is one cell thick there).

Convenience wrapper so callers don’t reach into the private <span class="pre">`_E`</span> / <span class="pre">`_H`</span> state; for the fields *recorded during the run*, prefer a detector on the source plane plus <a href="fdtdx.unfold_detector_states.html#fdtdx.unfold_detector_states" class="reference internal" title="fdtdx.unfold_detector_states"><span class="pre"><code class="sourceCode python">unfold_detector_states()</code></span></a>.

Parameters<span class="colon">:</span>  
- **source** – A placed mode source whose <span class="pre">`apply`</span> has already run (so <span class="pre">`_E`</span> / <span class="pre">`_H`</span> are populated), e.g. a <a href="fdtdx.ModePlaneSource.html#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.ModePlaneSource"><span class="pre"><code class="sourceCode python">ModePlaneSource</code></span></a>. Run <a href="fdtdx.apply_params.html#fdtdx.apply_params" class="reference internal" title="fdtdx.apply_params"><span class="pre"><code class="sourceCode python">fdtdx.apply_params()</code></span></a> first.

- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Simulation config; must have nonzero <span class="pre">`symmetry`</span> on at least one axis transverse to the source’s propagation axis.

Returns<span class="colon">:</span>  
Full-domain <span class="pre">`(E,`</span>` `<span class="pre">`H)`</span> mode profiles, shape <span class="pre">`(3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>.

Return type<span class="colon">:</span>  
tuple\[jax.Array, jax.Array\]

Raises<span class="colon">:</span>  
**ValueError** – If the mode has not been computed yet, the source is not a plane, or there is no transverse symmetry to unfold.

</div>
