<div id="fdtdx-ccprpole" class="section">

# fdtdx.CCPRPole<a href="#fdtdx-ccprpole" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">CCPRPole</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">pole</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">residue</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#CCPRPole" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.CCPRPole" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.Pole.html#fdtdx.Pole" class="reference internal" title="fdtdx.dispersion.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a>

General complex-conjugate pole-residue (CCPR) pole.

A single conjugate pair contributes to the susceptibility (in the <span class="pre">`exp(-i`</span>` `<span class="pre">`omega`</span>` `<span class="pre">`t)`</span> convention, Laplace variable <span class="pre">`s`</span>` `<span class="pre">`=`</span>` `<span class="pre">`-i`</span>` `<span class="pre">`omega`</span>):

<div class="math notranslate nohighlight">

\\\chi_p(\omega) = \frac{r}{-i\omega - q} + \frac{r^\*}{-i\omega - q^\*}\\

</div>

with **complex** pole <span class="pre">`q`</span> and **complex** residue <span class="pre">`r`</span>. Summing the pair with its conjugate guarantees a real time-domain response. Combined over a common denominator this equals the unified 2nd-order form

<div class="math notranslate nohighlight">

\\\chi_p(\omega) = \frac{a - i\omega b}{\omega_0^2 - \omega^2 - i\gamma\omega}\\

</div>

with

<div class="math notranslate nohighlight">

\\\omega_0^2 = \|q\|^2, \quad \gamma = -2\\\mathrm{Re}(q), \quad a = -2\\\mathrm{Re}(r q^\*), \quad b = 2\\\mathrm{Re}(r).\\

</div>

Lorentz and Drude poles are the special case <span class="pre">`b`</span>` `<span class="pre">`=`</span>` `<span class="pre">`0`</span> (purely imaginary residue). A non-zero <span class="pre">`b`</span> (<span class="pre">`=`</span>` `<span class="pre">`coupling_edot`</span>) is the extra degree of freedom that lets CCPR fit metals (gold, silver) and arbitrary vector-fitted permittivity data.

A stable, passive (lossy) medium requires <span class="pre">`Re(q)`</span>` `<span class="pre">`<`</span>` `<span class="pre">`0`</span> (so <span class="pre">`gamma`</span>` `<span class="pre">`>`</span>` `<span class="pre">`0`</span>).

Both <span class="pre">`pole`</span> and <span class="pre">`residue`</span> are either scalars (isotropic) or per-axis 3-tuples <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> for diagonally anisotropic dispersion (e.g. a vector-fitted uniaxial material with a different <span class="pre">`(q,`</span>` `<span class="pre">`r)`</span> set per axis).

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.CCPRPole.coupling_edot" class="reference internal" title="fdtdx.CCPRPole.coupling_edot"><span class="pre"><code class="sourceCode python">coupling_edot</code></span></a>

- <a href="#fdtdx.CCPRPole.coupling_edot_axes" class="reference internal" title="fdtdx.CCPRPole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>

- <a href="#fdtdx.CCPRPole.coupling_sq" class="reference internal" title="fdtdx.CCPRPole.coupling_sq"><span class="pre"><code class="sourceCode python">coupling_sq</code></span></a>

- <a href="#fdtdx.CCPRPole.coupling_sq_axes" class="reference internal" title="fdtdx.CCPRPole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>

- <a href="#fdtdx.CCPRPole.gamma" class="reference internal" title="fdtdx.CCPRPole.gamma"><span class="pre"><code class="sourceCode python">gamma</code></span></a>

- <a href="#fdtdx.CCPRPole.gamma_axes" class="reference internal" title="fdtdx.CCPRPole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>

- <a href="#fdtdx.CCPRPole.is_isotropic" class="reference internal" title="fdtdx.CCPRPole.is_isotropic"><span class="pre"><code class="sourceCode python">is_isotropic</code></span></a>

- <a href="#fdtdx.CCPRPole.omega_0" class="reference internal" title="fdtdx.CCPRPole.omega_0"><span class="pre"><code class="sourceCode python">omega_0</code></span></a>

- <a href="#fdtdx.CCPRPole.omega_0_axes" class="reference internal" title="fdtdx.CCPRPole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>

- <a href="#fdtdx.CCPRPole.pole" class="reference internal" title="fdtdx.CCPRPole.pole"><span class="pre"><code class="sourceCode python">pole</code></span></a>

- <a href="#fdtdx.CCPRPole.residue" class="reference internal" title="fdtdx.CCPRPole.residue"><span class="pre"><code class="sourceCode python">residue</code></span></a>

Methods

- <a href="#fdtdx.CCPRPole.aset" class="reference internal" title="fdtdx.CCPRPole.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.CCPRPole.from_critical_point" class="reference internal" title="fdtdx.CCPRPole.from_critical_point"><span class="pre"><code class="sourceCode python">from_critical_point</code></span></a>

