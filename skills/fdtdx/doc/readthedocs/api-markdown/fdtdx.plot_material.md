<div id="fdtdx-plot-material" class="section">

# fdtdx.plot_material<a href="#fdtdx-plot-material" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">plot_material</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">arrays</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">axs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">positions</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*, *<span class="n"><span class="pre">type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'permittivity'</span></span>*, *<span class="n"><span class="pre">material_axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/plot_material.html#plot_material" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.plot_material" class="headerlink" title="Link to this definition">#</a>  
Creates a visualization of material distribution showing slices in XY, XZ and YZ planes.

Generates three subplots showing 2D slices of the material distribution (permittivity or permeability) through the 3D simulation volume at specified positions.

Parameters<span class="colon">:</span>  
- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Configuration object containing simulation parameters like resolution

- **arrays** (<a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><em>ArrayContainer</em></a>) – Container holding the material arrays (permittivity, permeability)

- **filename** (*str* *\|* *Path* *\|* *None,* *optional*) – If provided, saves the plot to this file instead of displaying

- **axs** (*Any* *\|* *None,* *optional*) – Optional matplotlib axes to plot on. If None, creates new figure

- **plot_legend** (*bool,* *optional*) – Whether to add colorbar legends

- **positions** (*tuple\[float,* *float,* *float\],* *optional*) – Positions of slices in x, y, z directions (in meters). Zero means at center, 1e-6 would mean center+1µm

- **type** (*MaterialType,* *optional*) – Type of material to plot, either “permittivity” or “permeability”

- **material_axis** (*int,* *optional*) – Which component axis to plot (0, 1, or 2 for x, y, z components). For anisotropic materials this selects the diagonal element. Default is 0.

Returns<span class="colon">:</span>  
The generated figure object

Return type<span class="colon">:</span>  
Figure

<div class="admonition note">

Note

The plots show material values in 2D cross-sections, with positions in micrometers.

</div>

</div>
