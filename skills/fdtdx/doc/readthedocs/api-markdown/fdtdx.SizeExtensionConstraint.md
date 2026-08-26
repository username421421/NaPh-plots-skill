<div id="fdtdx-sizeextensionconstraint" class="section">

# fdtdx.SizeExtensionConstraint<a href="#fdtdx-sizeextensionconstraint" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">SizeExtensionConstraint</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">object</span></span>*, *<span class="n"><span class="pre">other_object</span></span>*, *<span class="n"><span class="pre">axis</span></span>*, *<span class="n"><span class="pre">direction</span></span>*, *<span class="n"><span class="pre">other_position</span></span>*, *<span class="n"><span class="pre">offset</span></span>*, *<span class="n"><span class="pre">grid_offset</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/object.html#SizeExtensionConstraint" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SizeExtensionConstraint" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="#fdtdx.SizeExtensionConstraint.object" class="reference internal" title="fdtdx.SizeExtensionConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

Defines how an object extends toward another object or boundary.

A constraint that extends one object’s size until it reaches another object or the simulation boundary. Can extend in positive or negative direction along an axis.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.SizeExtensionConstraint.object" class="reference internal" title="fdtdx.SizeExtensionConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.other_object" class="reference internal" title="fdtdx.SizeExtensionConstraint.other_object"><span class="pre"><code class="sourceCode python">other_object</code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.axis" class="reference internal" title="fdtdx.SizeExtensionConstraint.axis"><span class="pre"><code class="sourceCode python">axis</code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.direction" class="reference internal" title="fdtdx.SizeExtensionConstraint.direction"><span class="pre"><code class="sourceCode python">direction</code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.other_position" class="reference internal" title="fdtdx.SizeExtensionConstraint.other_position"><span class="pre"><code class="sourceCode python">other_position</code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.offset" class="reference internal" title="fdtdx.SizeExtensionConstraint.offset"><span class="pre"><code class="sourceCode python">offset</code></span></a>

- <a href="#fdtdx.SizeExtensionConstraint.grid_offset" class="reference internal" title="fdtdx.SizeExtensionConstraint.grid_offset"><span class="pre"><code class="sourceCode python">grid_offset</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.SizeExtensionConstraint.object" class="headerlink" title="Link to this definition">#</a>  
The object being extended

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">other_object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.SizeExtensionConstraint.other_object" class="headerlink" title="Link to this definition">#</a>  
Optional target object to extend to

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">axis</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.SizeExtensionConstraint.axis" class="headerlink" title="Link to this definition">#</a>  
Which axis to extend along

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">direction</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'+'`</span><span class="pre">,</span> <span class="pre">`'-'`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeExtensionConstraint.direction" class="headerlink" title="Link to this definition">#</a>  
Direction to extend (‘+’ or ‘-‘)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">other_position</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.SizeExtensionConstraint.other_position" class="headerlink" title="Link to this definition">#</a>  
Relative position on target (-1 to 1)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">offset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.SizeExtensionConstraint.offset" class="headerlink" title="Link to this definition">#</a>  
Additional real-space offset

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeExtensionConstraint.</span></span><span class="sig-name descname"><span class="pre">grid_offset</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.SizeExtensionConstraint.grid_offset" class="headerlink" title="Link to this definition">#</a>  
Additional grid-space offset

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
