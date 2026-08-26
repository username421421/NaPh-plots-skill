<div id="fdtdx-objectcontainer" class="section">

# fdtdx.ObjectContainer<a href="#fdtdx-objectcontainer" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">ObjectContainer</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">object_list</span></span>*, *<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">volume_idx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ObjectContainer" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ObjectContainer" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Container for managing simulation objects and their relationships.

This class provides a structured way to organize and access different types of simulation objects like sources, detectors, PML/periodic boundaries and devices. It maintains object lists and provides filtered access to specific object types.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_electric_conductivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_electric_conductivity"><span class="pre"><code class="sourceCode python">all_objects_diagonally_anisotropic_electric_conductivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_magnetic_conductivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_magnetic_conductivity"><span class="pre"><code class="sourceCode python">all_objects_diagonally_anisotropic_magnetic_conductivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permeability" class="reference internal" title="fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permeability"><span class="pre"><code class="sourceCode python">all_objects_diagonally_anisotropic_permeability</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permittivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permittivity"><span class="pre"><code class="sourceCode python">all_objects_diagonally_anisotropic_permittivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_isotropic_dispersion" class="reference internal" title="fdtdx.ObjectContainer.all_objects_isotropic_dispersion"><span class="pre"><code class="sourceCode python">all_objects_isotropic_dispersion</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_isotropic_electric_conductivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_isotropic_electric_conductivity"><span class="pre"><code class="sourceCode python">all_objects_isotropic_electric_conductivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_isotropic_magnetic_conductivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_isotropic_magnetic_conductivity"><span class="pre"><code class="sourceCode python">all_objects_isotropic_magnetic_conductivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_isotropic_permeability" class="reference internal" title="fdtdx.ObjectContainer.all_objects_isotropic_permeability"><span class="pre"><code class="sourceCode python">all_objects_isotropic_permeability</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_isotropic_permittivity" class="reference internal" title="fdtdx.ObjectContainer.all_objects_isotropic_permittivity"><span class="pre"><code class="sourceCode python">all_objects_isotropic_permittivity</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_non_dispersive" class="reference internal" title="fdtdx.ObjectContainer.all_objects_non_dispersive"><span class="pre"><code class="sourceCode python">all_objects_non_dispersive</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_non_electrically_conductive" class="reference internal" title="fdtdx.ObjectContainer.all_objects_non_electrically_conductive"><span class="pre"><code class="sourceCode python">all_objects_non_electrically_conductive</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_non_magnetic" class="reference internal" title="fdtdx.ObjectContainer.all_objects_non_magnetic"><span class="pre"><code class="sourceCode python">all_objects_non_magnetic</code></span></a>

- <a href="#fdtdx.ObjectContainer.all_objects_non_magnetically_conductive" class="reference internal" title="fdtdx.ObjectContainer.all_objects_non_magnetically_conductive"><span class="pre"><code class="sourceCode python">all_objects_non_magnetically_conductive</code></span></a>

- <a href="#fdtdx.ObjectContainer.any_object_subpixel_full_tensor" class="reference internal" title="fdtdx.ObjectContainer.any_object_subpixel_full_tensor"><span class="pre"><code class="sourceCode python">any_object_subpixel_full_tensor</code></span></a>

- <a href="#fdtdx.ObjectContainer.any_object_subpixel_smoothing" class="reference internal" title="fdtdx.ObjectContainer.any_object_subpixel_smoothing"><span class="pre"><code class="sourceCode python">any_object_subpixel_smoothing</code></span></a>

- <a href="#fdtdx.ObjectContainer.backward_detectors" class="reference internal" title="fdtdx.ObjectContainer.backward_detectors"><span class="pre"><code class="sourceCode python">backward_detectors</code></span></a>

- <a href="#fdtdx.ObjectContainer.bloch_objects" class="reference internal" title="fdtdx.ObjectContainer.bloch_objects"><span class="pre"><code class="sourceCode python">bloch_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.boundary_objects" class="reference internal" title="fdtdx.ObjectContainer.boundary_objects"><span class="pre"><code class="sourceCode python">boundary_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.detectors" class="reference internal" title="fdtdx.ObjectContainer.detectors"><span class="pre"><code class="sourceCode python">detectors</code></span></a>

- <a href="#fdtdx.ObjectContainer.devices" class="reference internal" title="fdtdx.ObjectContainer.devices"><span class="pre"><code class="sourceCode python">devices</code></span></a>

- <a href="#fdtdx.ObjectContainer.forward_detectors" class="reference internal" title="fdtdx.ObjectContainer.forward_detectors"><span class="pre"><code class="sourceCode python">forward_detectors</code></span></a>

