<div id="fdtdx-apply-params" class="section">

# fdtdx.apply_params<a href="#fdtdx-apply-params" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">apply_params</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">params</span></span>*, *<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">transform_kwargs</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/initialization.html#apply_params" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.apply_params" class="headerlink" title="Link to this definition">#</a>  
Applies parameters to devices and updates source states.

Parameters<span class="colon">:</span>  
- **arrays** (<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><em>ArrayContainer</em></a>) – Container with field arrays

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – Container with simulation objects

- **params** (*ParameterContainer*) – Container with device parameters

- **key** (*jax.Array* *\|* *None*) – JAX random key for source updates. When <span class="pre">`None`</span> (the default) a deterministic key is derived from <span class="pre">`_DEFAULT_KEY_SEED`</span>.

- **\*\*transform_kwargs** – Keyword arguments passed to the parameter transformation.

Returns<span class="colon">:</span>  
A tuple containing:  
- Updated ArrayContainer with applied device parameters

- Updated ObjectContainer with new source states

- Dictionary with parameter application info

Return type<span class="colon">:</span>  
tuple\[<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer">ArrayContainer</a>, <a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer">ObjectContainer</a>, dict\[str, Any\]\]

</div>
