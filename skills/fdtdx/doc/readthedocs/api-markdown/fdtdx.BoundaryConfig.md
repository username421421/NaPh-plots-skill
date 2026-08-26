<div id="fdtdx-boundaryconfig" class="section">

# fdtdx.BoundaryConfig<a href="#fdtdx-boundaryconfig" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">BoundaryConfig</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">boundary_type_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">boundary_type_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">boundary_type_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">boundary_type_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">boundary_type_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">boundary_type_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">thickness_grid_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">thickness_grid_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">thickness_grid_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">thickness_grid_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">thickness_grid_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">thickness_grid_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">kappa_start_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_start_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_minx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_maxx</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_miny</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_maxy</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_minz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order_maxz</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bloch_vector</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Configuration class for boundary conditions.

This class stores parameters for boundary conditions in all six directions (min/max x/y/z). Supports both PML and periodic boundaries. For PML, the parameters control the absorption properties and physical size of the PML regions.

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.BoundaryConfig.alpha_end_maxx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_maxx"><span class="pre"><code class="sourceCode python">alpha_end_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_end_maxy" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_maxy"><span class="pre"><code class="sourceCode python">alpha_end_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_end_maxz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_maxz"><span class="pre"><code class="sourceCode python">alpha_end_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_end_minx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_minx"><span class="pre"><code class="sourceCode python">alpha_end_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_end_miny" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_miny"><span class="pre"><code class="sourceCode python">alpha_end_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_end_minz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_end_minz"><span class="pre"><code class="sourceCode python">alpha_end_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_maxx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_maxx"><span class="pre"><code class="sourceCode python">alpha_order_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_maxy" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_maxy"><span class="pre"><code class="sourceCode python">alpha_order_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_maxz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_maxz"><span class="pre"><code class="sourceCode python">alpha_order_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_minx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_minx"><span class="pre"><code class="sourceCode python">alpha_order_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_miny" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_miny"><span class="pre"><code class="sourceCode python">alpha_order_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_order_minz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_order_minz"><span class="pre"><code class="sourceCode python">alpha_order_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_maxx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_maxx"><span class="pre"><code class="sourceCode python">alpha_start_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_maxy" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_maxy"><span class="pre"><code class="sourceCode python">alpha_start_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_maxz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_maxz"><span class="pre"><code class="sourceCode python">alpha_start_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_minx" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_minx"><span class="pre"><code class="sourceCode python">alpha_start_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_miny" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_miny"><span class="pre"><code class="sourceCode python">alpha_start_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.alpha_start_minz" class="reference internal" title="fdtdx.BoundaryConfig.alpha_start_minz"><span class="pre"><code class="sourceCode python">alpha_start_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.bloch_vector" class="reference internal" title="fdtdx.BoundaryConfig.bloch_vector"><span class="pre"><code class="sourceCode python">bloch_vector</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_maxx" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_maxx"><span class="pre"><code class="sourceCode python">boundary_type_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_maxy" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_maxy"><span class="pre"><code class="sourceCode python">boundary_type_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_maxz" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_maxz"><span class="pre"><code class="sourceCode python">boundary_type_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_minx" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_minx"><span class="pre"><code class="sourceCode python">boundary_type_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_miny" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_miny"><span class="pre"><code class="sourceCode python">boundary_type_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.boundary_type_minz" class="reference internal" title="fdtdx.BoundaryConfig.boundary_type_minz"><span class="pre"><code class="sourceCode python">boundary_type_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_maxx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_maxx"><span class="pre"><code class="sourceCode python">kappa_end_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_maxy" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_maxy"><span class="pre"><code class="sourceCode python">kappa_end_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_maxz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_maxz"><span class="pre"><code class="sourceCode python">kappa_end_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_minx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_minx"><span class="pre"><code class="sourceCode python">kappa_end_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_miny" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_miny"><span class="pre"><code class="sourceCode python">kappa_end_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_end_minz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_end_minz"><span class="pre"><code class="sourceCode python">kappa_end_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_maxx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_maxx"><span class="pre"><code class="sourceCode python">kappa_order_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_maxy" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_maxy"><span class="pre"><code class="sourceCode python">kappa_order_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_maxz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_maxz"><span class="pre"><code class="sourceCode python">kappa_order_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_minx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_minx"><span class="pre"><code class="sourceCode python">kappa_order_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_miny" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_miny"><span class="pre"><code class="sourceCode python">kappa_order_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_order_minz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_order_minz"><span class="pre"><code class="sourceCode python">kappa_order_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_maxx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_maxx"><span class="pre"><code class="sourceCode python">kappa_start_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_maxy" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_maxy"><span class="pre"><code class="sourceCode python">kappa_start_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_maxz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_maxz"><span class="pre"><code class="sourceCode python">kappa_start_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_minx" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_minx"><span class="pre"><code class="sourceCode python">kappa_start_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_miny" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_miny"><span class="pre"><code class="sourceCode python">kappa_start_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.kappa_start_minz" class="reference internal" title="fdtdx.BoundaryConfig.kappa_start_minz"><span class="pre"><code class="sourceCode python">kappa_start_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_maxx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_maxx"><span class="pre"><code class="sourceCode python">sigma_end_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_maxy" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_maxy"><span class="pre"><code class="sourceCode python">sigma_end_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_maxz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_maxz"><span class="pre"><code class="sourceCode python">sigma_end_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_minx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_minx"><span class="pre"><code class="sourceCode python">sigma_end_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_miny" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_miny"><span class="pre"><code class="sourceCode python">sigma_end_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_end_minz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_end_minz"><span class="pre"><code class="sourceCode python">sigma_end_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_maxx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_maxx"><span class="pre"><code class="sourceCode python">sigma_order_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_maxy" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_maxy"><span class="pre"><code class="sourceCode python">sigma_order_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_maxz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_maxz"><span class="pre"><code class="sourceCode python">sigma_order_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_minx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_minx"><span class="pre"><code class="sourceCode python">sigma_order_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_miny" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_miny"><span class="pre"><code class="sourceCode python">sigma_order_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_order_minz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_order_minz"><span class="pre"><code class="sourceCode python">sigma_order_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_maxx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_maxx"><span class="pre"><code class="sourceCode python">sigma_start_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_maxy" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_maxy"><span class="pre"><code class="sourceCode python">sigma_start_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_maxz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_maxz"><span class="pre"><code class="sourceCode python">sigma_start_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_minx" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_minx"><span class="pre"><code class="sourceCode python">sigma_start_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_miny" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_miny"><span class="pre"><code class="sourceCode python">sigma_start_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.sigma_start_minz" class="reference internal" title="fdtdx.BoundaryConfig.sigma_start_minz"><span class="pre"><code class="sourceCode python">sigma_start_minz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_maxx" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_maxx"><span class="pre"><code class="sourceCode python">thickness_grid_maxx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_maxy" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_maxy"><span class="pre"><code class="sourceCode python">thickness_grid_maxy</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_maxz" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_maxz"><span class="pre"><code class="sourceCode python">thickness_grid_maxz</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_minx" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_minx"><span class="pre"><code class="sourceCode python">thickness_grid_minx</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_miny" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_miny"><span class="pre"><code class="sourceCode python">thickness_grid_miny</code></span></a>

