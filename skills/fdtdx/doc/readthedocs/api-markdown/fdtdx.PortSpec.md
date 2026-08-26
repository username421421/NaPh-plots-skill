<div id="fdtdx-portspec" class="section">

# fdtdx.PortSpec<a href="#fdtdx-portspec" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">PortSpec</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">center</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">width</span></span>*, *<span class="n"><span class="pre">height</span></span>*, *<span class="n"><span class="pre">mode_index</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*, *<span class="n"><span class="pre">filter_pol</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'te'</span></span>*, *<span class="n"><span class="pre">name</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/utils/sparams.html#PortSpec" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PortSpec" class="headerlink" title="Link to this definition">#</a>  
Bases: <span class="pre">`object`</span>

Specification for a simulation port (input source or output detector).

Coordinates are expressed in the *core* coordinate system where the origin corresponds to the start of the simulation domain (excluding PML padding).

Parameters<span class="colon">:</span>  
- **center** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – 3-D centre position <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> in metres, relative to the start of the core region.

- **axis** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Propagation axis - <span class="pre">`0`</span> for x, <span class="pre">`1`</span> for y, <span class="pre">`2`</span> for z.

- **direction** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Literal`</span>\[<span class="pre">`'+'`</span>, <span class="pre">`'-'`</span>\]</span>) – Propagation direction along <span class="pre">`axis`</span> - <span class="pre">`'+'`</span> or <span class="pre">`'-'`</span>.

- **width** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Cross-section extent (metres) along the first transverse axis.

- **height** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Cross-section extent (metres) along the second transverse axis.

- **mode_index** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Waveguide mode index (default 0 = fundamental mode).

- **filter_pol** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`Optional`</span>\[<span class="pre">`Literal`</span>\[<span class="pre">`'te'`</span>, <span class="pre">`'tm'`</span>\]\]</span>) – Polarisation filter - <span class="pre">`'te'`</span>, <span class="pre">`'tm'`</span>, or <span class="pre">`None`</span>.

- **name** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – Optional name for the source/detector object.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.PortSpec.filter_pol" class="reference internal" title="fdtdx.PortSpec.filter_pol"><span class="pre"><code class="sourceCode python">filter_pol</code></span></a>

- <a href="#fdtdx.PortSpec.mode_index" class="reference internal" title="fdtdx.PortSpec.mode_index"><span class="pre"><code class="sourceCode python">mode_index</code></span></a>

- <a href="#fdtdx.PortSpec.name" class="reference internal" title="fdtdx.PortSpec.name"><span class="pre"><code class="sourceCode python">name</code></span></a>

- <a href="#fdtdx.PortSpec.center" class="reference internal" title="fdtdx.PortSpec.center"><span class="pre"><code class="sourceCode python">center</code></span></a>

- <a href="#fdtdx.PortSpec.axis" class="reference internal" title="fdtdx.PortSpec.axis"><span class="pre"><code class="sourceCode python">axis</code></span></a>

- <a href="#fdtdx.PortSpec.direction" class="reference internal" title="fdtdx.PortSpec.direction"><span class="pre"><code class="sourceCode python">direction</code></span></a>

- <a href="#fdtdx.PortSpec.width" class="reference internal" title="fdtdx.PortSpec.width"><span class="pre"><code class="sourceCode python">width</code></span></a>

- <a href="#fdtdx.PortSpec.height" class="reference internal" title="fdtdx.PortSpec.height"><span class="pre"><code class="sourceCode python">height</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">filter_pol</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Optional`</span><span class="pre">\[</span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'te'`</span><span class="pre">,</span> <span class="pre">`'tm'`</span><span class="pre">\]\]</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">'te'</span>*<a href="#fdtdx.PortSpec.filter_pol" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">mode_index</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">0</span>*<a href="#fdtdx.PortSpec.mode_index" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">name</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span><span class="w"> </span><span class="p"><span class="pre">=</span></span><span class="w"> </span><span class="pre">''</span>*<a href="#fdtdx.PortSpec.name" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">center</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.PortSpec.center" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.PortSpec.axis" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">direction</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'+'`</span><span class="pre">,</span> <span class="pre">`'-'`</span><span class="pre">\]</span>*<a href="#fdtdx.PortSpec.direction" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">width</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.PortSpec.width" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PortSpec.</span></span><span class="sig-name descname"><span class="pre">height</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.PortSpec.height" class="headerlink" title="Link to this definition">#</a>  

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
