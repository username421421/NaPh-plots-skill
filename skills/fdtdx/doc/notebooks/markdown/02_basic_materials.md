# Basic Materials and Objects

In FDTDX, simulation objects can have a material, which defines the permittivity, permeability and conductivity of the object.

Currently neither dispersion nor non-linear materials are implemented. The implementation of dispersion is scheduled in the near-mid future and afterwards an implementation of non-linear materials will follow.



```python
import fdtdx
```


```python
material = fdtdx.Material()
print(material)
```

The default material above with no parameters represents free space with a relative permittivity and permeability of 1. These values can be freely set by a user.


```python
material2 = fdtdx.Material(permittivity=2.5, permeability=1.7)
print(material2)
```

## fdtdx.UniformMaterial

The most basic and also probably most useful object is the UniformMaterialObject. As the name suggests, it has a single material. Importantly, every object in FDTDX needs to have a unique name! If no name is provided, then some name is chosen programmatically.


```python
uniform_obj = fdtdx.UniformMaterialObject(
    partial_real_shape=(0.6e-6, 0.6e-6, 0.6e-6),  # size of the object in meters
    material=material,  # material
    name="Uniform Material",  # name of the object, optional
)
print(uniform_obj)
```

There also exist Objects with more elaborate material distributions, but for the quickstart we will only cover this most basic material.