- <a href="#fdtdx.BoundaryConfig.thickness_grid_minz" class="reference internal" title="fdtdx.BoundaryConfig.thickness_grid_minz"><span class="pre"><code class="sourceCode python">thickness_grid_minz</code></span></a>

Methods

- <a href="#fdtdx.BoundaryConfig.aset" class="reference internal" title="fdtdx.BoundaryConfig.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.BoundaryConfig.from_uniform_bound" class="reference internal" title="fdtdx.BoundaryConfig.from_uniform_bound"><span class="pre"><code class="sourceCode python">from_uniform_bound</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_alpha_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_alpha_dict"><span class="pre"><code class="sourceCode python">get_alpha_dict</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_class_fields" class="reference internal" title="fdtdx.BoundaryConfig.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_dict"><span class="pre"><code class="sourceCode python">get_dict</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_inside_boundary_slice" class="reference internal" title="fdtdx.BoundaryConfig.get_inside_boundary_slice"><span class="pre"><code class="sourceCode python">get_inside_boundary_slice</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_kappa_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_kappa_dict"><span class="pre"><code class="sourceCode python">get_kappa_dict</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_order_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_order_dict"><span class="pre"><code class="sourceCode python">get_order_dict</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_public_fields" class="reference internal" title="fdtdx.BoundaryConfig.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_sigma_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_sigma_dict"><span class="pre"><code class="sourceCode python">get_sigma_dict</code></span></a>

