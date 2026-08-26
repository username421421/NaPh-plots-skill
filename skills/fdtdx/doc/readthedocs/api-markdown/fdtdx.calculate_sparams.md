<div id="fdtdx-calculate-sparams" class="section">

# fdtdx.calculate_sparams<a href="#fdtdx-calculate-sparams" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">calculate_sparams</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">input_port_names</span></span>*, *<span class="n"><span class="pre">show_progress</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">input_normalization_detector_name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">return_detector_states</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/sparams.html#calculate_sparams" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.calculate_sparams" class="headerlink" title="Link to this definition">#</a>  
Run FDTD simulations for multiple input ports and merge S-parameters.

Calls <a href="fdtdx.calculate_sparam.html#fdtdx.calculate_sparam" class="reference internal" title="fdtdx.calculate_sparam"><span class="pre"><code class="sourceCode python">calculate_sparam()</code></span></a> once per entry in *input_port_names* and merges all results into a single S-parameter dictionary.

Parameters<span class="colon">:</span>  
- **objects** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.fdtd.container.ObjectContainer"><span class="pre"><code class="sourceCode python">ObjectContainer</code></span></a></span>) – ObjectContainer from <a href="fdtdx.setup_sparams_simulation.html#fdtdx.setup_sparams_simulation" class="reference internal" title="fdtdx.setup_sparams_simulation"><span class="pre"><code class="sourceCode python">setup_sparams_simulation()</code></span></a>.

- **arrays** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a></span>) – ArrayContainer from <a href="fdtdx.setup_sparams_simulation.html#fdtdx.setup_sparams_simulation" class="reference internal" title="fdtdx.setup_sparams_simulation"><span class="pre"><code class="sourceCode python">setup_sparams_simulation()</code></span></a>.

- **config** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.config.SimulationConfig"><span class="pre"><code class="sourceCode python">SimulationConfig</code></span></a></span>) – SimulationConfig from <a href="fdtdx.setup_sparams_simulation.html#fdtdx.setup_sparams_simulation" class="reference internal" title="fdtdx.setup_sparams_simulation"><span class="pre"><code class="sourceCode python">setup_sparams_simulation()</code></span></a>.

- **input_port_names** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Sequence`</span>\[<span class="pre">`str`</span>\]</span>) – Names of the input ports to simulate.

- **show_progress** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Whether to display the simulation progress bar.

- **input_normalization_detector_name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span> \| <span class="pre">`None`</span></span>) – Passed through to <a href="fdtdx.calculate_sparam.html#fdtdx.calculate_sparam" class="reference internal" title="fdtdx.calculate_sparam"><span class="pre"><code class="sourceCode python">calculate_sparam()</code></span></a>.

- **key** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`None`</span></span>) – JAX random key. Defaults to <span class="pre">`PRNGKey(0)`</span>.

- **return_detector_states** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – When <span class="pre">`True`</span>, return the detector states from each simulation run as a list (one entry per input port). When <span class="pre">`False`</span> an empty list is returned.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`dict`</span>\[<span class="pre">`tuple`</span>\[<span class="pre">`str`</span>, <span class="pre">`str`</span>\], <span class="pre">`Array`</span>\], <span class="pre">`list`</span>\[<span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\]\]\]\]</span>

Returns<span class="colon">:</span>  
A 2-tuple <span class="pre">`(sparams,`</span>` `<span class="pre">`detector_states_list)`</span> where *sparams* is the merged <span class="pre">`dict[tuple[str,`</span>` `<span class="pre">`str],`</span>` `<span class="pre">`jax.Array]`</span> across all simulations and *detector_states_list* is either a list of per-simulation detector state dicts or an empty list.

</div>
