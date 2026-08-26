<div id="fdtdx-logger" class="section">

# fdtdx.Logger<a href="#fdtdx-logger" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Logger</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">experiment_name</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">save_source</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">save_script</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/logger.html#Logger" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Logger" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`object`</span>

Logger for managing experiment outputs and visualization.

Handles experiment logging, metrics tracking, and visualization of simulation results. Creates a working directory structure, initializes logging, and provides methods for saving figures, metrics, and device parameters.

Parameters<span class="colon">:</span>  
- **experiment_name** (*str*) – Name of the experiment. This is the naming of the parent directory where the experiment will be saved.

- **name** (*str* *\|* *None,* *optional*) – Optional specific name for the working directory. If None, uses timestamp.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Logger.params_dir" class="reference internal" title="fdtdx.Logger.params_dir"><span class="pre"><code class="sourceCode python">params_dir</code></span></a>

- <a href="#fdtdx.Logger.stl_dir" class="reference internal" title="fdtdx.Logger.stl_dir"><span class="pre"><code class="sourceCode python">stl_dir</code></span></a>

Methods

- <a href="#fdtdx.Logger.log_detectors" class="reference internal" title="fdtdx.Logger.log_detectors"><span class="pre"><code class="sourceCode python">log_detectors</code></span></a>

- <a href="#fdtdx.Logger.log_params" class="reference internal" title="fdtdx.Logger.log_params"><span class="pre"><code class="sourceCode python">log_params</code></span></a>

- <a href="#fdtdx.Logger.savefig" class="reference internal" title="fdtdx.Logger.savefig"><span class="pre"><code class="sourceCode python">savefig</code></span></a>

- <a href="#fdtdx.Logger.write" class="reference internal" title="fdtdx.Logger.write"><span class="pre"><code class="sourceCode python">write</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">params_dir</span></span><a href="#fdtdx.Logger.params_dir" class="headerlink" title="Link to this definition">#</a>  
Directory for storing parameter files.

Returns<span class="colon">:</span>  
Directory for parameter file outputs

Return type<span class="colon">:</span>  
Path

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">stl_dir</span></span><a href="#fdtdx.Logger.stl_dir" class="headerlink" title="Link to this definition">#</a>  
Directory for storing STL files.

Returns<span class="colon">:</span>  
Directory for STL file outputs

Return type<span class="colon">:</span>  
Path

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">log_detectors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">iter_idx</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">detector_states</span></span>*, *<span class="n"><span class="pre">exclude</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/logger.html#Logger.log_detectors" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Logger.log_detectors" class="headerlink" title="Link to this definition">#</a>  
Log detector states and generate visualization plots.

Creates plots for each detector’s state and saves them to the detector’s output directory. Handles both figure outputs and other detector-specific file formats.

Parameters<span class="colon">:</span>  
- **iter_idx** (*int*) – Current iteration index

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – Container with simulation objects

- **detector_states** (*dict\[str,* *DetectorState\]*) – Dictionary mapping detector names to their states

- **exclude** (*Sequence\[str\],* *optional*) – List of detector names to exclude from logging

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">log_params</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">iter_idx</span></span>*, *<span class="n"><span class="pre">params</span></span>*, *<span class="n"><span class="pre">objects</span></span>*, *<span class="n"><span class="pre">export_figure</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">export_stl</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">export_background_stl</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">transformation_kwargs</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/logger.html#Logger.log_params" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Logger.log_params" class="headerlink" title="Link to this definition">#</a>  
Log parameter states and export device visualizations.

Saves device parameters and optionally exports visualizations as figures or STL files. Tracks changes in device voxels between iterations.

Parameters<span class="colon">:</span>  
- **iter_idx** (*int*) – Current iteration index

- **params** (*ParameterContainer*) – Container with device parameters

- **objects** (<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><em>ObjectContainer</em></a>) – Container with simulation objects

- **export_figure** (*bool,* *optional*) – Whether to export index matrix figures

- **export_stl** (*bool,* *optional*) – Whether to export device geometry as STL

- **export_background_stl** (*bool,* *optional*) – Whether to export air regions as STL

- **\*\*transformation_kwargs** – keyword arguments passed to the parameter transformation

Returns<span class="colon">:</span>  
Number of voxels that changed since last iteration

Return type<span class="colon">:</span>  
int

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">savefig</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">directory</span></span>*, *<span class="n"><span class="pre">filename</span></span>*, *<span class="n"><span class="pre">fig</span></span>*, *<span class="n"><span class="pre">dpi</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">300</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/logger.html#Logger.savefig" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Logger.savefig" class="headerlink" title="Link to this definition">#</a>  
Save a matplotlib figure to file.

Creates a figures subdirectory if needed and saves the figure with specified settings.

Parameters<span class="colon">:</span>  
- **directory** (*Path*) – Base directory to save in

- **filename** (*str*) – Name for the figure file

- **fig** (*Figure*) – Matplotlib figure to save

- **dpi** (*int,* *optional*) – Resolution in dots per inch. Defaults to 300.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Logger.</span></span><span class="sig-name descname"><span class="pre">write</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">stats</span></span>*, *<span class="n"><span class="pre">do_print</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/logger.html#Logger.write" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Logger.write" class="headerlink" title="Link to this definition">#</a>  
Write statistics to CSV file and optionally print them.

Records metrics in a CSV file and optionally displays them in a formatted table. Automatically initializes CSV headers on first write.

Parameters<span class="colon">:</span>  
- **stats** (*dict*) – Dictionary of statistics to record

- **do_print** (*bool,* *optional*) – Whether to print stats to console. Defaults to true.

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
