<div id="fdtdx-color" class="section">

# fdtdx.Color<a href="#fdtdx-color" class="headerlink" title="Link to this heading">#</a>

*<span class="k"><span class="pre">class</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">Color</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">r</span></span>*, *<span class="n"><span class="pre">g</span></span>*, *<span class="n"><span class="pre">b</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color" class="headerlink" title="Link to this definition">#</a>  
Bases: <a href="fdtdx.TreeClass.html#fdtdx.TreeClass" class="reference internal" title="fdtdx.core.jax.pytrees.TreeClass"><span class="pre"><code class="sourceCode python">TreeClass</code></span></a>

Color representation with multiple format support.

The class contains colors which are from the XKCD color survey: <a href="https://xkcd.com/color/rgb.txt" class="reference external">https://xkcd.com/color/rgb.txt</a> and fdtdx implements most of them.

This class represents a color and provides methods to convert between different color formats. Internally, colors are stored as normalized RGB values in the range \[0, 1\].

<div id="quick-reference" class="section">

## Quick Reference<a href="#quick-reference" class="headerlink" title="Link to this heading">#</a>

Attributes

- <a href="#fdtdx.Color.b" class="reference internal" title="fdtdx.Color.b"><span class="pre"><code class="sourceCode python">b</code></span></a>

- <a href="#fdtdx.Color.g" class="reference internal" title="fdtdx.Color.g"><span class="pre"><code class="sourceCode python">g</code></span></a>

- <a href="#fdtdx.Color.r" class="reference internal" title="fdtdx.Color.r"><span class="pre"><code class="sourceCode python">r</code></span></a>

Methods

- <a href="#fdtdx.Color.aset" class="reference internal" title="fdtdx.Color.aset"><span class="pre"><code class="sourceCode python">aset</code></span></a>

- <a href="#fdtdx.Color.from_hex" class="reference internal" title="fdtdx.Color.from_hex"><span class="pre"><code class="sourceCode python">from_hex</code></span></a>

- <a href="#fdtdx.Color.from_rgb" class="reference internal" title="fdtdx.Color.from_rgb"><span class="pre"><code class="sourceCode python">from_rgb</code></span></a>

- <a href="#fdtdx.Color.get_class_fields" class="reference internal" title="fdtdx.Color.get_class_fields"><span class="pre"><code class="sourceCode python">get_class_fields</code></span></a>

- <a href="#fdtdx.Color.get_public_fields" class="reference internal" title="fdtdx.Color.get_public_fields"><span class="pre"><code class="sourceCode python">get_public_fields</code></span></a>

- <a href="#fdtdx.Color.to_hex" class="reference internal" title="fdtdx.Color.to_hex"><span class="pre"><code class="sourceCode python">to_hex</code></span></a>

- <a href="#fdtdx.Color.to_mpl" class="reference internal" title="fdtdx.Color.to_mpl"><span class="pre"><code class="sourceCode python">to_mpl</code></span></a>

- <a href="#fdtdx.Color.to_rgb_255" class="reference internal" title="fdtdx.Color.to_rgb_255"><span class="pre"><code class="sourceCode python">to_rgb_255</code></span></a>

- <a href="#fdtdx.Color.to_rgb_normalized" class="reference internal" title="fdtdx.Color.to_rgb_normalized"><span class="pre"><code class="sourceCode python">to_rgb_normalized</code></span></a>

</div>

</div>

<div id="attributes" class="section">

# Attributes<a href="#attributes" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">b</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.Color.b" class="headerlink" title="Link to this definition">#</a>  
Blue component, normalized to \[0, 1\]

Type<span class="colon">:</span>  
b (float)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">g</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.Color.g" class="headerlink" title="Link to this definition">#</a>  
Green component, normalized to \[0, 1\]

Type<span class="colon">:</span>  
g (float)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">r</span></span>*<span class="p"><span class="pre">:</span></span><span class="w"> </span><span class="pre">`float`</span>*<a href="#fdtdx.Color.r" class="headerlink" title="Link to this definition">#</a>  
Red component, normalized to \[0, 1\]

