<div id="fdtdx-gds-layer-stack" class="section">

# fdtdx.gds_layer_stack<a href="#fdtdx-gds-layer-stack" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">gds_layer_stack</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gds_source</span></span>*, *<span class="n"><span class="pre">cell_name</span></span>*, *<span class="n"><span class="pre">layers</span></span>*, *<span class="n"><span class="pre">materials</span></span>*, *<span class="n"><span class="pre">simulation_volume</span></span>*, *<span class="n"><span class="pre">gds_center</span></span>*, *<span class="n"><span class="pre">flatten</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#gds_layer_stack" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.gds_layer_stack" class="headerlink" title="Link to this definition">#</a>  
Build simulation objects from a GDS file according to a layer stack specification.

For each <a href="fdtdx.GDSLayerSpec.html#fdtdx.GDSLayerSpec" class="reference internal" title="fdtdx.GDSLayerSpec"><span class="pre"><code class="sourceCode python">GDSLayerSpec</code></span></a>, polygons are extracted from the named GDS cell, optionally etched by other layers, converted to metres, and wrapped in a <a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a>. Layers are always extruded along z (axis 2) — GDS encodes only x/y polygon geometry, so z is the only axis that can be inferred from the file. For non-z extrusion (e.g. cross-section simulations), construct <a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a> instances directly with the desired <span class="pre">`axis`</span>. Two constraints are generated per object:

- A position constraint aligning the object’s bottom face (z) with the simulation volume’s bottom face offset by <span class="pre">`spec.z_base`</span>.

- A size constraint matching the simulation volume’s extent in the x/y axes.

Parameters<span class="colon">:</span>  
- **gds_source** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span> \| <span class="pre">`Path`</span> \| <span class="pre">`Library`</span></span>) – Path to a <span class="pre">`.gds`</span> file or an already-loaded <span class="pre">`gdstk.Library`</span>.

- **cell_name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – Name of the GDS cell to read polygons from.

- **layers** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<a href="fdtdx.GDSLayerSpec.html#fdtdx.GDSLayerSpec" class="reference internal" title="fdtdx.objects.static_material.gds_layer_stack.GDSLayerSpec"><span class="pre"><code class="sourceCode python">GDSLayerSpec</code></span></a>\]</span>) – Ordered list of <a href="fdtdx.GDSLayerSpec.html#fdtdx.GDSLayerSpec" class="reference internal" title="fdtdx.GDSLayerSpec"><span class="pre"><code class="sourceCode python">GDSLayerSpec</code></span></a> objects.

- **materials** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <a href="fdtdx.Material.html#fdtdx.Material" class="reference internal" title="fdtdx.materials.Material"><span class="pre"><code class="sourceCode python">Material</code></span></a>\]</span>) – Materials dictionary forwarded to every <a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a>.

- **simulation_volume** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.SimulationVolume.html#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.objects.static_material.static.SimulationVolume"><span class="pre"><code class="sourceCode python">SimulationVolume</code></span></a></span>) – Used for size/position constraints.

- **gds_center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – GDS coordinate (in metres) that maps to the x/y centre of the simulation volume.

- **flatten** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>) – Flatten sub-cell references before reading polygons. Defaults to <span class="pre">`True`</span>.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`list`</span>\[<a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.objects.static_material.gds_layer_stack.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a>\], <span class="pre">`list`</span>\[<span class="pre">`Any`</span>\]\]</span>

Returns<span class="colon">:</span>  
<span class="pre">`(objects,`</span>` `<span class="pre">`constraints)`</span> - one <a href="fdtdx.GDSLayerObject.html#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">GDSLayerObject</code></span></a> and two constraints per layer spec.

Raises<span class="colon">:</span>  
**ValueError** – If *cell_name* is not found in the library. If *layers* is empty

</div>
