<div id="fdtdx-metric-efficiency" class="section">

# fdtdx.metric_efficiency<a href="#fdtdx-metric-efficiency" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">metric_efficiency</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">detector_states</span></span>*, *<span class="n"><span class="pre">in_names</span></span>*, *<span class="n"><span class="pre">out_names</span></span>*, *<span class="n"><span class="pre">metric_name</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/physics/losses.html#metric_efficiency" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.metric_efficiency" class="headerlink" title="Link to this definition">#</a>  
Calculate efficiency metrics between input and output detectors.

Computes efficiency ratios between input and output detectors by comparing their metric values (e.g. energy, power). For each input-output detector pair, calculates the ratio of output/input metric values.

Parameters<span class="colon">:</span>  
- **detector_states** (*dict\[str,* *dict\[str,* *jax.Array\]\]*) – Dictionary mapping detector names to their state dictionaries, which contain metric values as JAX arrays

- **in_names** (*Sequence\[str\]*) – Names of input detectors to use as reference

- **out_names** (*Sequence\[str\]*) – Names of output detectors to compare against inputs

- **metric_name** (*str*) – Name of the metric to compare between detectors (e.g. “energy”)

Returns<span class="colon">:</span>  
tuple containing:  
- jax.Array: Mean efficiency across all input-output pairs

- dict: Additional info including individual metric values and efficiencies with keys like:

  > <div>
  >
  > - ”{detector}\_{metric}” for raw metric values
  >
  > - ”{out}\_{by}\_{in}\_efficiency” for individual efficiency ratios
  >
  > </div>

Return type<span class="colon">:</span>  
tuple\[jax.Array, dict\[str, Any\]\]

</div>
