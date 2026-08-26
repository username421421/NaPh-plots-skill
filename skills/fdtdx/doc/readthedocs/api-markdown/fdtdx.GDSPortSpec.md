<div id="fdtdx-gdsportspec" class="section">

# fdtdx.GDSPortSpec<a href="#fdtdx-gdsportspec" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">GDSPortSpec</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">gds_layer</span></span>*, *<span class="n"><span class="pre">gds_datatype</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">propagation_axis</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">name_prefix</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'port'</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/static_material/gds_layer_stack.html#GDSPortSpec" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GDSPortSpec" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`object`</span>

Specification for a GDS port marker layer used to auto-generate sources or detectors.

A port marker is a polygon (typically a thin rectangle) on a dedicated GDS layer. Its centroid determines the x/y position of the source or detector plane inside the simulation. The source/detector is made 1 grid cell thick along <span class="pre">`propagation_axis`</span> and spans the full simulation cross-section on the remaining two axes.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.GDSPortSpec.gds_datatype" class="reference internal" title="fdtdx.GDSPortSpec.gds_datatype"><span class="pre"><code class="sourceCode python">gds_datatype</code></span></a>

- <a href="#fdtdx.GDSPortSpec.name_prefix" class="reference internal" title="fdtdx.GDSPortSpec.name_prefix"><span class="pre"><code class="sourceCode python">name_prefix</code></span></a>

- <a href="#fdtdx.GDSPortSpec.propagation_axis" class="reference internal" title="fdtdx.GDSPortSpec.propagation_axis"><span class="pre"><code class="sourceCode python">propagation_axis</code></span></a>

- <a href="#fdtdx.GDSPortSpec.gds_layer" class="reference internal" title="fdtdx.GDSPortSpec.gds_layer"><span class="pre"><code class="sourceCode python">gds_layer</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GDSPortSpec.</span></span><span class="sig-name descname"><span class="pre">gds_datatype</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a href="#fdtdx.GDSPortSpec.gds_datatype" class="headerlink" title="Link to this definition">#</a>  
GDS datatype of the port markers (default 0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSPortSpec.</span></span><span class="sig-name descname"><span class="pre">name_prefix</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'port'</span>*<a href="#fdtdx.GDSPortSpec.name_prefix" class="headerlink" title="Link to this definition">#</a>  
Prefix for generated object names. Objects are named <span class="pre">`"{name_prefix}_{index}"`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSPortSpec.</span></span><span class="sig-name descname"><span class="pre">propagation_axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a href="#fdtdx.GDSPortSpec.propagation_axis" class="headerlink" title="Link to this definition">#</a>  
Simulation axis along which the mode propagates (0=x, 1=y). Must be 0 or 1; the GDS layout encodes x/y positions only.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GDSPortSpec.</span></span><span class="sig-name descname"><span class="pre">gds_layer</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.GDSPortSpec.gds_layer" class="headerlink" title="Link to this definition">#</a>  
GDS layer containing the port marker polygons.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
