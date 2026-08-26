<div id="fdtdx-lorentzpole" class="section">

# fdtdx.LorentzPole<a href="#fdtdx-lorentzpole" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">LorentzPole</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">resonance_frequency</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">damping</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">delta_epsilon</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#LorentzPole" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.LorentzPole" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.Pole.html#fdtdx.Pole" class="reference internal" title="fdtdx.dispersion.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a>

Lorentz pole parameterised by its physical constants.

The contribution to the susceptibility is

<div class="math notranslate nohighlight">

\\\chi(\omega) = \frac{\Delta\varepsilon \cdot \omega_0^2}{\omega_0^2 - \omega^2 - i\gamma\omega}.\\

</div>

Each parameter is either a scalar (isotropic) or a per-axis 3-tuple <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> for diagonally anisotropic dispersion. An axis without a resonance is expressed by a zero <span class="pre">`delta_epsilon`</span> entry on that axis.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.LorentzPole.coupling_edot" class="reference internal" title="fdtdx.LorentzPole.coupling_edot"><span class="pre"><code class="sourceCode python">coupling_edot</code></span></a>

- <a href="#fdtdx.LorentzPole.coupling_edot_axes" class="reference internal" title="fdtdx.LorentzPole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>

- <a href="#fdtdx.LorentzPole.coupling_sq" class="reference internal" title="fdtdx.LorentzPole.coupling_sq"><span class="pre"><code class="sourceCode python">coupling_sq</code></span></a>

- <a href="#fdtdx.LorentzPole.coupling_sq_axes" class="reference internal" title="fdtdx.LorentzPole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>

- <a href="#fdtdx.LorentzPole.damping" class="reference internal" title="fdtdx.LorentzPole.damping"><span class="pre"><code class="sourceCode python">damping</code></span></a>

- <a href="#fdtdx.LorentzPole.delta_epsilon" class="reference internal" title="fdtdx.LorentzPole.delta_epsilon"><span class="pre"><code class="sourceCode python">delta_epsilon</code></span></a>

- <a href="#fdtdx.LorentzPole.gamma" class="reference internal" title="fdtdx.LorentzPole.gamma"><span class="pre"><code class="sourceCode python">gamma</code></span></a>

- <a href="#fdtdx.LorentzPole.gamma_axes" class="reference internal" title="fdtdx.LorentzPole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>

- <a href="#fdtdx.LorentzPole.is_isotropic" class="reference internal" title="fdtdx.LorentzPole.is_isotropic"><span class="pre"><code class="sourceCode python">is_isotropic</code></span></a>

- <a href="#fdtdx.LorentzPole.omega_0" class="reference internal" title="fdtdx.LorentzPole.omega_0"><span class="pre"><code class="sourceCode python">omega_0</code></span></a>

- <a href="#fdtdx.LorentzPole.omega_0_axes" class="reference internal" title="fdtdx.LorentzPole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>

- <a href="#fdtdx.LorentzPole.resonance_frequency" class="reference internal" title="fdtdx.LorentzPole.resonance_frequency"><span class="pre"><code class="sourceCode python">resonance_frequency</code></span></a>

Methods

- <a href="#fdtdx.LorentzPole.aset" class="reference internal" title="fdtdx.LorentzPole.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.LorentzPole.get_class_fields" class="reference internal" title="fdtdx.LorentzPole.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.LorentzPole.get_public_fields" class="reference internal" title="fdtdx.LorentzPole.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot</span></span><a href="#fdtdx.LorentzPole.coupling_edot" class="headerlink" title="Link to this definition">#</a>  
Coefficient <span class="pre">`b`</span> of the <span class="pre">`dE/dt`</span> driving term (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.LorentzPole.coupling_edot_axes" class="reference internal" title="fdtdx.LorentzPole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot_axes</span></span><a href="#fdtdx.LorentzPole.coupling_edot_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis coefficient <span class="pre">`b`</span> of the <span class="pre">`dE/dt`</span> driving term (rad/s).

Zero for Lorentz and Drude poles (their susceptibility numerator has no <span class="pre">`omega`</span> term). A non-zero value is what distinguishes a general complex-conjugate pole-residue (CCPR) pole — it corresponds to a non-zero real part of the residue and adds the <span class="pre">`b`</span>` `<span class="pre">`E'`</span> term to the ADE. Defaults to all-zero so existing pole types need not override it.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq</span></span><a href="#fdtdx.LorentzPole.coupling_sq" class="headerlink" title="Link to this definition">#</a>  
Effective squared coupling frequency <span class="pre">`K`</span> (rad^2/s^2).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.LorentzPole.coupling_sq_axes" class="reference internal" title="fdtdx.LorentzPole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq_axes</span></span><a href="#fdtdx.LorentzPole.coupling_sq_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">damping</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.LorentzPole.damping" class="headerlink" title="Link to this definition">#</a>  
Damping rate (rad/s). Must be \>= 0. Scalar or per-axis 3-tuple.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">delta_epsilon</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.LorentzPole.delta_epsilon" class="headerlink" title="Link to this definition">#</a>  
Oscillator strength (dimensionless); the zero-frequency contribution to the susceptibility. Scalar or per-axis 3-tuple.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">gamma</span></span><a href="#fdtdx.LorentzPole.gamma" class="headerlink" title="Link to this definition">#</a>  
Damping rate (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.LorentzPole.gamma_axes" class="reference internal" title="fdtdx.LorentzPole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">gamma_axes</span></span><a href="#fdtdx.LorentzPole.gamma_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">is_isotropic</span></span><a href="#fdtdx.LorentzPole.is_isotropic" class="headerlink" title="Link to this definition">#</a>  
Whether all pole parameters are identical on the three axes.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">omega_0</span></span><a href="#fdtdx.LorentzPole.omega_0" class="headerlink" title="Link to this definition">#</a>  
Resonance angular frequency (rad/s). Zero for pure Drude poles.

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.LorentzPole.omega_0_axes" class="reference internal" title="fdtdx.LorentzPole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">omega_0_axes</span></span><a href="#fdtdx.LorentzPole.omega_0_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">resonance_frequency</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.LorentzPole.resonance_frequency" class="headerlink" title="Link to this definition">#</a>  
Resonance angular frequency (rad/s). Must be \> 0. Scalar or per-axis 3-tuple.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.LorentzPole.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.LorentzPole.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">LorentzPole.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.LorentzPole.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
