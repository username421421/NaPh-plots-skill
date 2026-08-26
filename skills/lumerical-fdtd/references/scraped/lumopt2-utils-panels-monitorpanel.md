# MonitorPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#monitorpanel)

Source URL: https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html  
Area: Discovered official source  
Topic: Discovered from lumopt2 API reference  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `MonitorPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#monitorpanel)` for the topic `Discovered from lumopt2 API reference`. It captured 1 heading(s), 24 link(s), 0 code block(s), 73 inline code term(s), and 2 table(s). Main headings: MonitorPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#monitorpanel). Key detected terms: dataset, far, far-field, fdtd, lumopt, mode, monitor, optimization, port, s-parameter, transmission.

## Key Terms

- dataset
- far
- far-field
- fdtd
- lumopt
- mode
- monitor
- optimization
- port
- s-parameter
- transmission

## Captured Headings

- MonitorPanel [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#monitorpanel)

## Official Text Excerpt

> MonitorPanel # class lumopt2.utils.panels. MonitorPanel (title: str|None = None, monitor_name: str = '', result_name: str = '', wavelength: float|None = None, frequency: float|None = None, operation: Literal ['real', 'imag', 'abs', 'abs^2', 'angle'] = 'abs', cmap: str|None = None, axes_kwargs: Dict [str, Any]|None = None, image_kwargs: Dict [str, Any]|None = None, line_kwargs: Dict [str, Any]|None = None) # Live plot of an FDTD monitor result (field component, S-parameter, …). Auto-detects the result dimensionality and renders a 2D image, a 1D line plot, or a single scalar marker. For 2D images the panel reuses the same`matplotlib.image.AxesImage`and colorbar across iterations so updates are cheap. Attributes: monitor_name``str Name of the monitor in the FDTD project (e.g.`'optimization_dft'`,`'FDTD::ports::port_h_out'`). result_name``str Result field to fetch. Recognised forms: - `'Ex'`/`'Ey'`/`'Ez'`/`'Hx'`/`'Hy'`/`'Hz'`- one Cartesian component of the E/H field (the panel fetches the full vector via`getresult(mon, 'E')`/`getresult(mon, 'H')`and slices along the last axis). - `'E'`/`'H'`- the magnitude of the full field vector. - `'T'`/`'transmission'`- the bulk power transmission, i.e. the integrated Poynting flux through the monitor surface (sums every guided mode plus any radiation that hits the monitor). - `'T_out'`- the ...

## Code Block Inventory

- No code blocks detected

## Inline Code Inventory

- `'<key>.<attr>'`
- `'E'`
- `'E.Ey'`
- `'Ex'`
- `'Ey'`
- `'Ez'`
- `'FDTD::ports::port_h_out'`
- `'H'`
- `'Hx'`
- `'Hy'`
- `'Hz'`
- `'RdBu'`
- `'T'`
- `'T_out'`
- `'abs'`
- `'abs^2'`
- `'angle'`
- `'farfield.Ex'`
- `'imag'`
- `'inferno'`
- `'optimization_dft'`
- `'real'`
- `'transmission'`
- `'twilight'`
- `AttributeError`
- `Axes`
- `Axes.set_<name>`
- `MonitorPanel.axes_kwargs`
- `MonitorPanel.cmap`
- `MonitorPanel.frequency`
- `MonitorPanel.image_kwargs`
- `MonitorPanel.line_kwargs`
- `MonitorPanel.monitor_name`
- `MonitorPanel.on_optimization_end`
- `MonitorPanel.operation`
- `MonitorPanel.requires_forward_results`
- `MonitorPanel.result_name`
- `MonitorPanel.setup`
- `MonitorPanel.title`
- `MonitorPanel.update`
- `MonitorPanel.wavelength`
- `None`
- `PortResults`
- `attr`
- `ax.set(**axes_kwargs)`
- `c0/f`
- `clim`
- `cmap`
- `dict`
- `float`
- `frequency`
- `getresult`
- `getresult(mon, 'E')`
- `getresult(mon, 'H')`
- `getresult(monitor, key)`
- `getresult(port, 'expansion for port monitor')`
- `image.set(**image_kwargs)`
- `key`
- `line.set(**line_kwargs)`
- `matplotlib.image.AxesImage`
- `monitor_name`
- `np.abs`
- `operation`
- `operation='abs'`
- `optional`
- `result_name`
- `str`
- `{'clim': (-1, 1)}`
- `{'cmap': 'viridis'}`
- `{'color': 'red', 'linewidth': 2}`
- `{'xlabel': 'Wavelength (nm)'}`
- `{'ylim': (0, 1)}`
- `{'yscale': 'log'}`

## Table Inventory

- Table 1: 2 column(s), 3 row(s)
  - First row sample: MonitorPanel.on_optimization_end (ax, fig, ...) | Optional hook called once when the optimization completes.
- Table 2: 2 column(s), 11 row(s)
  - First row sample: MonitorPanel.axes_kwargs | 

## Official Links Found

- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#monitorpanel)
- [#](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.html#lumopt2.utils.panels.MonitorPanel)
- [PortResults](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.fom.simulation_results.PortResults.html#lumopt2.fom.simulation_results.PortResults)
- [MonitorPanel.on_optimization_end](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.on_optimization_end.html#lumopt2.utils.panels.MonitorPanel.on_optimization_end)
- [MonitorPanel.setup](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.setup.html#lumopt2.utils.panels.MonitorPanel.setup)
- [MonitorPanel.update](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.update.html#lumopt2.utils.panels.MonitorPanel.update)
- [MonitorPanel.axes_kwargs](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.axes_kwargs.html#lumopt2.utils.panels.MonitorPanel.axes_kwargs)
- [MonitorPanel.cmap](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.cmap.html#lumopt2.utils.panels.MonitorPanel.cmap)
- [MonitorPanel.frequency](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.frequency.html#lumopt2.utils.panels.MonitorPanel.frequency)
- [MonitorPanel.image_kwargs](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.image_kwargs.html#lumopt2.utils.panels.MonitorPanel.image_kwargs)
- [MonitorPanel.line_kwargs](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.line_kwargs.html#lumopt2.utils.panels.MonitorPanel.line_kwargs)
- [MonitorPanel.monitor_name](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.monitor_name.html#lumopt2.utils.panels.MonitorPanel.monitor_name)
- [MonitorPanel.operation](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.operation.html#lumopt2.utils.panels.MonitorPanel.operation)
- [MonitorPanel.requires_forward_results](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.requires_forward_results.html#lumopt2.utils.panels.MonitorPanel.requires_forward_results)
- [MonitorPanel.result_name](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.result_name.html#lumopt2.utils.panels.MonitorPanel.result_name)
- [MonitorPanel.title](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.title.html#lumopt2.utils.panels.MonitorPanel.title)
- [MonitorPanel.wavelength](https://lumerical.docs.pyansys.com/version/stable/api/lumopt2/_autosummary/lumopt2.utils.panels.MonitorPanel.wavelength.html#lumopt2.utils.panels.MonitorPanel.wavelength)

## Ansys-Related External Links Found

- None

## External Links Found

- [str](https://docs.python.org/3/library/stdtypes.html#str)
- [None](https://docs.python.org/3/library/constants.html#None)
- [float](https://docs.python.org/3/library/functions.html#float)
- [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)
- [Dict](https://docs.python.org/3/library/typing.html#typing.Dict)
- [Any](https://docs.python.org/3/library/typing.html#typing.Any)
- [dict](https://docs.python.org/3/library/stdtypes.html#dict)
