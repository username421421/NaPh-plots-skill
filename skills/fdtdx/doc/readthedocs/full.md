![](_images/logo.png)

<div id="fdtdx-documentation" class="section">

# FDTDX Documentation<a href="#fdtdx-documentation" class="headerlink" title="Link to this heading">#</a>

**FDTDX** is an efficient open-source Python package for the simulation and design of three-dimensional photonic nanostructures using the Finite-Difference Time-Domain (FDTD) method. Built on JAX, it provides native GPU support and automatic differentiation capabilities, making it ideal for large-scale design tasks.

<div id="key-features" class="section">

## Key Features<a href="#key-features" class="headerlink" title="Link to this heading">#</a>

The key features differentiating FDTDX from other simulation software packages like Meep (which is also great!) are the following:

- **High Performance**: GPU-accelerated FDTD simulations with multi-GPU scaling capabilities

- **Memory Efficient**: Leverages time-reversibility in Maxwell’s equations for efficient gradient computation

- **Automatic Differentiation**: Built-in gradient-based optimization for complex 3D structures

- **User-Friendly API**: Intuitive positioning and sizing of objects in absolute or relative coordinates

- **Large-Scale Design**: Capable of handling simulations with billions of grid cells

- **Open Source**: Freely available for research, development and commercial use.

Check out the Quickstart Guides for an introduction into FDTDX and the examples in the github repository!

</div>

<div id="installation" class="section">

## Installation<a href="#installation" class="headerlink" title="Link to this heading">#</a>

Install FDTDX using pip:

<div class="highlight-bash notranslate">

<div class="highlight">

    pip install fdtdx

</div>

</div>

For development installation, clone the repository and install in editable mode:

<div class="highlight-bash notranslate">

<div class="highlight">

    git clone https://github.com/ymahlau/fdtdx
    cd fdtdx
    pip install -e ".[dev]"

</div>

</div>

</div>

<div id="citation" class="section">

## Citation<a href="#citation" class="headerlink" title="Link to this heading">#</a>

If you find this repository helpful for your work, please consider citing:

<div class="highlight-bibtex notranslate">

<div class="highlight">

    @article{Mahlau2026,
       doi = {10.21105/joss.08912},
       url = {https://doi.org/10.21105/joss.08912},
       year = {2026},
       publisher = {The Open Journal},
       volume = {11},
       number = {117},
       pages = {8912},
       author = {Mahlau, Yannik and Schubert, Frederik and Berg, Lukas and Rosenhahn, Bodo},
       title = {FDTDX: High-Performance Open-Source FDTD Simulation with Automatic Differentiation},
       journal = {Journal of Open Source Software}
    }

</div>

</div>

<div class="toctree-wrapper compound">

<span id="document-01_quickstart"></span>

<div id="quickstart" class="section">

### Quickstart<a href="#quickstart" class="headerlink" title="Link to this heading">#</a>

Welcome to the Quickstart Guide! These interactive Jupyter notebooks are designed to get you up and running quickly. We recommend following them in order, from the fundamentals of JAX to running your very first end-to-end simulation.

<div class="toctree-wrapper compound">

<span id="document-notebooks/quickstart/01_jax_introduction"></span>

<div id="introduction-to-jax" class="section tex2jax_ignore mathjax_ignore">

#### Introduction to JAX<a href="#introduction-to-jax" class="headerlink" title="Link to this heading">#</a>

JAX is a high-performance numerical computing library developed by Google that brings together the familiar NumPy API with powerful features like automatic differentiation, just-in-time (JIT) compilation, and seamless GPU/TPU acceleration. Originally designed for machine learning research, JAX has become popular across scientific computing applications due to its speed and flexibility.

Jax itself provides a good introduction [here](https://docs.jax.dev/en/latest/tutorials.html) and [here](https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html). Otherwise, the following is a small crash course.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import jax
    import jax.numpy as jnp
    import fdtdx

</div>

</div>

</div>

</div>

<div id="functional-programming-paradigm" class="section">

##### Functional Programming Paradigm<a href="#functional-programming-paradigm" class="headerlink" title="Link to this heading">#</a>

JAX operates exclusively in a functional programming style, which means it requires you to write pure functions without side effects. This functional approach has several important implications:

<div id="immutable-data" class="section">

###### Immutable data<a href="#immutable-data" class="headerlink" title="Link to this heading">#</a>

Arrays and other data structures are treated as immutable. Operations create new objects rather than modifying existing ones, similar to how NumPy handles broadcasting operations.

This functional constraint enables JAX’s powerful transformations like jit (compilation), grad (automatic differentiation), vmap (vectorization), and pmap (parallelization). While the functional style requires some adjustment if you’re used to imperative programming, it unlocks JAX’s ability to automatically optimize and transform your numerical code in ways that would be impossible with stateful operations.

JAX functions cannot modify variables in-place or maintain internal state. Instead of operations like array\[0\] = 5, you must use functional equivalents like array.at\[0\].set(5) that return new arrays.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # This won't work in JAX
    def bad_function(x):
        x[0] = x[0] + 1  # In-place modification
        return x

    # This is the JAX way
    def good_function(x):
        return x.at[0].add(1)  # Returns new array

    print(good_function(jnp.asarray([4.0])))
    print(bad_function(jnp.asarray([4.0])))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    [5.]

</div>

</div>

<div class="output traceback highlight-ipythontb notranslate">

<div class="highlight">

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In[2], line 11
          8     return x.at[0].add(1)  # Returns new array
         10 print(good_function(jnp.asarray([4.0])))
    ---> 11 print(bad_function(jnp.asarray([4.0])))

    Cell In[2], line 3, in bad_function(x)
          2 def bad_function(x):
    ----> 3     x[0] = x[0] + 1  # In-place modification
          4     return x

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py:599, in _unimplemented_setitem(self, i, x)
        595 def _unimplemented_setitem(self, i, x):
        596   msg = ("JAX arrays are immutable and do not support in-place item assignment."
        597          " Instead of x[idx] = y, use x = x.at[idx].set(y) or another .at[] method:"
        598          " https://docs.jax.dev/en/latest/_autosummary/jax.numpy.ndarray.at.html")
    --> 599   raise TypeError(msg.format(type(self)))

    TypeError: JAX arrays are immutable and do not support in-place item assignment. Instead of x[idx] = y, use x = x.at[idx].set(y) or another .at[] method: https://docs.jax.dev/en/latest/_autosummary/jax.numpy.ndarray.at.html

</div>

</div>

</div>

</div>

</div>

<div id="no-side-effects-pure-functions" class="section">

###### No Side Effects (pure functions)<a href="#no-side-effects-pure-functions" class="headerlink" title="Link to this heading">#</a>

Functions should not print to console, write to files, or modify global variables during compilation. JAX’s Just-in-Time (JIT) compiler optimizes based on the assumption that functions are deterministic and side-effect free. As a consequence print statements are only executed during compilation (the first function call), but not afterwards.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    def example_function():
        x = jnp.ones((4,))
        print(x)

    jitted_fn = jax.jit(example_function)

    jitted_fn() # this will print traced value of x
    jitted_fn() # this executes compiled function does not print anything

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    JitTracer<float32[4]>

</div>

</div>

</div>

</div>

</div>

<div id="static-shapes-during-computation" class="section">

###### Static Shapes during computation<a href="#static-shapes-during-computation" class="headerlink" title="Link to this heading">#</a>

All Jax arrays need to have a static shape in compiled functions (as long as the input shape does not change). This means that there is a distinction between static and dynamic data. Static data (like python scalars) do not change when called with different input values. This static data can be used in if-clauses, or alter the shape of jax arrays. Dynamic data are jax arrays with possibly arbitrary values. This dynamic data cannot be used in if-clauses or to change the shapes of other jax arrays. As a rule of thumb, the computational graph of a function can only change based on static arrays, but not jax arrays.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    def if_clause(x):
        return 1.0 if x else 2.0  # computational graph changes depending on the value of x

    print(jax.jit(if_clause)(jnp.asarray(True)))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output traceback highlight-ipythontb notranslate">

<div class="highlight">

    ---------------------------------------------------------------------------
    TracerBoolConversionError                 Traceback (most recent call last)
    Cell In[7], line 4
          1 def if_clause(x):
          2     return 1.0 if x else 2.0#
    ----> 4 print(jax.jit(if_clause)(jnp.asarray(True)))

        [... skipping hidden 13 frame]

    Cell In[7], line 2, in if_clause(x)
          1 def if_clause(x):
    ----> 2     return 1.0 if x else 2.0

        [... skipping hidden 1 frame]

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/core.py:1721, in concretization_function_error.<locals>.error(self, arg)
       1720 def error(self, arg):
    -> 1721   raise TracerBoolConversionError(arg)

    TracerBoolConversionError: Attempted boolean conversion of traced array with shape bool[].
    The error occurred while tracing the function if_clause at /tmp/ipykernel_278296/1626192598.py:1 for jit. This concrete value was not available in Python because it depends on the value of the argument x.
    See https://docs.jax.dev/en/latest/errors.html#jax.errors.TracerBoolConversionError

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    def indexing_fn(x):
        return jnp.asarray([4.0, 2.0, 1.0, 3.0])[:x]  # depending on value of x different array shape is returned

    print(jax.jit(indexing_fn)(jnp.asarray(1)))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output traceback highlight-ipythontb notranslate">

<div class="highlight">

    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    Cell In[10], line 4
          1 def indexing_fn(x):
          2     return jnp.asarray([4.0, 2.0, 1.0, 3.0])[:x]
    ----> 4 print(jax.jit(indexing_fn)(jnp.asarray(1)))

        [... skipping hidden 13 frame]

    Cell In[10], line 2, in indexing_fn(x)
          1 def indexing_fn(x):
    ----> 2     return jnp.asarray([4.0, 2.0, 1.0, 3.0])[:x]

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py:1125, in _forward_operator_to_aval.<locals>.op(self, *args)
       1124 def op(self, *args):
    -> 1125   return getattr(self.aval, f"_{name}")(self, *args)

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/array_methods.py:660, in _getitem(self, item)
        659 def _getitem(self, item):
    --> 660   return indexing.rewriting_take(self, item)

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/indexing.py:664, in rewriting_take(arr, idx, indices_are_sorted, unique_indices, mode, fill_value, normalize_indices, out_sharding)
        660   out_sharding = canonicalize_sharding(out_sharding, 'take')
        661   return auto_axes(internal_gather, out_sharding=out_sharding,
        662                    axes=out_sharding.mesh.explicit_axes,  # type: ignore
        663                    )(arr, dynamic_idx)
    --> 664 return internal_gather(arr, dynamic_idx)

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/indexing.py:673, in _gather(arr, dynamic_idx, treedef, static_idx, indices_are_sorted, unique_indices, mode, fill_value, normalize_indices)
        670 def _gather(arr, dynamic_idx, *, treedef, static_idx, indices_are_sorted,
        671             unique_indices, mode, fill_value, normalize_indices):
        672   idx = merge_static_and_dynamic_indices(treedef, static_idx, dynamic_idx)
    --> 673   indexer = index_to_gather(np.shape(arr), idx, normalize_indices=normalize_indices)  # shared with _scatter_update
        674   jnp_error._check_precondition_oob_gather(arr.shape, indexer.gather_indices)
        675   y = arr

    File ~/nobackup/fdtdx-notebooks/.venv/lib/python3.12/site-packages/jax/_src/numpy/indexing.py:940, in index_to_gather(x_shape, idx, normalize_indices)
        931 if not all(_is_slice_element_none_or_constant_or_symbolic(elt)
        932            for elt in (i.start, i.stop, i.step)):
        933   msg = ("Array slice indices must have static start/stop/step to be used "
        934          "with NumPy indexing syntax. "
        935          f"Found slice({i.start}, {i.stop}, {i.step}). "
       (...)    938          "dynamic_update_slice (JAX does not support dynamically sized "
        939          "arrays within JIT compiled functions).")
    --> 940   raise IndexError(msg)
        942 start, step, slice_size = core.canonicalize_slice(i, x_shape[x_axis])
        943 slice_shape.append(slice_size)

    IndexError: Array slice indices must have static start/stop/step to be used with NumPy indexing syntax. Found slice(None, JitTracer<~int32[]>, None). To index a statically sized array at a dynamic position, try lax.dynamic_slice/dynamic_update_slice (JAX does not support dynamically sized arrays within JIT compiled functions).

</div>

</div>

</div>

</div>

</div>

</div>

<div id="treeclass-objects-in-fdtdx" class="section">

##### TreeClass Objects in FDTDX<a href="#treeclass-objects-in-fdtdx" class="headerlink" title="Link to this heading">#</a>

FDTDX leverages JAX’s functional programming paradigm through a specialized TreeClass system that makes it easy to work with complex hierarchical data structures while maintaining JAX compatibility. The TreeClass provides a clean, object-oriented interface that automatically integrates with JAX’s pytree system, allowing for seamless use with JAX transformations.

<div id="treeclass-structure" class="section">

###### TreeClass Structure<a href="#treeclass-structure" class="headerlink" title="Link to this heading">#</a>

The TreeClass system uses dataclass-like syntax with the @fdtdx.autoinit decorator to automatically generate initialization methods. Here’s how it works:

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    @fdtdx.autoinit
    class A(fdtdx.TreeClass):
        a: float = 2
        x: int = 5

    @fdtdx.autoinit
    class B(fdtdx.TreeClass):
        a1: A
        z: int = 7

    @fdtdx.autoinit
    class C(fdtdx.TreeClass):
        b_list: list[B]
        c: float = 2

</div>

</div>

</div>

</div>

These classes can be nested arbitrarily deep and contain lists, dictionaries, or other complex data structures. The @fdtdx.autoinit decorator automatically generates init methods that handle default values and type checking.

</div>

<div id="working-with-treeclass-instances" class="section">

###### Working with TreeClass Instances<a href="#working-with-treeclass-instances" class="headerlink" title="Link to this heading">#</a>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Create instances with default or custom values
    b = B(a1=A())  # Uses defaults: A(a=2, x=5), z=7
    print(b)
    b = b.aset("z", 25)  # Functional update
    print(b)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    B(a1=A(a=2, x=5), z=7)
    B(a1=A(a=2, x=5), z=25)

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Collections of TreeClass instances
    b2 = B(a1=A(a=10, x=11), z=12)
    b3 = B(a1=A(a=20, x=21), z=22)
    c = C(b_list=[b, b2])
    print(c)

    # Deep nested updates using path syntax
    c2 = c.aset("b_list->[0]->a1->a", 100)
    print(c2)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    C(b_list=[B(a1=A(a=2, x=5), z=25), B(a1=A(a=10, x=11), z=12)], c=2)
    C(b_list=[B(a1=A(a=100, x=5), z=25), B(a1=A(a=10, x=11), z=12)], c=2)

</div>

</div>

</div>

</div>

</div>

<div id="the-aset-method-functional-updates-made-easy" class="section">

###### The aset Method: Functional Updates Made Easy<a href="#the-aset-method-functional-updates-made-easy" class="headerlink" title="Link to this heading">#</a>

The aset method is the cornerstone of FDTDX’s functional approach. Unlike JAX’s standard .at\[\].set() which only works on pytree leaf nodes (typically arrays), aset can update any attribute at any level of nesting within a TreeClass hierarchy.

</div>

<div id="path-syntax-the-method-uses-an-intuitive-string-based-path-syntax-to-navigate-nested-structures" class="section">

###### Path Syntax: The method uses an intuitive string-based path syntax to navigate nested structures:<a href="#path-syntax-the-method-uses-an-intuitive-string-based-path-syntax-to-navigate-nested-structures" class="headerlink" title="Link to this heading">#</a>

- “attribute” - Direct attribute access

- “a-\>b” - Nested attribute access (a.b)

- “a-\>\[0\]” - List indexing

- “a-\>\[‘key’\]” - Dictionary key access

- “b_list-\>\[0\]-\>a1-\>a” - Complex nested path

- 

In the example c2 = c.aset(“b_list-\>\[0\]-\>a1-\>a”, 100), this path means: - Access the b_list attribute of c - Get the first element \[0\] of that list - Access the a1 attribute of that element - Access the a attribute of a1 - Set that value to 100

The method returns a completely new instance with the updated value, maintaining JAX’s functional programming requirements. This allows FDTDX data structures to be used seamlessly with JAX transformations like jit, grad, and vmap, while providing a much more intuitive interface than manually reconstructing nested data structures. This approach bridges the gap between JAX’s powerful functional capabilities and the practical need for complex, hierarchical data management in scientific computing applications.

</div>

</div>

<div id="how-jax-is-used-in-fdtdx" class="section">

##### How JAX is used in FDTDX<a href="#how-jax-is-used-in-fdtdx" class="headerlink" title="Link to this heading">#</a>

For a full example on how to use JAX with fdtdx, check out this [example](https://github.com/ymahlau/fdtdx/blob/main/examples/simulate_gaussian_source.py) or this [example](https://github.com/ymahlau/fdtdx/blob/main/examples/optimize_ceviche_corner.py). The script demonstrates FDTDX’s seamless integration with JAX’s jit transformation. The core simulation function sim_fn takes FDTDX TreeClass structures as arguments and is JIT-compiled:

<div class="highlight-python notranslate">

<div class="highlight">

    def sim_fn(
        params: fdtdx.ParameterContainer,
        arrays: fdtdx.ArrayContainer, 
        key: jax.Array,
    ):
        # Complex FDTD simulation logic with TreeClass structures
        arrays, new_objects, info = fdtdx.apply_params(arrays, objects, params, key)
        final_state = fdtdx.run_fdtd(arrays=arrays, objects=new_objects, config=config, key=key)
        # ... more operations
        return arrays, new_info
    jitted_loss = jax.jit(sim_fn, donate_argnames=["arrays"]).lower(params, arrays, key).compile()

</div>

</div>

<div id="jit-compilation-with-treeclass-arguments" class="section">

###### JIT compilation with TreeClass arguments<a href="#jit-compilation-with-treeclass-arguments" class="headerlink" title="Link to this heading">#</a>

Key Features:

- TreeClass Compatibility: The ParameterContainer and ArrayContainer are FDTDX TreeClass structures that work seamlessly with jit. JAX automatically handles the pytree registration, allowing these complex nested structures to be compiled efficiently.

- Memory Optimization: The donate_argnames=\[“arrays”\] parameter tells JAX it can reuse the memory of the arrays argument, which is crucial for large electromagnetic field arrays in FDTD simulations.

- Compilation Pipeline: The script uses .lower().compile() to explicitly control the compilation process, providing timing information for performance analysis.

While this specific example focuses on forward simulation, FDTDX is designed for gradient-based optimization. The GradientConfig setup shows how gradients would be computed:

<div class="highlight-python notranslate">

<div class="highlight">

    gradient_config = fdtdx.GradientConfig(
        recorder=fdtdx.Recorder(
            modules=[fdtdx.DtypeConversion(dtype=jnp.bfloat16)]
        )
    )

</div>

</div>

For gradient computation, you would typically use:

<div class="highlight-python notranslate">

<div class="highlight">

    # Hypothetical gradient computation
    grad_fn = jax.grad(sim_fn, argnums=0)  # Gradient w.r.t. params
    gradients = grad_fn(params, arrays, key)

</div>

</div>

</div>

</div>

</div>

<span id="document-notebooks/quickstart/02_basic_materials"></span>

<div id="basic-materials-and-objects" class="section tex2jax_ignore mathjax_ignore">

#### Basic Materials and Objects<a href="#basic-materials-and-objects" class="headerlink" title="Link to this heading">#</a>

In FDTDX, simulation objects can have a material, which defines the permittivity, permeability and conductivity of the object.

Currently neither dispersion nor non-linear materials are implemented. The implementation of dispersion is scheduled in the near-mid future and afterwards an implementation of non-linear materials will follow.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import fdtdx

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    material = fdtdx.Material()
    print(material)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Material(
      permittivity=#1.0, 
      permeability=#1.0, 
      electric_conductivity=#0.0, 
      magnetic_conductivity=#0.0
    )

</div>

</div>

</div>

</div>

The default material above with no parameters represents free space with a relative permittivity and permeability of 1. These values can be freely set by a user.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    material2 = fdtdx.Material(permittivity=2.5, permeability=1.7)
    print(material2)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Material(
      permittivity=#2.5, 
      permeability=#1.7, 
      electric_conductivity=#0.0, 
      magnetic_conductivity=#0.0
    )

</div>

</div>

</div>

</div>

<div id="fdtdx-uniformmaterial" class="section">

##### fdtdx.UniformMaterial<a href="#fdtdx-uniformmaterial" class="headerlink" title="Link to this heading">#</a>

The most basic and also probably most useful object is the UniformMaterialObject. As the name suggests, it has a single material. Importantly, every object in FDTDX needs to have a unique name! If no name is provided, then some name is chosen programmatically.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    uniform_obj = fdtdx.UniformMaterialObject(
        partial_real_shape=(0.6e-6, 0.6e-6, 0.6e-6),  # size of the object in meters
        material=material,  # material
        name="Uniform Material",  # name of the object, optional
    )
    print(uniform_obj)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    UniformMaterialObject(
      partial_real_shape=#(6e-07, 6e-07, 6e-07), 
      partial_grid_shape=#(None, None, None), 
      color=#(0.8470588235294118, 0.8627450980392157, 0.8392156862745098), 
      name=#Uniform Material, 
      max_random_real_offsets=#(0, 0, 0), 
      max_random_grid_offsets=#(0, 0, 0), 
      _grid_slice_tuple=#((-1, -1), (-1, -1), (-1, -1)), 
      placement_order=#0, 
      material=Material(
        permittivity=#1.0, 
        permeability=#1.0, 
        electric_conductivity=#0.0, 
        magnetic_conductivity=#0.0
      )
    )

</div>

</div>

</div>

</div>

There also exist Objects with more elaborate material distributions, but for the quickstart we will only cover this most basic material.

</div>

</div>

<span id="document-notebooks/quickstart/03_object_placement_guide"></span>

<div id="object-placement-guide" class="section tex2jax_ignore mathjax_ignore">

#### Object Placement Guide<a href="#object-placement-guide" class="headerlink" title="Link to this heading">#</a>

This guide explains how to position objects in a simulation scene in FDTDX. The basic workflow looks like this: 1. Define a Simulation volume 2. Define objects and sizing/placement constraints between objects 3. Compute the actual position of objects in the simulation scene by using the place_objects function 4. Optional, but recommend: Plot the simulation scene using plot_setup() 5. Run a simulation

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import fdtdx
    import jax

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    %matplotlib inline

</div>

</div>

</div>

</div>

<div id="basic-positioning" class="section">

##### Basic Positioning<a href="#basic-positioning" class="headerlink" title="Link to this heading">#</a>

In FDTDX, objects are positioned either directly or relation to other objects through constraints.

The first step should always be to define the size of the simulation volume. FDTDX always uses metrical units, i.e. meters or grid positions referring to the Yee-grid, which depends on the resolution used.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # create a list of objects
    object_list = []

    # create a simulation config
    config = fdtdx.SimulationConfig(
        time=200e-15,
        resolution=25e-9
    )
    # Create a simulation volume
    volume = fdtdx.SimulationVolume(
        partial_real_shape=(4e-6, 4e-6, 1.5e-6),
    )
    object_list.append(volume)

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key = jax.random.PRNGKey(seed=42)  # random key
    # place objects and resolve constraints
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=[],
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/fcf85b24b51db506a580a924191c8ae4584ec863aa4441231cbdc90f60d14f80.png)

</div>

</div>

Now, we can start to position some objects in the simulation scene. We start with a substrate at the bottom of simulation. To this end, we specify a constraint that aligns the objects in the z-axis (axis 2). The user should specify these constraints and collect them in a list.

Positional constraints define an anchor point for both objects, which are constrainted to be at the same position. The position of the anchor point can be specified in a relative coordinate system of each object. A relative coordinate system means that a position of -1 would place the anchor at the left boundary of the object, a position of 0 at the middle and a position of 1 at the right boundary.

In case of the substrate, we want the lower boundary of the substrate to be aligned with the lower boundary of the simulation volume. This ensures that the substrate is placed exactly at the bottom of the simulation. The margins and grid_margins arguments are optional and would allow to speficy a fixed distance between the anchor points. The margins argument is in units of meters, the grid margins in units of yee-grid cells.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # create list of constraints
    placement_constraints = []
    # create substrate
    substrate = fdtdx.UniformMaterialObject(
        partial_real_shape=(None, None, 0.6e-6),
        name="substrate",
        color=fdtdx.colors.DARK_GREY,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silica),
    )
    object_list.append(substrate)
    # place at the bottom of simulation volume
    substrate_constraint = substrate.place_relative_to(
        volume,
        axes=2,
        own_positions=-1,
        other_positions=-1,
        margins=0,
        grid_margins=0,
    )
    placement_constraints.append(substrate_constraint)
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/a359f15fc0dab4f991f7311a6d8cc487d026a0f9c67d80bc31755e57de70caa4.png)

