<div id="fdtdx-detectors-from-gds-ports" class="section">

# fdtdx.detectors_from_gds_ports<a href="#fdtdx-detectors-from-gds-ports" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">detectors_from_gds_ports</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gds_source</span></span>*, *<span class="n"><span class="pre">cell_name</span></span>*, *<span class="n"><span class="pre">port_specs</span></span>*, *<span class="n"><span class="pre">wave_characters</span></span>*, *<span class="n"><span class="pre">simulation_volume</span></span>*, *<span class="n"><span class="pre">gds_center</span></span>*, *<span class="n"><span class="pre">direction</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'+'</span></span>*, *<span class="n"><span class="pre">mode_index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">filter_pol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">height_axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">2</span></span>*, *<span class="n"><span class="pre">flatten</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#detectors_from_gds_ports" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.detectors_from_gds_ports" class="headerlink" title="Link to this definition">#</a>  
Create <a href="fdtdx.ModeOverlapDetector.html#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.objects.detectors.mode.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">ModeOverlapDetector</code></span></a> objects from GDS port markers.

Mirrors <a href="fdtdx.sources_from_gds_ports.html#fdtdx.sources_from_gds_ports" class="reference internal" title="fdtdx.sources_from_gds_ports"><span class="pre"><code class="sourceCode python">sources_from_gds_ports()</code></span></a> exactly but produces <a href="fdtdx.ModeOverlapDetector.html#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.objects.detectors.mode.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">ModeOverlapDetector</code></span></a> objects. <span class="pre">`wave_characters`</span> is a *sequence* to match the detector constructor signature.

See <a href="fdtdx.sources_from_gds_ports.html#fdtdx.sources_from_gds_ports" class="reference internal" title="fdtdx.sources_from_gds_ports"><span class="pre"><code class="sourceCode python">sources_from_gds_ports()</code></span></a> for full documentation of the constraint layout, ordering guarantee, and <span class="pre">`direction`</span> dict usage.

Parameters<span class="colon">:</span>  
- **gds_source** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span> \| <span class="pre">`Path`</span> \| <span class="pre">`Library`</span></span>) – Path to a <span class="pre">`.gds`</span> file or an already-loaded <span class="pre">`gdstk.Library`</span>.

- **cell_name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – GDS cell containing the port marker polygons.

- **port_specs** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<a href="fdtdx.GDSPortSpec.html#fdtdx.GDSPortSpec" class="reference internal" title="fdtdx.objects.static_material.gds_layer_stack.GDSPortSpec"><span class="pre"><code class="sourceCode python">GDSPortSpec</code></span></a>\]</span>) – List of <a href="fdtdx.GDSPortSpec.html#fdtdx.GDSPortSpec" class="reference internal" title="fdtdx.GDSPortSpec"><span class="pre"><code class="sourceCode python">GDSPortSpec</code></span></a> objects.

- **wave_characters** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Sequence`</span>\[<a href="fdtdx.WaveCharacter.html#fdtdx.WaveCharacter" class="reference internal" title="fdtdx.core.wavelength.WaveCharacter"><span class="pre"><code class="sourceCode python">WaveCharacter</code></span></a>\]</span>) – Sequence of wavelength characters forwarded to each detector.

- **simulation_volume** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.SimulationVolume.html#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.objects.static_material.static.SimulationVolume"><span class="pre"><code class="sourceCode python">SimulationVolume</code></span></a></span>) – Reference object for size/position constraints. Its <span class="pre">`partial_real_shape`</span> must be set on <span class="pre">`propagation_axis`</span>.

- **gds_center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – GDS coordinate (in metres) mapped to the x/y centre of the simulation volume.

- **direction** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Union`</span>\[<span class="pre">`Literal`</span>\[<span class="pre">`'+'`</span>, <span class="pre">`'-'`</span>\], <span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Literal`</span>\[<span class="pre">`'+'`</span>, <span class="pre">`'-'`</span>\]\]\]</span>) – Propagation direction (<span class="pre">`"+"`</span> or <span class="pre">`"-"`</span>), applied to all detectors. Pass a <span class="pre">`dict`</span> mapping port names to individual directions when needed.

- **mode_index** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Waveguide mode index.

- **filter_pol** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Optional`</span>\[<span class="pre">`Literal`</span>\[<span class="pre">`'te'`</span>, <span class="pre">`'tm'`</span>\]\]</span>) – Optional polarisation filter.

- **height_axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Simulation axis treated as the out-of-plane height; detectors are made to span the full simulation extent on this axis (default 2 = z). This assumes a single vertical stack — detectors run from one face of the simulation volume to the other along <span class="pre">`height_axis`</span>.

- **flatten** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Flatten sub-cell references before reading polygons.

Returns<span class="colon">:</span>  
propagation position, transverse center, full-height size, and vertical center.

Return type<span class="colon">:</span>  
<span class="pre">`(detectors,`</span>` `<span class="pre">`constraints)`</span> — four constraints per detector

Raises<span class="colon">:</span>  
**ValueError** – If <span class="pre">`propagation_axis`</span> is not 0 or 1, or if <span class="pre">`simulation_volume.partial_real_shape`</span> is <span class="pre">`None`</span> on <span class="pre">`propagation_axis`</span>.

</div>
