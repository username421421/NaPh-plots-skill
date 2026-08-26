<div id="fdtdx-unfold-detector-states" class="section">

# fdtdx.unfold_detector_states<a href="#fdtdx-unfold-detector-states" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">unfold_detector_states</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">config</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/symmetry.html#unfold_detector_states" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.unfold_detector_states" class="headerlink" title="Link to this definition">#</a>  
Reconstruct full-domain detector states from a symmetry-reduced simulation.

This is a pure post-processing step: it transforms each detector’s stored reduced-domain output into the full-domain result using the parity table, with no work added to the FDTD time loop. Each detector that sits on one or more symmetry planes is unfolded per its type — spatial outputs are mirrored with the correct per-component parity; <span class="pre">`reduce_volume`</span> sums/means are rescaled per component (even components double/keep, odd components vanish); <span class="pre">`as_slices`</span> energy planes are mirrored along their in-plane symmetric axes. Detectors that do not touch any symmetry plane are returned unchanged.

All detector types are supported except <span class="pre">`DiffractiveDetector`</span>, whose diffraction-order basis depends on the domain size and so cannot be recovered from the stored efficiencies; for that, unfold the fields with <a href="fdtdx.unfold_fields.html#fdtdx.unfold_fields" class="reference internal" title="fdtdx.unfold_fields"><span class="pre"><code class="sourceCode python">unfold_fields()</code></span></a> and recompute.

Parameters<span class="colon">:</span>  
- **arrays** (<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><em>ArrayContainer</em></a>) – Arrays returned by the reduced simulation.

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – The placed (reduced) objects.

- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Simulation config (must have nonzero <span class="pre">`symmetry`</span>).

Returns<span class="colon">:</span>  
A copy of <span class="pre">`arrays`</span> with <span class="pre">`detector_states`</span> reconstructed to full domain.

Return type<span class="colon">:</span>  
<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer">ArrayContainer</a>

Raises<span class="colon">:</span>  
- **ValueError** – If <span class="pre">`config.symmetry`</span> is <span class="pre">`(0,`</span>` `<span class="pre">`0,`</span>` `<span class="pre">`0)`</span> (nothing to unfold).

- **NotImplementedError** – For a <span class="pre">`DiffractiveDetector`</span> (see above).

</div>
