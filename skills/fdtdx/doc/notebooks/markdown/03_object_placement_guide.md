# Object Placement Guide

This guide explains how to position objects in a simulation scene in FDTDX. The basic workflow looks like this: 1. Define a Simulation volume 2. Define objects and sizing/placement constraints between objects 3. Compute the actual position of objects in the simulation scene by using the place_objects function 4. Optional, but recommend: Plot the simulation scene using plot_setup() 5. Run a simulation


```python
import fdtdx
import jax
```


```python
%matplotlib inline
```

## Basic Positioning

In FDTDX, objects are positioned either directly or relation to other objects through constraints.

The first step should always be to define the size of the simulation volume. FDTDX always uses metrical units, i.e. meters or grid positions referring to the Yee-grid, which depends on the resolution used.


```python
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
```


```python
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
```

Now, we can start to position some objects in the simulation scene. We start with a substrate at the bottom of simulation. To this end, we specify a constraint that aligns the objects in the z-axis (axis 2). The user should specify these constraints and collect them in a list.

Positional constraints define an anchor point for both objects, which are constrainted to be at the same position. The position of the anchor point can be specified in a relative coordinate system of each object. A relative coordinate system means that a position of -1 would place the anchor at the left boundary of the object, a position of 0 at the middle and a position of 1 at the right boundary.

In case of the substrate, we want the lower boundary of the substrate to be aligned with the lower boundary of the simulation volume. This ensures that the substrate is placed exactly at the bottom of the simulation. The margins and grid_margins arguments are optional and would allow to speficy a fixed distance between the anchor points. The margins argument is in units of meters, the grid margins in units of yee-grid cells.


```python
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
```

There exist a number of useful shorthands for rapid placements. Some of them are listed below that place a cube in the scene. The name and colors argument are only used for plotting.


```python
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
```

## Size Configuration

Object sizes can be specified in a number of ways. Firstly, one can directly set the size of an object in the init method. This can either be a specified in Yee-grid cells or metrical units (meter).


```python
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
```

## Size in grid units


```python
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
```

## Combination of grid and metrical units


```python
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
```

## Undefined Sizes can be useful

If the size of an object is only partially defined and does not have any constraints, the size is set to the size of the simulation volume in the respective axis. We actually already used this behavior to define the substrate above.


```python
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
```

Using this specification for the cube1, we get the following error:

Exception: Inconsisten grid shape (may be due to extension to infinity) at lower bound: 0 != 6 for axis=2, cube (<class 'fdtdx.objects.material.UniformMaterialObject'>). Object has a position constraint that puts the lower boundary at 6, but the lower bound was alreay computed to be at 0. This could be due to a missing size constraint/specification, which resulted in an expansion of the object to the simulation boundary (default size) or another constraint on this object.

The error occurs, because we tried to place the cube above the substrate, which is no longer possible if the z-size of the cube is the whole simulation size. When we remove the problematic placement constraint, we get the correct simulation scene.


```python
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
```

## Relative Sizing constraint

The size of an object can also be set in relation to another object. To demonstrate this, we define a second cube, which should be placed above the substrate and have a 200nm distance to the other cube in the x-axis.


```python
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
```

Now let's change the size definition of the second cube to a relative size constraint, which defines the y-size of the second cube as the size of the first cube in the z-axis.


```python
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
```

Another useful convenience wrapper is the following:


```python
object1.same_size(object2, axes=(0,1))
```

## Extending objects to other objects or Simulation boundaries

The last method to set the size of an object is to constrain the size, such that it extends up to another object in the simulation scene.


```python
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
```

This constrains the size of cube2 such that its upper boundary ("+") extends directly up to cube1 in the x-axis.

See the Objects API Reference for complete details on all positioning and sizing options.
