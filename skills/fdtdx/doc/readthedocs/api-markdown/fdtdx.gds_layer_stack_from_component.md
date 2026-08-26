<div id="fdtdx-gds-layer-stack-from-component" class="section">

# fdtdx.gds_layer_stack_from_component<a href="#fdtdx-gds-layer-stack-from-component" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">gds_layer_stack_from_component</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">component</span></span>*, *<span class="n"><span class="pre">layers</span></span>*, *<span class="n"><span class="pre">materials</span></span>*, *<span class="n"><span class="pre">simulation_volume</span></span>*, *<span class="n"><span class="pre">gds_center</span></span>*, *<span class="n"><span class="pre">cell_name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">flatten</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#gds_layer_stack_from_component" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.gds_layer_stack_from_component" class="headerlink" title="Link to this definition">#</a>  
Build a layer stack from a gdsfactory <span class="pre">`Component`</span>.

This is a thin wrapper around <a href="fdtdx.gds_layer_stack.html#fdtdx.gds_layer_stack" class="reference internal" title="fdtdx.gds_layer_stack"><span class="pre"><code class="sourceCode python">gds_layer_stack()</code></span></a> that accepts a <a href="https://gdsfactory.github.io/gdsfactory/" class="reference external">gdsfactory</a> <span class="pre">`Component`</span> object instead of a GDS file path. gdsfactory is **not** a required dependency of fdtdx; it must be installed separately (<span class="pre">`pip`</span>` `<span class="pre">`install`</span>` `<span class="pre">`gdsfactory`</span>).

The component is exported to a temporary GDS file, which is read back via <span class="pre">`gdstk.read_gds()`</span>. This approach is version-agnostic and works with all current gdsfactory releases.

Parameters<span class="colon">:</span>  
- **component** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Any`</span></span>) – A <span class="pre">`gdsfactory.Component`</span> instance.

- **layers** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<a href="fdtdx.GDSLayerSpec.html#fdtdx.GDSLayerSpec" class="reference internal" title="fdtdx.objects.static_material.gds_layer_stack.GDSLayerSpec"><span class="pre"><code class="sourceCode python">GDSLayerSpec</code></span></a>\]</span>) – Layer specifications forwarded to <a href="fdtdx.gds_layer_stack.html#fdtdx.gds_layer_stack" class="reference internal" title="fdtdx.gds_layer_stack"><span class="pre"><code class="sourceCode python">gds_layer_stack()</code></span></a>.

- **materials** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <a href="fdtdx.Material.html#fdtdx.Material" class="reference internal" title="fdtdx.materials.Material"><span class="pre"><code class="sourceCode python">Material</code></span></a>\]</span>) – Materials dictionary forwarded to every <a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a>.

- **simulation_volume** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.SimulationVolume.html#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.objects.static_material.static.SimulationVolume"><span class="pre"><code class="sourceCode python">SimulationVolume</code></span></a></span>) – Used for size/position constraints.

- **gds_center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – GDS coordinate (in metres) that maps to the x/y centre of the simulation volume.

- **cell_name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span> \| <span class="pre">`None`</span></span>) – GDS cell name to read. Defaults to <span class="pre">`component.name`</span>.

- **flatten** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Flatten sub-cell references before reading polygons.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`list`</span>\[<a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.objects.static_material.gds_layer_stack.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a>\], <span class="pre">`list`</span>\[<span class="pre">`Any`</span>\]\]</span>

Returns<span class="colon">:</span>  
<span class="pre">`(objects,`</span>` `<span class="pre">`constraints)`</span> - same as <a href="fdtdx.gds_layer_stack.html#fdtdx.gds_layer_stack" class="reference internal" title="fdtdx.gds_layer_stack"><span class="pre"><code class="sourceCode python">gds_layer_stack()</code></span></a>.

Raises<span class="colon">:</span>  
- **ImportError** – If gdsfactory is not installed.

- **ValueError** – If the resolved cell name is not found in the exported GDS.

</div>
