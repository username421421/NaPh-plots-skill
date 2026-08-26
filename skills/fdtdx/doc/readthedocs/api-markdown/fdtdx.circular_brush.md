<div id="fdtdx-circular-brush" class="section">

# fdtdx.circular_brush<a href="#fdtdx-circular-brush" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">circular_brush</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">diameter</span></span>*, *<span class="n"><span class="pre">size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/device/parameters/discretization.html#circular_brush" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.circular_brush" class="headerlink" title="Link to this definition">#</a>  
Creates a circular binary mask/brush for morphological operations.

Parameters<span class="colon">:</span>  
- **diameter** (*float*) – Diameter of the circle in grid units.

- **size** (*int* *\|* *None,* *optional*) – Optional size of the output array. If None, uses ceil(diameter) rounded up to next odd number.

Returns<span class="colon">:</span>  
Binary array containing a circular mask where True indicates points within the circle diameter.

Return type<span class="colon">:</span>  
jax.Array

</div>