- <a href="#fdtdx.CCPRPole.get_class_fields" class="reference internal" title="fdtdx.CCPRPole.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.CCPRPole.get_public_fields" class="reference internal" title="fdtdx.CCPRPole.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot</span></span><a href="#fdtdx.CCPRPole.coupling_edot" class="headerlink" title="Link to this definition">#</a>  
Coefficient <span class="pre">`b`</span> of the <span class="pre">`dE/dt`</span> driving term (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.CCPRPole.coupling_edot_axes" class="reference internal" title="fdtdx.CCPRPole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot_axes</span></span><a href="#fdtdx.CCPRPole.coupling_edot_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq</span></span><a href="#fdtdx.CCPRPole.coupling_sq" class="headerlink" title="Link to this definition">#</a>  
Effective squared coupling frequency <span class="pre">`K`</span> (rad^2/s^2).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.CCPRPole.coupling_sq_axes" class="reference internal" title="fdtdx.CCPRPole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq_axes</span></span><a href="#fdtdx.CCPRPole.coupling_sq_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">gamma</span></span><a href="#fdtdx.CCPRPole.gamma" class="headerlink" title="Link to this definition">#</a>  
Damping rate (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.CCPRPole.gamma_axes" class="reference internal" title="fdtdx.CCPRPole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">gamma_axes</span></span><a href="#fdtdx.CCPRPole.gamma_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">is_isotropic</span></span><a href="#fdtdx.CCPRPole.is_isotropic" class="headerlink" title="Link to this definition">#</a>  
Whether all pole parameters are identical on the three axes.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">omega_0</span></span><a href="#fdtdx.CCPRPole.omega_0" class="headerlink" title="Link to this definition">#</a>  
Resonance angular frequency (rad/s). Zero for pure Drude poles.

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.CCPRPole.omega_0_axes" class="reference internal" title="fdtdx.CCPRPole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">omega_0_axes</span></span><a href="#fdtdx.CCPRPole.omega_0_axes" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">pole</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`complex`</span> <span class="pre">\|</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`complex`</span><span class="pre">,</span> <span class="pre">`complex`</span><span class="pre">,</span> <span class="pre">`complex`</span><span class="pre">\]</span>*<a href="#fdtdx.CCPRPole.pole" class="headerlink" title="Link to this definition">#</a>  
Complex pole <span class="pre">`q`</span> (rad/s). <span class="pre">`Re(q)`</span>` `<span class="pre">`<`</span>` `<span class="pre">`0`</span> for a stable, lossy medium. Scalar or per-axis 3-tuple.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">residue</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`complex`</span> <span class="pre">\|</span> <span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`complex`</span><span class="pre">,</span> <span class="pre">`complex`</span><span class="pre">,</span> <span class="pre">`complex`</span><span class="pre">\]</span>*<a href="#fdtdx.CCPRPole.residue" class="headerlink" title="Link to this definition">#</a>  
Complex residue <span class="pre">`r`</span> (rad/s). Scalar or per-axis 3-tuple.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.CCPRPole.aset" class="headerlink" title="Link to this definition">#</a>  
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

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">from_critical_point</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">amplitude</span></span>*, *<span class="n"><span class="pre">phase</span></span>*, *<span class="n"><span class="pre">resonance_frequency</span></span>*, *<span class="n"><span class="pre">damping</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/dispersion.html#CCPRPole.from_critical_point" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.CCPRPole.from_critical_point" class="headerlink" title="Link to this definition">#</a>  
Build a CCPR pole from critical-point (modified-Lorentz) parameters.

The critical-point model term (<span class="pre">`exp(-i`</span>` `<span class="pre">`omega`</span>` `<span class="pre">`t)`</span> convention) is

<div class="math notranslate nohighlight">

\\\chi_p(\omega) = A\\\Omega\left\[ \frac{e^{i\phi}}{\Omega - \omega - i\Gamma} + \frac{e^{-i\phi}}{\Omega + \omega + i\Gamma}\right\],\\

</div>

which is the parameterization commonly reported for fitted metal permittivities. This maps to the complex pole/residue

<div class="math notranslate nohighlight">

\\q = -\Gamma - i\Omega, \qquad r = i\\A\\\Omega\\e^{i\phi}.\\

</div>

Parameters<span class="colon">:</span>  
- **amplitude** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Dimensionless amplitude <span class="math notranslate nohighlight">\\A\\</span>.

- **phase** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Phase <span class="math notranslate nohighlight">\\\phi\\</span> (radians).

- **resonance_frequency** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Resonance <span class="math notranslate nohighlight">\\\Omega\\</span> (rad/s).

- **damping** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span></span>) – Broadening <span class="math notranslate nohighlight">\\\Gamma\\</span> (rad/s), <span class="pre">`>`</span>` `<span class="pre">`0`</span> for loss.

Returns<span class="colon">:</span>  
Equivalent pole with the <span class="pre">`(q,`</span>` `<span class="pre">`r)`</span> above.

Return type<span class="colon">:</span>  
<a href="#fdtdx.CCPRPole" class="reference internal" title="fdtdx.CCPRPole">CCPRPole</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.CCPRPole.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">CCPRPole.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.CCPRPole.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