</div>

</div>

There exist a number of useful shorthands for rapid placements. Some of them are listed below that place a cube in the scene. The name and colors argument are only used for plotting.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # place an object on top (z-axis / 2) of another object
    cube1 = fdtdx.UniformMaterialObject(
        name="cube",
        color=fdtdx.colors.GREEN,
        partial_real_shape=(0.5e-6, 0.5e-6, 0.5e-6),
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )
    object_list.append(cube1)

    placement_constraints.append(
        cube1.place_above(substrate)
    )

    # place an object at the center of another object
    placement_constraints.append(
        cube1.place_at_center(
            substrate,
            axes=(0, 1),
        )
    )
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/e79276a71d038ccb2e60025b78120fe991d9e4387e436140f648f08901c271e4.png)

</div>

</div>

</div>

<div id="size-configuration" class="section">

##### Size Configuration<a href="#size-configuration" class="headerlink" title="Link to this heading">#</a>

Object sizes can be specified in a number of ways. Firstly, one can directly set the size of an object in the init method. This can either be a specified in Yee-grid cells or metrical units (meter).

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # size in meters
    cube1 = fdtdx.UniformMaterialObject(
        partial_real_shape=(0.3e-6, 1.0e-6, 0.7e-6),
        name="cube1",
        color=fdtdx.colors.GREEN,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1]

    # place an object at the center of another object
    placement_constraints = [substrate_constraint]
    placement_constraints.append(
        cube1.place_at_center(
            substrate,
            axes=(0, 1),
        )
    )
    placement_constraints.append(
        cube1.place_above(substrate)
    )
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/2b3e8a126d8a2fa59a479243545eac6b19de703ce36c0b417ba9a3cffff43908.png)

</div>

</div>

</div>

<div id="size-in-grid-units" class="section">

##### Size in grid units<a href="#size-in-grid-units" class="headerlink" title="Link to this heading">#</a>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube1 = fdtdx.UniformMaterialObject(
        partial_grid_shape=(20, 40, 8),
        name="cube1",
        color=fdtdx.colors.GREEN,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1]

    # place an object at the center of another object
    placement_constraints = [substrate_constraint]
    placement_constraints.append(
        cube1.place_at_center(
            substrate,
            axes=(0, 1),
        )
    )
    placement_constraints.append(
        cube1.place_above(substrate)
    )
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/e62cdef126b02db62c51d986035e868173b0fd365abce970c2abcbc810b3a593.png)

</div>

</div>

</div>

<div id="combination-of-grid-and-metrical-units" class="section">

##### Combination of grid and metrical units<a href="#combination-of-grid-and-metrical-units" class="headerlink" title="Link to this heading">#</a>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube1 = fdtdx.UniformMaterialObject(
        partial_real_shape=(None, 0.5e-6, None),
        partial_grid_shape=(12, None, 4),
        name="cube1",
        color=fdtdx.colors.GREEN,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1]

    # place an object at the center of another object
    placement_constraints = [substrate_constraint]
    placement_constraints.append(
        cube1.place_at_center(
            substrate,
            axes=(0, 1),
        )
    )
    placement_constraints.append(
        cube1.place_above(substrate)
    )
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )

    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/458b9800f226aaac8a4183e737b42c97d623f781963cb2d4a02ea34f23e42d81.png)

</div>

</div>

</div>

<div id="undefined-sizes-can-be-useful" class="section">

##### Undefined Sizes can be useful<a href="#undefined-sizes-can-be-useful" class="headerlink" title="Link to this heading">#</a>

If the size of an object is only partially defined and does not have any constraints, the size is set to the size of the simulation volume in the respective axis. We actually already used this behavior to define the substrate above.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # z-axis is undefined, size is extended to simulation size
    cube1 = fdtdx.UniformMaterialObject(
        partial_real_shape=(None, 0.5e-6, None),
        partial_grid_shape=(3, None, None),
        ...
    )
    # This now results in an error:
    placement_constraints.append(
        cube1.place_above(substrate)
    )

</div>

</div>

</div>

</div>

Using this specification for the cube1, we get the following error:

Exception: Inconsisten grid shape (may be due to extension to infinity) at lower bound: 0 != 6 for axis=2, cube (\<class ‘fdtdx.objects.material.UniformMaterialObject’\>). Object has a position constraint that puts the lower boundary at 6, but the lower bound was alreay computed to be at 0. This could be due to a missing size constraint/specification, which resulted in an expansion of the object to the simulation boundary (default size) or another constraint on this object.

The error occurs, because we tried to place the cube above the substrate, which is no longer possible if the z-size of the cube is the whole simulation size. When we remove the problematic placement constraint, we get the correct simulation scene.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube1 = fdtdx.UniformMaterialObject(
        partial_real_shape=(None, 0.5e-6, None),
        partial_grid_shape=(12, None, None),
        name="cube1",
        color=fdtdx.colors.GREEN,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1]

    # place an object at the center of another object
    center_constraint = cube1.place_at_center(
        substrate,
        axes=(0, 1),
    )
    placement_constraints = [center_constraint, substrate_constraint]

    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/1ab4caa08ebc8cc4cf280c98928ea1ede9dadf67bd474a50c545ec735c6356c8.png)

</div>

</div>

</div>

<div id="relative-sizing-constraint" class="section">

##### Relative Sizing constraint<a href="#relative-sizing-constraint" class="headerlink" title="Link to this heading">#</a>

The size of an object can also be set in relation to another object. To demonstrate this, we define a second cube, which should be placed above the substrate and have a 200nm distance to the other cube in the x-axis.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube2 = fdtdx.UniformMaterialObject(
        name="cube2",
        color=fdtdx.colors.MAGENTA,
        partial_real_shape=(0.5e-6, 0.5e-6, 0.5e-6),
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1, cube2]

    placement_constraints = [center_constraint, substrate_constraint]
    cube2_placement_constraints = [
        cube2.place_above(substrate),
        cube2.place_relative_to(
            cube1,
            axes=(0, 1),
            own_positions=(1, 0),
            other_positions=(-1, 0),
            margins=(-200e-9, 0)
        )
    ]
    placement_constraints.extend(cube2_placement_constraints)

    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/e47435c17bfa74417f8937e4b4d356c1e65949953c73ff187720e33a9856859c.png)

</div>

</div>

Now let’s change the size definition of the second cube to a relative size constraint, which defines the y-size of the second cube as the size of the first cube in the z-axis.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube2 = fdtdx.UniformMaterialObject(
        name="cube2",
        color=fdtdx.colors.MAGENTA,
        partial_real_shape=(0.5e-6, None, 0.5e-6),
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1, cube2]

    placement_constraints: list = [center_constraint, substrate_constraint]
    placement_constraints.extend([
        cube2.place_above(substrate),
        cube2.place_relative_to(
            cube1,
            axes=(0, 1),
            own_positions=(1, 0),
            other_positions=(-1, 0),
            margins=(-200e-9, 0)
        )
    ])
    placement_constraints.append(
        cube2.size_relative_to(
            cube1,
            axes=1,
            other_axes=2,
            proportions=1.0,
        )
    )
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/b0d9ed965a922653db3804d899469a9d7e7df1be6a637098f95e23b1e09faa9b.png)

</div>

</div>

Another useful convenience wrapper is the following:

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    object1.same_size(object2, axes=(0,1))

</div>

</div>

</div>

</div>

</div>

<div id="extending-objects-to-other-objects-or-simulation-boundaries" class="section">

##### Extending objects to other objects or Simulation boundaries<a href="#extending-objects-to-other-objects-or-simulation-boundaries" class="headerlink" title="Link to this heading">#</a>

The last method to set the size of an object is to constrain the size, such that it extends up to another object in the simulation scene.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # definition of first cube
    cube1 = fdtdx.UniformMaterialObject(
        partial_real_shape=(0.5e-6, 0.5e-6, 0.5e-6),
        name="cube",
        color=fdtdx.colors.GREEN,
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )
    placement_constraints: list = [substrate_constraint]
    placement_constraints.append(
        cube1.place_above(substrate)
    )
    placement_constraints.append(
        cube1.place_at_center(
            substrate,
            axes=(0, 1),
        )
    )
    cube2 = fdtdx.UniformMaterialObject(
        name="cube2",
        color=fdtdx.colors.MAGENTA,
        partial_real_shape=(None, 0.5e-6, 0.5e-6),
        material=fdtdx.Material(permittivity=fdtdx.constants.relative_permittivity_silicon),
    )

    object_list = [volume, substrate, cube1, cube2]

    placement_constraints.extend([
        cube2.place_above(substrate),
        # place at center of y-axis
        cube2.place_at_center(
            cube1,
            axes=1,
        ),
        # extend object up to first cube
        cube2.extend_to(
            cube1,
            axis=0,
            direction="+",
        )
    ])
    objects, arrays, params, config, info = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key= key,
    )
    # plot the simulation scene
    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
    )
    display(fig)

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/33def3bd1fbf524f7e491aad424dcddd9de0562ad7a4de6ccce686f88a73669b.png)

</div>

</div>

This constrains the size of cube2 such that its upper boundary (“+”) extends directly up to cube1 in the x-axis.

See the Objects API Reference for complete details on all positioning and sizing options.

</div>

</div>

<span id="document-notebooks/quickstart/04_basic_simulation"></span>

<div id="first-basic-simulation" class="section tex2jax_ignore mathjax_ignore">

#### First Basic Simulation<a href="#first-basic-simulation" class="headerlink" title="Link to this heading">#</a>

Now that we covered the basics of JAX, simulation materials and the placement of objects in the previous tutorials, let’s start to run the first actual simulation. In this simulation, we will use a source to show the interaction of light with some cuboid object floating in free space. Of course, this not very practical in real life, but it is a good starting point to show the features of FDTDX.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import fdtdx
    import jax
    import jax.numpy as jnp
    import matplotlib.pyplot as plt
    import pytreeclass as tc
    import time
    from IPython.display import Video

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    %matplotlib inline

</div>

</div>

</div>

</div>

<div id="setup-of-simulation-scence" class="section">

##### Setup of simulation scence<a href="#setup-of-simulation-scence" class="headerlink" title="Link to this heading">#</a>

Let’s start with a basic setup of a simulation scene. We need to specify a random key for possible stochastic operations. This simulation will be entirely deterministic, but we still need to specify the key. Then we specify a SimulationConfig object with some basic information on how long the simulation should run and how accurate it needs to be (resolution, dtype and courant factor).

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Create a JAX random key for reproducibility and stochastic operations
    key = jax.random.PRNGKey(seed=42)

    # intialize a list of objects
    object_list = []

    # Define simulation configuration (duration, resolution, data type, etc.)
    config = fdtdx.SimulationConfig(
        time=100e-15,
        resolution=100e-9,
        dtype=jnp.float32,
        courant_factor=0.99,
    )

</div>

</div>

</div>

</div>

Next, we specify the simulation volume. This includes the background material, which is used for all the space where we do not place objects in the following specifications.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    volume = fdtdx.SimulationVolume(
        partial_real_shape=(12.0e-6, 12e-6, 12e-6),
        material=fdtdx.Material(  # Background material
            permittivity=1.0,
            permeability=1.0,
        )
    )
    object_list.append(volume)

</div>

</div>

</div>

</div>

As we have seen in the object placement tutorial, in FDTDX objects are placed through constraints. We create an empty list of these constraints first and then iteratively add more constraints to the list.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    constraints = []

</div>

</div>

</div>

</div>

At first, we add the boundaries of our simulation to the constraints. We are using absorbing PML boundaries to prevent any reflections from the boundary of the simulation volume.

We could specify the boundary for each of the six sides of the simulation volume manually, but this would be tedious. Instead, we will use a handy shortcut provided by FDTDX. This creates PML boundaries on all six sides with the corresponding constraints. Here we use a thickness of 10 grid cells for the PML, which should be enough for most applications.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    bound_cfg = fdtdx.BoundaryConfig.from_uniform_bound(thickness=10, boundary_type="pml")
    bound_dict, c_list = fdtdx.boundary_objects_from_config(bound_cfg, volume)
    object_list.extend(bound_dict.values())
    constraints.extend(c_list)

</div>

</div>

</div>

</div>

Next, we create a light source. The source is placed at the top (z-axis) of the simulation volume and the propagation direction of the light is set downwards (“-“). The polarization is set for Ex-polarized light. Radius and standard deviation determine the spatial profile of the mode. A larger radius would make the emission area larger. A larger standard deviation would “flatten” the gaussian profile, making it more similar to a plane source. The radius and standard deviation should be set such that there is very little energy at the boundary of the source, because this can lead to artifacts.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    source = fdtdx.GaussianPlaneSource(
        partial_grid_shape=(None, None, 1),
        partial_real_shape=(10e-6, 10e-6, None),
        fixed_E_polarization_vector=(1, 0, 0),
        wave_character=fdtdx.WaveCharacter(wavelength=1.550e-6),
        radius=4e-6,
        std=1 / 3,
        direction="-",
    )

    object_list.append(source)
    constraints.extend(
        [
            source.place_relative_to(
                volume,
                axes=(0, 1, 2),
                own_positions=(0, 0, 1),
                other_positions=(0, 0, 1),
                margins=(0, 0, -1.5e-6),
            ),
        ]
    )

</div>

</div>

</div>

</div>

Next, we place a uniform cuboid at the center of the simulaiton volume. This will make the simulation a bit more interesting to look at, because otherwise we will only see the light emitted from the source.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube = fdtdx.UniformMaterialObject(
        partial_real_shape=(3e-6, 3e-6, 3e-6),
        material=fdtdx.Material(permittivity=2.0),
        name="Cube",
        color=fdtdx.colors.PINK,
    )
    object_list.append(cube)
    constraints.append(cube.place_at_center(volume))

</div>

</div>

</div>

</div>

In order to actually see a result from the simulation, we need to define a Detector. While the simulation function will return the E and H field after runnning the simulation, usually it is also necessary to read some physical metrics on intermediate time steps in the simulation. This is exactly what Detectors are for!

Here we use an EnergyDetector, which calculates the energy at every grid point within its volume. We also speciy a switch, which controls the time steps that the detector records. Our purpose here is to generate a video of the energy during the simulation. We do not need every single time step for this, so we only record every third time step.

The as_slices option is a memory optimization specific for creating images or videos. With this option set to True, only the values which are actually plotted will be saved instead of the whole simulation volume. If you need to read values from the whole volume, simply disable this option.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    video_energy_detector = fdtdx.EnergyDetector(
        name="Video",
        as_slices=True,
        switch=fdtdx.OnOffSwitch(interval=3),
        exact_interpolation=True,
        num_video_workers=8,
    )
    object_list.append(video_energy_detector)
    constraints.extend(video_energy_detector.same_position_and_size(volume))

</div>

</div>

</div>

</div>

These are all the objects we need for our simulation! Let’s resolve the constraints and plot the simulation scene to see if we made any mistakes. Note that it is good practice to split the random key to maintain randomness in JAX (see [here](https://docs.jax.dev/en/latest/notebooks/thinking_in_jax.html#pseudorandom-numbers) for more details)

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key, subkey = jax.random.split(key)
    objects, arrays, params, config, _ = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=constraints,
        key=subkey,
    )

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
        exclude_object_list=[video_energy_detector],
    )
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/19eb07f60d108e66ab3df19ed75acde609f63901412ab4a395a9b8145e230d2a.png)

</div>

</div>

Additionally, we can plot some statistics about the expected memory usage of our simulation. Note that this only includes the arrays that we specify before the simulation starts, not intermediate computational results during the simulation.

In this small simulation, the main memory requirement comes from the PML boundaries. In larger simulation, this requirement of the PML is dominated by the other items in the list.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    print(tc.tree_summary(arrays, depth=1))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    ┌──────────────────────┬──────────────────┬──────────┬────────┐
    │Name                  │Type              │Count     │Size    │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.E                    │f32[3,120,120,120]│5,184,000 │19.78MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.H                    │f32[3,120,120,120]│5,184,000 │19.78MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.psi_E                │f32[6,120,120,120]│10,368,000│39.55MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.psi_H                │f32[6,120,120,120]│10,368,000│39.55MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.alpha                │f32[6,120,120,120]│10,368,000│39.55MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.kappa                │f32[6,120,120,120]│10,368,000│39.55MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.sigma                │f32[6,120,120,120]│10,368,000│39.55MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.inv_permittivities   │f32[120,120,120]  │1,728,000 │6.59MB  │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.inv_permeabilities   │float             │1         │        │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.detector_states      │dict              │7,560,000 │28.84MB │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.recording_state      │NoneType          │          │        │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.electric_conductivity│NoneType          │          │        │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │.magnetic_conductivity│NoneType          │          │        │
    ├──────────────────────┼──────────────────┼──────────┼────────┤
    │Σ                     │ArrayContainer    │71,496,001│272.74MB│
    └──────────────────────┴──────────────────┴──────────┴────────┘

</div>

</div>

</div>

</div>

</div>

<div id="running-the-simulation" class="section">

##### Running the simulation<a href="#running-the-simulation" class="headerlink" title="Link to this heading">#</a>

Now let’s define a function that actually runs the simulation. In FDTDX, this is a two-part process.

Firstly, we call apply_params, which performs some calculations before the start of the simulation. If we have some parametric objects in the simulation, this function applies the given parameters and calculates the actual shapes of these objects. Additionally, some performance optimization are done here by calculating values for the simulation once before the simulation starts

Then, we call run_fdtd, which performs the FDTD simulation as a loop. The computation terminates as soon as the required number of time steps are reached.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    def sim_fn(
            params: fdtdx.ParameterContainer,
            arrays: fdtdx.ArrayContainer,
            key: jax.Array,
        ):
            # Apply parameters to objects and arrays
            arrays, new_objects, _ = fdtdx.apply_params(arrays, objects, params, key)

            # Run FDTD simulation (forward)
            final_state = fdtdx.run_fdtd(
                arrays=arrays,
                objects=new_objects,
                config=config,
                key=key,
            )
            _, arrays = final_state

            return arrays

</div>

</div>

</div>

</div>

In order to execute this function, we should first compile it. JAX provides a just-in-time compilation functionality with jax.jit, which automatically compiles a function as soon as it is called the first time. We extend this a little bit here by calling .lower() and .compile() to compile the function immediately and measure the compilation time. If this seems complicated, just omit the .lower() and .compile() and everything will still work the same, just the time measurement would be wrong.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    start_time = time.time()
    jitted_loss = jax.jit(sim_fn).lower(params, arrays, key).compile()
    end_time = time.time()
    print(f"Compilation time: {end_time - start_time} seconds")

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Compilation time: 0.7427017688751221 seconds

