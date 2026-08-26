<div id="fdtdx-wavecharacter" class="section">

# fdtdx.WaveCharacter<a href="#fdtdx-wavecharacter" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">WaveCharacter</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">phase_shift</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">0.0</span></span>*, *<span class="n"><span class="pre">period</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">frequency</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/wavelength.html#WaveCharacter" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.WaveCharacter" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Class describing a wavelength/period/frequency in free space. Importantly, the wave characteristic conversion is based on a free space wave when using the wavelength (For conversion, a refractive index of 1 is used).

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.WaveCharacter.frequency" class="reference internal" title="fdtdx.WaveCharacter.frequency"><span class="pre"><code class="sourceCode python">frequency</code></span></a>

- <a href="#fdtdx.WaveCharacter.period" class="reference internal" title="fdtdx.WaveCharacter.period"><span class="pre"><code class="sourceCode python">period</code></span></a>

- <a href="#fdtdx.WaveCharacter.phase_shift" class="reference internal" title="fdtdx.WaveCharacter.phase_shift"><span class="pre"><code class="sourceCode python">phase_shift</code></span></a>

- <a href="#fdtdx.WaveCharacter.wavelength" class="reference internal" title="fdtdx.WaveCharacter.wavelength"><span class="pre"><code class="sourceCode python">wavelength</code></span></a>

Methods

- <a href="#fdtdx.WaveCharacter.aset" class="reference internal" title="fdtdx.WaveCharacter.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.WaveCharacter.get_class_fields" class="reference internal" title="fdtdx.WaveCharacter.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.WaveCharacter.get_frequency" class="reference internal" title="fdtdx.WaveCharacter.get_frequency"><span class="pre"><code class="sourceCode python">get_frequency</code></span></a>

- <a href="#fdtdx.WaveCharacter.get_period" class="reference internal" title="fdtdx.WaveCharacter.get_period"><span class="pre"><code class="sourceCode python">get_period</code></span></a>

- <a href="#fdtdx.WaveCharacter.get_public_fields" class="reference internal" title="fdtdx.WaveCharacter.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.WaveCharacter.get_wavelength" class="reference internal" title="fdtdx.WaveCharacter.get_wavelength"><span class="pre"><code class="sourceCode python">get_wavelength</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">frequency</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.WaveCharacter.frequency" class="headerlink" title="Link to this definition">#</a>  
Optional frequency in Hz. Mutually exclusive with period and wavelength.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">period</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.WaveCharacter.period" class="headerlink" title="Link to this definition">#</a>  
Optional period in seconds. Mutually exclusive with wavelength and frequency. Defaults to None.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">phase_shift</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.WaveCharacter.phase_shift" class="headerlink" title="Link to this definition">#</a>  
Phase shift in radians. Defaults to 0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">wavelength</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.WaveCharacter.wavelength" class="headerlink" title="Link to this definition">#</a>  
Optional wavelength in meters for free space propagation. Mutually exclusive with period and frequency. Defaults to None.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.WaveCharacter.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.WaveCharacter.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">get_frequency</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/core/wavelength.html#WaveCharacter.get_frequency" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.WaveCharacter.get_frequency" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">get_period</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/core/wavelength.html#WaveCharacter.get_period" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.WaveCharacter.get_period" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.WaveCharacter.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">WaveCharacter.</span></span><span class="sig-name descname"><span class="pre">get_wavelength</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/core/wavelength.html#WaveCharacter.get_wavelength" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.WaveCharacter.get_wavelength" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
