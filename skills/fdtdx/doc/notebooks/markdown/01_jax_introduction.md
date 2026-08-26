# Introduction to JAX

JAX is a high-performance numerical computing library developed by Google that brings together the familiar NumPy API with powerful features like automatic differentiation, just-in-time (JIT) compilation, and seamless GPU/TPU acceleration. Originally designed for machine learning research, JAX has become popular across scientific computing applications due to its speed and flexibility.

Jax itself provides a good introduction <a href="https://docs.jax.dev/en/latest/tutorials.html">here</a> and <a href="https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html">here</a>. Otherwise, the following is a small crash course.


```python
import jax
import jax.numpy as jnp
import fdtdx
```

## Functional Programming Paradigm

JAX operates exclusively in a functional programming style, which means it requires you to write pure functions without side effects. This functional approach has several important implications:

### Immutable data

Arrays and other data structures are treated as immutable. Operations create new objects rather than modifying existing ones, similar to how NumPy handles broadcasting operations.

This functional constraint enables JAX's powerful transformations like jit (compilation), grad (automatic differentiation), vmap (vectorization), and pmap (parallelization). While the functional style requires some adjustment if you're used to imperative programming, it unlocks JAX's ability to automatically optimize and transform your numerical code in ways that would be impossible with stateful operations.

JAX functions cannot modify variables in-place or maintain internal state. Instead of operations like array[0] = 5, you must use functional equivalents like array.at[0].set(5) that return new arrays.


```python

# This won't work in JAX
def bad_function(x):
    x[0] = x[0] + 1  # In-place modification
    return x

# This is the JAX way
def good_function(x):
    return x.at[0].add(1)  # Returns new array

print(good_function(jnp.asarray([4.0])))
print(bad_function(jnp.asarray([4.0])))
```

### No Side Effects (pure functions)

Functions should not print to console, write to files, or modify global variables during compilation. JAX's Just-in-Time (JIT) compiler optimizes based on the assumption that functions are deterministic and side-effect free. As a consequence print statements are only executed during compilation (the first function call), but not afterwards.


```python
def example_function():
    x = jnp.ones((4,))
    print(x)

jitted_fn = jax.jit(example_function)

jitted_fn() # this will print traced value of x
jitted_fn() # this executes compiled function does not print anything
```

### Static Shapes during computation

All Jax arrays need to have a static shape in compiled functions (as long as the input shape does not change). This means that there is a distinction between static and dynamic data. Static data (like python scalars) do not change when called with different input values. This static data can be used in if-clauses, or alter the shape of jax arrays. Dynamic data are jax arrays with possibly arbitrary values. This dynamic data cannot be used in if-clauses or to change the shapes of other jax arrays. As a rule of thumb, the computational graph of a function can only change based on static arrays, but not jax arrays.



```python
def if_clause(x):
    return 1.0 if x else 2.0  # computational graph changes depending on the value of x

print(jax.jit(if_clause)(jnp.asarray(True)))
```


```python
def indexing_fn(x):
    return jnp.asarray([4.0, 2.0, 1.0, 3.0])[:x]  # depending on value of x different array shape is returned

print(jax.jit(indexing_fn)(jnp.asarray(1)))
```

## TreeClass Objects in FDTDX

FDTDX leverages JAX's functional programming paradigm through a specialized TreeClass system that makes it easy to work with complex hierarchical data structures while maintaining JAX compatibility. The TreeClass provides a clean, object-oriented interface that automatically integrates with JAX's pytree system, allowing for seamless use with JAX transformations.

### TreeClass Structure

The TreeClass system uses dataclass-like syntax with the @fdtdx.autoinit decorator to automatically generate initialization methods. Here's how it works:


```python
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
```

These classes can be nested arbitrarily deep and contain lists, dictionaries, or other complex data structures. The @fdtdx.autoinit decorator automatically generates init methods that handle default values and type checking.

### Working with TreeClass Instances


```python
# Create instances with default or custom values
b = B(a1=A())  # Uses defaults: A(a=2, x=5), z=7
print(b)
b = b.aset("z", 25)  # Functional update
print(b)


```


```python
# Collections of TreeClass instances
b2 = B(a1=A(a=10, x=11), z=12)
b3 = B(a1=A(a=20, x=21), z=22)
c = C(b_list=[b, b2])
print(c)

# Deep nested updates using path syntax
c2 = c.aset("b_list->[0]->a1->a", 100)
print(c2)
```

### The aset Method: Functional Updates Made Easy

The aset method is the cornerstone of FDTDX's functional approach. Unlike JAX's standard .at[].set() which only works on pytree leaf nodes (typically arrays), aset can update any attribute at any level of nesting within a TreeClass hierarchy.

### Path Syntax: The method uses an intuitive string-based path syntax to navigate nested structures:

- "attribute" - Direct attribute access
- "a->b" - Nested attribute access (a.b)
- "a->[0]" - List indexing
- "a->['key']" - Dictionary key access
- "b_list->[0]->a1->a" - Complex nested path
- 
In the example c2 = c.aset("b_list->[0]->a1->a", 100), this path means: - Access the b_list attribute of c - Get the first element [0] of that list - Access the a1 attribute of that element - Access the a attribute of a1 - Set that value to 100

The method returns a completely new instance with the updated value, maintaining JAX's functional programming requirements. This allows FDTDX data structures to be used seamlessly with JAX transformations like jit, grad, and vmap, while providing a much more intuitive interface than manually reconstructing nested data structures. This approach bridges the gap between JAX's powerful functional capabilities and the practical need for complex, hierarchical data management in scientific computing applications.

## How JAX is used in FDTDX

For a full example on how to use JAX with fdtdx, check out this <a href= "https://github.com/ymahlau/fdtdx/blob/main/examples/simulate_gaussian_source.py">example</a> or this <a href= https://github.com/ymahlau/fdtdx/blob/main/examples/optimize_ceviche_corner.py>example</a>. The script demonstrates FDTDX's seamless integration with JAX's jit transformation. The core simulation function sim_fn takes FDTDX TreeClass structures as arguments and is JIT-compiled:

```python
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
```

### JIT compilation with TreeClass arguments

Key Features:

- TreeClass Compatibility: The ParameterContainer and ArrayContainer are FDTDX TreeClass structures that work seamlessly with jit. JAX automatically handles the pytree registration, allowing these complex nested structures to be compiled efficiently.
- Memory Optimization: The donate_argnames=["arrays"] parameter tells JAX it can reuse the memory of the arrays argument, which is crucial for large electromagnetic field arrays in FDTD simulations.
- Compilation Pipeline: The script uses .lower().compile() to explicitly control the compilation process, providing timing information for performance analysis.
  
While this specific example focuses on forward simulation, FDTDX is designed for gradient-based optimization. The GradientConfig setup shows how gradients would be computed:

```python
gradient_config = fdtdx.GradientConfig(
    recorder=fdtdx.Recorder(
        modules=[fdtdx.DtypeConversion(dtype=jnp.bfloat16)]
    )
)
```

For gradient computation, you would typically use:
```python
# Hypothetical gradient computation
grad_fn = jax.grad(sim_fn, argnums=0)  # Gradient w.r.t. params
gradients = grad_fn(params, arrays, key)
```
