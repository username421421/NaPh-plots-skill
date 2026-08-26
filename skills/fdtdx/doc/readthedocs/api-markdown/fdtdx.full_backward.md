<div id="fdtdx-full-backward" class="section">

# fdtdx.full_backward<a href="#fdtdx-full-backward" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">full_backward</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">record_detectors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">reset_fields</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">start_time_step</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/backward.html#full_backward" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.full_backward" class="headerlink" title="Link to this definition">#</a>  
Perform full backward FDTD propagation from current state to start time.

Uses a while loop to repeatedly call backward() until reaching start_time_step. Leverages time-reversibility of Maxwell’s equations.

Parameters<span class="colon">:</span>  
- **state** (*SimulationState*) – Current simulation state tuple (time_step, arrays)

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – Container with simulation objects (sources, detectors, etc)

- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Simulation configuration parameters

- **key** (*jax.Array* *\|* *None*) – JAX PRNG key for random operations. When <span class="pre">`None`</span> (the default) a deterministic key is derived from a fixed seed.

- **record_detectors** (*bool*) – Whether to record detector states

- **reset_fields** (*bool*) – Whether to reset fields after each step

- **start_time_step** (*int,* *optional*) – Time step to propagate back to (default: 0)

Returns<span class="colon">:</span>  
Final state after backward propagation

Return type<span class="colon">:</span>  
SimulationState

</div>
