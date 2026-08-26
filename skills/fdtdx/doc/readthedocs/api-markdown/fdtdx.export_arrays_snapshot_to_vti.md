<div id="fdtdx-export-arrays-snapshot-to-vti" class="section">

# fdtdx.export_arrays_snapshot_to_vti<a href="#fdtdx-export-arrays-snapshot-to-vti" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">export_arrays_snapshot_to_vti</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">path</span></span>*, *<span class="n"><span class="pre">resolution</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/conversion/vti.html#export_arrays_snapshot_to_vti" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.export_arrays_snapshot_to_vti" class="headerlink" title="Link to this definition">#</a>  
Convenience function to export a snapshot of FDTD simulation arrays to a VTI file.

Extracts electromagnetic fields (E, H) and material properties (permittivity, permeability, conductivity) from the container. Inverse parameters are converted back to standard values (e.g., 1/inv_permittivity) for visualization.

Parameters<span class="colon">:</span>  
- **arrays** (<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><em>ArrayContainer</em></a>) – Container holding simulation state and material arrays.

- **path** (*Path* *\|* *str*) – Output file path.

- **resolution** (*float*) – Spatial resolution of the grid from the SimulationConfig.

</div>