- <a href="#fdtdx.ObjectContainer.has_dispersive_edot" class="reference internal" title="fdtdx.ObjectContainer.has_dispersive_edot"><span class="pre"><code class="sourceCode python">has_dispersive_edot</code></span></a>

- <a href="#fdtdx.ObjectContainer.max_num_dispersive_poles" class="reference internal" title="fdtdx.ObjectContainer.max_num_dispersive_poles"><span class="pre"><code class="sourceCode python">max_num_dispersive_poles</code></span></a>

- <a href="#fdtdx.ObjectContainer.object_list" class="reference internal" title="fdtdx.ObjectContainer.object_list"><span class="pre"><code class="sourceCode python">object_list</code></span></a>

- <a href="#fdtdx.ObjectContainer.objects" class="reference internal" title="fdtdx.ObjectContainer.objects"><span class="pre"><code class="sourceCode python">objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.pec_objects" class="reference internal" title="fdtdx.ObjectContainer.pec_objects"><span class="pre"><code class="sourceCode python">pec_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.periodic_objects" class="reference internal" title="fdtdx.ObjectContainer.periodic_objects"><span class="pre"><code class="sourceCode python">periodic_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.pmc_objects" class="reference internal" title="fdtdx.ObjectContainer.pmc_objects"><span class="pre"><code class="sourceCode python">pmc_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.pml_objects" class="reference internal" title="fdtdx.ObjectContainer.pml_objects"><span class="pre"><code class="sourceCode python">pml_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.sources" class="reference internal" title="fdtdx.ObjectContainer.sources"><span class="pre"><code class="sourceCode python">sources</code></span></a>

- <a href="#fdtdx.ObjectContainer.static_material_objects" class="reference internal" title="fdtdx.ObjectContainer.static_material_objects"><span class="pre"><code class="sourceCode python">static_material_objects</code></span></a>

- <a href="#fdtdx.ObjectContainer.volume" class="reference internal" title="fdtdx.ObjectContainer.volume"><span class="pre"><code class="sourceCode python">volume</code></span></a>

- <a href="#fdtdx.ObjectContainer.volume_idx" class="reference internal" title="fdtdx.ObjectContainer.volume_idx"><span class="pre"><code class="sourceCode python">volume_idx</code></span></a>

Methods

- <a href="#fdtdx.ObjectContainer.aset" class="reference internal" title="fdtdx.ObjectContainer.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.ObjectContainer.copy" class="reference internal" title="fdtdx.ObjectContainer.copy"><span class="pre"><code class="sourceCode python">copy</code></span></a>

- <a href="#fdtdx.ObjectContainer.get_class_fields" class="reference internal" title="fdtdx.ObjectContainer.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.ObjectContainer.get_public_fields" class="reference internal" title="fdtdx.ObjectContainer.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.ObjectContainer.index" class="reference internal" title="fdtdx.ObjectContainer.index"><span class="pre"><code class="sourceCode python">index</code></span></a>

- <a href="#fdtdx.ObjectContainer.replace_sources" class="reference internal" title="fdtdx.ObjectContainer.replace_sources"><span class="pre"><code class="sourceCode python">replace_sources</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_diagonally_anisotropic_electric_conductivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_electric_conductivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_diagonally_anisotropic_magnetic_conductivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_diagonally_anisotropic_permeability</span></span><a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permeability" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_diagonally_anisotropic_permittivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_diagonally_anisotropic_permittivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_isotropic_dispersion</span></span><a href="#fdtdx.ObjectContainer.all_objects_isotropic_dispersion" class="headerlink" title="Link to this definition">#</a>  
Whether every dispersive material applies the same poles to all three axes.

Drives the size of the material-component axis of the dispersive coefficient arrays: 1 (broadcast) when <span class="pre">`True`</span>, 3 (per-axis, diagonally anisotropic dispersion) when <span class="pre">`False`</span>.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_isotropic_electric_conductivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_isotropic_electric_conductivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_isotropic_magnetic_conductivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_isotropic_magnetic_conductivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_isotropic_permeability</span></span><a href="#fdtdx.ObjectContainer.all_objects_isotropic_permeability" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_isotropic_permittivity</span></span><a href="#fdtdx.ObjectContainer.all_objects_isotropic_permittivity" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_non_dispersive</span></span><a href="#fdtdx.ObjectContainer.all_objects_non_dispersive" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_non_electrically_conductive</span></span><a href="#fdtdx.ObjectContainer.all_objects_non_electrically_conductive" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_non_magnetic</span></span><a href="#fdtdx.ObjectContainer.all_objects_non_magnetic" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">all_objects_non_magnetically_conductive</span></span><a href="#fdtdx.ObjectContainer.all_objects_non_magnetically_conductive" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">any_object_subpixel_full_tensor</span></span><a href="#fdtdx.ObjectContainer.any_object_subpixel_full_tensor" class="headerlink" title="Link to this definition">#</a>  
True if any smoothed object requests the full 9-component tensor (vs the cheap 3-comp diagonal).

