<div id="fdtdx-material" class="section">

# fdtdx.Material<a href="#fdtdx-material" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Material</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">permittivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(1.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">1.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">1.0)</span></span>*, *<span class="n"><span class="pre">permeability</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(1.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">1.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">1.0)</span></span>*, *<span class="n"><span class="pre">electric_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*, *<span class="n"><span class="pre">magnetic_conductivity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*, *<span class="n"><span class="pre">dispersion</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/materials.html#Material" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Material" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Represents an electromagnetic material with specific electrical and magnetic properties.

This class stores the fundamental electromagnetic properties of a material for use in electromagnetic simulations. Supports both isotropic and anisotropic materials.

<div class="admonition note">

Note

All material properties are stored internally as 9-tuples (xx, xy, xz, yx, yy, yz, zx, zy, zz components). Scalar inputs are automatically broadcast to all diagonal components.

</div>

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Material.dispersion" class="reference internal" title="fdtdx.Material.dispersion"><span class="pre"><code class="sourceCode python">dispersion</code></span></a>

- <a href="#fdtdx.Material.electric_conductivity" class="reference internal" title="fdtdx.Material.electric_conductivity"><span class="pre"><code class="sourceCode python">electric_conductivity</code></span></a>

- <a href="#fdtdx.Material.has_isotropic_dispersion" class="reference internal" title="fdtdx.Material.has_isotropic_dispersion"><span class="pre"><code class="sourceCode python">has_isotropic_dispersion</code></span></a>

- <a href="#fdtdx.Material.is_all_diagonally_anisotropic" class="reference internal" title="fdtdx.Material.is_all_diagonally_anisotropic"><span class="pre"><code class="sourceCode python">is_all_diagonally_anisotropic</code></span></a>

- <a href="#fdtdx.Material.is_all_isotropic" class="reference internal" title="fdtdx.Material.is_all_isotropic"><span class="pre"><code class="sourceCode python">is_all_isotropic</code></span></a>

- <a href="#fdtdx.Material.is_diagonally_anisotropic_electric_conductivity" class="reference internal" title="fdtdx.Material.is_diagonally_anisotropic_electric_conductivity"><span class="pre"><code class="sourceCode python">is_diagonally_anisotropic_electric_conductivity</code></span></a>

- <a href="#fdtdx.Material.is_diagonally_anisotropic_magnetic_conductivity" class="reference internal" title="fdtdx.Material.is_diagonally_anisotropic_magnetic_conductivity"><span class="pre"><code class="sourceCode python">is_diagonally_anisotropic_magnetic_conductivity</code></span></a>

- <a href="#fdtdx.Material.is_diagonally_anisotropic_permeability" class="reference internal" title="fdtdx.Material.is_diagonally_anisotropic_permeability"><span class="pre"><code class="sourceCode python">is_diagonally_anisotropic_permeability</code></span></a>

- <a href="#fdtdx.Material.is_diagonally_anisotropic_permittivity" class="reference internal" title="fdtdx.Material.is_diagonally_anisotropic_permittivity"><span class="pre"><code class="sourceCode python">is_diagonally_anisotropic_permittivity</code></span></a>

- <a href="#fdtdx.Material.is_dispersive" class="reference internal" title="fdtdx.Material.is_dispersive"><span class="pre"><code class="sourceCode python">is_dispersive</code></span></a>

- <a href="#fdtdx.Material.is_electrically_conductive" class="reference internal" title="fdtdx.Material.is_electrically_conductive"><span class="pre"><code class="sourceCode python">is_electrically_conductive</code></span></a>

- <a href="#fdtdx.Material.is_isotropic_electric_conductivity" class="reference internal" title="fdtdx.Material.is_isotropic_electric_conductivity"><span class="pre"><code class="sourceCode python">is_isotropic_electric_conductivity</code></span></a>

- <a href="#fdtdx.Material.is_isotropic_magnetic_conductivity" class="reference internal" title="fdtdx.Material.is_isotropic_magnetic_conductivity"><span class="pre"><code class="sourceCode python">is_isotropic_magnetic_conductivity</code></span></a>

- <a href="#fdtdx.Material.is_isotropic_permeability" class="reference internal" title="fdtdx.Material.is_isotropic_permeability"><span class="pre"><code class="sourceCode python">is_isotropic_permeability</code></span></a>

- <a href="#fdtdx.Material.is_isotropic_permittivity" class="reference internal" title="fdtdx.Material.is_isotropic_permittivity"><span class="pre"><code class="sourceCode python">is_isotropic_permittivity</code></span></a>

