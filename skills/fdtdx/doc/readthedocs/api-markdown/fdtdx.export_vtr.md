<div id="fdtdx-export-vtr" class="section">

# fdtdx.export_vtr<a href="#fdtdx-export-vtr" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">export_vtr</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cell_data</span></span>*, *<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">grid</span></span>*, *<span class="n"><span class="pre">grid_slice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">compression_level</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-1</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/conversion/vti.html#export_vtr" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.export_vtr" class="headerlink" title="Link to this definition">#</a>  
Export cell data to a VTR (VTK RectilinearGrid) file.

VTR is the rectilinear counterpart to VTI: it stores explicit x/y/z point coordinates and can therefore represent non-uniform cell widths without resampling. Coordinates are written from <span class="pre">`RectilinearGrid`</span> edge arrays, while cell data uses the same appended compressed binary encoding as <span class="pre">`export_vti`</span>.

Parameters<span class="colon">:</span>  
- **cell_data** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\]</span>) – Dictionary mapping field names to scalar <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> arrays or vector <span class="pre">`(n,`</span>` `<span class="pre">`x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> arrays.

- **filename** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Path`</span> \| <span class="pre">`str`</span></span>) – Output <span class="pre">`.vtr`</span> path.

- **grid** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a></span>) – Rectilinear grid supplying physical edge coordinates.

- **grid_slice** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`slice`</span>, <span class="pre">`slice`</span>, <span class="pre">`slice`</span>\] \| <span class="pre">`None`</span></span>) – Optional spatial slice that selects a subgrid from <span class="pre">`grid`</span>.

- **compression_level** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – zlib compression level for appended cell data.

Raises<span class="colon">:</span>  
**AssertionError** – If cell data shape, dimensionality, dtype, or slice extent is incompatible with the selected grid coordinates.

</div>
