<div id="fdtdx-singlefrequencyprofile" class="section">

# fdtdx.SingleFrequencyProfile<a href="#fdtdx-singlefrequencyprofile" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">SingleFrequencyProfile</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">num_startup_periods</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">4</span></span>*, *<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">3.141592653589793</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/sources/profile.html#SingleFrequencyProfile" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SingleFrequencyProfile" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TemporalProfile.html#fdtdx.TemporalProfile" class="reference internal" title="fdtdx.objects.sources.profile.TemporalProfile"><span class="pre"><code class="sourceCode python">TemporalProfile</code></span></a>

Simple sinusoidal temporal profile at a single frequency.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.SingleFrequencyProfile.num_startup_periods" class="reference internal" title="fdtdx.SingleFrequencyProfile.num_startup_periods"><span class="pre"><code class="sourceCode python">num_startup_periods</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.phase_shift" class="reference internal" title="fdtdx.SingleFrequencyProfile.phase_shift"><span class="pre"><code class="sourceCode python">phase_shift</code></span></a>

Methods

- <a href="#fdtdx.SingleFrequencyProfile.aset" class="reference internal" title="fdtdx.SingleFrequencyProfile.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.frequency_spectrum" class="reference internal" title="fdtdx.SingleFrequencyProfile.frequency_spectrum"><span class="pre"><code class="sourceCode python">frequency_spectrum</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_amplitude" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_amplitude"><span class="pre"><code class="sourceCode python">get_amplitude</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_class_fields" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_frequency_plot_range" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_frequency_plot_range"><span class="pre"><code class="sourceCode python">get_frequency_plot_range</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_public_fields" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_reference_frequency" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_reference_frequency"><span class="pre"><code class="sourceCode python">get_reference_frequency</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.get_time_plot_range" class="reference internal" title="fdtdx.SingleFrequencyProfile.get_time_plot_range"><span class="pre"><code class="sourceCode python">get_time_plot_range</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.plot_time_signal_and_spectrum" class="reference internal" title="fdtdx.SingleFrequencyProfile.plot_time_signal_and_spectrum"><span class="pre"><code class="sourceCode python">plot_time_signal_and_spectrum</code></span></a>

- <a href="#fdtdx.SingleFrequencyProfile.sample_time_signal" class="reference internal" title="fdtdx.SingleFrequencyProfile.sample_time_signal"><span class="pre"><code class="sourceCode python">sample_time_signal</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">num_startup_periods</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.SingleFrequencyProfile.num_startup_periods" class="headerlink" title="Link to this definition">#</a>  
number of periods between start

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">phase_shift</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.SingleFrequencyProfile.phase_shift" class="headerlink" title="Link to this definition">#</a>  
Phase shift of the carrier wave

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.aset" class="headerlink" title="Link to this definition">#</a>  
Sets an attribute of this class. In contrast to the classical .at\[\].set(), this method updates the class attribute directly and does not only operate on jax pytree leaf nodes. Instead, replaces the full attribute with the new value.

The attribute can either be the attribute name of this class, or for nested classes it can also be the attribute name of a class, which itself is an attribute of this class. The syntax for this operation could look like this: “a-\>b-\>\[0\]-\>\[‘name’\]”. Here, the current class has an attribute a, which has an attribute b, which is a list, which we index at index 0, which is an element of type dictionary, which we index using the dictionary key ‘name’.

Note that dictionary keys cannot contain square brackets or single quotes (even if they are escaped).

Parameters<span class="colon">:</span>  
- **attr_name** (*str*) – Name of attribute to set

- **val** (*Any*) – Value to set the attribute to

- **create_new_ok** (*bool,* *optional*) – If false (default), throw an error if the attribute does not exist. If true, creates a new attribute if the attribute name does not exist yet.

Returns<span class="colon">:</span>  
Updated instance with new attribute value

Return type<span class="colon">:</span>  
Self

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">frequency_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*, *<span class="n"><span class="pre">num_time_steps</span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">normalize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.frequency_spectrum" class="headerlink" title="Link to this definition">#</a>  
Return the one-sided FFT magnitude of the sampled source signal.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_amplitude</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time</span></span>*, *<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/sources/profile.html#SingleFrequencyProfile.get_amplitude" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SingleFrequencyProfile.get_amplitude" class="headerlink" title="Link to this definition">#</a>  
Calculate the temporal amplitude at given time points.

Parameters<span class="colon">:</span>  
- **time** (*jax.Array*) – Time points to evaluate amplitude at

- **period** (*float*) – Period of the carrier wave (1/frequency)

- **phase_shift** (*float*) – Phase shift of the carrier wave

Returns<span class="colon">:</span>  
Amplitude values at the given time points

Return type<span class="colon">:</span>  
jax.Array

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_frequency_plot_range</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">frequencies</span></span>*, *<span class="n"><span class="pre">spectrum</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.get_frequency_plot_range" class="headerlink" title="Link to this definition">#</a>  
Return a profile-specific frequency plot range, or None to use automatic range detection.

Subclasses may override this hook when the profile has known physical frequency properties (e.g. a Gaussian pulse).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>\] \| <span class="pre">`None`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_reference_frequency</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.get_reference_frequency" class="headerlink" title="Link to this definition">#</a>  
Return the frequency expected to dominate the plotted spectrum.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">get_time_plot_range</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">total_time</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.get_time_plot_range" class="headerlink" title="Link to this definition">#</a>  
Return a profile-specific time plot range, or None to use automatic range detection.

Subclasses may override this hook when the profile has known physical time properties (e.g. a Gaussian pulse).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>\] \| <span class="pre">`None`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">plot_time_signal_and_spectrum</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*, *<span class="n"><span class="pre">num_time_steps</span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">axs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">time_range</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'auto'</span></span>*, *<span class="n"><span class="pre">frequency_range</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'auto'</span></span>*, *<span class="n"><span class="pre">relative_threshold</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.01</span></span>*, *<span class="n"><span class="pre">normalize_spectrum</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.plot_time_signal_and_spectrum" class="headerlink" title="Link to this definition">#</a>  
Plot the sampled source time signal and its one-sided frequency spectrum.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SingleFrequencyProfile.</span></span><span class="sig-name descname"><span class="pre">sample_time_signal</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">period</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*, *<span class="n"><span class="pre">num_time_steps</span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.SingleFrequencyProfile.sample_time_signal" class="headerlink" title="Link to this definition">#</a>  
Sample this temporal profile at the same cadence as an FDTD simulation.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`ndarray`</span>, <span class="pre">`ndarray`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
