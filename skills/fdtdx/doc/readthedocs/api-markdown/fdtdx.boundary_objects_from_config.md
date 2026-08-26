<div id="fdtdx-boundary-objects-from-config" class="section">

# fdtdx.boundary_objects_from_config<a href="#fdtdx-boundary-objects-from-config" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">boundary_objects_from_config</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">config</span></span>*, *<span class="n"><span class="pre">volume</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#boundary_objects_from_config" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.boundary_objects_from_config" class="headerlink" title="Link to this definition">#</a>  
Creates boundary objects from a boundary configuration.

Creates PerfectlyMatchedLayer, BlochBoundary, PerfectElectricConductor, or PerfectMagneticConductor objects for all six boundaries (min/max x/y/z) based on the provided configuration. Also generates position constraints to properly place the boundary objects relative to the simulation volume.

Parameters<span class="colon">:</span>  
- **config** (<a href="fdtdx.BoundaryConfig.html#fdtdx.BoundaryConfig" class="reference internal" title="fdtdx.BoundaryConfig"><em>BoundaryConfig</em></a>) – Configuration object containing boundary parameters

- **volume** (<a href="fdtdx.SimulationVolume.html#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.SimulationVolume"><em>SimulationVolume</em></a>) – The main simulation volume object that the boundaries will surround

Returns<span class="colon">:</span>  
tuple containing:  
- dict mapping boundary names (‘min_x’, ‘max_x’, etc) to boundary objects

- list of PositionConstraint objects for placing the boundaries

Return type<span class="colon">:</span>  
tuple\[dict\[str, AnyBoundary\], list\[<a href="fdtdx.PositionConstraint.html#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint">PositionConstraint</a>\]\]

</div>