</div>

</div>

</div>

</div>

Now we are ready to run the simulation. We can see that the simulation time is smaller than the compilation time, which can happen for small simulations. This might seem inefficient, but in pratice a few seconds usually don’t matter. And, we are now able to call the compiled function as often as we like.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    start_time = time.time()
    new_arrays = jitted_loss(params, arrays, subkey)
    end_time = time.time()
    print(f"Simulation runtime: {end_time - start_time} seconds")

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Simulation runtime: 0.0021200180053710938 seconds

</div>

</div>

</div>

</div>

</div>

<div id="visualizing-the-results-of-a-simulation" class="section">

##### Visualizing the results of a simulation<a href="#visualizing-the-results-of-a-simulation" class="headerlink" title="Link to this heading">#</a>

Now we have run the simulation, but how do we visualize the results? Our goal was to generate a video of the simulation, so let’s do this.

The syntax for generating a video in a jupyter notebook is currently a bit complicated, but for actual scripts FDTDX offers some utility functions to make this easier (see [here](https://github.com/ymahlau/fdtdx/blob/main/examples/simulate_gaussian_source.py) for an example script using the ExperimentLogger class of FDTDX). The reason the syntax is so complicated, is on the one hand because of the JAX-syntax which does not allow in-place updates. Additionally, the plot function saves a video to a temporary location. We can either access the video from there or move it to a more permament location

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    video_path = objects["Video"].draw_plot(new_arrays.detector_states["Video"])
    print(video_path)
    Video(list(video_path.values())[0], embed=True, width=720)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    {'sliced_video': '/var/folders/9c/sf1_5nb17v51rk1l8xcxshdc0000gn/T/tmpq47gqngf.mp4'}

</div>

</div>

<div class="output text_html">

Your browser does not support the video tag.

</div>

</div>

</div>

</div>

</div>

</div>

<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">

<div class="sd-row sd-row-cols-1 sd-row-cols-xs-1 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 sd-g-3 sd-g-xs-3 sd-g-sm-3 sd-g-md-3 sd-g-lg-3 docutils">

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

🚀 1. Introduction to JAX

</div>

New to JAX? Start here. Learn the basics of high-performance array computing, automatic differentiation, and how it powers FDTDX.

</div>

<a href="#document-notebooks/quickstart/01_jax_introduction" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Introduction to JAX</span></a>

</div>

</div>

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

🎨 2. Basic Materials

</div>

Discover how to define physical materials. Learn about different material types and their differences.

</div>

<a href="#document-notebooks/quickstart/02_basic_materials" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Basic Materials and Objects</span></a>

</div>

</div>

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

🏗️ 3. Object Placement Guide

</div>

This guide covers how to programmatically position, orient, and manage objects in your simulation scene.

</div>

<a href="#document-notebooks/quickstart/03_object_placement_guide" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Object Placement Guide</span></a>

</div>

</div>

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

⚙️ 4. Basic Simulation

</div>

Bring it all together. Set up your simulation scene, step through time, and run your first simulation.

</div>

<a href="#document-notebooks/quickstart/04_basic_simulation" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">First Basic Simulation</span></a>

</div>

</div>

</div>

</div>

</div>

<span id="document-02_physics"></span>

<div id="physics-tutorials" class="section">

### Physics Tutorials<a href="#physics-tutorials" class="headerlink" title="Link to this heading">#</a>

Welcome to the Phyiscs Tutorials! These tutorials dive into the phyics behind FDTDX, specifically Maxwell’s equations.

<div class="admonition note">

Note

**Stay tuned!** More guides and tutorials will follow shortly.

</div>

<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">

<div class="sd-row sd-row-cols-1 sd-row-cols-xs-1 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 sd-g-3 sd-g-xs-3 sd-g-sm-3 sd-g-md-3 sd-g-lg-3 docutils">

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

1\. Maxwell’s Equations

</div>

Learn about the fundamental electromagnetic equations.

</div>

<a href="#document-notebooks/physics/01_maxwell" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Maxwell’s Equations</span></a>

</div>

</div>

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

2\. FDTD

</div>

Learn how the fundamental physics is realized in a numerical finite-difference time-domain simulation.

</div>

<a href="#document-notebooks/physics/02_fdtd" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">FDTD Method</span></a>

</div>

</div>

</div>

</div>

<div class="toctree-wrapper compound">

<span id="document-notebooks/physics/01_maxwell"></span>

<div id="maxwell-s-equations" class="section tex2jax_ignore mathjax_ignore">

#### Maxwell’s Equations<a href="#maxwell-s-equations" class="headerlink" title="Link to this heading">#</a>

Maxwell’s Equations are a set of four laws that completely describe classical electromagnetism and ultimately reveal the true nature of light. These are the basic equations that FDTDX like any other electromagnetic simulation software is build on.

To understand the physics of these equations, we look at the interaction of four fundamental vector fields: the Electric Field (<span class="math notranslate nohighlight">\\\mathbf{E}\\</span>), the Electric Displacement Field (<span class="math notranslate nohighlight">\\\mathbf{D}\\</span>), the Magnetic Flux Density (<span class="math notranslate nohighlight">\\\mathbf{B}\\</span>), and the Magnetic Field (<span class="math notranslate nohighlight">\\\mathbf{H}\\</span>).

<div id="electric-connection-mathbf-d-and-mathbf-e" class="section">

##### Electric Connection: <span class="math notranslate nohighlight">\\\mathbf{D}\\</span> and <span class="math notranslate nohighlight">\\\mathbf{E}\\</span><a href="#electric-connection-mathbf-d-and-mathbf-e" class="headerlink" title="Link to this heading">#</a>

When you apply an external Electric Field (<span class="math notranslate nohighlight">\\\mathbf{E}\\</span>) to an insulating material (a dielectric), the atoms stretch. The negative electron clouds are pulled one way, and the positive nuclei are pushed the other. This stretching creates billions of microscopic dipoles, a phenomenon called Polarization (<span class="math notranslate nohighlight">\\\mathbf{P}\\</span>). The Electric Displacement Field (<span class="math notranslate nohighlight">\\\mathbf{D}\\</span>) was created to ignore this messy internal polarization and focus solely on the “free” charges we can control. Therefore, <span class="math notranslate nohighlight">\\\mathbf{D}\\</span> is essentially the fundamental electric field <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>, plus the material’s internal polarization response. The fundamental connection is: \$<span class="math notranslate nohighlight">\\ \mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} \\</span>\$

However, for a lot of materials the polarization is directly proportional to the applied electric field. This allows us to drastically simplify the equation into its most famous form: <span class="math notranslate nohighlight">\\ \mathbf{D} = \varepsilon \mathbf{E} \\</span>.

<span class="math notranslate nohighlight">\\\varepsilon\\</span> (epsilon) is the permittivity of the material. It is a single number that measures how much a material resists the formation of an electric field within it. It is calculated as <span class="math notranslate nohighlight">\\\varepsilon = \varepsilon_0 \varepsilon_r\\</span>, where <span class="math notranslate nohighlight">\\\varepsilon_0\\</span> is the vacuum permittivity and <span class="math notranslate nohighlight">\\\varepsilon_r\\</span> is the relative permittivity (or dielectric constant) of the specific material. In a pure vacuum, <span class="math notranslate nohighlight">\\\varepsilon_r = 1\\</span>, so <span class="math notranslate nohighlight">\\\mathbf{D} = \varepsilon_0 \mathbf{E}\\</span>.

</div>

<div id="magnetic-connection-mathbf-b-and-mathbf-h" class="section">

##### Magnetic Connection: <span class="math notranslate nohighlight">\\\mathbf{B}\\</span> and <span class="math notranslate nohighlight">\\\mathbf{H}\\</span><a href="#magnetic-connection-mathbf-b-and-mathbf-h" class="headerlink" title="Link to this heading">#</a>

Just as electric fields stretch atoms, magnetic fields force the electrons orbiting within atoms to align their spins. This alignment turns the atoms into tiny microscopic magnets, creating a collective effect called Magnetization (<span class="math notranslate nohighlight">\\\mathbf{M}\\</span>). The Magnetic Flux Density (<span class="math notranslate nohighlight">\\\mathbf{B}\\</span>) is the total, fundamental magnetic reality. It accounts for both the magnetic field generated by the actual electrical current running through your wires (<span class="math notranslate nohighlight">\\\mathbf{H}\\</span>) and the magnetic field added by the aligned atoms of the material (<span class="math notranslate nohighlight">\\\mathbf{M}\\</span>). The fundamental connection is: \$<span class="math notranslate nohighlight">\\ \mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M}) \\</span>\$

Just like with the electric fields, for a lot of materials, the magnetization is proportional to the magnetic field intensity. This allows us to combine the terms into a much simpler, highly practical equation: <span class="math notranslate nohighlight">\\ \mathbf{B} = \mu \mathbf{H} \\</span>.

<span class="math notranslate nohighlight">\\\mu\\</span> (mu) is the permeability of the material. It measures how easily a material can support the formation of a magnetic field within itself. It is calculated as <span class="math notranslate nohighlight">\\\mu = \mu_0 \mu_r\\</span>, where <span class="math notranslate nohighlight">\\\mu_0\\</span> is the vacuum permeability and <span class="math notranslate nohighlight">\\\mu_r\\</span> is the relative permeability of the material. In a pure vacuum, <span class="math notranslate nohighlight">\\\mu_r = 1\\</span>, so <span class="math notranslate nohighlight">\\\mathbf{B} = \mu_0 \mathbf{H}\\</span>. In highly magnetic materials like iron, <span class="math notranslate nohighlight">\\\mu_r\\</span> can be in the thousands, which is why an iron core drastically magnifies the <span class="math notranslate nohighlight">\\\mathbf{B}\\</span> field inside an electromagnet.

</div>

<div id="gausss-law-for-electricity" class="section">

##### Gauss’s Law for Electricity<a href="#gausss-law-for-electricity" class="headerlink" title="Link to this heading">#</a>

If you have a positive charge, electric field lines radiate outward from it. If you have a negative charge, the field lines point inward. In this macroscopic form, the law specifically states that the outward flow (or flux) of the electric displacement field from a closed region is directly proportional only to the free electric charge enclosed within it, neatly hiding the complex internal polarization of the material itself. Specifically: \$<span class="math notranslate nohighlight">\\ \nabla \cdot \mathbf{D} = \rho_v \\</span>\$

<span class="math notranslate nohighlight">\\\nabla \cdot \mathbf{D}\\</span> (divergence of <span class="math notranslate nohighlight">\\\mathbf{D}\\</span>) represents the outward flow of the electric displacement field. <span class="math notranslate nohighlight">\\\rho_v\\</span> is the free volume charge density (the measurable, physical charge you can add or remove, ignoring the microscopic bound charges within the atoms of a material).

</div>

<div id="gausss-law-for-magnetism" class="section">

##### Gauss’s Law for Magnetism<a href="#gausss-law-for-magnetism" class="headerlink" title="Link to this heading">#</a>

Magnetic fields do not have isolated “charges” (monopoles). While you can have an isolated positive or negative electric charge, you can never have an isolated “North” or “South” magnetic pole. If you break a bar magnet in half, you just get two smaller magnets, each with its own North and South pole. Because of this, magnetic field lines have no beginning or end; they always form continuous, closed loops. Specifically: \$<span class="math notranslate nohighlight">\\ \nabla \cdot \mathbf{B} = 0 \\</span>\$

<span class="math notranslate nohighlight">\\\nabla \cdot \mathbf{B}\\</span> (divergence of <span class="math notranslate nohighlight">\\\mathbf{B}\\</span>) is exactly zero everywhere. What flows into a region must flow out, meaning there is no single “source” or “sink” for a magnetic field.

</div>

<div id="faradays-law-of-induction" class="section">

##### Faraday’s Law of Induction<a href="#faradays-law-of-induction" class="headerlink" title="Link to this heading">#</a>

A changing magnetic field generates an electric field.This is the principle behind almost all modern power generation. If you fluctuate a magnetic field, it creates a swirling electric field in the surrounding space. If a wire is present, this field pushes electrons through it, creating an electrical current. Specifically: \$<span class="math notranslate nohighlight">\\ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\</span>\$

<span class="math notranslate nohighlight">\\\nabla \times \mathbf{E}\\</span> (curl of <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>) represents the swirling, circulating nature of the induced electric field. <span class="math notranslate nohighlight">\\-\frac{\partial \mathbf{B}}{\partial t}\\</span> represents the rate at which the magnetic flux density is changing over time. The negative sign (Lenz’s Law) dictates that the induced field opposes the change that created it.

</div>

<div id="the-ampere-maxwell-law" class="section">

##### The Ampère-Maxwell Law<a href="#the-ampere-maxwell-law" class="headerlink" title="Link to this heading">#</a>

Magnetic fields are generated by flowing electrical currents and by changing electric fields. Ampère originally discovered that a wire carrying a current generates a magnetic field around it. However, Maxwell noticed a flaw in the math when dealing with broken circuits, like charging capacitors. He realized that just as a changing magnetic field creates an electric field (Faraday’s Law), a changing electric field must create a magnetic field. Specifically: \$<span class="math notranslate nohighlight">\\ \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \\</span>\$

<span class="math notranslate nohighlight">\\\nabla \times \mathbf{H}\\</span> represents the swirling magnetic field intensity. <span class="math notranslate nohighlight">\\\mathbf{J}\\</span> is the free current density (the actual, macroscopic flow of electrical charge). <span class="math notranslate nohighlight">\\\frac{\partial \mathbf{D}}{\partial t}\\</span> is Maxwell’s addition, known as the “displacement current.” It represents the magnetic field generated by a changing electric displacement field over time.

</div>

<div id="electromagnetic-wave-equation" class="section">

##### Electromagnetic Wave Equation<a href="#electromagnetic-wave-equation" class="headerlink" title="Link to this heading">#</a>

The electromagnetic (EM) wave equation is a second-order partial differential equation derived from Maxwell’s equations that describes the propagation of electric and magnetic fields through vacuum or a medium. To derive this equation, we want to decouple <span class="math notranslate nohighlight">\\ \mathbf{E} \\</span> and <span class="math notranslate nohighlight">\\ \mathbf{B} \\</span> to find an equation that describes only the electric field. To do this, we take the curl (<span class="math notranslate nohighlight">\\ \nabla \times \\</span>) of both sides of Faraday’s Law:

<div class="math notranslate nohighlight">

\\ \nabla \times (\nabla \times \mathbf{E}) = \nabla \times \left(-\frac{\partial \mathbf{B}}{\partial t}\right) \\

</div>

Because space and time derivatives are independent, we can swap the order of the curl and the time derivative on the right side:

<div class="math notranslate nohighlight">

\\ \nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t} (\nabla \times \mathbf{B}) \\

</div>

Now, we use a standard vector calculus identity for the “curl of a curl”, which states that for any vector field <span class="math notranslate nohighlight">\\ \mathbf{A} \\</span>: \$<span class="math notranslate nohighlight">\\ \nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A} \\</span><span class="math notranslate nohighlight">\\ Applying this to the left side of the previous equation for electric field gives: \\</span><span class="math notranslate nohighlight">\\ \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E} = -\frac{\partial}{\partial t} (\nabla \times \mathbf{B}) \\</span>\$

Now we bring in the other Maxwell equations to simplify both sides:

- Left side: If we assume a vacuum (no electric charges), we know from Gauss’s Law that <span class="math notranslate nohighlight">\\\nabla \cdot \mathbf{E} = 0 \\</span>. Therefore, the term <span class="math notranslate nohighlight">\\ \nabla(\nabla \cdot \mathbf{E})\\</span> completely vanishes.

- Right side: From the Ampere-Maxwell Law, we can substitute <span class="math notranslate nohighlight">\\\nabla \times \mathbf{B} \\</span> with <span class="math notranslate nohighlight">\\ \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}\\</span>.

Plugging these substitutions back in, we get: \$<span class="math notranslate nohighlight">\\-\nabla^2 \mathbf{E} = -\frac{\partial}{\partial t} ( \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} )\\</span>\$

Multiply both sides by -1 and pull the constants out of the derivative: \$<span class="math notranslate nohighlight">\\\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} \\</span>\$

This is the final wave equation for electric fields. Note: You can repeat this exact same process starting with Ampere’s Law (taking the curl of <span class="math notranslate nohighlight">\\ \mathbf{B} \\</span>) to find the identical wave equation for the magnetic field: \$<span class="math notranslate nohighlight">\\ \nabla^2 \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2} \\</span>\$

The equation we just found perfectly matches the standard 3D wave equation from classical physics <span class="math notranslate nohighlight">\\ \nabla^2 f = \frac{1}{v^2} \frac{\partial^2 f}{\partial t^2} \\</span>. By comparing our derived equation to the standard wave equation, we can see that electric fields propagate as waves, and their velocity <span class="math notranslate nohighlight">\\ v \\</span> squared is given by <span class="math notranslate nohighlight">\\ \frac{1}{v^2} = \mu_0 \epsilon_0 \\</span> with <span class="math notranslate nohighlight">\\ v = \frac{1}{\sqrt{\mu_0 \epsilon_0}} \\</span> . When you plug in the known constants for <span class="math notranslate nohighlight">\\ \mu_0 \\</span> and <span class="math notranslate nohighlight">\\ \epsilon_0 \\</span>, you get exactly <span class="math notranslate nohighlight">\\ c \\</span> (the speed of light, roughly <span class="math notranslate nohighlight">\\3 \times 10^8\\</span> m/s).

</div>

</div>

<span id="document-notebooks/physics/02_fdtd"></span>

<div id="fdtd-method" class="section tex2jax_ignore mathjax_ignore">

#### FDTD Method<a href="#fdtd-method" class="headerlink" title="Link to this heading">#</a>

The **Finite-Difference Time-Domain (FDTD)** method is a numerical technique for solving Maxwell’s equations — the fundamental equations governing all electromagnetic phenomena. It was first proposed by Kane Yee in 1966 and remains one of the most widely used computational electromagnetics methods today.

FDTD is a **full-wave** method, meaning it captures all electromagnetic wave effects without approximation: reflection, diffraction, dispersion, polarization, and nonlinear interactions. It works by discretizing both space and time into a grid and marching the electric and magnetic fields forward in time using simple update equations derived from Maxwell’s equations.

FDTD fits best in the **“resonance region”** — problems where the feature sizes of interest are on the order of a wavelength. Specifically:

- **Antenna design and analysis**

- **Electromagnetic compatibility (EMC) testing**

- **Photonic devices** (waveguides, filters, resonators)

- **Radar cross-section computation**

- **Biological tissue interaction with EM fields**

- **Optical components** (gratings, lenses, photonic crystals)

It is *less* suited for problems where features are either extremely small compared to the wavelength (quasi-static methods are more efficient) or extremely large (ray-based methods like geometric optics are preferable).

<div id="finite-differences" class="section">

##### Finite Differences<a href="#finite-differences" class="headerlink" title="Link to this heading">#</a>

FDTD replaces continuous derivatives with discrete approximations. The key tool is the **central difference approximation**.

Consider a function <span class="math notranslate nohighlight">\\f(x)\\</span>. From Taylor series expansions about <span class="math notranslate nohighlight">\\x_0\\</span> with offsets of <span class="math notranslate nohighlight">\\\pm\delta/2\\</span>: \$<span class="math notranslate nohighlight">\\\begin{aligned}f(x_0 + \delta/2) &= f(x_0) + (\delta/2)f'(x_0) + \frac{1}{2!}(\delta/2)^2f''(x_0) + \dots \\ f(x_0 - \delta/2) &= f(x_0) - (\delta/2)f'(x_0) + \frac{1}{2!}(\delta/2)^2f''(x_0) - \dots\end{aligned}\\</span>\$

Subtracting the second from the first and dividing by <span class="math notranslate nohighlight">\\\delta\\</span>: \$<span class="math notranslate nohighlight">\\\left.\frac{df}{dx}\right\|\_{x=x_0} \approx \frac{f(x_0 + \delta/2) - f(x_0 - \delta/2)}{\delta} + \mathcal{O}(\delta^2)\\</span>\$

This is the **central difference formula**. The crucial insight: the error term scales as <span class="math notranslate nohighlight">\\\delta^2\\</span>, so halving the grid spacing reduces the error by a factor of four. This **second-order accuracy** is what Yee chose for his FDTD algorithm.

> <div>
>
> **Key insight**: The function is sampled not at <span class="math notranslate nohighlight">\\x_0\\</span> itself, but at the two neighboring half-points. This staggering is the geometric heart of the FDTD method.
>
> </div>

</div>

<div id="leap-frog-scheme" class="section">

##### Leap-Frog Scheme<a href="#leap-frog-scheme" class="headerlink" title="Link to this heading">#</a>

FDTD directly discretizes the Ampère-Maxwell Law and Faraday’s Law of Induction in differential form. To make these equations useful for time-stepping, we substitute the fundamental connections <span class="math notranslate nohighlight">\\\mathbf{B} = \mu \mathbf{H}\\</span> and <span class="math notranslate nohighlight">\\\mathbf{D} = \varepsilon \mathbf{E}\\</span>. Assuming a region with no free current (<span class="math notranslate nohighlight">\\\mathbf{J} = 0\\</span>), this gives us our working equations:

**Faraday’s Law of Induction**: how a changing <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>-field creates <span class="math notranslate nohighlight">\\\mathbf{H}\\</span>. Starting from the fundamental law <span class="math notranslate nohighlight">\\\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}\\</span>, we substitute <span class="math notranslate nohighlight">\\\mathbf{B}\\</span> to get: \$<span class="math notranslate nohighlight">\\-\mu \frac{\partial \mathbf{H}}{\partial t} = \nabla \times \mathbf{E}\\</span>\$

