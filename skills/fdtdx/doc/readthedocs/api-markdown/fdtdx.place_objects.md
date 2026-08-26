<div id="fdtdx-place-objects" class="section">

# fdtdx.place_objects<a href="#fdtdx-place-objects" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">place_objects</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">object_list</span></span>*, *<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">constraints</span></span>*, *<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/initialization.html#place_objects" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.place_objects" class="headerlink" title="Link to this definition">#</a>  
Places simulation objects according to specified constraints and initializes containers.

Parameters<span class="colon">:</span>  
- **objects** (*list\[*<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>*\]*) – List of all simulation objects, including the simulation volume.

- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Simulation configuration.

- **constraints** (*Sequence\[Constraint\]*) – List of positioning/sizing constraints referencing object names.

- **key** (*jax.Array* *\|* *None*) – JAX random key for initialization. When <span class="pre">`None`</span> (the default) a deterministic key is derived from <span class="pre">`_DEFAULT_KEY_SEED`</span>.

Returns<span class="colon">:</span>  
A tuple containing:  
- ObjectContainer with placed simulation objects

- ArrayContainer with initialized field arrays

- ParameterContainer with device parameters

- Updated SimulationConfig

- Dictionary with additional initialization info

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer">ObjectContainer</a>, <a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer">ArrayContainer</a>, ParameterContainer, <a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig">SimulationConfig</a>, dict\[str, Any\]\]

Raises<span class="colon">:</span>  
**ValueError** – If constraint resolution fails for one or more objects.

</div>