- <a href="#fdtdx.Material.is_magnetic" class="reference internal" title="fdtdx.Material.is_magnetic"><span class="pre"><code class="sourceCode python">is_magnetic</code></span></a>

- <a href="#fdtdx.Material.is_magnetically_conductive" class="reference internal" title="fdtdx.Material.is_magnetically_conductive"><span class="pre"><code class="sourceCode python">is_magnetically_conductive</code></span></a>

- <a href="#fdtdx.Material.magnetic_conductivity" class="reference internal" title="fdtdx.Material.magnetic_conductivity"><span class="pre"><code class="sourceCode python">magnetic_conductivity</code></span></a>

- <a href="#fdtdx.Material.permeability" class="reference internal" title="fdtdx.Material.permeability"><span class="pre"><code class="sourceCode python">permeability</code></span></a>

- <a href="#fdtdx.Material.permittivity" class="reference internal" title="fdtdx.Material.permittivity"><span class="pre"><code class="sourceCode python">permittivity</code></span></a>

Methods

- <a href="#fdtdx.Material.aset" class="reference internal" title="fdtdx.Material.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity</code></span></a>

- <a href="#fdtdx.Material.from_loss_tangent" class="reference internal" title="fdtdx.Material.from_loss_tangent"><span class="pre"><code class="sourceCode python">from_loss_tangent</code></span></a>

- <a href="#fdtdx.Material.from_refractive_index" class="reference internal" title="fdtdx.Material.from_refractive_index"><span class="pre"><code class="sourceCode python">from_refractive_index</code></span></a>

- <a href="#fdtdx.Material.get_class_fields" class="reference internal" title="fdtdx.Material.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.Material.get_public_fields" class="reference internal" title="fdtdx.Material.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">dispersion</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><a href="fdtdx.DispersionModel.html#fdtdx.DispersionModel" class="reference internal" title="fdtdx.dispersion.DispersionModel"><span class="pre"><code class="sourceCode python">DispersionModel</code></span></a> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.Material.dispersion" class="headerlink" title="Link to this definition">#</a>  
Optional dispersion model. When set, <a href="#fdtdx.Material.permittivity" class="reference internal" title="fdtdx.Material.permittivity"><span class="pre"><code class="sourceCode python">permittivity</code></span></a> represents the high-frequency permittivity <span class="math notranslate nohighlight">\\\varepsilon\_\infty\\</span>; the full <span class="math notranslate nohighlight">\\\varepsilon(\omega)\\</span> is <span class="math notranslate nohighlight">\\\varepsilon\_\infty + \chi(\omega)\\</span> from the dispersion model. Defaults to <span class="pre">`None`</span> (non-dispersive).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">electric_conductivity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.Material.electric_conductivity" class="headerlink" title="Link to this definition">#</a>  
The electrical conductivity of the material in siemens per meter (S/m), which describes how easily electric current can flow through it. Higher values indicate materials that conduct electricity more easily. For isotropic materials, provide a scalar float. For diagonally anisotropic materials, provide a tuple of 3 floats (σx, σy, σz). For fully anisotropic materials, provide either:

> <div>
>
> - A tuple of 9 floats (σxx, σxy, σxz, σyx, σyy, σyz, σzx, σzy, σzz), or
>
> - A nested tuple ((σxx, σxy, σxz), (σyx, σyy, σyz), (σzx, σzy, σzz))
>
> </div>