- <a href="#fdtdx.BoundaryConfig.get_type_dict" class="reference internal" title="fdtdx.BoundaryConfig.get_type_dict"><span class="pre"><code class="sourceCode python">get_type_dict</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_maxx" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at max x boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_maxy" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at max y boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_maxz" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at max z boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_minx" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at min x boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_miny" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at min y boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_end_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_end_minz" class="headerlink" title="Link to this definition">#</a>  
Final alpha value at min z boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_maxx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at max x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_maxy" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at max y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_maxz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at max z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_minx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at min x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_miny" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at min y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_order_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_order_minz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for alpha grading at min z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_maxx" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at max x boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_maxy" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at max y boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_maxz" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at max z boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_minx" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at min x boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_miny" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at min y boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">alpha_start_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.alpha_start_minz" class="headerlink" title="Link to this definition">#</a>  
Initial alpha value at min z boundary. Default 0.01 \* 2 \* jnp.pi \* c / wavelength \* eps0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">bloch_vector</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`tuple`</span><span class="pre">\[</span><span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">,</span> <span class="pre">`float`</span><span class="pre">\]</span>*<a href="#fdtdx.BoundaryConfig.bloch_vector" class="headerlink" title="Link to this definition">#</a>  
Bloch wave vector (k_x, k_y, k_z) in rad/m. Each component provides the phase shift for the corresponding axis when that axis uses “bloch” boundaries. The full 3D vector is stored on every BlochBoundary; each boundary extracts the component along its own axis to compute exp(i \* k_axis \* L_axis).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_maxx" class="headerlink" title="Link to this definition">#</a>  
Boundary type at maximum x (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_maxy" class="headerlink" title="Link to this definition">#</a>  
Boundary type at maximum y (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_maxz" class="headerlink" title="Link to this definition">#</a>  
Boundary type at maximum z (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_minx" class="headerlink" title="Link to this definition">#</a>  
Boundary type at minimum x (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_miny" class="headerlink" title="Link to this definition">#</a>  
Boundary type at minimum y (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">boundary_type_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`str`</span>*<a href="#fdtdx.BoundaryConfig.boundary_type_minz" class="headerlink" title="Link to this definition">#</a>  
Boundary type at minimum z (“pml”, “periodic”, “pec”, “pmc”, or “bloch”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_maxx" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at max x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_maxy" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at max y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_maxz" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at max z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_minx" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at min x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_miny" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at min y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_end_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_end_minz" class="headerlink" title="Link to this definition">#</a>  
Final kappa value at min z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_maxx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at max x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_maxy" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at max y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_maxz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at max z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_minx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at min x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_miny" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at min y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_order_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_order_minz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for kappa grading at min z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_maxx" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at max x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_maxy" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at max y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_maxz" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at max z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_minx" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at min x boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_miny" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at min y boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">kappa_start_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.kappa_start_minz" class="headerlink" title="Link to this definition">#</a>  
Initial kappa value at min z boundary. Default 1.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_maxx" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at max x boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_maxy" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at max y boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_maxz" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at max z boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_minx" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at min x boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_miny" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at min y boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_end_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_end_minz" class="headerlink" title="Link to this definition">#</a>  
Final sigma value at min z boundary. Default -(3.0 + 1) \* jnp.log(1e-6) / (2 \* (eta0 / 1.0) \* (self.thickness \* self.\_config.uniform_spacing())).

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_maxx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at max x boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_maxy" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at max y boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_maxz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at max z boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_minx" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at min x boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_miny" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at min y boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_order_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_order_minz" class="headerlink" title="Link to this definition">#</a>  
Polynomial order for sigma grading at min z boundary. Default 3.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_maxx" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at max x boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_maxy" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at max y boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_maxz" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at max z boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_minx" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at min x boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_miny" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at min y boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">sigma_start_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span> <span class="pre">\|</span> <span class="pre">`None`</span>*<a href="#fdtdx.BoundaryConfig.sigma_start_minz" class="headerlink" title="Link to this definition">#</a>  
Initial sigma value at min z boundary. Default 0.0.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_maxx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_maxx" class="headerlink" title="Link to this definition">#</a>  
Number of grid cells for PML at maximum x boundary. Default 10.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_maxy</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_maxy" class="headerlink" title="Link to this definition">#</a>  
Number of grid cells for PML at maximum y boundary. Default 10.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_maxz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_maxz" class="headerlink" title="Link to this definition">#</a>  
Number of grid cells for PML at maximum z boundary. Default 10.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_minx</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_minx" class="headerlink" title="Link to this definition">#</a>  
Number of grid cells for PML at minimum x boundary. Default 10.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_miny</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_miny" class="headerlink" title="Link to this definition">#</a>  
Boundary type at minimum y (“pml” or “periodic”). Default “pml”.

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">thickness_grid_minz</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`int`</span>*<a href="#fdtdx.BoundaryConfig.thickness_grid_minz" class="headerlink" title="Link to this definition">#</a>  
Number of grid cells for PML at minimum z boundary. Default 10.

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.BoundaryConfig.aset" class="headerlink" title="Link to this definition">#</a>  
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

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">from_uniform_bound</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">thickness</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">10</span></span>*, *<span class="n"><span class="pre">boundary_type</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'pml'</span></span>*, *<span class="n"><span class="pre">kappa_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">kappa_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">alpha_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_start</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_end</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">sigma_order</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">override_types</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">bloch_vector</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">(0.0,</span> <span class="pre">0.0,</span> <span class="pre">0.0)</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.from_uniform_bound" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.from_uniform_bound" class="headerlink" title="Link to this definition">#</a>  
Creates a BoundaryConfig with uniform parameters for all boundaries.

Parameters<span class="colon">:</span>  
- **thickness** (*int,* *optional*) – Grid thickness to use for all PML boundaries. Defaults to 10.

- **boundary_type** (*str,* *optional*) – Type of boundary to use (“pml” or “periodic”). Defaults to “pml”.

- **kappa_start** (*float,* *optional*) – Initial kappa value for all boundaries. Defaults to 1.0.

- **kappa_end** (*float,* *optional*) – Final kappa value for all boundaries. Defaults to 1.5.

- **kappa_order** (*float,* *optional*) – Polynomial order for kappa grading at all boundaries. Defaults to 1.0.

- **alpha_start** (*float,* *optional*) – Initial alpha value for all boundaries. Defaults to 1e-8.

- **alpha_end** (*float,* *optional*) – Final alpha value for all boundaries. Defaults to 1e-8.

- **alpha_order** (*float,* *optional*) – Polynomial order for alpha grading at all boundaries. Defaults to 1.0.

- **sigma_start** (*float,* *optional*) – Initial sigma value for all boundaries. Defaults to 0.0.

- **sigma_end** (*float,* *optional*) – Final sigma value for all boundaries. Defaults to 1.0.

- **sigma_order** (*float,* *optional*) – Polynomial order for sigma grading at all boundaries. Defaults to 3.0.

- **override_types** (*dict\[str,* *str\],* *optional*) – Dictionary mapping specific boundaries (“min_x”, “max_x”, “min_y”, “max_y”, “min_z”, “max_z”) to their boundary types (“pml”, “periodic”), overriding the global boundary_type. Defaults to None.

- **bloch_vector** (*tuple\[float,* *float,* *float\],* *optional*) – Bloch wave vector (k_x, k_y, k_z) in rad/m. Each component sets the phase shift for the corresponding axis. Defaults to (0, 0, 0).

Returns<span class="colon">:</span>  
New config object with uniform parameters

Return type<span class="colon">:</span>  
<a href="#fdtdx.BoundaryConfig" class="reference internal" title="fdtdx.BoundaryConfig">BoundaryConfig</a>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_alpha_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prop</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_alpha_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_alpha_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their alpha values.

Parameters<span class="colon">:</span>  
**prop** (*Literal\["alpha_start",* *"alpha_end"\]*) – Which alpha property to get, either “alpha_start” or “alpha_end”.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective alpha values.

Return type<span class="colon">:</span>  
dict\[str, float \| None\]

Raises<span class="colon">:</span>  
**Exception** – If prop is not “alpha_start” or “alpha_end”

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.BoundaryConfig.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their grid thicknesses.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective grid thickness values.

Return type<span class="colon">:</span>  
dict\[str, int\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_inside_boundary_slice</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_inside_boundary_slice" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_inside_boundary_slice" class="headerlink" title="Link to this definition">#</a>  
Gets slice objects for the non-PML interior region of the simulation volume.

Returns<span class="colon">:</span>  
Three slice objects for indexing the x, y, z dimensions  
respectively, excluding the PML boundary regions.

Return type<span class="colon">:</span>  
tuple\[slice, slice, slice\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_kappa_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prop</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_kappa_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_kappa_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their kappa values.

Parameters<span class="colon">:</span>  
**prop** (*Literal\["kappa_start",* *"kappa_end"\]*) – Which kappa property to get, either “kappa_start” or “kappa_end”.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective kappa values.

Return type<span class="colon">:</span>  
dict\[str, float \| None\]

Raises<span class="colon">:</span>  
**Exception** – If prop is not “kappa_start” or “kappa_end”

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_order_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prop</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_order_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_order_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their polynomial order values.

Parameters<span class="colon">:</span>  
**prop** (*Literal\["sigma_order",* *"alpha_order",* *"kappa_order"\]*) – Which order property to get.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective order values.

Return type<span class="colon">:</span>  
dict\[str, float \| None\]

Raises<span class="colon">:</span>  
**Exception** – If prop is not one of the valid options

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.BoundaryConfig.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_sigma_dict</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">prop</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_sigma_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_sigma_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their sigma values.

Parameters<span class="colon">:</span>  
**prop** (*Literal\["sigma_start",* *"sigma_end"\]*) – Which sigma property to get, either “sigma_start” or “sigma_end”.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective sigma values.

Return type<span class="colon">:</span>  
dict\[str, float \| None\]

Raises<span class="colon">:</span>  
**Exception** – If prop is not “sigma_start” or “sigma_end”

<!-- -->

<span class="sig-prename descclassname"><span class="pre">BoundaryConfig.</span></span><span class="sig-name descname"><span class="pre">get_type_dict</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/objects/boundaries/initialization.html#BoundaryConfig.get_type_dict" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.BoundaryConfig.get_type_dict" class="headerlink" title="Link to this definition">#</a>  
Gets a dictionary mapping boundary names to their boundary types.

Returns<span class="colon">:</span>  
Dictionary with keys ‘min_x’, ‘max_x’, ‘min_y’, ‘max_y’, ‘min_z’, ‘max_z’  
mapping to their respective boundary types (“pml” or “periodic”).

Return type<span class="colon">:</span>  
dict\[str, str\]

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
