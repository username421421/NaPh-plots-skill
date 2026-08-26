<div id="fdtdx-positionconstraint" class="section">

# fdtdx.PositionConstraint<a href="#fdtdx-positionconstraint" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">PositionConstraint</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">object</span></span>*, *<span class="n"><span class="pre">other_object</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">object_positions</span></span>*, *<span class="n"><span class="pre">other_object_positions</span></span>*, *<span class="n"><span class="pre">margins</span></span>*, *<span class="n"><span class="pre">grid_margins</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/object.html#PositionConstraint" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.PositionConstraint" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="#fdtdx.PositionConstraint.object" class="reference internal" title="fdtdx.PositionConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

Defines a positional relationship between two simulation objects.

A constraint that positions one object relative to another, with optional margins and offsets. Used to specify how objects should be placed in the simulation volume relative to each other.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.PositionConstraint.object" class="reference internal" title="fdtdx.PositionConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

- <a href="#fdtdx.PositionConstraint.other_object" class="reference internal" title="fdtdx.PositionConstraint.other_object"><span class="pre"><code class="sourceCode python">other_object</code></span></a>

- <a href="#fdtdx.PositionConstraint.axes" class="reference internal" title="fdtdx.PositionConstraint.axes"><span class="pre"><code class="sourceCode python">axes</code></span></a>

- <a href="#fdtdx.PositionConstraint.object_positions" class="reference internal" title="fdtdx.PositionConstraint.object_positions"><span class="pre"><code class="sourceCode python">object_positions</code></span></a>

- <a href="#fdtdx.PositionConstraint.other_object_positions" class="reference internal" title="fdtdx.PositionConstraint.other_object_positions"><span class="pre"><code class="sourceCode python">other_object_positions</code></span></a>

- <a href="#fdtdx.PositionConstraint.margins" class="reference internal" title="fdtdx.PositionConstraint.margins"><span class="pre"><code class="sourceCode python">margins</code></span></a>

- <a href="#fdtdx.PositionConstraint.grid_margins" class="reference internal" title="fdtdx.PositionConstraint.grid_margins"><span class="pre"><code class="sourceCode python">grid_margins</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.PositionConstraint.object" class="headerlink" title="Link to this definition">#</a>  
The “child” object whose position is being adjusted

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">other_object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.PositionConstraint.other_object" class="headerlink" title="Link to this definition">#</a>  
The “parent” object that serves as reference

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">axes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.PositionConstraint.axes" class="headerlink" title="Link to this definition">#</a>  
Which axes (x,y,z) this constraint applies to

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">object_positions</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.PositionConstraint.object_positions" class="headerlink" title="Link to this definition">#</a>  
Relative positions on child object (-1 to 1)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">other_object_positions</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.PositionConstraint.other_object_positions" class="headerlink" title="Link to this definition">#</a>  
Relative positions on parent object (-1 to 1)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">margins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.PositionConstraint.margins" class="headerlink" title="Link to this definition">#</a>  
Optional real-space margins between objects

<!-- -->

<span class="sig-prename descclassname"><span class="pre">PositionConstraint.</span></span><span class="sig-name descname"><span class="pre">grid_margins</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.PositionConstraint.grid_margins" class="headerlink" title="Link to this definition">#</a>  
Optional grid-space margins between objects

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
