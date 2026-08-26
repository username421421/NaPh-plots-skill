<div id="fdtdx-frozen-field" class="section">

# fdtdx.frozen_field<a href="#fdtdx-frozen-field" class="headerlink" title="Link to this heading">#</a>

<span class="sig-prename descclassname"><span class="pre">fdtdx.</span></span><span class="sig-name descname"><span class="pre">frozen_field</span></span><span class="sig-paren">(</span>*<span class="keyword-only-separator o"><span class="abbr" title="Keyword-only parameters separator (PEP 3102)"><span class="pre">\*</span></span></span>*, *<span class="n"><span class="pre">default</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">null</span></span>*, *<span class="n"><span class="pre">init</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">repr</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span>*, *<span class="n"><span class="pre">kind</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'KW_ONLY'</span></span>*, *<span class="n"><span class="pre">metadata</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*, *<span class="n"><span class="pre">on_setattr</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">on_getattr</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">()</span></span>*, *<span class="n"><span class="pre">alias</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span>*<span class="sig-paren">)</span><a href="../_modules/fdtdx/core/jax/pytrees.html#frozen_field" class="reference internal"><span class="viewcode-link"><span class="pre">[source]</span></span></a><a href="#fdtdx.frozen_field" class="headerlink" title="Link to this definition">#</a>  
Creates a field that automatically freezes on set and unfreezes on get.

This field behaves like a regular pytreeclass field but ensures values are frozen when stored and unfrozen when accessed.

Parameters<span class="colon">:</span>  
- **default** (*Any,* *optional*) – The default value for the field. Defaults to None.

- **init** (*bool,* *optional*) – Whether to include the field in \_\_init\_\_. Defaults to True.

- **repr** (*bool,* *optional*) – Whether to include the field in \_\_repr\_\_. Defaults to True.

- **kind** (*ArgKindType,* *optional*) – The argument kind (POS_ONLY, POS_OR_KW, etc.). Defaults to KW_ONLY.

- **metadata** (*dict\[str,* *Any\]* *\|* *None,* *optional*) – Additional metadata for the field. Defaults to None.

- **on_setattr** (*Sequence\[Any\],* *optional*) – Additional setattr callbacks (applied after freezing). Defaults to no callbacks.

- **on_getattr** (*Sequence\[Any\],* *optional*) – Additional getattr callbacks (applied after unfreezing). Defaults to no callbacks.

- **alias** (*str* *\|* *None,* *optional*) – Alternative name for the field in \_\_init\_\_. Defaults to None

Returns<span class="colon">:</span>  
A Field instance configured with freeze/unfreeze behavior

Return type<span class="colon">:</span>  
Any

</div>
