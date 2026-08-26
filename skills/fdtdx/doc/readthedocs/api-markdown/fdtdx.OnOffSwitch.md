<div id="fdtdx-onoffswitch" class="section">

# fdtdx.OnOffSwitch<a href="#fdtdx-onoffswitch" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">OnOffSwitch</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">start_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">start_after_periods</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">end_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">end_after_periods</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">on_for_time</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">on_for_periods</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">period</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">fixed_on_time_steps</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">is_always_off</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*, *<span class="n"><span class="pre">interval</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/switch.html#OnOffSwitch" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.OnOffSwitch" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.OnOffSwitch.end_after_periods" class="reference internal" title="fdtdx.OnOffSwitch.end_after_periods"><span class="pre"><code class="sourceCode python">end_after_periods</code></span></a>

- <a href="#fdtdx.OnOffSwitch.end_time" class="reference internal" title="fdtdx.OnOffSwitch.end_time"><span class="pre"><code class="sourceCode python">end_time</code></span></a>

- <a href="#fdtdx.OnOffSwitch.fixed_on_time_steps" class="reference internal" title="fdtdx.OnOffSwitch.fixed_on_time_steps"><span class="pre"><code class="sourceCode python">fixed_on_time_steps</code></span></a>

- <a href="#fdtdx.OnOffSwitch.interval" class="reference internal" title="fdtdx.OnOffSwitch.interval"><span class="pre"><code class="sourceCode python">interval</code></span></a>

- <a href="#fdtdx.OnOffSwitch.is_always_off" class="reference internal" title="fdtdx.OnOffSwitch.is_always_off"><span class="pre"><code class="sourceCode python">is_always_off</code></span></a>

- <a href="#fdtdx.OnOffSwitch.is_default_always_on" class="reference internal" title="fdtdx.OnOffSwitch.is_default_always_on"><span class="pre"><code class="sourceCode python">is_default_always_on</code></span></a>

- <a href="#fdtdx.OnOffSwitch.on_for_periods" class="reference internal" title="fdtdx.OnOffSwitch.on_for_periods"><span class="pre"><code class="sourceCode python">on_for_periods</code></span></a>

- <a href="#fdtdx.OnOffSwitch.on_for_time" class="reference internal" title="fdtdx.OnOffSwitch.on_for_time"><span class="pre"><code class="sourceCode python">on_for_time</code></span></a>

- <a href="#fdtdx.OnOffSwitch.period" class="reference internal" title="fdtdx.OnOffSwitch.period"><span class="pre"><code class="sourceCode python">period</code></span></a>

- <a href="#fdtdx.OnOffSwitch.start_after_periods" class="reference internal" title="fdtdx.OnOffSwitch.start_after_periods"><span class="pre"><code class="sourceCode python">start_after_periods</code></span></a>

- <a href="#fdtdx.OnOffSwitch.start_time" class="reference internal" title="fdtdx.OnOffSwitch.start_time"><span class="pre"><code class="sourceCode python">start_time</code></span></a>

Methods

- <a href="#fdtdx.OnOffSwitch.aset" class="reference internal" title="fdtdx.OnOffSwitch.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.OnOffSwitch.calculate_on_list" class="reference internal" title="fdtdx.OnOffSwitch.calculate_on_list"><span class="pre"><code class="sourceCode python">calculate_on_list</code></span></a>

- <a href="#fdtdx.OnOffSwitch.calculate_time_step_to_on_arr_idx" class="reference internal" title="fdtdx.OnOffSwitch.calculate_time_step_to_on_arr_idx"><span class="pre"><code class="sourceCode python">calculate_time_step_to_on_arr_idx</code></span></a>

- <a href="#fdtdx.OnOffSwitch.get_class_fields" class="reference internal" title="fdtdx.OnOffSwitch.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.OnOffSwitch.get_public_fields" class="reference internal" title="fdtdx.OnOffSwitch.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.OnOffSwitch.is_on_at_time_step" class="reference internal" title="fdtdx.OnOffSwitch.is_on_at_time_step"><span class="pre"><code class="sourceCode python">is_on_at_time_step</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">end_after_periods</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.end_after_periods" class="headerlink" title="Link to this definition">#</a>  
end time after the period

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">end_time</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.end_time" class="headerlink" title="Link to this definition">#</a>  
end time of the switch

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">fixed_on_time_steps</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`list`</span><span class="pre">\[</span><span class="pre">`int`</span><span class="pre">\]</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.fixed_on_time_steps" class="headerlink" title="Link to this definition">#</a>  
list of fixed time steps

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">interval</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.OnOffSwitch.interval" class="headerlink" title="Link to this definition">#</a>  
interval of the switch

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">is_always_off</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`bool`</span>*<a href="#fdtdx.OnOffSwitch.is_always_off" class="headerlink" title="Link to this definition">#</a>  
whether switch is always off

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">is_default_always_on</span></span><a href="#fdtdx.OnOffSwitch.is_default_always_on" class="headerlink" title="Link to this definition">#</a>  
Return whether the switch is the default all-steps-on switch.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">on_for_periods</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.on_for_periods" class="headerlink" title="Link to this definition">#</a>  
period when the switch is active

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">on_for_time</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.on_for_time" class="headerlink" title="Link to this definition">#</a>  
time when the switch is active

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">period</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.period" class="headerlink" title="Link to this definition">#</a>  
period of the switch

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">start_after_periods</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.start_after_periods" class="headerlink" title="Link to this definition">#</a>  
start time after the period

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">start_time</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.OnOffSwitch.start_time" class="headerlink" title="Link to this definition">#</a>  
start time of the switch

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.OnOffSwitch.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">calculate_on_list</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">num_total_time_steps</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/switch.html#OnOffSwitch.calculate_on_list" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.OnOffSwitch.calculate_on_list" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`bool`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">calculate_time_step_to_on_arr_idx</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">num_total_time_steps</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/switch.html#OnOffSwitch.calculate_time_step_to_on_arr_idx" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.OnOffSwitch.calculate_time_step_to_on_arr_idx" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`int`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.OnOffSwitch.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.OnOffSwitch.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">OnOffSwitch.</span></span><span class="sig-name descname"><span class="pre">is_on_at_time_step</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">time_step</span></span>*, *<span class="n"><span class="pre">time_step_duration</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/switch.html#OnOffSwitch.is_on_at_time_step" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.OnOffSwitch.is_on_at_time_step" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`bool`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
