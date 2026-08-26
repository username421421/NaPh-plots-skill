<div id="fdtdx-fieldstate" class="section">

# fdtdx.FieldState<a href="#fdtdx-fieldstate" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">FieldState</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">E</span></span>*, *<span class="n"><span class="pre">H</span></span>*, *<span class="n"><span class="pre">psi_E</span></span>*, *<span class="n"><span class="pre">psi_H</span></span>*, *<span class="n"><span class="pre">dispersive_P_curr</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">dispersive_P_prev</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#FieldState" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.FieldState" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Dynamic electromagnetic field state that evolves each time step.

Grouping these together makes it impossible to forget a field when resetting simulation state — ArrayContainer.reset() zeroes this entire struct at once.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.FieldState.E" class="reference internal" title="fdtdx.FieldState.E"><span class="pre"><code class="sourceCode python">E</code></span></a>

- <a href="#fdtdx.FieldState.H" class="reference internal" title="fdtdx.FieldState.H"><span class="pre"><code class="sourceCode python">H</code></span></a>

- <a href="#fdtdx.FieldState.dispersive_P_curr" class="reference internal" title="fdtdx.FieldState.dispersive_P_curr"><span class="pre"><code class="sourceCode python">dispersive_P_curr</code></span></a>

- <a href="#fdtdx.FieldState.dispersive_P_prev" class="reference internal" title="fdtdx.FieldState.dispersive_P_prev"><span class="pre"><code class="sourceCode python">dispersive_P_prev</code></span></a>

- <a href="#fdtdx.FieldState.psi_E" class="reference internal" title="fdtdx.FieldState.psi_E"><span class="pre"><code class="sourceCode python">psi_E</code></span></a>

- <a href="#fdtdx.FieldState.psi_H" class="reference internal" title="fdtdx.FieldState.psi_H"><span class="pre"><code class="sourceCode python">psi_H</code></span></a>

Methods

- <a href="#fdtdx.FieldState.aset" class="reference internal" title="fdtdx.FieldState.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.FieldState.get_class_fields" class="reference internal" title="fdtdx.FieldState.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.FieldState.get_public_fields" class="reference internal" title="fdtdx.FieldState.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">E</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.FieldState.E" class="headerlink" title="Link to this definition">#</a>  
Electric field array.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">H</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span>*<a href="#fdtdx.FieldState.H" class="headerlink" title="Link to this definition">#</a>  
Magnetic field array.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">dispersive_P_curr</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.FieldState.dispersive_P_curr" class="headerlink" title="Link to this definition">#</a>  
Dispersive ADE polarization state at time step <span class="pre">`n`</span>. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>. <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">dispersive_P_prev</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`Array`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.FieldState.dispersive_P_prev" class="headerlink" title="Link to this definition">#</a>  
Dispersive ADE polarization state at time step <span class="pre">`n-1`</span>. Shape <span class="pre">`(num_poles,`</span>` `<span class="pre">`3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span>. <span class="pre">`None`</span> for non-dispersive simulations.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">psi_E</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Array`</span><span class="pre">,</span> <span class="pre">`Array`</span><span class="pre">\]\]</span>*<a href="#fdtdx.FieldState.psi_E" class="headerlink" title="Link to this definition">#</a>  
PML auxiliary electric field, stored as a dictionary mapping each PML object’s name to a tuple of two arrays (each of shape <span class="pre">`pml.grid_shape`</span>).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">psi_H</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`dict`</span><span class="pre">\[</span><span class="pre">`str`</span><span class="pre">,</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`Array`</span><span class="pre">,</span> <span class="pre">`Array`</span><span class="pre">\]\]</span>*<a href="#fdtdx.FieldState.psi_H" class="headerlink" title="Link to this definition">#</a>  
PML auxiliary magnetic field, stored as a dictionary mapping each PML object’s name to a tuple of two arrays (each of shape <span class="pre">`pml.grid_shape`</span>).

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.FieldState.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.FieldState.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">FieldState.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.FieldState.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
