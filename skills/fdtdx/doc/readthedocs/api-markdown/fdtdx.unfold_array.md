<div id="fdtdx-unfold-array" class="section">

# fdtdx.unfold_array<a href="#fdtdx-unfold-array" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">unfold_array</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">arr</span></span>*, *<span class="n"><span class="pre">symmetry</span></span>*, *<span class="n"><span class="pre">spatial_axes</span></span>*, *<span class="n"><span class="pre">signs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/symmetry.html#unfold_array" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.unfold_array" class="headerlink" title="Link to this definition">#</a>  
Mirror-and-concatenate a spatial array along each symmetric axis.

Generic building block used by <a href="fdtdx.unfold_detector_states.html#fdtdx.unfold_detector_states" class="reference internal" title="fdtdx.unfold_detector_states"><span class="pre"><code class="sourceCode python">unfold_detector_states()</code></span></a>. For every axis <span class="pre">`a`</span> with <span class="pre">`symmetry[a]`</span>` `<span class="pre">`!=`</span>` `<span class="pre">`0`</span> the array is flipped along its corresponding array axis <span class="pre">`spatial_axes[a]`</span> (optionally multiplied by a broadcastable per-component sign), and the mirror image is concatenated in front of the original.

Parameters<span class="colon">:</span>  
- **arr** (*jax.Array*) – Array to unfold.

- **symmetry** (*tuple\[int,* *int,* *int\]*) – Per-axis symmetry <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>; <span class="pre">`0`</span> axes are skipped.

- **spatial_axes** (*tuple\[int,* *int,* *int\]*) – For each physical axis, the corresponding array axis.

- **signs** (*dict\[int,* *jax.Array\]* *\|* *None*) – Optional mapping physical-axis → broadcastable sign array applied to the mirror image (defaults to <span class="pre">`+1`</span>).

Returns<span class="colon">:</span>  
The unfolded array.

Return type<span class="colon">:</span>  
jax.Array

</div>
