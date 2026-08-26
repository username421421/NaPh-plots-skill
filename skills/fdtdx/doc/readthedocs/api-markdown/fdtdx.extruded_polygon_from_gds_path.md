<div id="fdtdx-extruded-polygon-from-gds-path" class="section">

# fdtdx.extruded_polygon_from_gds_path<a href="#fdtdx-extruded-polygon-from-gds-path" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">extruded_polygon_from_gds_path</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gds_file</span></span>*, *<span class="n"><span class="pre">cell_name</span></span>*, *<span class="n"><span class="pre">layer</span></span>*, *<span class="n"><span class="pre">datatype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">polygon_index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="o"><span class="pre">\*\*</span></span><span class="n"><span class="pre">kwargs</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/polygon.html#extruded_polygon_from_gds_path" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.extruded_polygon_from_gds_path" class="headerlink" title="Link to this definition">#</a>  
Create an ExtrudedPolygon from a polygon in a GDS file.

Parameters<span class="colon">:</span>  
- **gds_file** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span> \| <span class="pre">`Path`</span></span>) – Path to the .gds file.

- **cell_name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – Name of the GDS cell containing the polygon.

- **layer** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – GDS layer number to read.

- **datatype** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – GDS datatype (default 0).

- **polygon_index** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Which polygon to use when multiple exist on the layer (default 0).

- **\*\*kwargs** – Forwarded to ExtrudedPolygon (axis, material_name, materials, …).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.ExtrudedPolygon.html#fdtdx.ExtrudedPolygon" class="reference internal" title="fdtdx.objects.static_material.polygon.ExtrudedPolygon"><span class="pre"><code class="sourceCode python">ExtrudedPolygon</code></span></a></span>

Returns<span class="colon">:</span>  
ExtrudedPolygon with vertices centered around the origin in metres.

Raises<span class="colon">:</span>  
- **ValueError** – If the cell or layer/datatype combination is not found.

- **IndexError** – If polygon_index is out of range.

</div>
