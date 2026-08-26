<div id="fdtdx-pole" class="section">

# fdtdx.Pole<a href="#fdtdx-pole" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Pole</span></span><a href="../_modules/fdtdx/dispersion.html#Pole" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Pole" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>, <span class="pre">`ABC`</span>

Abstract base class for a single 2nd-order ADE pole.

Concrete subclasses store physically-meaningful parameters (e.g. <span class="pre">`delta_epsilon`</span> for Lorentz, <span class="pre">`omega_p`</span> for Drude) and expose the unified <span class="pre">`(omega_0,`</span>` `<span class="pre">`gamma,`</span>` `<span class="pre">`coupling_sq)`</span> triplet the FDTD loop needs via per-axis properties. New pole types can subclass <a href="#fdtdx.Pole" class="reference internal" title="fdtdx.Pole"><span class="pre"><code class="sourceCode python">Pole</code></span></a> as long as they fit the 2nd-order ODE form.

Every parameter may differ per grid axis (diagonally anisotropic dispersion); the canonical accessors are the <span class="pre">`*_axes`</span> properties returning <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span> tuples. The scalar accessors (<span class="pre">`omega_0`</span> etc.) are a convenience for isotropic poles and raise for per-axis ones.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Pole.coupling_edot" class="reference internal" title="fdtdx.Pole.coupling_edot"><span class="pre"><code class="sourceCode python">coupling_edot</code></span></a>

- <a href="#fdtdx.Pole.coupling_edot_axes" class="reference internal" title="fdtdx.Pole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>

- <a href="#fdtdx.Pole.coupling_sq" class="reference internal" title="fdtdx.Pole.coupling_sq"><span class="pre"><code class="sourceCode python">coupling_sq</code></span></a>

- <a href="#fdtdx.Pole.coupling_sq_axes" class="reference internal" title="fdtdx.Pole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>

- <a href="#fdtdx.Pole.gamma" class="reference internal" title="fdtdx.Pole.gamma"><span class="pre"><code class="sourceCode python">gamma</code></span></a>

- <a href="#fdtdx.Pole.gamma_axes" class="reference internal" title="fdtdx.Pole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>

- <a href="#fdtdx.Pole.is_isotropic" class="reference internal" title="fdtdx.Pole.is_isotropic"><span class="pre"><code class="sourceCode python">is_isotropic</code></span></a>

- <a href="#fdtdx.Pole.omega_0" class="reference internal" title="fdtdx.Pole.omega_0"><span class="pre"><code class="sourceCode python">omega_0</code></span></a>

- <a href="#fdtdx.Pole.omega_0_axes" class="reference internal" title="fdtdx.Pole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>

Methods

- <a href="#fdtdx.Pole.aset" class="reference internal" title="fdtdx.Pole.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.Pole.get_class_fields" class="reference internal" title="fdtdx.Pole.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.Pole.get_public_fields" class="reference internal" title="fdtdx.Pole.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot</span></span><a href="#fdtdx.Pole.coupling_edot" class="headerlink" title="Link to this definition">#</a>  
Coefficient <span class="pre">`b`</span> of the <span class="pre">`dE/dt`</span> driving term (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.Pole.coupling_edot_axes" class="reference internal" title="fdtdx.Pole.coupling_edot_axes"><span class="pre"><code class="sourceCode python">coupling_edot_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">coupling_edot_axes</span></span><a href="#fdtdx.Pole.coupling_edot_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis coefficient <span class="pre">`b`</span> of the <span class="pre">`dE/dt`</span> driving term (rad/s).

Zero for Lorentz and Drude poles (their susceptibility numerator has no <span class="pre">`omega`</span> term). A non-zero value is what distinguishes a general complex-conjugate pole-residue (CCPR) pole — it corresponds to a non-zero real part of the residue and adds the <span class="pre">`b`</span>` `<span class="pre">`E'`</span> term to the ADE. Defaults to all-zero so existing pole types need not override it.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq</span></span><a href="#fdtdx.Pole.coupling_sq" class="headerlink" title="Link to this definition">#</a>  
Effective squared coupling frequency <span class="pre">`K`</span> (rad^2/s^2).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.Pole.coupling_sq_axes" class="reference internal" title="fdtdx.Pole.coupling_sq_axes"><span class="pre"><code class="sourceCode python">coupling_sq_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">coupling_sq_axes</span></span><a href="#fdtdx.Pole.coupling_sq_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis effective squared coupling frequency <span class="pre">`K`</span> (rad^2/s^2).

<span class="pre">`delta_epsilon`</span>` `<span class="pre">`*`</span>` `<span class="pre">`omega_0**2`</span> for a Lorentz pole and <span class="pre">`omega_p**2`</span> for a Drude pole.

This is the coefficient <span class="pre">`a`</span> of the <span class="pre">`E`</span> driving term in the unified 2nd-order ODE <span class="pre">`p''`</span>` `<span class="pre">`+`</span>` `<span class="pre">`gamma`</span>` `<span class="pre">`p'`</span>` `<span class="pre">`+`</span>` `<span class="pre">`omega_0**2`</span>` `<span class="pre">`p`</span>` `<span class="pre">`=`</span>` `<span class="pre">`a`</span>` `<span class="pre">`E`</span>` `<span class="pre">`+`</span>` `<span class="pre">`b`</span>` `<span class="pre">`E'`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">gamma</span></span><a href="#fdtdx.Pole.gamma" class="headerlink" title="Link to this definition">#</a>  
Damping rate (rad/s).

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.Pole.gamma_axes" class="reference internal" title="fdtdx.Pole.gamma_axes"><span class="pre"><code class="sourceCode python">gamma_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">gamma_axes</span></span><a href="#fdtdx.Pole.gamma_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis damping rate (rad/s).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">is_isotropic</span></span><a href="#fdtdx.Pole.is_isotropic" class="headerlink" title="Link to this definition">#</a>  
Whether all pole parameters are identical on the three axes.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">omega_0</span></span><a href="#fdtdx.Pole.omega_0" class="headerlink" title="Link to this definition">#</a>  
Resonance angular frequency (rad/s). Zero for pure Drude poles.

Raises <span class="pre">`ValueError`</span> for per-axis poles; use <a href="#fdtdx.Pole.omega_0_axes" class="reference internal" title="fdtdx.Pole.omega_0_axes"><span class="pre"><code class="sourceCode python">omega_0_axes</code></span></a>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">omega_0_axes</span></span><a href="#fdtdx.Pole.omega_0_axes" class="headerlink" title="Link to this definition">#</a>  
Per-axis resonance angular frequency (rad/s). Zero for pure Drude poles.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Pole.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Pole.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Pole.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Pole.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
