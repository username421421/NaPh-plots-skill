<div id="fdtdx-dispersionmodel" class="section">

# fdtdx.DispersionModel<a href="#fdtdx-dispersionmodel" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">DispersionModel</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">poles</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#DispersionModel" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DispersionModel" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Linear susceptibility built from a sum of 2nd-order ADE poles.

The high-frequency permittivity <span class="math notranslate nohighlight">\\\varepsilon\_\infty\\</span> is NOT stored here - it lives in the parent <a href="fdtdx.Material.html#fdtdx.Material" class="reference internal" title="fdtdx.materials.Material"><span class="pre"><code class="sourceCode python">Material</code></span></a> as the existing <span class="pre">`permittivity`</span> field. This keeps a single source of truth for the <span class="pre">`inv_permittivities`</span> array.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.DispersionModel.is_isotropic" class="reference internal" title="fdtdx.DispersionModel.is_isotropic"><span class="pre"><code class="sourceCode python">is_isotropic</code></span></a>

- <a href="#fdtdx.DispersionModel.num_poles" class="reference internal" title="fdtdx.DispersionModel.num_poles"><span class="pre"><code class="sourceCode python">num_poles</code></span></a>

- <a href="#fdtdx.DispersionModel.poles" class="reference internal" title="fdtdx.DispersionModel.poles"><span class="pre"><code class="sourceCode python">poles</code></span></a>

Methods

- <a href="#fdtdx.DispersionModel.aset" class="reference internal" title="fdtdx.DispersionModel.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.DispersionModel.get_class_fields" class="reference internal" title="fdtdx.DispersionModel.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.DispersionModel.get_public_fields" class="reference internal" title="fdtdx.DispersionModel.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.DispersionModel.permittivity" class="reference internal" title="fdtdx.DispersionModel.permittivity"><span class="pre"><code class="sourceCode python">permittivity</code></span></a>

- <a href="#fdtdx.DispersionModel.permittivity_axes" class="reference internal" title="fdtdx.DispersionModel.permittivity_axes"><span class="pre"><code class="sourceCode python">permittivity_axes</code></span></a>

- <a href="#fdtdx.DispersionModel.susceptibility" class="reference internal" title="fdtdx.DispersionModel.susceptibility"><span class="pre"><code class="sourceCode python">susceptibility</code></span></a>

- <a href="#fdtdx.DispersionModel.susceptibility_axes" class="reference internal" title="fdtdx.DispersionModel.susceptibility_axes"><span class="pre"><code class="sourceCode python">susceptibility_axes</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">is_isotropic</span></span><a href="#fdtdx.DispersionModel.is_isotropic" class="headerlink" title="Link to this definition">#</a>  
Whether every pole applies the same parameters to all three axes.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">num_poles</span></span><a href="#fdtdx.DispersionModel.num_poles" class="headerlink" title="Link to this definition">#</a>  
Number of poles in this model.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">poles</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><a href="fdtdx.Pole.html#fdtdx.Pole" class="reference internal" title="fdtdx.dispersion.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a><span class="pre">,</span> <span class="pre">`...`</span><span class="pre">\]</span>*<a href="#fdtdx.DispersionModel.poles" class="headerlink" title="Link to this definition">#</a>  
Tuple of poles making up the susceptibility model.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.DispersionModel.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.DispersionModel.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.DispersionModel.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">permittivity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">omega</span></span>*, *<span class="n"><span class="pre">eps_inf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#DispersionModel.permittivity" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DispersionModel.permittivity" class="headerlink" title="Link to this definition">#</a>  
Complex relative permittivity <span class="math notranslate nohighlight">\\\varepsilon(\omega) = \varepsilon\_\infty + \chi(\omega)\\</span>.

Raises <span class="pre">`ValueError`</span> for models with per-axis poles; use <a href="#fdtdx.DispersionModel.permittivity_axes" class="reference internal" title="fdtdx.DispersionModel.permittivity_axes"><span class="pre"><code class="sourceCode python">permittivity_axes()</code></span></a> for those.

Parameters<span class="colon">:</span>  
- **omega** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span></span>) – Angular frequency (rad/s).

- **eps_inf** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – High-frequency permittivity. Defaults to 1.0 (vacuum).

Returns<span class="colon">:</span>  
Relative permittivity at <span class="pre">`omega`</span>.

Return type<span class="colon">:</span>  
complex

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">permittivity_axes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">omega</span></span>*, *<span class="n"><span class="pre">eps_inf</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#DispersionModel.permittivity_axes" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DispersionModel.permittivity_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis complex relative permittivity <span class="math notranslate nohighlight">\\\varepsilon_a(\omega) = \varepsilon\_{\infty,a} + \chi_a(\omega)\\</span>.

Parameters<span class="colon">:</span>  
- **omega** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span></span>) – Angular frequency (rad/s).

- **eps_inf** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>) – High-frequency permittivity — scalar or per-axis 3-tuple (the diagonal of the ε∞ tensor). Defaults to 1.0.

Returns<span class="colon">:</span>  
Relative permittivity at <span class="pre">`omega`</span> per axis <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>.

Return type<span class="colon">:</span>  
tuple

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">susceptibility</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">omega</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#DispersionModel.susceptibility" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DispersionModel.susceptibility" class="headerlink" title="Link to this definition">#</a>  
Evaluate the complex susceptibility <span class="math notranslate nohighlight">\\\chi(\omega)\\</span>.

Uses the <span class="pre">`exp(-i`</span>` `<span class="pre">`omega`</span>` `<span class="pre">`t)`</span> Fourier convention (damping appears with a <span class="pre">`-i`</span>` `<span class="pre">`gamma`</span>` `<span class="pre">`omega`</span> term in the Lorentz denominator).

Raises <span class="pre">`ValueError`</span> for models with per-axis poles; use <a href="#fdtdx.DispersionModel.susceptibility_axes" class="reference internal" title="fdtdx.DispersionModel.susceptibility_axes"><span class="pre"><code class="sourceCode python">susceptibility_axes()</code></span></a> for those.

Parameters<span class="colon">:</span>  
**omega** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span></span>) – Angular frequency (rad/s).

Returns<span class="colon">:</span>  
<span class="math notranslate nohighlight">\\\chi(\omega) = \sum_p \chi_p(\omega)\\</span>.

Return type<span class="colon">:</span>  
complex

<!-- -->

<span class="sig-prename descclassname"><span class="pre">DispersionModel.</span></span><span class="sig-name descname"><span class="pre">susceptibility_axes</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">omega</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#DispersionModel.susceptibility_axes" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.DispersionModel.susceptibility_axes" class="headerlink" title="Link to this definition">#</a>  
Evaluate the per-axis complex susceptibility <span class="math notranslate nohighlight">\\(\chi_x, \chi_y, \chi_z)\\</span>.

Uses the <span class="pre">`exp(-i`</span>` `<span class="pre">`omega`</span>` `<span class="pre">`t)`</span> Fourier convention (damping appears with a <span class="pre">`-i`</span>` `<span class="pre">`gamma`</span>` `<span class="pre">`omega`</span> term in the Lorentz denominator). For an isotropic model all three entries are equal.

Parameters<span class="colon">:</span>  
**omega** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span></span>) – Angular frequency (rad/s).

Returns<span class="colon">:</span>  
<span class="math notranslate nohighlight">\\\chi_a(\omega) = \sum_p \chi\_{p,a}(\omega)\\</span> for each axis <span class="pre">`a`</span> in <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>.

Return type<span class="colon">:</span>  
tuple

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
