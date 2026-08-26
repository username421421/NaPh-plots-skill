<div id="fdtdx-export-stl" class="section">

# fdtdx.export_stl<a href="#fdtdx-export-stl" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">export_stl</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">matrix</span></span>*, *<span class="n"><span class="pre">stl_filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">voxel_grid_size</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(1,</span> <span class="pre">1,</span> <span class="pre">1)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/conversion/stl.html#export_stl" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.export_stl" class="headerlink" title="Link to this definition">#</a>  
Export a 3D boolean matrix to an STL file.

Converts a 3D boolean matrix into a mesh representation and saves it as an STL file. True values in the matrix are converted to solid voxels in the output mesh.

Parameters<span class="colon">:</span>  
- **matrix** (*np.ndarray*) – 3D boolean numpy array representing the voxel grid.

- **stl_filename** (*Path* *\|* *str* *\|* *None,* *optional*) – Output STL file path. If given, save the stl to this path. Defaults to None.

- **voxel_grid_size** (*tuple\[int,* *int,* *int\],* *optional*) – Physical size of each voxel as (x, y, z) integers. Defaults to (1, 1, 1).

Returns<span class="colon">:</span>  
STL mesh.

Return type<span class="colon">:</span>  
trimesh.Trimesh

Raises<span class="colon">:</span>  
**Exception** – If input matrix is not 3-dimensional.

</div>