When True the permittivity is allocated as a full 9-component tensor and the anisotropic update kernel is used; when False (all smoothed objects diagonal) a 3-component diagonal allocation runs on the cheaper elementwise update, which is exact for axis-aligned interfaces.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">any_object_subpixel_smoothing</span></span><a href="#fdtdx.ObjectContainer.any_object_subpixel_smoothing" class="headerlink" title="Link to this definition">#</a>  
True if any static multi-material object requests sub-pixel dielectric smoothing.

When True the permittivity must be allocated as an anisotropic effective permittivity at interface cells even though every underlying material is isotropic. The default (diagonal) variant uses a 3-component allocation; a full 9-component tensor is only used when <span class="pre">`any_object_subpixel_full_tensor`</span> is also True.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">backward_detectors</span></span><a href="#fdtdx.ObjectContainer.backward_detectors" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">bloch_objects</span></span><a href="#fdtdx.ObjectContainer.bloch_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">boundary_objects</span></span><a href="#fdtdx.ObjectContainer.boundary_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">detectors</span></span><a href="#fdtdx.ObjectContainer.detectors" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">devices</span></span><a href="#fdtdx.ObjectContainer.devices" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">forward_detectors</span></span><a href="#fdtdx.ObjectContainer.forward_detectors" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">has_dispersive_edot</span></span><a href="#fdtdx.ObjectContainer.has_dispersive_edot" class="headerlink" title="Link to this definition">#</a>  
Whether any object uses a CCPR pole with a non-zero <span class="pre">`dE/dt`</span> coupling.

This gates allocation of the <span class="pre">`dispersive_c4`</span> coefficient array: when <span class="pre">`False`</span> (all poles are Lorentz/Drude, or there is no dispersion) the ADE update takes the classic <span class="pre">`c4`</span>-free path and stays bit-identical to pre-CCPR behaviour.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">max_num_dispersive_poles</span></span><a href="#fdtdx.ObjectContainer.max_num_dispersive_poles" class="headerlink" title="Link to this definition">#</a>  
Maximum number of dispersive poles required across all objects.

Walks every object (UniformMaterialObject, Device, StaticMultiMaterialObject) and returns the largest pole count of any Material attached to them. Drives the leading dimension of the per-cell dispersive coefficient and polarization arrays, which are zero-padded for materials with fewer poles.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">object_list</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`list`</span><span class="pre">\[</span><a href="fdtdx.SimulationObject.html#fdtdx.SimulationObject" class="reference internal" title="fdtdx.objects.object.SimulationObject"><span class="pre"><code class="sourceCode python">SimulationObject</code></span></a><span class="pre">\]</span>*<a href="#fdtdx.ObjectContainer.object_list" class="headerlink" title="Link to this definition">#</a>  
List of all simulation objects in the container.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">objects</span></span><a href="#fdtdx.ObjectContainer.objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">pec_objects</span></span><a href="#fdtdx.ObjectContainer.pec_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">periodic_objects</span></span><a href="#fdtdx.ObjectContainer.periodic_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">pmc_objects</span></span><a href="#fdtdx.ObjectContainer.pmc_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">pml_objects</span></span><a href="#fdtdx.ObjectContainer.pml_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">sources</span></span><a href="#fdtdx.ObjectContainer.sources" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">static_material_objects</span></span><a href="#fdtdx.ObjectContainer.static_material_objects" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">volume</span></span><a href="#fdtdx.ObjectContainer.volume" class="headerlink" title="Link to this definition">#</a>  

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">volume_idx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.ObjectContainer.volume_idx" class="headerlink" title="Link to this definition">#</a>  
Index of the volume object in the object list.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.ObjectContainer.aset" class="headerlink" title="Link to this definition">#</a>  
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

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">copy</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ObjectContainer.copy" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ObjectContainer.copy" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.fdtd.container.ObjectContainer"><span class="pre"><code class="sourceCode python">ObjectContainer</code></span></a></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ObjectContainer.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.ObjectContainer.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">index</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">name</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ObjectContainer.index" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ObjectContainer.index" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">ObjectContainer.</span></span><span class="sig-name descname"><span class="pre">replace_sources</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">sources</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/container.html#ObjectContainer.replace_sources" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.ObjectContainer.replace_sources" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`Self`</span></span>

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
