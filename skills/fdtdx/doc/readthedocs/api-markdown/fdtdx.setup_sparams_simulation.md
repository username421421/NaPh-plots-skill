<div id="fdtdx-setup-sparams-simulation" class="section">

# fdtdx.setup_sparams_simulation<a href="#fdtdx-setup-sparams-simulation" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">setup_sparams_simulation</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">polygons</span></span>*, *<span class="n"><span class="pre">input_ports</span></span>*, *<span class="n"><span class="pre">output_ports</span></span>*, *<span class="n"><span class="pre">wavelength</span></span>*, *<span class="n"><span class="pre">resolution</span></span>*, *<span class="n"><span class="pre">max_time</span></span>*, *<span class="n"><span class="pre">domain_size</span></span>*, *<span class="n"><span class="pre">background_material</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">pml_layers</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/sparams.html#setup_sparams_simulation" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.setup_sparams_simulation" class="headerlink" title="Link to this definition">#</a>  
Set up an FDTD simulation scene for S-parameter extraction.

Builds a fully initialised simulation scene containing:

- A background <a href="fdtdx.SimulationVolume.html#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.objects.static_material.static.SimulationVolume"><span class="pre"><code class="sourceCode python">SimulationVolume</code></span></a> surrounded by PML absorbing boundaries on all six sides.

- Any GDS-derived <a href="fdtdx.ExtrudedPolygon.html#fdtdx.ExtrudedPolygon" class="reference internal" title="fdtdx.objects.static_material.polygon.ExtrudedPolygon"><span class="pre"><code class="sourceCode python">ExtrudedPolygon</code></span></a> objects placed at their requested positions.

- A <a href="fdtdx.ModePlaneSource.html#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.objects.sources.mode.ModePlaneSource"><span class="pre"><code class="sourceCode python">ModePlaneSource</code></span></a> for every input port.

- A <a href="fdtdx.ModeOverlapDetector.html#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.objects.detectors.mode.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">ModeOverlapDetector</code></span></a> for every output port.

To compute the full S-matrix, call this function once per input port (each time with a single entry in *input_ports*) and collect the detector readings.

Parameters<span class="colon">:</span>  
- **polygons** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`tuple`</span>\[<a href="fdtdx.ExtrudedPolygon.html#fdtdx.ExtrudedPolygon" class="reference internal" title="fdtdx.objects.static_material.polygon.ExtrudedPolygon"><span class="pre"><code class="sourceCode python">ExtrudedPolygon</code></span></a>, <span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]\]\]</span>) – Pairs of <span class="pre">`(ExtrudedPolygon,`</span>` `<span class="pre">`center_offset)`</span> where <span class="pre">`center_offset`</span> is the 3-D centre of the polygon in the *core* coordinate system (metres, origin at the start of the core region). The polygon’s <span class="pre">`partial_real_shape`</span> must be fully specified at construction time (no <span class="pre">`None`</span> entries).

- **input_ports** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<a href="fdtdx.PortSpec.html#fdtdx.PortSpec" class="reference internal" title="fdtdx.utils.sparams.PortSpec"><span class="pre"><code class="sourceCode python">PortSpec</code></span></a>\]</span>) – Ports that receive a <a href="fdtdx.ModePlaneSource.html#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.objects.sources.mode.ModePlaneSource"><span class="pre"><code class="sourceCode python">ModePlaneSource</code></span></a>.

- **output_ports** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<a href="fdtdx.PortSpec.html#fdtdx.PortSpec" class="reference internal" title="fdtdx.utils.sparams.PortSpec"><span class="pre"><code class="sourceCode python">PortSpec</code></span></a>\]</span>) – Ports that receive a <a href="fdtdx.ModeOverlapDetector.html#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.objects.detectors.mode.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">ModeOverlapDetector</code></span></a>.

- **wavelength** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Free-space wavelength in metres.

- **resolution** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Spatial resolution (voxel size) in metres.

- **max_time** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Total simulation time in seconds.

- **domain_size** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – Size of the *core* simulation region (excluding PML) as <span class="pre">`(Lx,`</span>` `<span class="pre">`Ly,`</span>` `<span class="pre">`Lz)`</span> in metres.

- **background_material** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.Material.html#fdtdx.Material" class="reference internal" title="fdtdx.materials.Material"><span class="pre"><code class="sourceCode python">Material</code></span></a> \| <span class="pre">`None`</span></span>) – Material filling the simulation volume. Defaults to air (<span class="pre">`Material()`</span>).

- **pml_layers** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Number of PML grid cells added to every face.

- **key** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Array`</span> \| <span class="pre">`None`</span></span>) – JAX random key used by <span class="pre">`place_objects()`</span>. Defaults to <span class="pre">`PRNGKey(0)`</span> when <span class="pre">`None`</span>. Usually not necessary to specify since simulation is deterministic.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<a href="fdtdx.ObjectContainer.html#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.fdtd.container.ObjectContainer"><span class="pre"><code class="sourceCode python">ObjectContainer</code></span></a>, <a href="fdtdx.ArrayContainer.html#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.fdtd.container.ArrayContainer"><span class="pre"><code class="sourceCode python">ArrayContainer</code></span></a>, <a href="fdtdx.SimulationConfig.html#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.config.SimulationConfig"><span class="pre"><code class="sourceCode python">SimulationConfig</code></span></a>\]</span>

Returns<span class="colon">:</span>  
A 3-tuple <span class="pre">`(objects,`</span>` `<span class="pre">`arrays,`</span>` `<span class="pre">`config)`</span>, ready to pass to <a href="fdtdx.calculate_sparam.html#fdtdx.calculate_sparam" class="reference internal" title="fdtdx.calculate_sparam"><span class="pre"><code class="sourceCode python">calculate_sparam()</code></span></a>.

</div>
