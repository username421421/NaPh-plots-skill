<div id="fdtdx-recorder" class="section">

# fdtdx.Recorder<a href="#fdtdx-recorder" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Recorder</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">modules</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/recorder.html#Recorder" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Recorder" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Records and compresses simulation data over time using a sequence of processing modules.

The Recorder manages a pipeline of modules that process simulation data at each timestep. It supports both compression modules that reduce data size and time filters that control when data is recorded. The recorder handles initialization, compression and decompression of simulation data through its module pipeline.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Recorder.modules" class="reference internal" title="fdtdx.Recorder.modules"><span class="pre"><code class="sourceCode python">modules</code></span></a>

Methods

- <a href="#fdtdx.Recorder.aset" class="reference internal" title="fdtdx.Recorder.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.Recorder.compress" class="reference internal" title="fdtdx.Recorder.compress"><span class="pre"><code class="sourceCode python">compress</code></span></a>

- <a href="#fdtdx.Recorder.decompress" class="reference internal" title="fdtdx.Recorder.decompress"><span class="pre"><code class="sourceCode python">decompress</code></span></a>

- <a href="#fdtdx.Recorder.get_class_fields" class="reference internal" title="fdtdx.Recorder.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.Recorder.get_public_fields" class="reference internal" title="fdtdx.Recorder.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.Recorder.init_state" class="reference internal" title="fdtdx.Recorder.init_state"><span class="pre"><code class="sourceCode python">init_state</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">modules</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Sequence`</span><span class="pre">\[</span><span class="pre">`CompressionModule`</span> <span class="pre">\|</span> <span class="pre">`TimeStepFilter`</span><span class="pre">\]</span>*<a href="#fdtdx.Recorder.modules" class="headerlink" title="Link to this definition">#</a>  
Sequence of processing modules to apply to the simulation data. Can be either CompressionModule for data reduction or TimeStepFilter for controlling recording frequency.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Recorder.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">compress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">values</span></span>*, *<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/recorder.html#Recorder.compress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Recorder.compress" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.interfaces.state.RecordingState"><span class="pre"><code class="sourceCode python">RecordingState</code></span></a></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">decompress</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">state</span></span>*, *<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">key</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/recorder.html#Recorder.decompress" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Recorder.decompress" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`dict`</span>\[<span class="pre">`str`</span>, <span class="pre">`Array`</span>\], <a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.interfaces.state.RecordingState"><span class="pre"><code class="sourceCode python">RecordingState</code></span></a>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Recorder.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Recorder.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Recorder.</span></span><span class="sig-name descname"><span class="pre">init_state</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">input_shape_dtypes</span></span>*, *<span class="n"><span class="pre">max_time_steps</span></span>*, *<span class="n"><span class="pre">backend</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/interfaces/recorder.html#Recorder.init_state" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Recorder.init_state" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`Self`</span>, <a href="fdtdx.RecordingState.html#fdtdx.RecordingState" class="reference internal" title="fdtdx.interfaces.state.RecordingState"><span class="pre"><code class="sourceCode python">RecordingState</code></span></a>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
