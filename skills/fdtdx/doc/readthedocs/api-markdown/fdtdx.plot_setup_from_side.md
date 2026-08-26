<div id="fdtdx-plot-setup-from-side" class="section">

# fdtdx.plot_setup_from_side<a href="#fdtdx-plot-setup-from-side" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">plot_setup_from_side</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">viewing_side</span></span>*, *<span class="n"><span class="pre">exclude_object_list</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">ax</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">plot_legend</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">exclude_xy_plane_object_list</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_yz_plane_object_list</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_xz_plane_object_list</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">exclude_large_object_ratio</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">auto_exclude_full_coverage</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/plot_setup.html#plot_setup_from_side" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.plot_setup_from_side" class="headerlink" title="Link to this definition">#</a>  
Creates a visualization of the simulation setup from a single viewing side.

Generates a single subplot showing a cross-section of the simulation volume and the objects within it from the specified viewing side. Objects are drawn as colored rectangles with optional legends.

Parameters<span class="colon">:</span>  
- **config** (<a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><em>SimulationConfig</em></a>) – Configuration object containing simulation parameters like resolution

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – Container holding all simulation objects to be plotted

- **viewing_side** (*Literal\['x',* *'y',* *'z'\]*) – Which plane to view (‘x’ for YZ, ‘y’ for XZ, ‘z’ for XY)

- **exclude_object_list** (*list\[*<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>*\]* *\|* *None,* *optional*) – List of objects to exclude from all plots

- **filename** (*str* *\|* *Path* *\|* *None,* *optional*) – If provided, saves the plot to this file instead of displaying

- **ax** (*Any* *\|* *None,* *optional*) – Optional matplotlib axis to plot on. If None, creates new figure

- **plot_legend** (*bool,* *optional*) – Whether to add a legend showing object names/types

- **exclude_xy_plane_object_list** (*list\[*<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>*\]* *\|* *None,* *optional*) – Objects to exclude from XY plane plot

- **exclude_yz_plane_object_list** (*list\[*<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>*\]* *\|* *None,* *optional*) – Objects to exclude from YZ plane plot

- **exclude_xz_plane_object_list** (*list\[*<a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><em>SimulationObject</em></a>*\]* *\|* *None,* *optional*) – Objects to exclude from XZ plane plot

- **exclude_large_object_ratio** (*float* *\|* *None,* *optional*) – If provided, excludes objects that cover more than this ratio of the image (e.g., 1.0 excludes objects covering 100% of the image)

- **auto_exclude_full_coverage** (*bool,* *optional*) – Automatically exclude objects that cover 100% of the viewing plane

Returns<span class="colon">:</span>  
The generated figure object

Return type<span class="colon">:</span>  
Figure

<div class="admonition note">

Note

The plots show object positions in micrometers, converting from simulation units. PML objects are automatically excluded from their respective boundary planes.

</div>

</div>