**The Ampère-Maxwell Law**: how a changing <span class="math notranslate nohighlight">\\\mathbf{H}\\</span>-field creates <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>. Starting from the fundamental law <span class="math notranslate nohighlight">\\\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}\\</span>, we substitute <span class="math notranslate nohighlight">\\\mathbf{D}\\</span> and set <span class="math notranslate nohighlight">\\\mathbf{J}\\</span> to zero to get: \$<span class="math notranslate nohighlight">\\\varepsilon \frac{\partial \mathbf{E}}{\partial t} = \nabla \times \mathbf{H}\\</span>\$

These two equations are coupled: <span class="math notranslate nohighlight">\\\mathbf{E}\\</span> drives changes in <span class="math notranslate nohighlight">\\\mathbf{H}\\</span>, and <span class="math notranslate nohighlight">\\\mathbf{H}\\</span> drives changes in <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>. The FDTD algorithm exploits this coupling with a leap-frog time-stepping scheme:

1.  Update <span class="math notranslate nohighlight">\\\mathbf{H}\\</span> using the current <span class="math notranslate nohighlight">\\\mathbf{E}\\</span>

2.  Update <span class="math notranslate nohighlight">\\\mathbf{E}\\</span> using the newly updated <span class="math notranslate nohighlight">\\\mathbf{H}\\</span>.

3.  Repeat

This leap-frog approach means <span class="math notranslate nohighlight">\\\mathbf{E}\\</span> and <span class="math notranslate nohighlight">\\\mathbf{H}\\</span> are never known at the same instant — they are staggered by half a time step. This staggering in time mirrors the staggering in space, and together they form the Yee grid.

</div>

<div id="the-yee-algorithm" class="section">

##### The Yee Algorithm<a href="#the-yee-algorithm" class="headerlink" title="Link to this heading">#</a>

The Yee algorithm (1966) is summarized in five steps:

1.  **Discretize space and time** so that E and H fields are staggered both spatially and temporally.

2.  **Replace derivatives** in Ampere’s and Faraday’s laws with central differences.

3.  **Solve** the resulting difference equations for the “future” unknown fields in terms of the “past” known fields, producing **update equations**.

4.  **Evaluate H** one half time-step into the future (H becomes “known”).

5.  **Evaluate E** one full time-step into the future (E becomes “known”).

6.  Repeat steps 4–5.

<div id="the-staggered-grid-1d" class="section">

###### The staggered grid (1D)<a href="#the-staggered-grid-1d" class="headerlink" title="Link to this heading">#</a>

In 1D, if only Ez and Hy are non-zero (assuming variation in x only):

<div class="highlight-default notranslate">

<div class="highlight">

    Space:    ...  Ez[m-1]  Hy[m-1/2]  Ez[m]  Hy[m+1/2]  Ez[m+1]  ...
                      ←——Δx/2——→←—Δx/2——→

    Time:     ... Hy^(q-1/2)   Ez^q    Hy^(q+1/2)  Ez^(q+1) ...
                  ←——Δt/2——→←——Δt/2——→

</div>

</div>

- **Ez nodes** (circles) sit at integer spatial positions m, sampled at integer time steps q.

- **Hy nodes** (triangles) sit at half-integer spatial positions m+½, sampled at half-integer time steps q+½.

This interlocking is not just mathematical bookkeeping — it is precisely what makes the central difference formula accurate. Each derivative is evaluated exactly at the midpoint between the two sample values.

</div>

</div>

<div id="update-equations-in-1d" class="section">

##### Update Equations in 1D<a href="#update-equations-in-1d" class="headerlink" title="Link to this heading">#</a>

Starting from the 1D form of Faraday’s law applied at the space-time point <span class="math notranslate nohighlight">\\((m+1/2)\Delta x, q\Delta t)\\</span>: \$<span class="math notranslate nohighlight">\\\mu \frac{H_y^{q+1/2}\[m+1/2\] - H_y^{q-1/2}\[m+1/2\]}{\Delta t} = \frac{E_z^q\[m+1\] - E_z^q\[m\]}{\Delta x}\\</span>\$

Solving for the future H-field: \$<span class="math notranslate nohighlight">\\H_y^{q+1/2}\[m+1/2\] = H_y^{q-1/2}\[m+1/2\] + \left(\frac{\Delta t}{\mu\Delta x}\right) \cdot \left(E_z^q\[m+1\] - E_z^q\[m\]\right)\\</span>\$

Similarly, from Ampere’s law applied at <span class="math notranslate nohighlight">\\(m\Delta x, (q+1/2)\Delta t)\\</span>: \$<span class="math notranslate nohighlight">\\E_z^{q+1}\[m\] = E_z^q\[m\] + \left(\frac{\Delta t}{\varepsilon\Delta x}\right) \cdot \left(H_y^{q+1/2}\[m+1/2\] - H_y^{q+1/2}\[m-1/2\]\right)\\</span>\$

These two equations are the **heart of FDTD**. They say:

- The future H depends only on its past value and the neighboring E values.

- The future E depends only on its past value and the neighboring H values.

No matrix inversion, no global solve — just local arithmetic at each grid point, repeated at every time step.

</div>

<div id="d-yee-grid" class="section">

##### 3D Yee Grid<a href="#d-yee-grid" class="headerlink" title="Link to this heading">#</a>

The 3D Yee grid, introduced by Kane Yee in 1966, is the fundamental spatial building block of the FDTD method. Instead of calculating both electric and magnetic fields at the exact same point in space, the Yee cell staggers them across a three-dimensional cubic lattice. In this arrangement, the electric field components are positioned at the centers of the cube’s edges, while the magnetic field components are placed at the centers of the cube’s faces.

This staggered layout is geometrically brilliant because it mirrors the physical behavior described by Maxwell’s equations. Every electric field vector is naturally surrounded by a closed loop of magnetic field vectors (capturing Ampere’s Law), and every magnetic field vector is surrounded by a closed loop of electric field vectors (capturing Faraday’s Law). Furthermore, this interlocking grid inherently enforces the divergence-free nature of magnetic fields across the simulation space, ensuring long-term physical accuracy without requiring extra corrective calculations. The visualization below illustrates this interleaved structure (adapted from meep documentation):

![3d yee cell](https://github.com/ymahlau/fdtdx-notebooks/blob/main/img/yee_cube.png?raw=true)

<div id="the-courant-stability-condition" class="section">

###### The Courant Stability Condition<a href="#the-courant-stability-condition" class="headerlink" title="Link to this heading">#</a>

Introducing the Courant number <span class="math notranslate nohighlight">\\S_c = c\Delta t/\Delta x\\</span> (where <span class="math notranslate nohighlight">\\c = 1/\sqrt{\varepsilon_0\mu_0}\\</span> is the speed of light), the update coefficients simplify to: \$<span class="math notranslate nohighlight">\\\begin{aligned}\frac{\Delta t}{\varepsilon\Delta x} &= S_c \cdot \frac{\eta_0}{\varepsilon_r} \quad &\text{(for the E update)} \\ \frac{\Delta t}{\mu\Delta x} &= \frac{S_c}{\mu_r \cdot \eta_0} \quad &\text{(for the H update)}\end{aligned}\\</span>\$

where<span class="math notranslate nohighlight">\\\eta_0 = \sqrt{\mu_0/\varepsilon_0} \approx 377\\ \Omega\\</span> is the free-space impedance. FDTD is an explicit time-marching algorithm. If the time step is too large, the simulation goes **unstable** — field values grow without bound, producing meaningless results. The stability condition in 1D is:

<div class="math notranslate nohighlight">

\\S_c = \frac{c\Delta t}{\Delta x} \le 1\\

</div>

In 2D: \$<span class="math notranslate nohighlight">\\\frac{c\Delta t}{\Delta x} \le \frac{1}{\sqrt{2}} \quad \text{(for square cells, } \Delta x = \Delta y \text{)}\\</span>\$

In 3D: \$<span class="math notranslate nohighlight">\\\frac{c\Delta t}{\Delta x} \le \frac{1}{\sqrt{3}} \quad \text{(for cubic cells)}\\</span>\$

**Physical intuition**: In each update cycle, information can only travel one spatial step. If Δt is too large, a disturbance could “jump” farther than one cell, violating causality as represented on the grid — and the algorithm blows up. The optimal Sc = 1 (in 1D) is also the most accurate, since it minimizes numerical dispersion. In practice, 1D simulations use Sc = 0.99, while 2D and 3D simulations use Sc = 0.99/√2 and 0.99/√3, respectively. This gives a little bit of safety buffer to prevent instabilities.

</div>

<div id="memory-and-time-requirements" class="section">

###### Memory and time requirements<a href="#memory-and-time-requirements" class="headerlink" title="Link to this heading">#</a>

<div class="pst-scrollable-table-container">

| Dimension | Memory (per field) | Time steps for accuracy           |
|-----------|--------------------|-----------------------------------|
| 1D        | O(N)               | O(N)                              |
| 2D        | O(N²)              | O(N²)                             |
| 3D        | O(N³)              | O(N⁴) (halving Δx also halves Δt) |

</div>

This is why 3D FDTD simulations can be expensive — a 2x increase in resolution in all directions increases memory by 8x and compute by 16x.

</div>

</div>

<div id="common-pitfalls-and-best-practices" class="section">

##### Common Pitfalls and Best Practices<a href="#common-pitfalls-and-best-practices" class="headerlink" title="Link to this heading">#</a>

<div id="grid-resolution" class="section">

###### Grid resolution<a href="#grid-resolution" class="headerlink" title="Link to this heading">#</a>

As a rule of thumb, use **at least 10–20 cells per wavelength** (at the highest frequency of interest). More cells reduce numerical dispersion but increase memory and time:

<div class="math notranslate nohighlight">

\\\begin{split}\begin{aligned}\Delta x &\le \frac{\lambda\_{\text{min}}}{10} \quad &\rightarrow \quad \text{safe rule} \\ \Delta x &\le \frac{\lambda\_{\text{min}}}{20} \quad &\rightarrow \quad \text{more accurate}\end{aligned}\end{split}\\

</div>

</div>

<div id="numerical-dispersion" class="section">

###### Numerical dispersion<a href="#numerical-dispersion" class="headerlink" title="Link to this heading">#</a>

Waves on an FDTD grid travel at speeds that differ slightly from c, and the error depends on the direction of propagation and the wavelength relative to the grid spacing. In 1D with Sc = 1, dispersion is zero — the scheme is exact. In 2D and 3D, some residual dispersion always exists.

</div>

<div id="staircasing-of-curved-boundaries" class="section">

###### Staircasing of curved boundaries<a href="#staircasing-of-curved-boundaries" class="headerlink" title="Link to this heading">#</a>

Diagonal or curved boundaries must be approximated using staircase steps along the Cartesian grid. This introduces O(Δx) error (first-order) at boundaries, even though the bulk update equations are second-order. Conformal methods like subpixel-smoothing can mitigate this.

</div>

<div id="near-to-far-field-transformation" class="section">

###### Near-to-far-field transformation<a href="#near-to-far-field-transformation" class="headerlink" title="Link to this heading">#</a>

FDTD computes near fields on the grid. To obtain far-field quantities (radiation patterns, RCS), a surface integration — the near-to-far-field (NTFF) transformation — should be applied over a closed Huygens surface that encloses all sources and scatterers.

</div>

</div>

<div id="references" class="section">

##### References<a href="#references" class="headerlink" title="Link to this heading">#</a>

- Schneider, J. B. (2010). Understanding the finite-difference time-domain method. School of electrical engineering and computer science Washington State University, 28.

</div>

</div>

</div>

</div>

<span id="document-03_components"></span>

<div id="component-examples" class="section">

### Component Examples<a href="#component-examples" class="headerlink" title="Link to this heading">#</a>

Welcome to the Component Examples! These interactive Jupyter notebooks dive into the specific building blocks available in FDTDX. Explore these guides to learn how to effectively set up various sources, detectors, and other essential simulation components.

<div class="admonition note">

Note

**Stay tuned!** More component guides and tutorials will follow shortly.

</div>

<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">

<div class="sd-row sd-row-cols-1 sd-row-cols-xs-1 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 sd-g-3 sd-g-xs-3 sd-g-sm-3 sd-g-md-3 sd-g-lg-3 docutils">

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

1\. Uniform Plane Source

</div>

Learn how to inject uniform plane waves into your simulation domain.

</div>

<a href="#document-notebooks/components/01_uniform_plane_source" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Uniform Plane Source</span></a>

</div>

</div>

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

2\. Mode Source & Detector

</div>

Explore how to inject and measure specific guided optical modes.

</div>

<a href="#document-notebooks/components/02_mode_source_detector" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">Mode Source and Detector</span></a>

</div>

</div>

</div>

</div>

<div class="toctree-wrapper compound">

<span id="document-notebooks/components/01_uniform_plane_source"></span>

<div id="uniform-plane-source" class="section tex2jax_ignore mathjax_ignore">

#### Uniform Plane Source<a href="#uniform-plane-source" class="headerlink" title="Link to this heading">#</a>

This notebook gives an example of using some more functions to setup and run a simulation. In this simulation, we will use a uniform plane source to show the interaction of light with some cuboid object floating in free space.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import time
    import jax
    import jax.numpy as jnp
    import fdtdx
    import matplotlib.pyplot as plt
    from IPython.display import Video

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    %matplotlib inline

</div>

</div>

</div>

</div>

</div>

<div id="setup-of-simulation-scence" class="section tex2jax_ignore mathjax_ignore">

#### Setup of simulation scence<a href="#setup-of-simulation-scence" class="headerlink" title="Link to this heading">#</a>

Let’s start with a basic setup of a simulation scene. We need to specify a random key for possible stochastic operations. This simulation will be entirely deterministic, but we still need to specify the key. Then we specify a SimulationConfig object with some basic information on how long the simulation should run and how accurate it needs to be (resolution, dtype and courant factor).

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Create a JAX random key for reproducibility and stochastic operations
    key = jax.random.PRNGKey(seed=42)

    object_list = []

    # Define simulation configuration (duration, resolution, data type, etc.)
    config = fdtdx.SimulationConfig(
        time=100e-15,
        resolution=100e-9,
        dtype=jnp.float32,
        courant_factor=0.99
    )

</div>

</div>

</div>

</div>

Next, we specify the simulation volume. This includes the background material, which is used for all the space where we do not place objects in the following specifications.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    volume = fdtdx.SimulationVolume(
        partial_real_shape=(12.0e-6, 12e-6, 12e-6),
        material=fdtdx.Material(  # Background material
            permittivity=1.0,
            permeability=1.0,
        )
    )
    object_list.append(volume)

</div>

</div>

</div>

</div>

As we have seen in the object placement tutorial, in FDTDX objects are placed through constraints. We create an empty list of these constraints first and then iteratively add more constraints to the list.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    constraints = []

</div>

</div>

</div>

</div>

At first, we add the boundaries of our simulation to the constraints. We are using absorbing PML boundaries at the top and bottom (Z-axis) to prevent any reflections from the boundary of the simulation volume. In the XY-plane we use periodic boundaries to simulate an infinite plane wave.

We could specify the boundary for each of the six sides of the simulation volume manually, but this would be tedious. Instead, we will use a handy shortcut provided by FDTDX. This creates PML boundaries on all six sides with the corresponding constraints. Here we use a thickness of 10 grid cells for the PML, which should be enough for most applications.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    bound_cfg = fdtdx.BoundaryConfig.from_uniform_bound(boundary_type="periodic", override_types={"min_z": "pml", "max_z": "pml"},)
    bound_dict, c_list = fdtdx.boundary_objects_from_config(bound_cfg, volume)
    constraints.extend(c_list)
    object_list.extend(bound_dict.values())

</div>

</div>

</div>

</div>

The UniformPlaneSource is designed to model a plane wave source with uniform spatial intensity distribution. It is placed at the top (z-axis) of the simulation volume, and the light is propagated downwards, indicated by the direction “-”. The polarization of the light is set to Ex-polarized, meaning the electric field oscillates in the x-direction. Unlike the Gaussian source, the spatial profile of the uniform source is constant across its entire area, without any Gaussian shaping. As a result, the light intensity is uniformly distributed across the source, making it suitable for simulations where consistent illumination is needed. Since there is no Gaussian profile to define the radius or standard deviation, the emission is typically spread across the entire defined area. The source’s parameters, such as wavelength and polarization, can be adjusted to match specific simulation requirements, with the wavelength in this example set to 1.550 µm.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    source = fdtdx.UniformPlaneSource(
        partial_grid_shape=(None, None, 1),
        fixed_E_polarization_vector=(1, 0, 0),
        wave_character=fdtdx.WaveCharacter(wavelength=1.550e-6),
        direction="-",
    )

    object_list.append(source)
    constraints.extend(
        [
            source.place_relative_to(
                volume,
                axes=(0, 1, 2),
                own_positions=(0, 0, 1),
                other_positions=(0, 0, 1),
                margins=(0, 0, -1.5e-6),
            ),
            source.same_size(volume, axes=(0, 1))
        ]
    )

</div>

</div>

</div>

</div>

Next, we place a uniform cuboid at the center of the simulaiton volume. This will make the simulation a bit more interesting to look at, because otherwise we will only see the light emitted from the source.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cube = fdtdx.UniformMaterialObject(
        partial_real_shape=(3e-6, 3e-6, 3e-6),  # size of the object in meters
        material=fdtdx.Material(permittivity=2.5, permeability=1.7),  # material
        name="Cube",
        color = fdtdx.colors.PINK,  # name of the object, optional
    )
    object_list.append(cube)
    constraints.append(cube.place_at_center(volume))

</div>

</div>

</div>

</div>

In order to actually see a result from the simulation, we need to define a Detector. While the simulation function will return the E and H field after runnning the simulation, usually it is also necessary to read some physical metrics on intermediate time steps in the simulation. This is exactly what Detectors are for!

Here we use an EnergyDetector, which calculates the energy at every grid point within its volume. We also speciy a switch, which controls the time steps that the detector records. Our purpose here is to generate a video of the energy during the simulation. We do not need every single time step for this, so we only record every third time step.

The as_slices option is a memory optimization specific for creating images or videos. With this option set to True, only the values which are actually plotted will be saved instead of the whole simulation volume. If you need to read values from the whole volume, simply disable this option.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    video_energy_detector = fdtdx.EnergyDetector(
        name="Video",
        as_slices=True,
        switch=fdtdx.OnOffSwitch(interval=3),
        exact_interpolation=True,
        num_video_workers=8,
    )
    object_list.append(video_energy_detector)
    constraints.extend(video_energy_detector.same_position_and_size(volume))

</div>

</div>

</div>

</div>

These are all the objects we need for our simulation! Let’s resolve the constraints and plot the simulation scene to see if we made any mistakes. Note that it is good practice to split the random key to maintain randomness in JAX

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key, subkey = jax.random.split(key)
    objects, arrays, params, config, _ = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=constraints,
        key=subkey,
    )

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    fig = fdtdx.plot_setup(
        config=config,
        objects=objects,
        exclude_object_list=[video_energy_detector],
    )
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

![](_images/169ead0830bd668e25171b268e013654f0b9eb9b8bc8a7c92119877196944060.png)

</div>

</div>

</div>

<div id="running-the-simulation" class="section tex2jax_ignore mathjax_ignore">

#### Running the simulation<a href="#running-the-simulation" class="headerlink" title="Link to this heading">#</a>

Now let’s define a function that actually runs the simulation. In FDTDX, this is a two-part process.

Firstly, we call apply_params, which performs some calculations before the start of the simulation. If we have some parametric objects in the simulation, this function applies the given parameters and calculates the actual shapes of these objects. Additionally, some performance optimization are done here by calculating values for the simulation once before the simulation starts

Then, we call run_fdtd, which performs the FDTD simulation as a loop. The computation terminates as soon as the required number of time steps are reached.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    def sim_fn(
            params: fdtdx.ParameterContainer,
            arrays: fdtdx.ArrayContainer,
            key: jax.Array,
        ):
            # Apply parameters to objects and arrays
            arrays, new_objects, _ = fdtdx.apply_params(arrays, objects, params, key)

            # Run FDTD simulation (forward)
            final_state = fdtdx.run_fdtd(
                arrays=arrays,
                objects=new_objects,
                config=config,
                key=key,
            )
            _, arrays = final_state

            return arrays

</div>

</div>

</div>

</div>

In order to execute this function, we should first compile it. JAX provides a just-in-time compilation functionality with jax.jit, which automatically compiles a function as soon as it is called the first time. We extend this a little bit here by calling .lower() and .compile() to compile the function immediately and measure the compilation time. If this seems complicated, just omit the .lower() and .compile() and everything will still work the same, just the time measurement would be wrong.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    start_time = time.time()
    jitted_loss = jax.jit(sim_fn).lower(params, arrays, key).compile()
    end_time = time.time()
    print(f"Compilation time: {end_time - start_time} seconds")

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Compilation time: 3.778167247772217 seconds

</div>

</div>

</div>

</div>

Now we are ready to run the simulation. We can see that the simulation time is smaller than the compilation time, which can happen for small simulations. This might seem inefficient, but in pratice a few seconds usually don’t matter. And, we are now able to call the compiled function as often as we like.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    start_time = time.time()
    new_arrays = jitted_loss(params, arrays, subkey)
    end_time = time.time()
    print(f"Simulation runtime: {end_time - start_time} seconds")

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    Simulation runtime: 1.0212416648864746 seconds

</div>

</div>

</div>

</div>

</div>

<div id="visualizing-the-results-of-a-simulation" class="section tex2jax_ignore mathjax_ignore">

#### Visualizing the results of a simulation<a href="#visualizing-the-results-of-a-simulation" class="headerlink" title="Link to this heading">#</a>

