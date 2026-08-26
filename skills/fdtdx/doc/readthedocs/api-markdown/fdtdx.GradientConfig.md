<div id="fdtdx-gradientconfig" class="section">

# fdtdx.GradientConfig<a href="#fdtdx-gradientconfig" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">GradientConfig</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">method</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'reversible'</span></span>*, *<span class="n"><span class="pre">recorder</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">num_checkpoints</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">num_checkpoints_reversible</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/config.html#GradientConfig" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.GradientConfig" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Configuration for gradient computation in simulations.

This class handles settings for automatic differentiation, supporting either invertible differentiation with a recorder or checkpointing-based differentiation.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.GradientConfig.method" class="reference internal" title="fdtdx.GradientConfig.method"><span class="pre"><code class="sourceCode python">method</code></span></a>

- <a href="#fdtdx.GradientConfig.num_checkpoints" class="reference internal" title="fdtdx.GradientConfig.num_checkpoints"><span class="pre"><code class="sourceCode python">num_checkpoints</code></span></a>

- <a href="#fdtdx.GradientConfig.num_checkpoints_reversible" class="reference internal" title="fdtdx.GradientConfig.num_checkpoints_reversible"><span class="pre"><code class="sourceCode python">num_checkpoints_reversible</code></span></a>

- <a href="#fdtdx.GradientConfig.recorder" class="reference internal" title="fdtdx.GradientConfig.recorder"><span class="pre"><code class="sourceCode python">recorder</code></span></a>

Methods

- <a href="#fdtdx.GradientConfig.aset" class="reference internal" title="fdtdx.GradientConfig.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.GradientConfig.get_class_fields" class="reference internal" title="fdtdx.GradientConfig.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.GradientConfig.get_public_fields" class="reference internal" title="fdtdx.GradientConfig.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">method</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Literal`</span><span class="pre">\[</span><span class="pre">`'reversible'`</span><span class="pre">,</span> <span class="pre">`'checkpointed'`</span><span class="pre">\]</span>*<a href="#fdtdx.GradientConfig.method" class="headerlink" title="Link to this definition">#</a>  
Method for gradient computation. Can be either “reversible” when using the time reversible autodiff, or “checkpointed” for the exact checkpointing algorithm.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">num_checkpoints</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.GradientConfig.num_checkpoints" class="headerlink" title="Link to this definition">#</a>  
Optional number of checkpoints for checkpointing-based differentiation. Needs to be provided for checkpointing gradient computation. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">num_checkpoints_reversible</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.GradientConfig.num_checkpoints_reversible" class="headerlink" title="Link to this definition">#</a>  
Number of interior full-field checkpoints for the <span class="pre">`"reversible"`</span> method. The reversible backward pass reconstructs the field state by running the simulation in reverse; for lossy/dispersive materials this reverse reconstruction can accumulate numerical error over the full trajectory. Setting this to <span class="pre">`k`</span>` `<span class="pre">`-`</span>` `<span class="pre">`1`</span> partitions the run into <span class="pre">`k`</span> slices and stores a full-field checkpoint at each interior slice boundary during the forward pass. The backward pass then resets the reverse reconstruction to the exact checkpoint at every boundary, bounding the reconstruction drift to a single slice (<span class="pre">`~time_steps_total`</span>` `<span class="pre">`/`</span>` `<span class="pre">`k`</span> steps) at the cost of O(k) field memory. The default <span class="pre">`0`</span> reproduces the classic single full reverse pass (no interior checkpoints; only the final field, which is available for free, is used). Ignored by the <span class="pre">`"checkpointed"`</span> method. Must not exceed <span class="pre">`time_steps_total`</span>` `<span class="pre">`-`</span>` `<span class="pre">`1`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">recorder</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.Recorder.html#fdtdx.Recorder" class="reference internal" title="fdtdx.interfaces.recorder.Recorder"><span class="pre"><code class="sourceCode python">Recorder</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.GradientConfig.recorder" class="headerlink" title="Link to this definition">#</a>  
Optional recorder for invertible differentiation. Needs to be provided for reversible autodiff. Defaults to None

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.GradientConfig.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.GradientConfig.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">GradientConfig.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.GradientConfig.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
