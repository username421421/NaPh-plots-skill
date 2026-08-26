<div id="fdtdx-extend-material-to-pml" class="section">

# fdtdx.extend_material_to_pml<a href="#fdtdx-extend-material-to-pml" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">extend_material_to_pml</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">arrays</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/extend_pml.html#extend_material_to_pml" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.extend_material_to_pml" class="headerlink" title="Link to this definition">#</a>  
Extend interior-edge material values into each PML region.

For each PML boundary in <span class="pre">`objects.pml_objects`</span>, the material values at the last non-PML grid cell (the “interior edge”) are broadcast across the entire PML depth. This is applied to <span class="pre">`inv_permittivities`</span>, <span class="pre">`inv_permeabilities`</span> (when it is an array rather than a scalar float), <span class="pre">`electric_conductivity`</span>, and <span class="pre">`magnetic_conductivity`</span> (when they are not <span class="pre">`None`</span>).

Parameters<span class="colon">:</span>  
- **objects** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.fdtd.container.ObjectContainer"><span class="pre"><code class="sourceCode python">ObjectContainer</code></span></a></span>) – ObjectContainer returned by <a href="fdtdx.place_objects.html#fdtdx.place_objects" class="reference internal" title="fdtdx.place_objects"><span class="pre"><code class="sourceCode python">place_objects()</code></span></a>.

- **arrays** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a></span>) – ArrayContainer returned by <a href="fdtdx.place_objects.html#fdtdx.place_objects" class="reference internal" title="fdtdx.place_objects"><span class="pre"><code class="sourceCode python">place_objects()</code></span></a>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a></span>

Returns<span class="colon">:</span>  
Updated ArrayContainer with PML regions filled from interior-edge values.

Warns<span class="colon">:</span>  
**UserWarning** – If a PML region already contains non-default (non-background) material values that would be overwritten.

</div>