Now we have run the simulation, but how do we visualize the results? Our goal was to generate a video of the simulation, so let’s do this.

The syntax for generating a video in a jupyter notebook is currently a bit complicated, but for actual scripts FDTDX offers some utility functions to make this easier. The reason the syntax is so complicated, is on the one hand because of the JAX-syntax which does not allow in-place updates. Additionally, the plot function saves a video to a temporary location. We can either access the video from there or move it to a more permament location

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    video_path = objects["Video"].draw_plot(new_arrays.detector_states["Video"])
    print(video_path)
    Video(list(video_path.values())[0], embed=True, width=720)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    {'sliced_video': '/tmp/tmpct19t9xe.mp4'}

</div>

</div>

<div class="output text_html">

Your browser does not support the video tag.

</div>

</div>

</div>

</div>

<span id="document-notebooks/components/02_mode_source_detector"></span>

<div id="mode-source-and-detector" class="section tex2jax_ignore mathjax_ignore">

#### Mode Source and Detector<a href="#mode-source-and-detector" class="headerlink" title="Link to this heading">#</a>

This tutorial gives an introduction to modes in FDTD simulations and how they are used withing the fdtdx.ModeSource and fdtdx.ModeOverlapDetector.

<div id="introduction-to-modes-in-fdtd" class="section">

##### Introduction to Modes in FDTD<a href="#introduction-to-modes-in-fdtd" class="headerlink" title="Link to this heading">#</a>

Modes are fundamental solutions to Maxwell’s equations that describe how electromagnetic fields propagate through waveguides, optical fibers, and other guiding structures. In the context of FDTD (Finite-Difference Time-Domain) simulations, modes represent the characteristic field patterns that can propagate along a given cross-section of a waveguiding structure without changing their transverse profile.

</div>

<div id="what-are-electromagnetic-modes" class="section">

##### What are Electromagnetic Modes?<a href="#what-are-electromagnetic-modes" class="headerlink" title="Link to this heading">#</a>

An electromagnetic mode is a self-consistent field distribution that maintains its shape as it propagates along a waveguide. Each mode is characterized by:

Mode profile: The transverse electric and magnetic field distribution (Ex, Ey, Hx, Hy) Effective index (neff): Determines the phase velocity of the mode Propagation constant ( ): Related to the effective index by = neff × , where is the free-space wavenumber Common types of modes include:

TEM Modes: Transverse Electromagnetic, where both electric and magnetic field components along the propagation direction are zero (e.g., Ez = 0 and Hz = 0 for z-propagating modes). TE modes: Transverse Electric, where the electric field component along the propagation direction is zero (e.g., Ez = 0 for z-propagating modes, Ex = 0 for x-propagating modes) TM modes: Transverse Magnetic, where the magnetic field component along the propagation direction is zero (e.g., Hz = 0 for z-propagating modes, Hx = 0 for x-propagating modes) Hybrid modes: Both electric and magnetic field components along the propagation direction are non-zero (e.g., both Ez ≠ 0 and Hz ≠ 0 for z-propagating modes). These are common in optical fibers and integrated photonics where the waveguide geometry breaks the symmetry required for pure TE or TM modes.

</div>

<div id="let-the-confusion-begin" class="section">

##### Let the confusion begin<a href="#let-the-confusion-begin" class="headerlink" title="Link to this heading">#</a>

In integrated photonics waveguides, there do not exist clean modes from the above definition due to complex geometries. Therefore, technincally all modes are hybrid modes in integrated photonics. Usually a different convention is used to describe modes:

- “TE-like” or “quasi-TE”: The dominant electric field component is in the plane of the substrate (typically horizontal for a silicon-on-insulator waveguide)

- “TM-like” or “quasi-TM”: The dominant electric field component is perpendicular to the substrate plane (typically vertical) FDTDX follows these conventions for both mode source and detector.

</div>

<div id="mode-sources-in-fdtd" class="section">

##### Mode Sources in FDTD<a href="#mode-sources-in-fdtd" class="headerlink" title="Link to this heading">#</a>

The fdtdx.ModeSource launches specific modes into your simulation domain. Instead of using plane waves or point sources, mode sources inject the exact field pattern of a waveguide mode, which is essential for:

- Exciting single-mode or multi-mode waveguides

- Studying mode coupling and conversion

- Analyzing transmission and reflection of guided modes

- Simulating realistic input conditions for photonic devices

</div>

<div id="mode-overlap-detection" class="section">

##### Mode Overlap Detection<a href="#mode-overlap-detection" class="headerlink" title="Link to this heading">#</a>

The fdtdx.ModeOverlapDetector calculates how much power is coupled into specific modes by computing the overlap integral between the simulated fields and the analytical mode profiles. This enables:

- Quantitative measurement of transmission and reflection coefficients

- Analysis of mode conversion efficiency

- Characterization of coupling between different waveguide modes

- S-parameter extraction for photonic circuits

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import fdtdx
    import jax
    import jax.numpy as jnp
    from matplotlib import pyplot as plt
    import pytreeclass as tc
    from IPython.display import Video

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    %matplotlib inline

</div>

</div>

</div>

</div>

</div>

<div id="simulation-scene" class="section">

##### Simulation Scene<a href="#simulation-scene" class="headerlink" title="Link to this heading">#</a>

Let’s set up a simulation scene for inserting and analyzing modes in a silicon waveguide. It consists of a silicon waveguide on top of a silica substrate. The waveguide has air cladding on the top/sides. The simulation volume has absorbing perfectly matched layers (PML) as boundary conditions.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key = jax.random.PRNGKey(0)

    object_list = []

    config = fdtdx.SimulationConfig(
        time=100e-15,
        resolution=20e-9,
        dtype=jnp.float32,
        courant_factor=0.99,
    )

    materials = {
        "air": fdtdx.Material(),
        "silicon": fdtdx.Material(permittivity=3.45**2),
        "silica": fdtdx.Material(permittivity=1.44**2)
    }

    volume = fdtdx.SimulationVolume(
        partial_real_shape=(8.0e-6, 1.5e-6, 1.5e-6),
        material=materials["air"]  # background material
    )
    object_list.append(volume)

    # Perfectly Matched layers to absorb energy at boundaries
    bound_cfg = fdtdx.BoundaryConfig.from_uniform_bound(thickness=10, boundary_type="pml")
    bound_dict, boundary_constraint_list = fdtdx.boundary_objects_from_config(bound_cfg, volume)
    object_list.extend(bound_dict.values())

    substrate = fdtdx.UniformMaterialObject(
        name="Substrate",
        partial_real_shape=(None, None, 0.6e-6),
        material=materials["silica"],
        color=fdtdx.colors.BROWN,
    )
    object_list.append(substrate)

    waveguide = fdtdx.UniformMaterialObject(
        name="Waveguide",
        partial_real_shape=(None, 460e-9, 220e-9),
        material=materials["silicon"],
        color=fdtdx.colors.PINK,
    )
    object_list.append(waveguide)

    placement_constraints = [
        # boundary placement constraints
        *boundary_constraint_list,
        # place substrate at bottom of simulation volume
        substrate.place_relative_to(
            volume,
            axes=2,
            other_positions=-1,
            own_positions=-1,
        ),
        # place waveguide above substrate
        waveguide.place_above(substrate),
        # place waveguide at center in y-direction
        waveguide.place_at_center(volume, axes=1)
    ]

    # compile constraints into a simulation scene
    key, subkey = jax.random.split(key)
    objects, arrays, params, config, _ = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key=subkey,
    )
    # plot the simulation scene
    plt.clf()
    fdtdx.plot_setup(config=config, objects=objects)
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 640x480 with 0 Axes>

</div>

</div>

![](_images/85b22844457981a67584e82a202ee5f8dc5d59b24f4ca68ef0646368fa49fbde.png)

</div>

</div>

To see if it is actually possible to perform a simulation of this size, we can analyze some parameters of the simulation setup. Specifically, we should see if our simulation runtime is long enough, such that light can traverse the waveguide from one side of the simulation to the other.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    wavelength = 1.55e-6
    period = fdtdx.constants.wavelength_to_period(wavelength)
    period_steps = round(period / config.time_step_duration)
    print(f"{config.time_steps_total=}")
    print(f"{config.max_travel_distance=}")
    print(f"{period_steps=}")
    print(tc.tree_summary(arrays, depth=1))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    config.time_steps_total=2623
    config.max_travel_distance=2.9979245800000002e-05
    period_steps=136
    ┌──────────────────────┬────────────────┬──────────┬────────┐
    │Name                  │Type            │Count     │Size    │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.E                    │f32[3,400,75,75]│6,750,000 │25.75MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.H                    │f32[3,400,75,75]│6,750,000 │25.75MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.psi_E                │f32[6,400,75,75]│13,500,000│51.50MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.psi_H                │f32[6,400,75,75]│13,500,000│51.50MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.alpha                │f32[6,400,75,75]│13,500,000│51.50MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.kappa                │f32[6,400,75,75]│13,500,000│51.50MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.sigma                │f32[6,400,75,75]│13,500,000│51.50MB │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.inv_permittivities   │f32[400,75,75]  │2,250,000 │8.58MB  │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.inv_permeabilities   │float           │1         │        │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.detector_states      │dict            │          │        │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.recording_state      │NoneType        │          │        │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.electric_conductivity│NoneType        │          │        │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │.magnetic_conductivity│NoneType        │          │        │
    ├──────────────────────┼────────────────┼──────────┼────────┤
    │Σ                     │ArrayContainer  │83,250,001│317.57MB│
    └──────────────────────┴────────────────┴──────────┴────────┘

</div>

</div>

</div>

</div>

This simulation scene looks good, but we also need to add a source to insert energy into the simulation. We will add the source on the left side of the simulation and set it up to insert a specific mode propagating to the right (positive x-direction). The source needs to be large enough to contain the whole mode profile, so we will just let it automatically be extended to the simulation size in the y/z-axes.

Additionally, we will add an energy detector, which will record the energy in the whole simulation volume and automatically create a video for us.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    source = fdtdx.ModePlaneSource(
        mode_index=0,
        filter_pol="te",
        partial_grid_shape=(1, None, None),  # single grid shape in propagation direction
        direction='+',
        wave_character=fdtdx.WaveCharacter(wavelength=wavelength),
        name="source",
        color=fdtdx.colors.GREEN,
    )
    object_list.append(source)

    energy_detector = fdtdx.EnergyDetector(
        name="energy detector",
        switch=fdtdx.OnOffSwitch(interval=5),  # only record every k time steps to save some memory
        as_slices=True,  # for the video, we only need to save slices
        num_video_workers=None,
    )
    object_list.append(energy_detector)

    placement_constraints.extend([
        source.place_relative_to(
            volume,
            axes=0,
            own_positions=-1,
            other_positions=-1,
            margins=1e-6,
        ),
        *energy_detector.same_position_and_size(volume),  # type: ignore
    ])

    # compile constraints into a simulation scene
    key, subkey = jax.random.split(key)
    objects, arrays, params, config, _ = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key=subkey,
    )
    # plot the simulation scene
    plt.clf()
    fdtdx.plot_setup(
        config=config, 
        objects=objects,
        # exclude some objects for better visibility
        exclude_object_list=[energy_detector],
        exclude_yz_plane_object_list=[source],
    )
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 640x480 with 0 Axes>

</div>

</div>

![](_images/0c2f2c862ccea93184e7d6dc8e5835ffcaa6e52e582b13dfe91ecc0c9523e377.png)

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Now we can see that in the array container, some space got allocated for the detectors:
    print(tc.tree_summary(arrays, depth=1))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    ┌──────────────────────┬────────────────┬───────────┬────────┐
    │Name                  │Type            │Count      │Size    │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.E                    │f32[3,400,75,75]│6,750,000  │25.75MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.H                    │f32[3,400,75,75]│6,750,000  │25.75MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.psi_E                │f32[6,400,75,75]│13,500,000 │51.50MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.psi_H                │f32[6,400,75,75]│13,500,000 │51.50MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.alpha                │f32[6,400,75,75]│13,500,000 │51.50MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.kappa                │f32[6,400,75,75]│13,500,000 │51.50MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.sigma                │f32[6,400,75,75]│13,500,000 │51.50MB │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.inv_permittivities   │f32[400,75,75]  │2,250,000  │8.58MB  │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.inv_permeabilities   │float           │1          │        │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.detector_states      │dict            │34,453,125 │131.43MB│
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.recording_state      │NoneType        │           │        │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.electric_conductivity│NoneType        │           │        │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │.magnetic_conductivity│NoneType        │           │        │
    ├──────────────────────┼────────────────┼───────────┼────────┤
    │Σ                     │ArrayContainer  │117,703,126│449.00MB│
    └──────────────────────┴────────────────┴───────────┴────────┘

</div>

</div>

</div>

</div>

Now let’s run a simulation and see how it looks. But wait, first we should see if the mode we specified is actually correct. Before running a simulation in fdtdx, the apply_params function always needs to be called which is a preprocessing step. In this step, among other things, the mode is calculated.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    arrays, new_objects, info = fdtdx.apply_params(arrays, objects, params, key)

</div>

</div>

</div>

</div>

Now we can inspect the mode of the Mode source and plot their fields. This also let’s us verify that it is actually a te-mode as specified above, since the main electrical component is in the y-direction (perpendicular to the substrate). Note that the Ex/Hx components are zero here, because the source only needs to the real parts of the mode fields. The actual mode also has imaginary components.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # inspect the mode
    plt.clf()
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    # First row: E field components
    im1 = axes[0, 0].imshow(new_objects[source.name]._E[0].squeeze().T)
    axes[0, 0].set_title('Ex')
    axes[0, 0].axis('off')
    plt.colorbar(im1, ax=axes[0, 0], shrink=0.8)

    im2 =axes[0, 1].imshow(new_objects[source.name]._E[1].squeeze().T)
    axes[0, 1].set_title('Ey')
    axes[0, 1].axis('off')
    plt.colorbar(im2, ax=axes[0, 1], shrink=0.8)

    im3 = axes[0, 2].imshow(new_objects[source.name]._E[2].squeeze().T)
    axes[0, 2].set_title('Ez')
    axes[0, 2].axis('off')
    plt.colorbar(im3, ax=axes[0, 2], shrink=0.8)

    # Second row: H field components
    im4 = axes[1, 0].imshow(new_objects[source.name]._H[0].squeeze().T)
    axes[1, 0].set_title('Hx')
    axes[1, 0].axis('off')
    plt.colorbar(im4, ax=axes[1, 0], shrink=0.8)

    im5 = axes[1, 1].imshow(new_objects[source.name]._H[1].squeeze().T)
    axes[1, 1].set_title('Hy')
    axes[1, 1].axis('off')
    plt.colorbar(im5, ax=axes[1, 1], shrink=0.8)

    im6 = axes[1, 2].imshow(new_objects[source.name]._H[2].squeeze().T)
    axes[1, 2].set_title('Hz')
    axes[1, 2].axis('off')
    plt.colorbar(im6, ax=axes[1, 2], shrink=0.8)


    plt.tight_layout()
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 640x480 with 0 Axes>

</div>

</div>

![](_images/79812822d6dde1f29952f0a19158d564683359fb94f2d324cf37259b4295955d.png)

</div>

</div>

Let’s run a simulation and see how it looks! Note that generating the video can take some time, depending on how many video workers were specified above.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key, subkey = jax.random.split(key)
    _, arrays = jax.jit(fdtdx.run_fdtd)(arrays, new_objects, config, subkey)
    # log energy detector, which creates a video of the whole simulation volume
    video_path = new_objects[energy_detector.name].draw_plot(arrays.detector_states[energy_detector.name])
    print(video_path)
    Video(list(video_path.values())[0], embed=True, width=720)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    {'sliced_video': '/var/folders/9c/sf1_5nb17v51rk1l8xcxshdc0000gn/T/tmpjci0epvc.mp4'}

</div>

</div>

<div class="output text_html">

Your browser does not support the video tag.

</div>

</div>

</div>

We can see that the source works as intended. The source only emits light only in a single direction since the ModeSource uses a Total-Field Scattered-Field formulation.

