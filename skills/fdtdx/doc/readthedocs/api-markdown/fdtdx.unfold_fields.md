<div id="fdtdx-unfold-fields" class="section">

# fdtdx.unfold_fields<a href="#fdtdx-unfold-fields" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">unfold_fields</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">field</span></span>*, *<span class="n"><span class="pre">symmetry</span></span>*, *<span class="n"><span class="pre">field_type</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/fdtd/symmetry.html#unfold_fields" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.unfold_fields" class="headerlink" title="Link to this definition">#</a>  
Reconstruct a full-domain <span class="pre">`(3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span> field array from the reduced field.

Mirrors the field across each symmetric axis with the correct per-component parity and concatenates the mirror image in front of the kept half, so the symmetry plane ends up at the center of the reconstructed array.

Parameters<span class="colon">:</span>  
- **field** (*jax.Array*) – Reduced field, shape <span class="pre">`(3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span> (component axis first).

- **symmetry** (*tuple\[int,* *int,* *int\]*) – Per-axis symmetry <span class="pre">`(x,`</span>` `<span class="pre">`y,`</span>` `<span class="pre">`z)`</span>; see module docstring.

- **field_type** (*Literal\["E",* *"H"\]*) – Whether <span class="pre">`field`</span> is the electric or magnetic field.

Returns<span class="colon">:</span>  
Full-domain field; each symmetric axis is doubled in size.

Return type<span class="colon">:</span>  
jax.Array

</div>