Stored internally as a 9-tuple. Defaults to (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">has_isotropic_dispersion</span></span><a href="#fdtdx.Material.has_isotropic_dispersion" class="headerlink" title="Link to this definition">#</a>  
Check whether the material’s dispersion (if any) is isotropic.

Returns<span class="colon">:</span>  
True if the material is non-dispersive or every pole of its dispersion model applies the same parameters to all three axes.

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_all_diagonally_anisotropic</span></span><a href="#fdtdx.Material.is_all_diagonally_anisotropic" class="headerlink" title="Link to this definition">#</a>  
Check if all material properties are diagonally anisotropic (no off-diagonal components).

Returns<span class="colon">:</span>  
True if material is diagonally anisotropic

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_all_isotropic</span></span><a href="#fdtdx.Material.is_all_isotropic" class="headerlink" title="Link to this definition">#</a>  
Check if all material properties are isotropic (all components equal and no off-diagonal components).

Returns<span class="colon">:</span>  
True if material is isotropic, False if anisotropic

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_diagonally_anisotropic_electric_conductivity</span></span><a href="#fdtdx.Material.is_diagonally_anisotropic_electric_conductivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has diagonally anisotropic electric conductivity (no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has diagonally anisotropic electric conductivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_diagonally_anisotropic_magnetic_conductivity</span></span><a href="#fdtdx.Material.is_diagonally_anisotropic_magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has diagonally anisotropic magnetic conductivity (no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has diagonally anisotropic magnetic conductivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_diagonally_anisotropic_permeability</span></span><a href="#fdtdx.Material.is_diagonally_anisotropic_permeability" class="headerlink" title="Link to this definition">#</a>  
Check if material has diagonally anisotropic permeability (no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has diagonally anisotropic permeability

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_diagonally_anisotropic_permittivity</span></span><a href="#fdtdx.Material.is_diagonally_anisotropic_permittivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has diagonally anisotropic permittivity (no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has diagonally anisotropic permittivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_dispersive</span></span><a href="#fdtdx.Material.is_dispersive" class="headerlink" title="Link to this definition">#</a>  
Check if the material has a non-trivial dispersion model.

Returns<span class="colon">:</span>  
True if a <a href="fdtdx.DispersionModel.html#fdtdx.DispersionModel" class="reference internal" title="fdtdx.DispersionModel"><span class="pre"><code class="sourceCode python">DispersionModel</code></span></a> with at least one pole is attached.

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_electrically_conductive</span></span><a href="#fdtdx.Material.is_electrically_conductive" class="headerlink" title="Link to this definition">#</a>  
Check if material is electrically conductive (conductivity != 0.0 for any component).

Returns<span class="colon">:</span>  
True if material is electrically conductive

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_isotropic_electric_conductivity</span></span><a href="#fdtdx.Material.is_isotropic_electric_conductivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has isotropic electric conductivity (all components equal and no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has isotropic electric conductivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_isotropic_magnetic_conductivity</span></span><a href="#fdtdx.Material.is_isotropic_magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has isotropic magnetic conductivity (all components equal and no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has isotropic magnetic conductivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_isotropic_permeability</span></span><a href="#fdtdx.Material.is_isotropic_permeability" class="headerlink" title="Link to this definition">#</a>  
Check if material has isotropic permeability (all components equal and no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has isotropic permeability

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_isotropic_permittivity</span></span><a href="#fdtdx.Material.is_isotropic_permittivity" class="headerlink" title="Link to this definition">#</a>  
Check if material has isotropic permittivity (all components equal and no off-diagonal components).

Returns<span class="colon">:</span>  
True if material has isotropic permittivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_magnetic</span></span><a href="#fdtdx.Material.is_magnetic" class="headerlink" title="Link to this definition">#</a>  
Check if material has magnetic properties (permeability != 1.0 for any component).

Returns<span class="colon">:</span>  
True if material is magnetic

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">is_magnetically_conductive</span></span><a href="#fdtdx.Material.is_magnetically_conductive" class="headerlink" title="Link to this definition">#</a>  
Check if material has magnetic conductivity (magnetic loss != 0.0 for any component).

Returns<span class="colon">:</span>  
True if material has magnetic conductivity

Return type<span class="colon">:</span>  
bool

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">magnetic_conductivity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.Material.magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  
The magnetic conductivity, or magnetic loss of the material. This is an artificial parameter for numerical applications and does not represent an actual physical unit, even though often described in Ohm/m. The naming can be misleading, because it does not actually describe a conductivity, but rather an “equivalent magnetic loss parameter”. For isotropic materials, provide a scalar float. For diagonally anisotropic materials, provide a tuple of 3 floats (σx, σy, σz). For fully anisotropic materials, provide either:

> <div>
>
> - A tuple of 9 floats (σxx, σxy, σxz, σyx, σyy, σyz, σzx, σzy, σzz), or
>
> - A nested tuple ((σxx, σxy, σxz), (σyx, σyy, σyz), (σzx, σzy, σzz))
>
> </div>

Stored internally as a 9-tuple. Defaults to (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">permeability</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.Material.permeability" class="headerlink" title="Link to this definition">#</a>  
The relative permeability of the material, which describes how the magnetic field is affected by the material. Higher values indicate greater magnetic response to an applied magnetic field. For isotropic materials, provide a scalar float. For diagonally anisotropic materials, provide a tuple of 3 floats (μx, μy, μz). For fully anisotropic materials, provide either:

> <div>
>
> - A tuple of 9 floats (μxx, μxy, μxz, μyx, μyy, μyz, μzx, μzy, μzz), or
>
> - A nested tuple ((μxx, μxy, μxz), (μyx, μyy, μyz), (μzx, μzy, μzz))
>
> </div>

Stored internally as a 9-tuple. Defaults to (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">permittivity</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.Material.permittivity" class="headerlink" title="Link to this definition">#</a>  
The relative permittivity (dielectric constant) of the material, which describes how the electric field is affected by the material. Higher values indicate greater electric polarization in response to an applied electric field. For isotropic materials, provide a scalar float. For diagonally anisotropic materials, provide a tuple of 3 floats (εx, εy, εz). For fully anisotropic materials, provide either:

> <div>
>
> - A tuple of 9 floats (εxx, εxy, εxz, εyx, εyy, εyz, εzx, εzy, εzz), or
>
> - A nested tuple ((εxx, εxy, εxz), (εyx, εyy, εyz), (εzx, εzy, εzz))
>
> </div>

Stored internally as a 9-tuple. Defaults to (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0).

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Material.aset" class="headerlink" title="Link to this definition">#</a>  
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

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">from_complex_permittivity</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">permittivity</span></span>*, *<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">reference</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">frequency</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">permeability</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/materials.html#Material.from_complex_permittivity" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Material.from_complex_permittivity" class="headerlink" title="Link to this definition">#</a>  
Build a non-dispersive lossy material from a complex permittivity.

The imaginary part of the permittivity is converted to an equivalent electric conductivity <span class="math notranslate nohighlight">\\\sigma = \omega_0 \varepsilon_0 \varepsilon''\\</span> at the reference angular frequency <span class="math notranslate nohighlight">\\\omega_0 = 2\pi f_0\\</span>. Likewise, a complex <span class="pre">`permeability`</span> maps its imaginary part to a magnetic conductivity <span class="math notranslate nohighlight">\\\sigma_m = \omega_0 \mu_0 \mu''\\</span>.

Sign convention: <span class="math notranslate nohighlight">\\e^{-i\omega t}\\</span>, so a *positive* imaginary part denotes loss (<span class="math notranslate nohighlight">\\\varepsilon = \varepsilon' + i\varepsilon''\\</span>), matching the dispersion model used elsewhere in FDTDX.

<div class="admonition warning">

Warning

This reproduces the requested complex permittivity *exactly only at* the reference frequency. A constant conductivity yields <span class="math notranslate nohighlight">\\\varepsilon''(\omega) = \sigma / (\varepsilon_0 \omega)\\</span>, which falls off as <span class="math notranslate nohighlight">\\1/\omega\\</span> away from <span class="math notranslate nohighlight">\\\omega_0\\</span> — the causal behaviour of a conductor, not a frequency-flat loss. For a material whose <span class="math notranslate nohighlight">\\\varepsilon(\omega)\\</span> must be matched across a band, use a dispersion model instead. The reference frequency is consumed only to pick <span class="math notranslate nohighlight">\\\sigma\\</span>; it is not stored on the material and need not match any source.

</div>

Parameters<span class="colon">:</span>  
- **permittivity** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Complex relative permittivity <span class="math notranslate nohighlight">\\\varepsilon' + i\varepsilon''\\</span>. Scalar (isotropic) or a flat 3-tuple (diagonally anisotropic).

- **reference** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.WaveCharacter.html#fdtdx.WaveCharacter" class="reference internal" title="fdtdx.core.wavelength.WaveCharacter"><span class="pre"><code class="sourceCode python">WaveCharacter</code></span></a> \| <span class="pre">`None`</span></span>) – Reference wave characteristic. Provide exactly one of <span class="pre">`reference`</span>, <span class="pre">`wavelength`</span>, or <span class="pre">`frequency`</span>.

- **wavelength** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Free-space reference wavelength (m).

- **frequency** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Reference frequency (Hz).

- **permeability** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Optional complex relative permeability <span class="math notranslate nohighlight">\\\mu' + i\mu''\\</span>. Defaults to <span class="pre">`1.0`</span> (non-magnetic, lossless).

Returns<span class="colon">:</span>  
Material with real permittivity/permeability and the derived electric/magnetic conductivities.

Return type<span class="colon">:</span>  
<a href="#fdtdx.Material" class="reference internal" title="fdtdx.Material">Material</a>

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">from_loss_tangent</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">permittivity</span></span>*, *<span class="n"><span class="pre">loss_tangent</span></span>*, *<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">reference</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">frequency</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">permeability</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1.0</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/materials.html#Material.from_loss_tangent" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Material.from_loss_tangent" class="headerlink" title="Link to this definition">#</a>  
Build a non-dispersive lossy material from a real permittivity and loss tangent.

The loss tangent <span class="math notranslate nohighlight">\\\tan\delta = \varepsilon''/\varepsilon'\\</span> defines the imaginary part <span class="math notranslate nohighlight">\\\varepsilon'' = \varepsilon' \tan\delta\\</span>, which maps to an equivalent electric conductivity <span class="math notranslate nohighlight">\\\sigma = \omega_0 \varepsilon_0 \varepsilon' \tan\delta\\</span> at the reference frequency (see <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity()</code></span></a>).

<div class="admonition warning">

Warning

The loss is matched exactly only at the reference frequency (see <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity()</code></span></a>).

</div>

Parameters<span class="colon">:</span>  
- **permittivity** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Real relative permittivity <span class="math notranslate nohighlight">\\\varepsilon'\\</span>. Scalar (isotropic) or a flat 3-tuple (diagonally anisotropic).

- **loss_tangent** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Loss tangent <span class="math notranslate nohighlight">\\\tan\delta\\</span>. Scalar, or a flat 3-tuple matching <span class="pre">`permittivity`</span>.

- **reference** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.WaveCharacter.html#fdtdx.WaveCharacter" class="reference internal" title="fdtdx.core.wavelength.WaveCharacter"><span class="pre"><code class="sourceCode python">WaveCharacter</code></span></a> \| <span class="pre">`None`</span></span>) – Reference wave characteristic. Provide exactly one of <span class="pre">`reference`</span>, <span class="pre">`wavelength`</span>, or <span class="pre">`frequency`</span>.

- **wavelength** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Free-space reference wavelength (m).

- **frequency** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Reference frequency (Hz).

- **permeability** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Optional complex relative permeability. Defaults to <span class="pre">`1.0`</span>.

Returns<span class="colon">:</span>  
The equivalent lossy material.

Return type<span class="colon">:</span>  
<a href="#fdtdx.Material" class="reference internal" title="fdtdx.Material">Material</a>

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">from_refractive_index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">refractive_index</span></span>*, *<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">reference</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">wavelength</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">frequency</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/materials.html#Material.from_refractive_index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Material.from_refractive_index" class="headerlink" title="Link to this definition">#</a>  
Build a non-dispersive lossy material from a complex refractive index.

The complex refractive index <span class="math notranslate nohighlight">\\\tilde{n} = n + i\kappa\\</span> maps to the relative permittivity <span class="math notranslate nohighlight">\\\varepsilon = \tilde{n}^2 = (n^2 - \kappa^2) + i\\2 n \kappa\\</span>, whose imaginary part becomes an equivalent electric conductivity at the reference frequency (see <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity()</code></span></a>). Assumes a non-magnetic medium (<span class="math notranslate nohighlight">\\\mu_r = 1\\</span>); for magnetic materials specify <span class="math notranslate nohighlight">\\\varepsilon\\</span> and <span class="math notranslate nohighlight">\\\mu\\</span> directly via <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity()</code></span></a>.

Sign convention: <span class="math notranslate nohighlight">\\e^{-i\omega t}\\</span>, so a *positive* extinction coefficient <span class="math notranslate nohighlight">\\\kappa\\</span> denotes loss.

<div class="admonition warning">

Warning

The loss is matched exactly only at the reference frequency (see <a href="#fdtdx.Material.from_complex_permittivity" class="reference internal" title="fdtdx.Material.from_complex_permittivity"><span class="pre"><code class="sourceCode python">from_complex_permittivity()</code></span></a>).

</div>

Parameters<span class="colon">:</span>  
- **refractive_index** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`complex`</span> \| <span class="pre">`float`</span> \| <span class="pre">`tuple`</span></span>) – Complex refractive index <span class="math notranslate nohighlight">\\n + i\kappa\\</span>. Scalar (isotropic) or a flat 3-tuple (diagonally anisotropic).

- **reference** (<span class="sphinx_autodoc_typehints-type"><a href="fdtdx.WaveCharacter.html#fdtdx.WaveCharacter" class="reference internal" title="fdtdx.core.wavelength.WaveCharacter"><span class="pre"><code class="sourceCode python">WaveCharacter</code></span></a> \| <span class="pre">`None`</span></span>) – Reference wave characteristic. Provide exactly one of <span class="pre">`reference`</span>, <span class="pre">`wavelength`</span>, or <span class="pre">`frequency`</span>.

- **wavelength** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Free-space reference wavelength (m).

- **frequency** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`float`</span> \| <span class="pre">`None`</span></span>) – Reference frequency (Hz).

Returns<span class="colon">:</span>  
The equivalent lossy material.

Return type<span class="colon">:</span>  
<a href="#fdtdx.Material" class="reference internal" title="fdtdx.Material">Material</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Material.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Material.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Material.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
