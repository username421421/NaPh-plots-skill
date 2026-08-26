<div id="fdtdx-compute-eps-spectrum-from-coefficients" class="section">

# fdtdx.compute_eps_spectrum_from_coefficients<a href="#fdtdx-compute-eps-spectrum-from-coefficients" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_eps_spectrum_from_coefficients</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">c1</span></span>*, *<span class="n"><span class="pre">c2</span></span>*, *<span class="n"><span class="pre">c3</span></span>*, *<span class="n"><span class="pre">inv_eps_inf</span></span>*, *<span class="n"><span class="pre">omegas</span></span>*, *<span class="n"><span class="pre">dt</span></span>*, *<span class="n"><span class="pre">weights</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">c4</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#compute_eps_spectrum_from_coefficients" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_eps_spectrum_from_coefficients" class="headerlink" title="Link to this definition">#</a>  
Spatially-averaged complex permittivity spectrum for a block of cells.

For each angular frequency in <span class="pre">`omegas`</span>, evaluates the per-cell complex permittivity <span class="math notranslate nohighlight">\\\varepsilon(\omega) = \varepsilon\_\infty + \chi(\omega)\\</span> where <span class="math notranslate nohighlight">\\\chi\\</span> is reconstructed from the ADE recurrence coefficients, and averages over the spatial axes (uniformly or with supplied weights).

This is the broadband generalization of the single-frequency <span class="pre">`effective_inv_permittivity()`</span> used for carrier-frequency impedance matching — callers that need a frequency-dependent impedance (e.g. for a convolution-based broadband source correction) use this to build the <span class="math notranslate nohighlight">\\\varepsilon(\omega)\\</span> spectrum that feeds <a href="fdtdx.compute_impedance_corrected_temporal_profile.html#fdtdx.compute_impedance_corrected_temporal_profile" class="reference internal" title="fdtdx.compute_impedance_corrected_temporal_profile"><span class="pre"><code class="sourceCode python">compute_impedance_corrected_temporal_profile()</code></span></a>.

Parameters<span class="colon">:</span>  
- **c1** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`ndarray`</span></span>) – ADE coefficient array of shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`num_components,`</span>` `<span class="pre">`*spatial)`</span> as stored on <a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a>, with <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3)`</span> (the material-component axis; size 3 for per-axis anisotropic dispersion). Anisotropic components are averaged, mirroring the <span class="pre">`inv_eps_inf`</span> reduction.

- **c2** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`ndarray`</span></span>) – ADE coefficient array, same shape as <span class="pre">`c1`</span>.

- **c3** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`ndarray`</span></span>) – ADE coefficient array, same shape as <span class="pre">`c1`</span>.

- **inv_eps_inf** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`ndarray`</span></span>) – Per-cell inverse of the high-frequency permittivity, shape <span class="pre">`(num_components,`</span>` `<span class="pre">`*spatial)`</span> with <span class="pre">`num_components`</span>` `<span class="pre">`in`</span>` `<span class="pre">`(1,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`9)`</span>. For anisotropic tensors (9 components) only the diagonal entries are used.

- **omegas** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span></span>) – 1D array of angular frequencies (rad/s) to evaluate at.

- **dt** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Simulation time step (seconds) used to derive the coefficients.

- **weights** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span> \| <span class="pre">`None`</span></span>) – Optional spatial weights with the same shape as the trailing axes of <span class="pre">`c1`</span>. If <span class="pre">`None`</span>, uniform averaging.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span></span>

Returns<span class="colon">:</span>  
Complex numpy array of shape <span class="pre">`(len(omegas),)`</span> — the volume-averaged <span class="math notranslate nohighlight">\\\varepsilon(\omega)\\</span> at each requested frequency.

</div>