Now let’s also add a ModeOverlapDetector, which measures the field compoments in a simulation in the frequency domain. Afterwards, we can compare the measured fields with a computed mode to see how much Overlap there is. This is closely related to the [S-parameters](https://en.wikipedia.org/wiki/Scattering_parameters).

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    detector = fdtdx.ModeOverlapDetector(
        mode_index=0,
        filter_pol="te",
        partial_grid_shape=(1, None, None),  # single grid shape in propagation direction
        direction='+',
        wave_characters=(fdtdx.WaveCharacter(wavelength=wavelength),),
        name="mode detector",
        switch=fdtdx.OnOffSwitch(period=period, start_time=0.75*config.time, on_for_periods=2)
    )
    object_list.append(detector)
    placement_constraints.append(detector.place_at_center(volume))

    # compile constraints into a simulation scene
    key, subkey = jax.random.split(key)
    objects, arrays, params, config, _ = fdtdx.place_objects(
        object_list=object_list,
        config=config,
        constraints=placement_constraints,
        key=subkey,
    )
    # plot the simulation scene
    plt.clf()
    fdtdx.plot_setup(
        config=config, 
        objects=objects,
        # exclude some objects for better visibility
        exclude_object_list=[energy_detector],
        exclude_yz_plane_object_list=[source, detector],
    )
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 640x480 with 0 Axes>

</div>

</div>

![](_images/3d41ccc0a7acd8e27fea60dffec0917f95de3d69761bb5590f7c83c081d476f3.png)

</div>

</div>

We placed the detector in the middle of the simulation volume to give it some distance from the source. Note that we only start to measure fields with the detector after 75% of the simulation time has already passed, because light first needs to travel to the detector. After 75% of the time, a steady state should be reached where we can calculate the fourier components. This could be done more efficiently with a pulsed source, but for the sake of this tutorial we will keep it simple.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    arrays, new_objects, info = fdtdx.apply_params(arrays, objects, params, key)
    key, subkey = jax.random.split(key)
    _, arrays = jax.jit(fdtdx.run_fdtd)(arrays, new_objects, config, subkey)

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    overlap = new_objects[detector.name].compute_overlap(arrays.detector_states[detector.name])
    print(jnp.abs(overlap))

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    0.985381

</div>

</div>

</div>

</div>

There is some loss in the simulation due to numerical dispersion, as well as some loss because the mode source does not insert the mode perfectly in the simulation. As a result the detector only measures about 97.5% of the energy reaching the detector.

</div>

</div>

</div>

</div>

<span id="document-04_advanced"></span>

<div id="advanced" class="section">

### Advanced<a href="#advanced" class="headerlink" title="Link to this heading">#</a>

Welcome to the Advanced guides!

<div class="admonition note">

Note

**Stay tuned!** More advanced guides and tutorials will follow shortly.

</div>

<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">

<div class="sd-row sd-row-cols-1 sd-row-cols-xs-1 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 sd-g-3 sd-g-xs-3 sd-g-sm-3 sd-g-md-3 sd-g-lg-3 docutils">

<div class="sd-col sd-d-flex-row docutils">

<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover docutils">

<div class="sd-card-body docutils">

<div class="sd-card-title sd-font-weight-bold docutils">

1\. 2D Simulation

</div>

Learn how to set up and run two-dimensional simulations within the 3D-Framework

</div>

<a href="#document-notebooks/advanced/01_2d_simulation" class="sd-stretched-link sd-hide-link-text reference internal"><span class="doc">2D Simulations</span></a>

</div>

</div>

</div>

</div>

<div class="toctree-wrapper compound">

<span id="document-notebooks/advanced/01_2d_simulation"></span>

<div id="d-simulations" class="section tex2jax_ignore mathjax_ignore">

#### 2D Simulations<a href="#d-simulations" class="headerlink" title="Link to this heading">#</a>

Currently, **FDTDX does not natively support true 2D simulations**. However, a 2D problem can still be simulated by constructing a very thin 3D domain and enforcing periodicity in the third dimension. This notebook demonstrates how to implement such a setup.

In this example, we simulate a **2D electromagnetic problem in the x–y plane**. The **x and y directions represent the actual physical simulation dimensions**, where the fields evolve and interact with objects. The **z direction does not represent a real physical dimension of the problem**. Instead, it acts as a small **buffer dimension required by the FDTDX solver**, which currently operates on 3D grids.

To emulate a 2D system, the computational domain is constructed as a **3-cell extrusion along the z-axis**:

- The simulation volume is **three cells thick in the z direction**.

- The **first and last cells in z (indices 0 and 2)** use **periodic boundary conditions**.

- All materials and structures are **uniform along the z direction**.

Because the geometry and material properties do not vary along z and periodic boundaries are enforced, the electromagnetic fields also remain invariant in that direction. As a result, the simulation effectively behaves as a **2D simulation in the x–y plane**, while the z dimension simply enables compatibility with the 3D FDTD implementation in FDTDX.

Note: Some special sources (mode / gaussian plane sources) may not currently work in this 2D trick. But a standard plane source does.

------------------------------------------------------------------------

<div id="imports-setup" class="section">

##### Imports & Setup<a href="#imports-setup" class="headerlink" title="Link to this heading">#</a>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    import fdtdx
    import jax
    import jax.numpy as jnp
    import matplotlib.pyplot as plt
    from IPython.display import HTML
    from IPython.display import Video
    %matplotlib inline

</div>

</div>

</div>

</div>

</div>

<div id="simulation-configuration" class="section">

##### Simulation Configuration<a href="#simulation-configuration" class="headerlink" title="Link to this heading">#</a>

Here we define the basic simulation parameters:

- The **material type** and its **permittivity**.

- The **simulation configuration**, which includes parameters such as the simulation duration, spatial resolution, numerical precision (<span class="pre">`dtype`</span>), and the Courant stability factor.

- The **boundary conditions** used for the computational domain.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # 1) Basic FDTD config
    config = fdtdx.SimulationConfig(
        time=100e-15,           # total simulated time
        resolution=50e-9,       # spatial resolution
        dtype=jnp.float32,
        courant_factor=0.99,
    )

    material = fdtdx.Material(permittivity=1.0)

    materials = {
        "air": material,
        "cylinder": fdtdx.Material(permittivity=2.25),
    }


    # create a volume that is large in x/y, thin in z
    volume = fdtdx.SimulationVolume(
        partial_real_shape=(8e-6, 4e-6, 0.3e-6),  # ~3 cells in z
        material=material
    )

    # --- Compute grid cell counts manually ---
    dx = config.resolution
    nx = int(volume.partial_real_shape[0] / dx)
    ny = int(volume.partial_real_shape[1] / dx)
    nz = int(volume.partial_real_shape[2] / dx)

</div>

</div>

</div>

</div>

We enforce **periodic boundary conditions along the z direction** (between the first and last grid slices). This ensures that the fields repeat in the z direction and therefore remain invariant, effectively reproducing a **2D simulation in the x–y plane**.

In FDTDX, periodicity can be defined through **boundary configuration objects**, although it can also be implemented manually if needed.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # create periodic boundaries in z
    bound_cfg = fdtdx.BoundaryConfig.from_uniform_bound(
        thickness=1, 
        boundary_type="periodic"
    )
    bound_dict, bc_constraints = fdtdx.boundary_objects_from_config(bound_cfg, volume)

</div>

</div>

</div>

</div>

</div>

<div id="plane-source" class="section">

##### Plane Source<a href="#plane-source" class="headerlink" title="Link to this heading">#</a>

Next, we place a **plane source** that emits light in the **+x direction** into the simulation domain.

For this setup, we use a standard <span class="pre">`UniformPlaneSource`</span>. Currently, **mode sources are not supported when using the 2D extrusion approach** described above.

The source is **extruded along the z direction**, meaning it is uniform across the thin buffer dimension. This maintains the effective 2D behavior of the simulation.

At this stage, we also initialize the lists for **objects** and **constraints**, which will allow us to easily append additional simulation components later.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    from fdtdx import UniformPlaneSource, WaveCharacter

    source = fdtdx.UniformPlaneSource(
    fixed_E_polarization_vector=(0,0,1),
    partial_grid_shape=(1, None, None),
    partial_real_position=(0.0, None, None),  # x = 0, span y/z
    wave_character=fdtdx.WaveCharacter(wavelength=1.55e-6),
    direction="+",
    name="plane_source",
    )

    objects = []
    constraints = []

</div>

</div>

</div>

</div>

</div>

<div id="cylinder-scatterer" class="section">

##### Cylinder (Scatterer)<a href="#cylinder-scatterer" class="headerlink" title="Link to this heading">#</a>

We place a **cylindrical scatterer** at the center of the simulation domain.

The cylinder extends fully along the **z direction**, which means that in the effective **2D x–y view it appears as a circle**.

In FDTDX, the <span class="pre">`Cylinder`</span> primitive is defined as a 3D object that is extruded along one axis (in this case the z axis). When used in the thin-domain setup described above, it therefore behaves like a **2D circular scatterer**.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    cyl = fdtdx.Cylinder(
        partial_real_shape=(0.5e-6, 0.5e-6, 0.3e-6),
        radius=0.25e-6,
        axis=2,
        materials=materials,
        material_name="cylinder",
        name="cylinder",
    )

</div>

</div>

</div>

</div>

Let’s assemble all the objects and constraints in our lists.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # Assemble objects and constraints
    objects.append(volume)
    objects.append(source)

    # add boundary objects + constraints (FIX)
    for val in bound_dict.values():
        if isinstance(val, tuple):
            bound_obj, bound_constraint = val
            objects.append(bound_obj)
            constraints.append(bound_constraint)
        else:
            # periodic boundary (object only)
            objects.append(val)

    # add cylinder + its constraint
    objects.append(cyl)
    constraints.append(cyl.place_at_center(volume))
    constraints.extend(
        source.same_position_and_size(volume, axes=(1, 2))
    )

</div>

</div>

</div>

</div>

In order to actually see a result from the simulation, we need to define a Detector.

Here we use an EnergyDetector, which calculates the energy at every grid point within its volume. We also speciy a switch, which controls the time steps that the detector records. Our purpose here is to generate a video of the energy during the simulation. We do not need every single time step for this, so we only record every fifth time step.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    video_detector = fdtdx.EnergyDetector(
        name="Ez_video",
        switch=fdtdx.OnOffSwitch(interval=5)
    )
    objects.append(video_detector)
    constraints.extend(video_detector.same_position_and_size(volume))

</div>

</div>

</div>

</div>

</div>

<div id="place-objects-build-scene" class="section">

##### Place Objects & Build Scene<a href="#place-objects-build-scene" class="headerlink" title="Link to this heading">#</a>

Now compute actual positions for all objects.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key = jax.random.PRNGKey(42)
    key, subkey = jax.random.split(key)

    objs, arrays, params, config, _ = fdtdx.place_objects(
    object_list=objects,
    config=config,
    constraints=constraints,
    key=subkey,
    )

</div>

</div>

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    plt.figure(figsize=(8, 6))
    fdtdx.plot_setup(config=config, objects = objs, exclude_object_list=[video_detector])
    plt.title("Simulation Setup (x–y view)")
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 800x600 with 0 Axes>

</div>

</div>

![](_images/5478eb87d662da3ee37e771ecf8254452b7dd82ab4089f2c139d0d7e583567bd.png)

</div>

</div>

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    from fdtdx.utils.plot_material import plot_material


    plt.figure(figsize=(8, 6))
    plot_material(
        arrays=arrays,
        config=config,
    )
    plt.title("Material Distribution (Permittivity)")
    plt.tight_layout()
    plt.show()

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output text_plain highlight-myst-ansi notranslate">

<div class="highlight">

    <Figure size 800x600 with 0 Axes>

</div>

</div>

![](_images/4cadcbf2657f51e530263dc3a0ed8dd6dfa60c72416a06cfe3dbead456b3a007.png)

</div>

</div>

</div>

<div id="running-the-simulation" class="section">

##### Running the Simulation<a href="#running-the-simulation" class="headerlink" title="Link to this heading">#</a>

Now let’s define a function that actually runs the simulation. In FDTDX, this is a two-part process.

Firstly, we call apply_params, which performs some calculations before the start of the simulation. If we have some parametric objects in the simulation, this function applies the given parameters and calculates the actual shapes of these objects. Additionally, some performance optimization are done here by calculating values for the simulation once before the simulation starts

Then, we call run_fdtd, which performs the FDTD simulation as a loop. The computation terminates as soon as the required number of time steps are reached.

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    key, subkey = jax.random.split(key)

    arrays, new_objects, info = fdtdx.apply_params(arrays, objs, params, key)

    final_timestamp, new_arrays = fdtdx.run_fdtd(
        config=config,
        objects=new_objects,
        arrays=arrays,
        key=key
    )

</div>

</div>

</div>

</div>

</div>

<div id="visualizing-the-simulation" class="section">

##### Visualizing the Simulation<a href="#visualizing-the-simulation" class="headerlink" title="Link to this heading">#</a>

Now we have run the simulation, but how do we visualize the results? Our goal was to generate a video of the simulation, so let’s do this.

The syntax for generating a video in a jupyter notebook is currently a bit complicated, but for actual scripts FDTDX offers some utility functions to make this easier. The reason the syntax is so complicated, is on the one hand because of the JAX-syntax which does not allow in-place updates. Additionally, the plot function saves a video to a temporary location. We can either access the video from there or move it to a more permament location

<div class="cell docutils container">

<div class="cell_input docutils container">

<div class="highlight-ipython3 notranslate">

<div class="highlight">

    # get the recorded detector state
    detector_state = new_arrays.detector_states["Ez_video"]

    # generate video (mp4)
    video_path = new_objects["Ez_video"].draw_plot(detector_state)

    print(video_path)
    Video(list(video_path.values())[0], embed=True, width=720)

</div>

</div>

</div>

<div class="cell_output docutils container">

<div class="output stream highlight-myst-ansi notranslate">

<div class="highlight">

    {'energy': '/var/folders/9c/sf1_5nb17v51rk1l8xcxshdc0000gn/T/tmpullv72qe.mp4'}

</div>

</div>

<div class="output text_html">

Your browser does not support the video tag.

</div>

</div>

</div>

</div>

</div>

</div>

</div>

<span id="document-05_contributing"></span>

<div id="contributing" class="section">

### Contributing<a href="#contributing" class="headerlink" title="Link to this heading">#</a>

We encourage community contributions of any kind to fdtdx! The following includes a list of useful information on how to make meaningful contributions.

<div id="installation" class="section">

#### Installation<a href="#installation" class="headerlink" title="Link to this heading">#</a>

**1. Fork and Clone** As the first step, make a fork of the fdtdx repository, clone the fork, and create a new branch for the feature you want to develop:

<div class="highlight-bash notranslate">

<div class="highlight">

    git clone https://github.com/YOUR-USERNAME/fdtdx
    cd fdtdx
    git checkout -b name-of-your-feature-branch

</div>

</div>

**2. Set up the Environment (Recommended: uv)** We recommend using <a href="https://docs.astral.sh/uv/" class="reference external">uv</a> for development speed and reliability. First, follow the installation instructions on their <a href="https://docs.astral.sh/uv/getting-started/installation/" class="reference external">website</a>.

Then, install the development dependencies:

<div class="highlight-bash notranslate">

<div class="highlight">

    uv sync --extra=dev
    source .venv/bin/activate

</div>

</div>

This activates your virtual environment. You should run the activation command anytime you start a new shell.

*Note: If you need a specific version of JAX (e.g., with CUDA support), you can install it inside the environment:*

<div class="highlight-bash notranslate">

<div class="highlight">

    pip install -U jax[cuda]

</div>

</div>

**Alternative: Standard pip** If you prefer not to use uv, you can use a standard virtual environment:

<div class="highlight-bash notranslate">

<div class="highlight">

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -e .[dev]

</div>

</div>

</div>

<div id="checklist" class="section">

#### Checklist<a href="#checklist" class="headerlink" title="Link to this heading">#</a>

This is a checklist that you should go through before making a PR. The individual points are explained in more detail below.

- \[ \] Implement your feature and unit tests for your new feature

- \[ \] Check if all unit tests run: <span class="pre">`pytest`</span>` `<span class="pre">`tests/`</span>

- \[ \] Check if all pre-commit checks are passing: <span class="pre">`uv`</span>` `<span class="pre">`run`</span>` `<span class="pre">`pre-commit`</span>` `<span class="pre">`run`</span>` `<span class="pre">`--all`</span>

- \[ \] If you added any new features, that should be top-level imported, add them to <span class="pre">`__all__`</span> in <span class="pre">`src/fdtdx/__init__.py`</span>

- \[ \] If you want your new feature to be present in the documentation, add an entry to <span class="pre">`docs/source/07_api.rst`</span>

- \[ \] Optional: If you want to go above and beyond, add a notebook showcasing your feature in the <a href="https://github.com/ymahlau/fdtdx-notebooks/" class="reference external">notebooks repository</a>. Afterwards you can add an entry in the docs to include your new notebook.

</div>

<div id="creating-and-running-unit-tests" class="section">

#### Creating and running unit tests<a href="#creating-and-running-unit-tests" class="headerlink" title="Link to this heading">#</a>

Testing is an important part of software development. Therefore, we ask you to create unit tests for any software that you write for this repository. Please also run all unit tests before opening a pull request to make sure that all existing test cases still work as intended.

You can run the unit tests with the <span class="pre">`pytest`</span> command in the fdtdx repository. If you want to specify a single test file to run you could specify the file after the command itself: <span class="pre">`pytest`</span>` `<span class="pre">`tests/unit/conversion/test_json.py`</span>

The unit tests are located in the <span class="pre">`/tests`</span> folder, which mirrors the structure of the <span class="pre">`/src`</span> folder. Therefore, if you are adding software to a file in the /src folder, please add the test cases at the corresponding location in the /tests folder.

</div>

<div id="pull-requests" class="section">

#### Pull Requests<a href="#pull-requests" class="headerlink" title="Link to this heading">#</a>

If you want to get some early feedback, it is very useful to make a draft pull request. This way we (the development team) can review the changes on a high-level early on.

Pull requests should follow the standard guidelines for good software development:

- The changes of a pull-request should address a single feature or issue. Please do not make pull-requests with various changes at once. In that case split the PR into multiple individual PRs.

</div>

<div id="preventing-merge-conflicts" class="section">

#### Preventing merge conflicts<a href="#preventing-merge-conflicts" class="headerlink" title="Link to this heading">#</a>

To prevent conflicts, keep your fork synchronized with the main repository.

1.  **Register Upstream:**

    <div class="highlight-bash notranslate">

    <div class="highlight">

        git remote add upstream https://github.com/ymahlau/fdtdx.git

    </div>

    </div>

2.  **Sync Regularly:** Before starting new work, pull the latest changes:

    <div class="highlight-bash notranslate">

    <div class="highlight">

        git fetch upstream
        git merge upstream/main

    </div>

    </div>

</div>

<div id="code-quality" class="section">

#### Code quality<a href="#code-quality" class="headerlink" title="Link to this heading">#</a>

We use automatic checks to standardize code formatting. You can install these checks to run automatically on every commit:

<div class="highlight-bash notranslate">

<div class="highlight">

    pre-commit install

</div>

</div>

You can also run them manually at any time:

<div class="highlight-bash notranslate">

<div class="highlight">

    pre-commit run --all-files

</div>

</div>

</div>

<div id="documentation" class="section">

#### Documentation<a href="#documentation" class="headerlink" title="Link to this heading">#</a>

You can locally build the sphinx documentation of fdtdx using the following commands.

<div class="highlight-bash notranslate">

<div class="highlight">

    sh docs/scripts/sync_notebooks.sh && uv run sphinx-autobuild -W --keep-going docs/source/ docs/build/

</div>

</div>

If you changed anything in the documentation, make sure to run the command above to check if the documentation still works as expected.

</div>

<div id="questions" class="section">

#### Questions<a href="#questions" class="headerlink" title="Link to this heading">#</a>

If you have any questions do not hesitate to ask them! We know that it can be very challenging to get started with JAX specifically and will help you with all problems that might come up.

If there exists already an issue or discussion regarding the feature which you would like to implement, please post your question there. If there does not exist an issue / discussion, create a new one!

</div>

</div>

<span id="document-06_faq"></span>

<div id="faq" class="section">

### FAQ<a href="#faq" class="headerlink" title="Link to this heading">#</a>

<div id="i-have-a-question-not-listed-anywhere" class="section">

#### I have a question not listed anywhere<a href="#i-have-a-question-not-listed-anywhere" class="headerlink" title="Link to this heading">#</a>

If you find yourself pondering about a question which is not answered in the documentation, feel free to open a discussion <a href="https://github.com/ymahlau/fdtdx/discussions" class="reference external">here</a> . We are regularly checking the discussion section and will answer any questions.

</div>

<div id="i-suspect-there-is-a-bug-in-the-code" class="section">

#### I suspect there is a bug in the code<a href="#i-suspect-there-is-a-bug-in-the-code" class="headerlink" title="Link to this heading">#</a>

FDTDX is a relatively new software such that it may happen that there are bugs in the code present, even though we do all we can do avoid this by running a lot of testing. If you find a bug, or even just suspect that there is one feel free to open an issue on github <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">here</a> .

</div>

<div id="there-is-a-feature-missing-in-fdtdx-that-i-really-need" class="section">

#### There is a feature missing in FDTDX that I really need<a href="#there-is-a-feature-missing-in-fdtdx-that-i-really-need" class="headerlink" title="Link to this heading">#</a>

We have made a small roadmap of our plans for fdtdx <a href="https://github.com/ymahlau/fdtdx/discussions/273" class="reference external">here</a> . If you find yourself missing a feature in FDTDX for your specific application, feel free to ask for it there or open an issue <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">here</a> . While we cannot promise that we will implement all requested features, we will be open to any discussion. Additionally, we are happy to receive community contributions as well if you feel comfortable implementing the feature yourself. We will also help you with any questions regarding the implementation and internals of FDTDX that may come up during the implementation process. Please take a look at the <a href="#document-05_contributing" class="reference internal"><span class="doc">Contributing</span></a> guidelines for more details.

</div>

</div>

<span id="document-07_api"></span>

<div id="api" class="section">

### API<a href="#api" class="headerlink" title="Link to this heading">#</a>

<div class="pst-scrollable-table-container">

|  |  |
|----|----|
| <a href="#document-api/fdtdx.apply_params#fdtdx.apply_params" class="reference internal" title="fdtdx.apply_params"><span class="pre"><code class="sourceCode python">fdtdx.apply_params</code></span></a>(arrays, objects, params) | Applies parameters to devices and updates source states. |
| <a href="#document-api/fdtdx.ArrayContainer#fdtdx.ArrayContainer" class="reference internal" title="fdtdx.ArrayContainer"><span class="pre"><code class="sourceCode python">fdtdx.ArrayContainer</code></span></a>(fields, ...\[, ...\]) | Container for simulation field arrays and states. |
| <a href="#document-api/fdtdx.autoinit#fdtdx.autoinit" class="reference internal" title="fdtdx.autoinit"><span class="pre"><code class="sourceCode python">fdtdx.autoinit</code></span></a>(klass) | Wrapper around tc.autoinit that preserves parameter requirement information |
| <a href="#document-api/fdtdx.BinaryMedianFilterModule#fdtdx.BinaryMedianFilterModule" class="reference internal" title="fdtdx.BinaryMedianFilterModule"><span class="pre"><code class="sourceCode python">fdtdx.BinaryMedianFilterModule</code></span></a>(\*\[, ...\]) | Performs 3D binary median filtering on the design. |
| <a href="#document-api/fdtdx.BlochBoundary#fdtdx.BlochBoundary" class="reference internal" title="fdtdx.BlochBoundary"><span class="pre"><code class="sourceCode python">fdtdx.BlochBoundary</code></span></a>(\*\[, partial_real_shape, ...\]) | Implements Bloch periodic boundary conditions. |
| <a href="#document-api/fdtdx.boundary_objects_from_config#fdtdx.boundary_objects_from_config" class="reference internal" title="fdtdx.boundary_objects_from_config"><span class="pre"><code class="sourceCode python">fdtdx.boundary_objects_from_config</code></span></a>(config, ...) | Creates boundary objects from a boundary configuration. |
| <a href="#document-api/fdtdx.BoundaryConfig#fdtdx.BoundaryConfig" class="reference internal" title="fdtdx.BoundaryConfig"><span class="pre"><code class="sourceCode python">fdtdx.BoundaryConfig</code></span></a>(\*\[, ...\]) | Configuration class for boundary conditions. |
| <a href="#document-api/fdtdx.BrushConstraint2D#fdtdx.BrushConstraint2D" class="reference internal" title="fdtdx.BrushConstraint2D"><span class="pre"><code class="sourceCode python">fdtdx.BrushConstraint2D</code></span></a>(\*\[, brush, axis, ...\]) | Applies 2D brush-based constraints to ensure minimum feature sizes. |
| <a href="#document-api/fdtdx.calculate_sparam#fdtdx.calculate_sparam" class="reference internal" title="fdtdx.calculate_sparam"><span class="pre"><code class="sourceCode python">fdtdx.calculate_sparam</code></span></a>(objects, arrays, ...) | Run the FDTD simulation and extract S-parameters from mode-overlap detectors. |
| <a href="#document-api/fdtdx.calculate_sparams#fdtdx.calculate_sparams" class="reference internal" title="fdtdx.calculate_sparams"><span class="pre"><code class="sourceCode python">fdtdx.calculate_sparams</code></span></a>(objects, arrays, ...) | Run FDTD simulations for multiple input ports and merge S-parameters. |
| <a href="#document-api/fdtdx.CCPRPole#fdtdx.CCPRPole" class="reference internal" title="fdtdx.CCPRPole"><span class="pre"><code class="sourceCode python">fdtdx.CCPRPole</code></span></a>(\*\[, pole, residue\]) | General complex-conjugate pole-residue (CCPR) pole. |
| <a href="#document-api/fdtdx.circular_brush#fdtdx.circular_brush" class="reference internal" title="fdtdx.circular_brush"><span class="pre"><code class="sourceCode python">fdtdx.circular_brush</code></span></a>(diameter\[, size\]) | Creates a circular binary mask/brush for morphological operations. |
| <a href="#document-api/fdtdx.ClosedSurfacePhasorPoyntingFluxDetector#fdtdx.ClosedSurfacePhasorPoyntingFluxDetector" class="reference internal" title="fdtdx.ClosedSurfacePhasorPoyntingFluxDetector"><span class="pre"><code class="sourceCode python">fdtdx.ClosedSurfacePhasorPoyntingFluxDetector</code></span></a>(\[...\]) | Net time-averaged Poynting flux through a closed box surface (frequency domain). |
| <a href="#document-api/fdtdx.ClosedSurfacePoyntingFluxDetector#fdtdx.ClosedSurfacePoyntingFluxDetector" class="reference internal" title="fdtdx.ClosedSurfacePoyntingFluxDetector"><span class="pre"><code class="sourceCode python">fdtdx.ClosedSurfacePoyntingFluxDetector</code></span></a>(\[...\]) | Net Poynting flux through the closed surface of a rectangular box. |
| <a href="#document-api/fdtdx.ClosestIndex#fdtdx.ClosestIndex" class="reference internal" title="fdtdx.ClosestIndex"><span class="pre"><code class="sourceCode python">fdtdx.ClosestIndex</code></span></a>(\*\[, ...\]) | Maps continuous latent values to nearest allowed material indices. |
| <a href="#document-api/fdtdx.Color#fdtdx.Color" class="reference internal" title="fdtdx.Color"><span class="pre"><code class="sourceCode python">fdtdx.Color</code></span></a>(r, g, b) | Color representation with multiple format support. |
| <a href="#document-api/fdtdx.compute_energy#fdtdx.compute_energy" class="reference internal" title="fdtdx.compute_energy"><span class="pre"><code class="sourceCode python">fdtdx.compute_energy</code></span></a>(E, H, inv_permittivity, ...) | Computes the total electromagnetic energy density of the field. |
| <a href="#document-api/fdtdx.compute_eps_spectrum_from_coefficients#fdtdx.compute_eps_spectrum_from_coefficients" class="reference internal" title="fdtdx.compute_eps_spectrum_from_coefficients"><span class="pre"><code class="sourceCode python">fdtdx.compute_eps_spectrum_from_coefficients</code></span></a>(c1, ...) | Spatially-averaged complex permittivity spectrum for a block of cells. |
| <a href="#document-api/fdtdx.compute_impedance_corrected_temporal_profile#fdtdx.compute_impedance_corrected_temporal_profile" class="reference internal" title="fdtdx.compute_impedance_corrected_temporal_profile"><span class="pre"><code class="sourceCode python">fdtdx.compute_impedance_corrected_temporal_profile</code></span></a>(...) | FIR-filter a raw source temporal profile for broadband impedance matching. |
| <a href="#document-api/fdtdx.compute_integrated_power#fdtdx.compute_integrated_power" class="reference internal" title="fdtdx.compute_integrated_power"><span class="pre"><code class="sourceCode python">fdtdx.compute_integrated_power</code></span></a>(E, H, axis\[, ...\]) | Computes the integrated power (Poynting flux) across a transverse plane. |
| <a href="#document-api/fdtdx.compute_mode#fdtdx.compute_mode" class="reference internal" title="fdtdx.compute_mode"><span class="pre"><code class="sourceCode python">fdtdx.compute_mode</code></span></a>(frequency, ...\[, ...\]) | Compute optical modes of a waveguide cross-section. |
| <a href="#document-api/fdtdx.compute_pole_coefficients#fdtdx.compute_pole_coefficients" class="reference internal" title="fdtdx.compute_pole_coefficients"><span class="pre"><code class="sourceCode python">fdtdx.compute_pole_coefficients</code></span></a>(poles, dt) | Compute the discrete-time ADE recurrence coefficients of isotropic poles. |
| <a href="#document-api/fdtdx.compute_pole_coefficients_per_axis#fdtdx.compute_pole_coefficients_per_axis" class="reference internal" title="fdtdx.compute_pole_coefficients_per_axis"><span class="pre"><code class="sourceCode python">fdtdx.compute_pole_coefficients_per_axis</code></span></a>(...) | Compute the per-axis discrete-time ADE recurrence coefficients. |
| <a href="#document-api/fdtdx.compute_poynting_flux#fdtdx.compute_poynting_flux" class="reference internal" title="fdtdx.compute_poynting_flux"><span class="pre"><code class="sourceCode python">fdtdx.compute_poynting_flux</code></span></a>(E, H\[, axis\]) | Calculates the Poynting vector (energy flux) from E and H fields. |
| <a href="#document-api/fdtdx.ConnectHolesAndStructures#fdtdx.ConnectHolesAndStructures" class="reference internal" title="fdtdx.ConnectHolesAndStructures"><span class="pre"><code class="sourceCode python">fdtdx.ConnectHolesAndStructures</code></span></a>(\*\[, ...\]) | Connects floating polymer regions and ensures air holes connect to outside. |
| <a href="#document-api/fdtdx.CustomTimeSignalProfile#fdtdx.CustomTimeSignalProfile" class="reference internal" title="fdtdx.CustomTimeSignalProfile"><span class="pre"><code class="sourceCode python">fdtdx.CustomTimeSignalProfile</code></span></a>(\*\[, signal, ...\]) | Sampled waveform temporal profile for arbitrary time signals. |
| <a href="#document-api/fdtdx.Cylinder#fdtdx.Cylinder" class="reference internal" title="fdtdx.Cylinder"><span class="pre"><code class="sourceCode python">fdtdx.Cylinder</code></span></a>(\*\[, partial_real_shape, ...\]) | A cylindrical optical fiber with configurable properties. |
| <a href="#document-api/fdtdx.Detector#fdtdx.Detector" class="reference internal" title="fdtdx.Detector"><span class="pre"><code class="sourceCode python">fdtdx.Detector</code></span></a>(\[\_signed_data, ...\]) | Base class for electromagnetic field detectors in FDTD simulations. |
| <a href="#document-api/fdtdx.DetectorState#fdtdx.DetectorState" class="reference internal" title="fdtdx.DetectorState"><span class="pre"><code class="sourceCode python">fdtdx.DetectorState</code></span></a> | maps detector output names to JAX arrays. |
| <a href="#document-api/fdtdx.Device#fdtdx.Device" class="reference internal" title="fdtdx.Device"><span class="pre"><code class="sourceCode python">fdtdx.Device</code></span></a>(\*\[, partial_real_shape, ...\]) | Abstract base class for devices with optimizable permittivity distributions. |
| <a href="#document-api/fdtdx.DiagonalSymmetry2D#fdtdx.DiagonalSymmetry2D" class="reference internal" title="fdtdx.DiagonalSymmetry2D"><span class="pre"><code class="sourceCode python">fdtdx.DiagonalSymmetry2D</code></span></a>(\*\[, min_min_to_max_max\]) | Enforce diagonal symmetry by effectively halving the parameter space. |
| <a href="#document-api/fdtdx.DiagonalSymmetry3D#fdtdx.DiagonalSymmetry3D" class="reference internal" title="fdtdx.DiagonalSymmetry3D"><span class="pre"><code class="sourceCode python">fdtdx.DiagonalSymmetry3D</code></span></a>(\*\[, ...\]) | Enforce diagonal symmetry in 3D across one of six possible diagonal planes. |
| <a href="#document-api/fdtdx.DispersionModel#fdtdx.DispersionModel" class="reference internal" title="fdtdx.DispersionModel"><span class="pre"><code class="sourceCode python">fdtdx.DispersionModel</code></span></a>(\*\[, poles\]) | Linear susceptibility built from a sum of 2nd-order ADE poles. |
| <a href="#document-api/fdtdx.DrudePole#fdtdx.DrudePole" class="reference internal" title="fdtdx.DrudePole"><span class="pre"><code class="sourceCode python">fdtdx.DrudePole</code></span></a>(\*\[, plasma_frequency, damping\]) | Drude pole parameterised by its physical constants. |
| <a href="#document-api/fdtdx.DtypeConversion#fdtdx.DtypeConversion" class="reference internal" title="fdtdx.DtypeConversion"><span class="pre"><code class="sourceCode python">fdtdx.DtypeConversion</code></span></a>(\*\[, dtype, exclude_filter\]) | Compression module that converts data types of field values. |
| <a href="#document-api/fdtdx.EnergyDetector#fdtdx.EnergyDetector" class="reference internal" title="fdtdx.EnergyDetector"><span class="pre"><code class="sourceCode python">fdtdx.EnergyDetector</code></span></a>(\[\_signed_data, ...\]) | Detector for measuring electromagnetic energy distribution. |
| <a href="#document-api/fdtdx.export_arrays_snapshot_to_vti#fdtdx.export_arrays_snapshot_to_vti" class="reference internal" title="fdtdx.export_arrays_snapshot_to_vti"><span class="pre"><code class="sourceCode python">fdtdx.export_arrays_snapshot_to_vti</code></span></a>(arrays, ...) | Convenience function to export a snapshot of FDTD simulation arrays to a VTI file. |
| <a href="#document-api/fdtdx.export_json#fdtdx.export_json" class="reference internal" title="fdtdx.export_json"><span class="pre"><code class="sourceCode python">fdtdx.export_json</code></span></a>(obj) | Create a dictionary from the given object for exporting to JSON. |
| <a href="#document-api/fdtdx.export_json_str#fdtdx.export_json_str" class="reference internal" title="fdtdx.export_json_str"><span class="pre"><code class="sourceCode python">fdtdx.export_json_str</code></span></a>(obj) | Create a json string from the given object. |
| <a href="#document-api/fdtdx.export_stl#fdtdx.export_stl" class="reference internal" title="fdtdx.export_stl"><span class="pre"><code class="sourceCode python">fdtdx.export_stl</code></span></a>(matrix\[, stl_filename, ...\]) | Export a 3D boolean matrix to an STL file. |
| <a href="#document-api/fdtdx.export_vti#fdtdx.export_vti" class="reference internal" title="fdtdx.export_vti"><span class="pre"><code class="sourceCode python">fdtdx.export_vti</code></span></a>(cell_data, filename, resolution) | Export a dictionary of arrays to a VTI (VTK ImageData) file. |
| <a href="#document-api/fdtdx.export_vtr#fdtdx.export_vtr" class="reference internal" title="fdtdx.export_vtr"><span class="pre"><code class="sourceCode python">fdtdx.export_vtr</code></span></a>(cell_data, filename, grid) | Export cell data to a VTR (VTK RectilinearGrid) file. |
| <a href="#document-api/fdtdx.extend_material_to_pml#fdtdx.extend_material_to_pml" class="reference internal" title="fdtdx.extend_material_to_pml"><span class="pre"><code class="sourceCode python">fdtdx.extend_material_to_pml</code></span></a>(objects, arrays) | Extend interior-edge material values into each PML region. |
| <a href="#document-api/fdtdx.ExtrudedPolygon#fdtdx.ExtrudedPolygon" class="reference internal" title="fdtdx.ExtrudedPolygon"><span class="pre"><code class="sourceCode python">fdtdx.ExtrudedPolygon</code></span></a>(\*\[, ...\]) | A polygon object specified by a list of vertices. |
| <a href="#document-api/fdtdx.extruded_polygon_from_gds#fdtdx.extruded_polygon_from_gds" class="reference internal" title="fdtdx.extruded_polygon_from_gds"><span class="pre"><code class="sourceCode python">fdtdx.extruded_polygon_from_gds</code></span></a>(lib, ...\[, ...\]) | Create an ExtrudedPolygon from a polygon in an already-loaded gdstk Library. |
| <a href="#document-api/fdtdx.extruded_polygon_from_gds_path#fdtdx.extruded_polygon_from_gds_path" class="reference internal" title="fdtdx.extruded_polygon_from_gds_path"><span class="pre"><code class="sourceCode python">fdtdx.extruded_polygon_from_gds_path</code></span></a>(...\[, ...\]) | Create an ExtrudedPolygon from a polygon in a GDS file. |
| <a href="#document-api/fdtdx.field#fdtdx.field" class="reference internal" title="fdtdx.field"><span class="pre"><code class="sourceCode python">fdtdx.field</code></span></a>(\*\[, default, init, repr, kind, ...\]) | A wrapper for pytreeclass fields. |
| <a href="#document-api/fdtdx.FieldDetector#fdtdx.FieldDetector" class="reference internal" title="fdtdx.FieldDetector"><span class="pre"><code class="sourceCode python">fdtdx.FieldDetector</code></span></a>(\[\_signed_data, ...\]) | Detector for measuring field components of electromagnetic fields in the time domain. |
| <a href="#document-api/fdtdx.FieldProjectionAngleDetector#fdtdx.FieldProjectionAngleDetector" class="reference internal" title="fdtdx.FieldProjectionAngleDetector"><span class="pre"><code class="sourceCode python">fdtdx.FieldProjectionAngleDetector</code></span></a>(\[...\]) | Frequency-domain detector for projecting a phasor plane to observation angles. |
| <a href="#document-api/fdtdx.FieldProjectionCartesianDetector#fdtdx.FieldProjectionCartesianDetector" class="reference internal" title="fdtdx.FieldProjectionCartesianDetector"><span class="pre"><code class="sourceCode python">fdtdx.FieldProjectionCartesianDetector</code></span></a>(\[...\]) | Frequency-domain detector for projecting phasors to a Cartesian observation plane. |
| <a href="#document-api/fdtdx.FieldProjectionKSpaceDetector#fdtdx.FieldProjectionKSpaceDetector" class="reference internal" title="fdtdx.FieldProjectionKSpaceDetector"><span class="pre"><code class="sourceCode python">fdtdx.FieldProjectionKSpaceDetector</code></span></a>(\[...\]) | Frequency-domain detector for projecting phasors to a k-space direction grid. |
| <a href="#document-api/fdtdx.FieldState#fdtdx.FieldState" class="reference internal" title="fdtdx.FieldState"><span class="pre"><code class="sourceCode python">fdtdx.FieldState</code></span></a>(E, H, psi_E, psi_H\[, ...\]) | Dynamic electromagnetic field state that evolves each time step. |
| <a href="#document-api/fdtdx.frozen_field#fdtdx.frozen_field" class="reference internal" title="fdtdx.frozen_field"><span class="pre"><code class="sourceCode python">fdtdx.frozen_field</code></span></a>(\*\[, default, init, repr, ...\]) | Creates a field that automatically freezes on set and unfreezes on get. |
| <a href="#document-api/fdtdx.frozen_private_field#fdtdx.frozen_private_field" class="reference internal" title="fdtdx.frozen_private_field"><span class="pre"><code class="sourceCode python">fdtdx.frozen_private_field</code></span></a>(\*\[, default, ...\]) | Creates a field that automatically freezes on set and unfreezes on get, sets the default to None and init to False. |
| <a href="#document-api/fdtdx.full_backward#fdtdx.full_backward" class="reference internal" title="fdtdx.full_backward"><span class="pre"><code class="sourceCode python">fdtdx.full_backward</code></span></a>(state, objects, config) | Perform full backward FDTD propagation from current state to start time. |
| <a href="#document-api/fdtdx.GaussianPlaneSource#fdtdx.GaussianPlaneSource" class="reference internal" title="fdtdx.GaussianPlaneSource"><span class="pre"><code class="sourceCode python">fdtdx.GaussianPlaneSource</code></span></a>(\[...\]) |  |
| <a href="#document-api/fdtdx.GaussianPulseProfile#fdtdx.GaussianPulseProfile" class="reference internal" title="fdtdx.GaussianPulseProfile"><span class="pre"><code class="sourceCode python">fdtdx.GaussianPulseProfile</code></span></a>(\*\[, ...\]) | Gaussian pulse temporal profile with carrier wave. |
| <a href="#document-api/fdtdx.GaussianSmoothing2D#fdtdx.GaussianSmoothing2D" class="reference internal" title="fdtdx.GaussianSmoothing2D"><span class="pre"><code class="sourceCode python">fdtdx.GaussianSmoothing2D</code></span></a>(\*\[, std_discrete, ...\]) | Applies Gaussian smoothing to 2D parameter arrays. |
| <a href="#document-api/fdtdx.GradientConfig#fdtdx.GradientConfig" class="reference internal" title="fdtdx.GradientConfig"><span class="pre"><code class="sourceCode python">fdtdx.GradientConfig</code></span></a>(\*\[, method, recorder, ...\]) | Configuration for gradient computation in simulations. |
| <a href="#document-api/fdtdx.GridCoordinateConstraint#fdtdx.GridCoordinateConstraint" class="reference internal" title="fdtdx.GridCoordinateConstraint"><span class="pre"><code class="sourceCode python">fdtdx.GridCoordinateConstraint</code></span></a>(\*, object, ...) | Constrains an object's position to specific grid coordinates. |
| <a href="#document-api/fdtdx.HorizontalSymmetry2D#fdtdx.HorizontalSymmetry2D" class="reference internal" title="fdtdx.HorizontalSymmetry2D"><span class="pre"><code class="sourceCode python">fdtdx.HorizontalSymmetry2D</code></span></a>() | Enforce horizontal (x-axis) mirror symmetry. |
| <a href="#document-api/fdtdx.HorizontalSymmetry3D#fdtdx.HorizontalSymmetry3D" class="reference internal" title="fdtdx.HorizontalSymmetry3D"><span class="pre"><code class="sourceCode python">fdtdx.HorizontalSymmetry3D</code></span></a>(\*\[, mirror_axis\]) | Enforce horizontal mirror symmetry in 3D along the x or y axis. |
| <a href="#document-api/fdtdx.import_from_json#fdtdx.import_from_json" class="reference internal" title="fdtdx.import_from_json"><span class="pre"><code class="sourceCode python">fdtdx.import_from_json</code></span></a>(json_str) |  |
| <a href="#document-api/fdtdx.LinearReconstructEveryK#fdtdx.LinearReconstructEveryK" class="reference internal" title="fdtdx.LinearReconstructEveryK"><span class="pre"><code class="sourceCode python">fdtdx.LinearReconstructEveryK</code></span></a>(\*\[, k, ...\]) | Time step filter that performs linear reconstruction between sampled steps. |
| <a href="#document-api/fdtdx.Logger#fdtdx.Logger" class="reference internal" title="fdtdx.Logger"><span class="pre"><code class="sourceCode python">fdtdx.Logger</code></span></a>(experiment_name\[, name, ...\]) | Logger for managing experiment outputs and visualization. |
| <a href="#document-api/fdtdx.LorentzPole#fdtdx.LorentzPole" class="reference internal" title="fdtdx.LorentzPole"><span class="pre"><code class="sourceCode python">fdtdx.LorentzPole</code></span></a>(\*\[, resonance_frequency, ...\]) | Lorentz pole parameterised by its physical constants. |
| <a href="#document-api/fdtdx.Material#fdtdx.Material" class="reference internal" title="fdtdx.Material"><span class="pre"><code class="sourceCode python">fdtdx.Material</code></span></a>(\*\[, permittivity, ...\]) | Represents an electromagnetic material with specific electrical and magnetic properties. |
| <a href="#document-api/fdtdx.metric_efficiency#fdtdx.metric_efficiency" class="reference internal" title="fdtdx.metric_efficiency"><span class="pre"><code class="sourceCode python">fdtdx.metric_efficiency</code></span></a>(detector_states, ...) | Calculate efficiency metrics between input and output detectors. |
| <a href="#document-api/fdtdx.ModeOverlapDetector#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">fdtdx.ModeOverlapDetector</code></span></a>(\[\_signed_data, ...\]) | Detector for measuring the overlap of a waveguide mode with the simulation fields. |
| <a href="#document-api/fdtdx.ModePlaneSource#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.ModePlaneSource"><span class="pre"><code class="sourceCode python">fdtdx.ModePlaneSource</code></span></a>(\[temporal_profile, ...\]) |  |
| <a href="#document-api/fdtdx.normalize_by_energy#fdtdx.normalize_by_energy" class="reference internal" title="fdtdx.normalize_by_energy"><span class="pre"><code class="sourceCode python">fdtdx.normalize_by_energy</code></span></a>(E, H, ...) | Normalizes electromagnetic fields by their total energy. |
| <a href="#document-api/fdtdx.normalize_by_poynting_flux#fdtdx.normalize_by_poynting_flux" class="reference internal" title="fdtdx.normalize_by_poynting_flux"><span class="pre"><code class="sourceCode python">fdtdx.normalize_by_poynting_flux</code></span></a>(E, H, axis) | Normalize fields so the integrated Poynting flux along <span class="pre">`axis`</span> is one. |
| <a href="#document-api/fdtdx.ObjectContainer#fdtdx.ObjectContainer" class="reference internal" title="fdtdx.ObjectContainer"><span class="pre"><code class="sourceCode python">fdtdx.ObjectContainer</code></span></a>(object_list, \*\[, ...\]) | Container for managing simulation objects and their relationships. |
| <a href="#document-api/fdtdx.OnOffSwitch#fdtdx.OnOffSwitch" class="reference internal" title="fdtdx.OnOffSwitch"><span class="pre"><code class="sourceCode python">fdtdx.OnOffSwitch</code></span></a>(\*\[, start_time, ...\]) |  |
| <a href="#document-api/fdtdx.ParameterContainer#fdtdx.ParameterContainer" class="reference internal" title="fdtdx.ParameterContainer"><span class="pre"><code class="sourceCode python">fdtdx.ParameterContainer</code></span></a> | Type alias for parameter dictionaries. |
| <a href="#document-api/fdtdx.ParameterTransformation#fdtdx.ParameterTransformation" class="reference internal" title="fdtdx.ParameterTransformation"><span class="pre"><code class="sourceCode python">fdtdx.ParameterTransformation</code></span></a>() |  |
| <a href="#document-api/fdtdx.PerfectElectricConductor#fdtdx.PerfectElectricConductor" class="reference internal" title="fdtdx.PerfectElectricConductor"><span class="pre"><code class="sourceCode python">fdtdx.PerfectElectricConductor</code></span></a>(\*\[, ...\]) | Implements perfect electric conductor (PEC) boundary conditions. |
| <a href="#document-api/fdtdx.PerfectMagneticConductor#fdtdx.PerfectMagneticConductor" class="reference internal" title="fdtdx.PerfectMagneticConductor"><span class="pre"><code class="sourceCode python">fdtdx.PerfectMagneticConductor</code></span></a>(\*\[, ...\]) | Implements perfect magnetic conductor (PMC) boundary conditions. |
| <a href="#document-api/fdtdx.PerfectlyMatchedLayer#fdtdx.PerfectlyMatchedLayer" class="reference internal" title="fdtdx.PerfectlyMatchedLayer"><span class="pre"><code class="sourceCode python">fdtdx.PerfectlyMatchedLayer</code></span></a>(\*\[, ...\]) | Implements a Convolutional Perfectly Matched Layer (CPML) boundary condition. |
| <a href="#document-api/fdtdx.PeriodicBoundary#fdtdx.PeriodicBoundary" class="reference internal" title="fdtdx.PeriodicBoundary"><span class="pre"><code class="sourceCode python">fdtdx.PeriodicBoundary</code></span></a> | alias of <a href="#document-api/fdtdx.BlochBoundary#fdtdx.BlochBoundary" class="reference internal" title="fdtdx.objects.boundaries.bloch.BlochBoundary"><span class="pre"><code class="sourceCode python">BlochBoundary</code></span></a> |
| <a href="#document-api/fdtdx.PhasorDetector#fdtdx.PhasorDetector" class="reference internal" title="fdtdx.PhasorDetector"><span class="pre"><code class="sourceCode python">fdtdx.PhasorDetector</code></span></a>(\[\_signed_data, ...\]) | Detector for measuring frequency components of electromagnetic fields using an efficient Phasor Implementation. |
| <a href="#document-api/fdtdx.PhasorPoyntingFluxDetector#fdtdx.PhasorPoyntingFluxDetector" class="reference internal" title="fdtdx.PhasorPoyntingFluxDetector"><span class="pre"><code class="sourceCode python">fdtdx.PhasorPoyntingFluxDetector</code></span></a>(\[...\]) | Time-averaged Poynting flux through a single plane in the frequency domain. |
| <a href="#document-api/fdtdx.PillarDiscretization#fdtdx.PillarDiscretization" class="reference internal" title="fdtdx.PillarDiscretization"><span class="pre"><code class="sourceCode python">fdtdx.PillarDiscretization</code></span></a>(\*\[, axis, ...\]) | Constraint module for mapping pillar structures to allowed configurations. |
| <a href="#document-api/fdtdx.place_objects#fdtdx.place_objects" class="reference internal" title="fdtdx.place_objects"><span class="pre"><code class="sourceCode python">fdtdx.place_objects</code></span></a>(object_list, config, ...) | Places simulation objects according to specified constraints and initializes containers. |
| <a href="#document-api/fdtdx.plot_field_slice#fdtdx.plot_field_slice" class="reference internal" title="fdtdx.plot_field_slice"><span class="pre"><code class="sourceCode python">fdtdx.plot_field_slice</code></span></a>(E, H\[, filename, ...\]) | Creates a visualization of electromagnetic field components. |
| <a href="#document-api/fdtdx.plot_field_slice_component#fdtdx.plot_field_slice_component" class="reference internal" title="fdtdx.plot_field_slice_component"><span class="pre"><code class="sourceCode python">fdtdx.plot_field_slice_component</code></span></a>(field, ...) | Plots a single component of the electromagnetic field. |
| <a href="#document-api/fdtdx.plot_material#fdtdx.plot_material" class="reference internal" title="fdtdx.plot_material"><span class="pre"><code class="sourceCode python">fdtdx.plot_material</code></span></a>(config, arrays\[, ...\]) | Creates a visualization of material distribution showing slices in XY, XZ and YZ planes. |
| <a href="#document-api/fdtdx.plot_material_from_side#fdtdx.plot_material_from_side" class="reference internal" title="fdtdx.plot_material_from_side"><span class="pre"><code class="sourceCode python">fdtdx.plot_material_from_side</code></span></a>(config, ...\[, ...\]) | Creates a visualization of material distribution from a single viewing side. |
| <a href="#document-api/fdtdx.plot_setup#fdtdx.plot_setup" class="reference internal" title="fdtdx.plot_setup"><span class="pre"><code class="sourceCode python">fdtdx.plot_setup</code></span></a>(config, objects\[, ...\]) | Creates a visualization of the simulation setup showing objects in XY, XZ and YZ planes. |
| <a href="#document-api/fdtdx.plot_setup_from_side#fdtdx.plot_setup_from_side" class="reference internal" title="fdtdx.plot_setup_from_side"><span class="pre"><code class="sourceCode python">fdtdx.plot_setup_from_side</code></span></a>(config, objects, ...) | Creates a visualization of the simulation setup from a single viewing side. |
| <a href="#document-api/fdtdx.PointDipoleSource#fdtdx.PointDipoleSource" class="reference internal" title="fdtdx.PointDipoleSource"><span class="pre"><code class="sourceCode python">fdtdx.PointDipoleSource</code></span></a>(\[temporal_profile, ...\]) | Soft point dipole source (electric or magnetic). |
| <a href="#document-api/fdtdx.PointSymmetry2D#fdtdx.PointSymmetry2D" class="reference internal" title="fdtdx.PointSymmetry2D"><span class="pre"><code class="sourceCode python">fdtdx.PointSymmetry2D</code></span></a>() | Enforce 180-degree rotational (point) symmetry. |
| <a href="#document-api/fdtdx.PointSymmetry3D#fdtdx.PointSymmetry3D" class="reference internal" title="fdtdx.PointSymmetry3D"><span class="pre"><code class="sourceCode python">fdtdx.PointSymmetry3D</code></span></a>() | Enforce 180-degree rotational (point) symmetry in 3D. |
| <a href="#document-api/fdtdx.Pole#fdtdx.Pole" class="reference internal" title="fdtdx.Pole"><span class="pre"><code class="sourceCode python">fdtdx.Pole</code></span></a>() | Abstract base class for a single 2nd-order ADE pole. |
| <a href="#document-api/fdtdx.PortSpec#fdtdx.PortSpec" class="reference internal" title="fdtdx.PortSpec"><span class="pre"><code class="sourceCode python">fdtdx.PortSpec</code></span></a>(center, axis, direction, ...) | Specification for a simulation port (input source or output detector). |
| <a href="#document-api/fdtdx.PositionConstraint#fdtdx.PositionConstraint" class="reference internal" title="fdtdx.PositionConstraint"><span class="pre"><code class="sourceCode python">fdtdx.PositionConstraint</code></span></a>(\*, object, ...) | Defines a positional relationship between two simulation objects. |
| <a href="#document-api/fdtdx.PoyntingFluxDetector#fdtdx.PoyntingFluxDetector" class="reference internal" title="fdtdx.PoyntingFluxDetector"><span class="pre"><code class="sourceCode python">fdtdx.PoyntingFluxDetector</code></span></a>(\[\_signed_data, ...\]) | Detector for measuring Poynting flux in electromagnetic simulations. |
| <a href="#document-api/fdtdx.private_field#fdtdx.private_field" class="reference internal" title="fdtdx.private_field"><span class="pre"><code class="sourceCode python">fdtdx.private_field</code></span></a>(\*\[, default, init, ...\]) | Creates a field that sets the default to None and init to False. |
| <a href="#document-api/fdtdx.QuasiUniformGrid#fdtdx.QuasiUniformGrid" class="reference internal" title="fdtdx.QuasiUniformGrid"><span class="pre"><code class="sourceCode python">fdtdx.QuasiUniformGrid</code></span></a>(\*\[, dx, dy, dz, center\]) | Unresolved policy for a rectilinear grid with independent per-axis spacings. |
| <a href="#document-api/fdtdx.RealCoordinateConstraint#fdtdx.RealCoordinateConstraint" class="reference internal" title="fdtdx.RealCoordinateConstraint"><span class="pre"><code class="sourceCode python">fdtdx.RealCoordinateConstraint</code></span></a>(\*, object, ...) | Constrains an object's position to specific real-space coordinates. |
| <a href="#document-api/fdtdx.Recorder#fdtdx.Recorder" class="reference internal" title="fdtdx.Recorder"><span class="pre"><code class="sourceCode python">fdtdx.Recorder</code></span></a>(modules) | Records and compresses simulation data over time using a sequence of processing modules. |
| <a href="#document-api/fdtdx.RecordingState#fdtdx.RecordingState" class="reference internal" title="fdtdx.RecordingState"><span class="pre"><code class="sourceCode python">fdtdx.RecordingState</code></span></a>(data, state) | Container for simulation recording state data. |
| <a href="#document-api/fdtdx.RectilinearGrid#fdtdx.RectilinearGrid" class="reference internal" title="fdtdx.RectilinearGrid"><span class="pre"><code class="sourceCode python">fdtdx.RectilinearGrid</code></span></a>(\*\[, x_edges, y_edges, ...\]) | Realized rectilinear simulation grid described by physical cell edges. |
| <a href="#document-api/fdtdx.RemoveFloatingMaterial#fdtdx.RemoveFloatingMaterial" class="reference internal" title="fdtdx.RemoveFloatingMaterial"><span class="pre"><code class="sourceCode python">fdtdx.RemoveFloatingMaterial</code></span></a>(\*\[, ...\]) | Finds all material that floats in the air and sets their permittivity to air. |
| <a href="#document-api/fdtdx.resolve_object_constraints#fdtdx.resolve_object_constraints" class="reference internal" title="fdtdx.resolve_object_constraints"><span class="pre"><code class="sourceCode python">fdtdx.resolve_object_constraints</code></span></a>(objects, ...) | Resolve object constraints into grid slices and shapes. |
| <a href="#document-api/fdtdx.run_fdtd#fdtdx.run_fdtd" class="reference internal" title="fdtdx.run_fdtd"><span class="pre"><code class="sourceCode python">fdtdx.run_fdtd</code></span></a>(arrays, objects, config\[, ...\]) |  |
| <a href="#document-api/fdtdx.setup_sparams_simulation#fdtdx.setup_sparams_simulation" class="reference internal" title="fdtdx.setup_sparams_simulation"><span class="pre"><code class="sourceCode python">fdtdx.setup_sparams_simulation</code></span></a>(polygons, ...) | Set up an FDTD simulation scene for S-parameter extraction. |
| <a href="#document-api/fdtdx.SimulationConfig#fdtdx.SimulationConfig" class="reference internal" title="fdtdx.SimulationConfig"><span class="pre"><code class="sourceCode python">fdtdx.SimulationConfig</code></span></a>(\*\[, time, grid, ...\]) | Configuration settings for FDTD simulations. |
| <a href="#document-api/fdtdx.SimulationObject#fdtdx.SimulationObject" class="reference internal" title="fdtdx.SimulationObject"><span class="pre"><code class="sourceCode python">fdtdx.SimulationObject</code></span></a>(\*\[, ...\]) | Abstract base class for objects in a 3D simulation environment. |
| <a href="#document-api/fdtdx.SimulationState#fdtdx.SimulationState" class="reference internal" title="fdtdx.SimulationState"><span class="pre"><code class="sourceCode python">fdtdx.SimulationState</code></span></a> | a tuple of (time_step, ArrayContainer). |
| <a href="#document-api/fdtdx.SimulationVolume#fdtdx.SimulationVolume" class="reference internal" title="fdtdx.SimulationVolume"><span class="pre"><code class="sourceCode python">fdtdx.SimulationVolume</code></span></a>(\*\[, ...\]) | Background material for the entire simulation volume. |
| <a href="#document-api/fdtdx.SingleFrequencyProfile#fdtdx.SingleFrequencyProfile" class="reference internal" title="fdtdx.SingleFrequencyProfile"><span class="pre"><code class="sourceCode python">fdtdx.SingleFrequencyProfile</code></span></a>(\[...\]) | Simple sinusoidal temporal profile at a single frequency. |
| <a href="#document-api/fdtdx.SizeConstraint#fdtdx.SizeConstraint" class="reference internal" title="fdtdx.SizeConstraint"><span class="pre"><code class="sourceCode python">fdtdx.SizeConstraint</code></span></a>(\*, object, ...) | Defines a size relationship between two simulation objects. |
| <a href="#document-api/fdtdx.SizeExtensionConstraint#fdtdx.SizeExtensionConstraint" class="reference internal" title="fdtdx.SizeExtensionConstraint"><span class="pre"><code class="sourceCode python">fdtdx.SizeExtensionConstraint</code></span></a>(\*, object, ...) | Defines how an object extends toward another object or boundary. |
| <a href="#document-api/fdtdx.Sphere#fdtdx.Sphere" class="reference internal" title="fdtdx.Sphere"><span class="pre"><code class="sourceCode python">fdtdx.Sphere</code></span></a>(\*\[, partial_real_position, ...\]) | A sphere or ellipsoid object with configurable properties. |
| <a href="#document-api/fdtdx.StandardToCustomRange#fdtdx.StandardToCustomRange" class="reference internal" title="fdtdx.StandardToCustomRange"><span class="pre"><code class="sourceCode python">fdtdx.StandardToCustomRange</code></span></a>(\*\[, min_value, ...\]) | Maps standard \[0,1\] range to custom range \[min_value, max_value\]. |
| <a href="#document-api/fdtdx.StandardToInversePermittivityRange#fdtdx.StandardToInversePermittivityRange" class="reference internal" title="fdtdx.StandardToInversePermittivityRange"><span class="pre"><code class="sourceCode python">fdtdx.StandardToInversePermittivityRange</code></span></a>() | Maps standard \[0,1\] range to inverse permittivity range. |
| <a href="#document-api/fdtdx.StandardToPlusOneMinusOneRange#fdtdx.StandardToPlusOneMinusOneRange" class="reference internal" title="fdtdx.StandardToPlusOneMinusOneRange"><span class="pre"><code class="sourceCode python">fdtdx.StandardToPlusOneMinusOneRange</code></span></a>() | Maps standard \[0,1\] range to \[-1,1\] range. |
| <a href="#document-api/fdtdx.SubpixelSmoothedProjection#fdtdx.SubpixelSmoothedProjection" class="reference internal" title="fdtdx.SubpixelSmoothedProjection"><span class="pre"><code class="sourceCode python">fdtdx.SubpixelSmoothedProjection</code></span></a>(\*\[, ...\]) | This function is adapted from the Meep repository: <a href="https://github.com/NanoComp/meep/blob/master/python/adjoint/filters.py" class="github reference external">NanoComp/meep</a> |
| <a href="#document-api/fdtdx.TanhProjection#fdtdx.TanhProjection" class="reference internal" title="fdtdx.TanhProjection"><span class="pre"><code class="sourceCode python">fdtdx.TanhProjection</code></span></a>(\*\[, projection_midpoint\]) | Tanh projection filter. |
| <a href="#document-api/fdtdx.TemporalProfile#fdtdx.TemporalProfile" class="reference internal" title="fdtdx.TemporalProfile"><span class="pre"><code class="sourceCode python">fdtdx.TemporalProfile</code></span></a>() | Base class for temporal profiles of sources. |
| <a href="#document-api/fdtdx.TFSFPlaneSourceRegion#fdtdx.TFSFPlaneSourceRegion" class="reference internal" title="fdtdx.TFSFPlaneSourceRegion"><span class="pre"><code class="sourceCode python">fdtdx.TFSFPlaneSourceRegion</code></span></a>(\[...\]) | Total-Field/Scattered-Field (TFSF) *box* source. |
| <a href="#document-api/fdtdx.TreeClass#fdtdx.TreeClass" class="reference internal" title="fdtdx.TreeClass"><span class="pre"><code class="sourceCode python">fdtdx.TreeClass</code></span></a>(\*a, \*\*k) | Extended tree class with improved attribute setting functionality. |
| <a href="#document-api/fdtdx.unfold_array#fdtdx.unfold_array" class="reference internal" title="fdtdx.unfold_array"><span class="pre"><code class="sourceCode python">fdtdx.unfold_array</code></span></a>(arr, symmetry, spatial_axes) | Mirror-and-concatenate a spatial array along each symmetric axis. |
| <a href="#document-api/fdtdx.unfold_detector_states#fdtdx.unfold_detector_states" class="reference internal" title="fdtdx.unfold_detector_states"><span class="pre"><code class="sourceCode python">fdtdx.unfold_detector_states</code></span></a>(arrays, ...) | Reconstruct full-domain detector states from a symmetry-reduced simulation. |
| <a href="#document-api/fdtdx.unfold_fields#fdtdx.unfold_fields" class="reference internal" title="fdtdx.unfold_fields"><span class="pre"><code class="sourceCode python">fdtdx.unfold_fields</code></span></a>(field, symmetry, field_type) | Reconstruct a full-domain <span class="pre">`(3,`</span>` `<span class="pre">`Nx,`</span>` `<span class="pre">`Ny,`</span>` `<span class="pre">`Nz)`</span> field array from the reduced field. |
| <a href="#document-api/fdtdx.unfold_source_mode#fdtdx.unfold_source_mode" class="reference internal" title="fdtdx.unfold_source_mode"><span class="pre"><code class="sourceCode python">fdtdx.unfold_source_mode</code></span></a>(source, config) | Reconstruct the full-domain <span class="pre">`(E,`</span>` `<span class="pre">`H)`</span> mode profile a mode source injects. |
| <a href="#document-api/fdtdx.UniformGrid#fdtdx.UniformGrid" class="reference internal" title="fdtdx.UniformGrid"><span class="pre"><code class="sourceCode python">fdtdx.UniformGrid</code></span></a>(\*\[, spacing, center\]) | Unresolved policy for a uniform rectilinear grid. |
| <a href="#document-api/fdtdx.UniformMaterialObject#fdtdx.UniformMaterialObject" class="reference internal" title="fdtdx.UniformMaterialObject"><span class="pre"><code class="sourceCode python">fdtdx.UniformMaterialObject</code></span></a>(\*\[, ...\]) |  |
| <a href="#document-api/fdtdx.UniformPlaneSource#fdtdx.UniformPlaneSource" class="reference internal" title="fdtdx.UniformPlaneSource"><span class="pre"><code class="sourceCode python">fdtdx.UniformPlaneSource</code></span></a>(\[temporal_profile, ...\]) |  |
| <a href="#document-api/fdtdx.VerticalSymmetry2D#fdtdx.VerticalSymmetry2D" class="reference internal" title="fdtdx.VerticalSymmetry2D"><span class="pre"><code class="sourceCode python">fdtdx.VerticalSymmetry2D</code></span></a>() | Enforce vertical (y-axis) mirror symmetry. |
| <a href="#document-api/fdtdx.VerticalSymmetry3D#fdtdx.VerticalSymmetry3D" class="reference internal" title="fdtdx.VerticalSymmetry3D"><span class="pre"><code class="sourceCode python">fdtdx.VerticalSymmetry3D</code></span></a>() | Enforce vertical (z-axis) mirror symmetry in 3D. |
| <a href="#document-api/fdtdx.WaveCharacter#fdtdx.WaveCharacter" class="reference internal" title="fdtdx.WaveCharacter"><span class="pre"><code class="sourceCode python">fdtdx.WaveCharacter</code></span></a>(\*\[, phase_shift, ...\]) | Class describing a wavelength/period/frequency in free space. |
| <a href="#document-api/fdtdx.wavelength_to_period#fdtdx.wavelength_to_period" class="reference internal" title="fdtdx.wavelength_to_period"><span class="pre"><code class="sourceCode python">fdtdx.wavelength_to_period</code></span></a>(wavelength) | Convert wavelength to time period using speed of light. |
| <a href="#document-api/fdtdx.GDSLayerObject#fdtdx.GDSLayerObject" class="reference internal" title="fdtdx.GDSLayerObject"><span class="pre"><code class="sourceCode python">fdtdx.GDSLayerObject</code></span></a>(\*\[, ...\]) | A simulation object built from a set of GDS polygons extruded along one axis. |
| <a href="#document-api/fdtdx.GDSLayerSpec#fdtdx.GDSLayerSpec" class="reference internal" title="fdtdx.GDSLayerSpec"><span class="pre"><code class="sourceCode python">fdtdx.GDSLayerSpec</code></span></a>(gds_layer, material_name, ...) | Specification for a single GDS layer to be imported as a simulation object. |
| <a href="#document-api/fdtdx.GDSPortSpec#fdtdx.GDSPortSpec" class="reference internal" title="fdtdx.GDSPortSpec"><span class="pre"><code class="sourceCode python">fdtdx.GDSPortSpec</code></span></a>(gds_layer\[, gds_datatype, ...\]) | Specification for a GDS port marker layer used to auto-generate sources or detectors. |
| <a href="#document-api/fdtdx.detectors_from_gds_ports#fdtdx.detectors_from_gds_ports" class="reference internal" title="fdtdx.detectors_from_gds_ports"><span class="pre"><code class="sourceCode python">fdtdx.detectors_from_gds_ports</code></span></a>(gds_source, ...) | Create <a href="#document-api/fdtdx.ModeOverlapDetector#fdtdx.ModeOverlapDetector" class="reference internal" title="fdtdx.objects.detectors.mode.ModeOverlapDetector"><span class="pre"><code class="sourceCode python">ModeOverlapDetector</code></span></a> objects from GDS port markers. |
| <a href="#document-api/fdtdx.gds_layer_stack#fdtdx.gds_layer_stack" class="reference internal" title="fdtdx.gds_layer_stack"><span class="pre"><code class="sourceCode python">fdtdx.gds_layer_stack</code></span></a>(gds_source, cell_name, ...) | Build simulation objects from a GDS file according to a layer stack specification. |
| <a href="#document-api/fdtdx.gds_layer_stack_from_component#fdtdx.gds_layer_stack_from_component" class="reference internal" title="fdtdx.gds_layer_stack_from_component"><span class="pre"><code class="sourceCode python">fdtdx.gds_layer_stack_from_component</code></span></a>(...\[, ...\]) | Build a layer stack from a gdsfactory <span class="pre">`Component`</span>. |
| <a href="#document-api/fdtdx.sources_from_gds_ports#fdtdx.sources_from_gds_ports" class="reference internal" title="fdtdx.sources_from_gds_ports"><span class="pre"><code class="sourceCode python">fdtdx.sources_from_gds_ports</code></span></a>(gds_source, ...) | Create <a href="#document-api/fdtdx.ModePlaneSource#fdtdx.ModePlaneSource" class="reference internal" title="fdtdx.objects.sources.mode.ModePlaneSource"><span class="pre"><code class="sourceCode python">ModePlaneSource</code></span></a> objects from GDS port markers. |

</div>

</div>

</div>

</div>

</div>
