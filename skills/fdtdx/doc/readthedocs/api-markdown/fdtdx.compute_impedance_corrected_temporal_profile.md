<div id="fdtdx-compute-impedance-corrected-temporal-profile" class="section">

# fdtdx.compute_impedance_corrected_temporal_profile<a href="#fdtdx-compute-impedance-corrected-temporal-profile" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">compute_impedance_corrected_temporal_profile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">raw_samples</span></span>*, *<span class="n"><span class="pre">dt</span></span>*, *<span class="n"><span class="pre">eps_spectrum</span></span>*, *<span class="n"><span class="pre">eps_center</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#compute_impedance_corrected_temporal_profile" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.compute_impedance_corrected_temporal_profile" class="headerlink" title="Link to this definition">#</a>  
FIR-filter a raw source temporal profile for broadband impedance matching.

Given the unfiltered E-side temporal profile <span class="pre">`s(n·dt)`</span> and the complex permittivity spectrum <span class="pre">`eps_spectrum`</span>` `<span class="pre">`=`</span>` `<span class="pre">`ε(ω_k)`</span> at the rFFT frequencies of a zero-padded version of <span class="pre">`s`</span>, returns the H-side temporal profile <span class="pre">`s_H(n·dt)`</span> whose spectrum satisfies <span class="math notranslate nohighlight">\\\tilde{s}\_H(\omega) = \tilde{s}(\omega) \cdot G(\omega)\\</span> with

<div class="math notranslate nohighlight">

\\G(\omega) = \frac{\eta(\omega_c)}{\eta(\omega)} = \sqrt{\frac{\varepsilon(\omega)}{\varepsilon(\omega_c)}}\\

</div>

(assuming a non-dispersive permeability). Injecting the prescribed E and H fields as <span class="pre">`E(x,t)`</span>` `<span class="pre">`=`</span>` `<span class="pre">`E_spatial(x)·s(t)`</span> and <span class="pre">`H(x,t)`</span>` `<span class="pre">`=`</span>` `<span class="pre">`(H_spatial(x)/η(ω_c))·s_H(t)`</span> then reproduces a physical plane wave at every frequency in the pulse bandwidth, not just at <span class="pre">`ω_c`</span>. In the non-dispersive limit <span class="pre">`ε(ω)`</span>` `<span class="pre">`≡`</span>` `<span class="pre">`ε_c`</span> and <span class="pre">`G`</span> is the identity so <span class="pre">`s_H`</span>` `<span class="pre">`==`</span>` `<span class="pre">`s`</span>.

Implementation: zero-pads to <span class="pre">`M`</span>` `<span class="pre">`=`</span>` `<span class="pre">`2·(len(eps_spectrum)`</span>` `<span class="pre">`-`</span>` `<span class="pre">`1)`</span> for linear convolution, takes a real FFT, multiplies by <span class="pre">`G`</span>, and transforms back with <span class="pre">`numpy.fft.irfft()`</span> (which enforces a real output via Hermitian symmetry of the positive-frequency spectrum).

Parameters<span class="colon">:</span>  
- **raw_samples** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span></span>) – Real 1-D array of the unfiltered temporal profile sampled at integer time steps, <span class="pre">`s[n]`</span>` `<span class="pre">`=`</span>` `<span class="pre">`s(n·dt)`</span>.

- **dt** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Simulation time step (seconds). Present for API symmetry; the actual time step is encoded in <span class="pre">`eps_spectrum`</span>.

- **eps_spectrum** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span></span>) – Complex 1-D array of length <span class="pre">`M/2`</span>` `<span class="pre">`+`</span>` `<span class="pre">`1`</span> giving <span class="math notranslate nohighlight">\\\varepsilon(\omega)\\</span> at <span class="math notranslate nohighlight">\\\omega_k = 2\pi \cdot k / (M \cdot \Delta t)\\</span> for <span class="pre">`k`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0,`</span>` `<span class="pre">`...,`</span>` `<span class="pre">`M/2`</span>.

- **eps_center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span></span>) – Scalar complex <span class="math notranslate nohighlight">\\\varepsilon(\omega_c)\\</span> at the source carrier frequency.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`ndarray`</span></span>

Returns<span class="colon">:</span>  
Real 1-D array of length <span class="pre">`len(raw_samples)`</span> containing <span class="pre">`s_H[n]`</span>.

</div>
