<div id="fdtdx-sizeconstraint" class="section">

# fdtdx.SizeConstraint<a href="#fdtdx-sizeconstraint" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">SizeConstraint</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">object</span></span>*, *<span class="n"><span class="pre">other_object</span></span>*, *<span class="n"><span class="pre">axes</span></span>*, *<span class="n"><span class="pre">other_axes</span></span>*, *<span class="n"><span class="pre">proportions</span></span>*, *<span class="n"><span class="pre">offsets</span></span>*, *<span class="n"><span class="pre">grid_offsets</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/object.html#SizeConstraint" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.SizeConstraint" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="#fdtdx.SizeConstraint.object" class="reference internal" title="fdtdx.SizeConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

Defines a size relationship between two simulation objects.

A constraint that sets the size of one object relative to another, with optional proportions and offsets. Used to specify how objects should be sized relative to each other in the simulation.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.SizeConstraint.object" class="reference internal" title="fdtdx.SizeConstraint.object"><span class="pre"><code class="sourceCode python"><span class="bu">object</span></code></span></a>

- <a href="#fdtdx.SizeConstraint.other_object" class="reference internal" title="fdtdx.SizeConstraint.other_object"><span class="pre"><code class="sourceCode python">other_object</code></span></a>

- <a href="#fdtdx.SizeConstraint.axes" class="reference internal" title="fdtdx.SizeConstraint.axes"><span class="pre"><code class="sourceCode python">axes</code></span></a>

- <a href="#fdtdx.SizeConstraint.other_axes" class="reference internal" title="fdtdx.SizeConstraint.other_axes"><span class="pre"><code class="sourceCode python">other_axes</code></span></a>

- <a href="#fdtdx.SizeConstraint.proportions" class="reference internal" title="fdtdx.SizeConstraint.proportions"><span class="pre"><code class="sourceCode python">proportions</code></span></a>

- <a href="#fdtdx.SizeConstraint.offsets" class="reference internal" title="fdtdx.SizeConstraint.offsets"><span class="pre"><code class="sourceCode python">offsets</code></span></a>

- <a href="#fdtdx.SizeConstraint.grid_offsets" class="reference internal" title="fdtdx.SizeConstraint.grid_offsets"><span class="pre"><code class="sourceCode python">grid_offsets</code></span></a>

Methods

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.SizeConstraint.object" class="headerlink" title="Link to this definition">#</a>  
The “child” object whose size is being adjusted

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">other_object</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.SizeConstraint.other_object" class="headerlink" title="Link to this definition">#</a>  
The “parent” object that serves as reference

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">axes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeConstraint.axes" class="headerlink" title="Link to this definition">#</a>  
Which axes of the child to constrain

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">other_axes</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeConstraint.other_axes" class="headerlink" title="Link to this definition">#</a>  
Which axes of the parent to reference

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">proportions</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeConstraint.proportions" class="headerlink" title="Link to this definition">#</a>  
Size multipliers relative to parent

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeConstraint.offsets" class="headerlink" title="Link to this definition">#</a>  
Additional real-space size offsets

<!-- -->

<span class="sig-prename descclassname"><span class="pre">SizeConstraint.</span></span><span class="sig-name descname"><span class="pre">grid_offsets</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.SizeConstraint.grid_offsets" class="headerlink" title="Link to this definition">#</a>  
Additional grid-space size offsets

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
