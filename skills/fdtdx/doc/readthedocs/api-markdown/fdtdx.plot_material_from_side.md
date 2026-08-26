<div id="fdtdx-plot-material-from-side" class="section">

# fdtdx.plot_material_from_side<a href="#fdtdx-plot-material-from-side" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">plot_material_from_side</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">viewing_side</span></span>*, *<span class="n"><span class="pre">material_axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">position</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'permittivity'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/plot_material.html#plot_material_from_side" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.plot_material_from_side" class="headerlink" title="Link to this definition">#</a>  
Creates a visualization of material distribution from a single viewing side.

Generates a single subplot showing a 2D slice of the material distribution (permittivity or permeability) through the 3D simulation volume at a specified position.

Parameters<span class="colon">:</span>  
- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Configuration object containing simulation parameters like resolution

- **arrays** (<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><em>ArrayContainer</em></a>) – Container holding the material arrays (permittivity, permeability)

- **viewing_side** (*Literal\['x',* *'y',* *'z'\]*) – Which plane to view (‘x’ for YZ, ‘y’ for XZ, ‘z’ for XY)

- **material_axis** (*int*) – Index into the leading component dimension of the material array (for anisotropic materials).

- **filename** (*str* *\|* *Path* *\|* *None,* *optional*) – If provided, saves the plot to this file instead of displaying

- **ax** (*Any* *\|* *None,* *optional*) – Optional matplotlib axis to plot on. If None, creates new figure

- **plot_legend** (*bool,* *optional*) – Whether to add a colorbar legend

- **position** (*float,* *optional*) – Position of the slice in meters. Zero means at center, 1e-6 would mean center+1µm

- **type** (*MaterialType,* *optional*) – Type of material to plot, either “permittivity” or “permeability”

Returns<span class="colon">:</span>  
The generated figure object

Return type<span class="colon">:</span>  
Figure

<div class="admonition note">

Note

The plots show material values in a 2D cross-section, with positions in micrometers.

</div>

</div>
