<div id="fdtdx-recordingstate" class="section">

# fdtdx.RecordingState<a href="#fdtdx-recordingstate" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">RecordingState</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">data</span></span>*, *<span class="n"><span class="pre">state</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/state.html#RecordingState" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.RecordingState" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Container for simulation recording state data.

Holds field data and state information for FDTD simulations.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.RecordingState.data" class="reference internal" title="fdtdx.RecordingState.data"><span class="pre"><code class="sourceCode python">data</code></span></a>

- <a href="#fdtdx.RecordingState.state" class="reference internal" title="fdtdx.RecordingState.state"><span class="pre"><code class="sourceCode python">state</code></span></a>

Methods

- <a href="#fdtdx.RecordingState.aset" class="reference internal" title="fdtdx.RecordingState.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.RecordingState.get_class_fields" class="reference internal" title="fdtdx.RecordingState.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.RecordingState.get_public_fields" class="reference internal" title="fdtdx.RecordingState.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">RecordingState.</span></span><span class="sig-name descname"><span class="pre">data</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`Array`</span><span class="pre">\]</span>*<a href="#fdtdx.RecordingState.data" class="headerlink" title="Link to this definition">#</a>  
Dictionary mapping field names to their array values.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RecordingState.</span></span><span class="sig-name descname"><span class="pre">state</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`Array`</span><span class="pre">\]</span>*<a href="#fdtdx.RecordingState.state" class="headerlink" title="Link to this definition">#</a>  
Dictionary mapping state variable names to their array values.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">RecordingState.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.RecordingState.aset" class="headerlink" title="Link to this definition">#</a>  
Sets an attribute of this class. In contrast to the classical .at\[\].set(), this method updates the class attribute directly and does not only operate on jax pytree leaf nodes. Instead, replaces the full attribute with the new value.

The attribute can either be the attribute name of this class, or for nested classes it can also be the attribute name of a class, which itself is an attribute of this class. The syntax for this operation could look like this: “a-\>b-\>\[0\]-\>\[‘name’\]”. Here, the current class has an attribute a, which has an attribute b, which is a list, which we index at index 0, which is an element of type dictionary, which we index using the dictionary key ‘name’.

Note that dictionary keys cannot contain square brackets or single quotes (even if they are escaped).

Parameters<span class="colon">:</span>  
- **attr_name** (*str*) – Name of attribute to set

- **val** (*Any*) – Value to set the attribute to

- **create_new_ok** (*bool,* *optional*) – If false (default), throw an error if the attribute does not exist. If true, creates a new attribute if the attribute name does not exist yet.

Returns<span class="colon">:</span>  
Updated instance with new attribute value

Return type<span class="colon">:</span>  
Self

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RecordingState.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.RecordingState.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">RecordingState.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.RecordingState.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