Type<span class="colon">:</span>  
r (float)

</div>

<div id="methods" class="section">

# Methods<a href="#methods" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">aset</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">attr_name</span></span>*, *<span class="n"><span class="pre">val</span></span>*, *<span class="n"><span class="pre">create_new_ok</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span>*<span class="sig-paren">)</span><a href="#fdtdx.Color.aset" class="headerlink" title="Link to this definition">#</a>  
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

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">from_hex</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">hex_string</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.from_hex" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.from_hex" class="headerlink" title="Link to this definition">#</a>  
Create a Color from a hexadecimal color string.

Parameters<span class="colon">:</span>  
**hex_string** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>) – Hex color string (e.g., “#FF0000”, “FF0000”, “#F00”)

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="#fdtdx.Color" class="reference internal" title="fdtdx.colors.Color"><span class="pre"><code class="sourceCode python">Color</code></span></a></span>

Returns<span class="colon">:</span>  
Color instance

Raises<span class="colon">:</span>  
**ValueError** – If hex string is invalid

<!-- -->

*<span class="k"><span class="pre">classmethod</span></span><span class="w"> </span>*<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">from_rgb</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">r</span></span>*, *<span class="n"><span class="pre">g</span></span>*, *<span class="n"><span class="pre">b</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.from_rgb" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.from_rgb" class="headerlink" title="Link to this definition">#</a>  
Create a Color from 8-bit RGB values (0-255).

Parameters<span class="colon">:</span>  
- **r** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Red component (0-255)

- **g** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Green component (0-255)

- **b** (<span class="sphinx_autodoc_typehints-type"><span class="pre">`int`</span></span>) – Blue component (0-255)

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><a href="#fdtdx.Color" class="reference internal" title="fdtdx.colors.Color"><span class="pre"><code class="sourceCode python">Color</code></span></a></span>

Returns<span class="colon">:</span>  
Color instance

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">get_class_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Color.get_class_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">get_public_fields</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="#fdtdx.Color.get_public_fields" class="headerlink" title="Link to this definition">#</a>  
Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`list`</span>\[<span class="pre">`TreeClassField`</span>\]</span>

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">to_hex</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.to_hex" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.to_hex" class="headerlink" title="Link to this definition">#</a>  
Return color as hexadecimal string.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`str`</span></span>

Returns<span class="colon">:</span>  
Hex color string with leading \# (e.g., “#FF0000”)

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">to_mpl</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.to_mpl" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.to_mpl" class="headerlink" title="Link to this definition">#</a>  
Return color in matplotlib-compatible format.

This is an alias for to_rgb_normalized() for clarity when using with matplotlib.

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>

Returns<span class="colon">:</span>  
Tuple of (r, g, b) with values in \[0, 1\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">to_rgb_255</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.to_rgb_255" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.to_rgb_255" class="headerlink" title="Link to this definition">#</a>  
Return color as 8-bit RGB tuple (0-255).

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`int`</span>, <span class="pre">`int`</span>, <span class="pre">`int`</span>\]</span>

Returns<span class="colon">:</span>  
Tuple of (r, g, b) with integer values in \[0, 255\]

<!-- -->

<span class="sig-prename descclassname"><span class="pre">Color.</span></span><span class="sig-name descname"><span class="pre">to_rgb_normalized</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a href="../_modules/fdtdx/colors.html#Color.to_rgb_normalized" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.Color.to_rgb_normalized" class="headerlink" title="Link to this definition">#</a>  
Return color as normalized RGB tuple \[0, 1\].

Return type<span class="colon">:</span>  
<span class="sphinx_autodoc_typehints-type"><span class="pre">`tuple`</span>\[<span class="pre">`float`</span>, <span class="pre">`float`</span>, <span class="pre">`float`</span>\]</span>

Returns<span class="colon">:</span>  
Tuple of (r, g, b) with values in \[0, 1\]

If you find any errors in the documentation, please report them in the <a href="https://github.com/ymahlau/fdtdx/issues" class="reference external">Github Issues</a>!

</div>
