<div id="fdtdx-export-vti" class="section">

# fdtdx.export_vti<a href="#fdtdx-export-vti" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">export_vti</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">cell_data</span></span>*, *<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">resolution</span></span>*, *<span class="n"><span class="pre">offset</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0,</span> <span class="pre">0,</span> <span class="pre">0)</span></span>*, *<span class="n"><span class="pre">grid_slice</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">compression_level</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-1</span></span>*, *<span class="n"><span class="pre">grid</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/conversion/vti.html#export_vti" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.export_vti" class="headerlink" title="Link to this definition">#</a>  
Export a dictionary of arrays to a VTI (VTK ImageData) file.

Writes an XML-formatted VTI file with appended binary data. Supports both 3D scalar fields (x, y, z) and 4D vector fields (n, x, y, z). All arrays must share the same spatial dimensions.

Parameters<span class="colon">:</span>  
- **cell_data** (*dict\[str,* *jax.Array\]*) – Dictionary mapping field names to numpy arrays.

- **filename** (*Path* *\|* *str*) – Output file path.

- **resolution** (*float*) – Voxel spacing for the grid.

- **offset** (*tuple\[int,* *int,* *int\],* *optional*) – Global grid index offset (x, y, z). Useful when aligning multiple VTI files. Defaults to (0, 0, 0).

- **grid_slice** (*Slice3D* *\|* *None,* *optional*) – Slice for defining the offset, if provided. Useful when aligning multiple VTI files. Overrides offset. Defaults to None.

- **compression_level** (*int,* *optional*) – zlib compression level. Use level 0 for no compression (fastest) and level 9 for highest compression (smallest file size). Defaults to -1, which currently corresponds to level 6 compression.

- **grid** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RectilinearGrid.html#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.core.grid.RectilinearGrid"><span class="pre"><code class="sourceCode python">RectilinearGrid</code></span></a> \| <span class="pre">`None`</span></span>) – Optional grid metadata. VTI is an image-data format and can only encode uniform spacing. Passing a non-uniform grid raises and callers should use <a href="fdtdx.export_vtr.html#fdtdx.export_vtr" class="reference internal" title="fdtdx.export_vtr"><span class="pre"><code class="sourceCode python">export_vtr()</code></span></a> instead.

Raises<span class="colon">:</span>  
**AssertionError** – If arrays have mismatched shapes, invalid dimensions, or unsupported dtypes.

</div>
