<div id="fdtdx-gridcoordinateconstraint" class="section">

# fdtdx.GridCoordinateConstraint<a href="#fdtdx-gridcoordinateconstraint" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">GridCoordinateConstraint</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">object</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">sides</span></span>*, *<span class="n"><span class="pre">coordinates</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/object.html#GridCoordinateConstraint" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GridCoordinateConstraint" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="#fdtdx.GridCoordinateConstraint.object" class="reference internal" title="fdtdx.GridCoordinateConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

Constrains an object’s position to specific grid coordinates.

Forces specific sides of an object to align with given grid coordinates. Used for precise positioning in the discretized simulation space.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.GridCoordinateConstraint.object" class="reference internal" title="fdtdx.GridCoordinateConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

- <a href="#fdtdx.GridCoordinateConstraint.axes" class="reference internal" title="fdtdx.GridCoordinateConstraint.axes"><span class="pre"><code class="sourceCode python">axes</code></span></a>

- <a href="#fdtdx.GridCoordinateConstraint.sides" class="reference internal" title="fdtdx.GridCoordinateConstraint.sides"><span class="pre"><code class="sourceCode python">sides</code></span></a>

- <a href="#fdtdx.GridCoordinateConstraint.coordinates" class="reference internal" title="fdtdx.GridCoordinateConstraint.coordinates"><span class="pre"><code class="sourceCode python">coordinates</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GridCoordinateConstraint.</span></span><span class="sig-name descname"><span class="pre">object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.GridCoordinateConstraint.object" class="headerlink" title="Link to this definition">#</a>  
The object to position

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GridCoordinateConstraint.</span></span><span class="sig-name descname"><span class="pre">axes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.GridCoordinateConstraint.axes" class="headerlink" title="Link to this definition">#</a>  
Which axes to constrain

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GridCoordinateConstraint.</span></span><span class="sig-name descname"><span class="pre">sides</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'+'`</span><span class="pre">,</span> <span class="pre">`'-'`</span><span class="pre">\],</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.GridCoordinateConstraint.sides" class="headerlink" title="Link to this definition">#</a>  
Which side of each axis (‘+’ or ‘-‘)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GridCoordinateConstraint.</span></span><span class="sig-name descname"><span class="pre">coordinates</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.GridCoordinateConstraint.coordinates" class="headerlink" title="Link to this definition">#</a>  
Grid coordinates to align with

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
