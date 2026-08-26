# Getting Started with lumopt - Python API

Source URL: https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API  
Area: Discovered official source  
Topic: Discovered from Units and normalization conventions  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Getting Started with lumopt - Python API` for the topic `Discovered from Units and normalization conventions`. It captured 14 heading(s), 22 link(s), 14 code block(s), 0 inline code term(s), and 2 table(s). Main headings: Getting Started with lumopt - Python API, Install, Project Init, Base Simulation, Required Objects, Set-up Classes, Wavelengths, ModeMatch. Key detected terms: command, convergence, fdtd, gaussian, geometry, grating, import, lumapi, lumopt, mesh, mode, monitor, optimization, plane, port, python.

## Key Terms

- command
- convergence
- fdtd
- gaussian
- geometry
- grating
- import
- lumapi
- lumopt
- mesh
- mode
- monitor
- optimization
- plane
- port
- python
- python-api
- script
- solver
- source
- transmission

## Captured Headings

- Getting Started with lumopt - Python API
- Install
- Project Init
- Base Simulation
- Required Objects
- Set-up Classes
- Wavelengths
- ModeMatch
- PortTransmission
- IntensityVolume
- Optimization Classes
- ScipyOptimizer
- Optimization
- Superoptimization

## Official Text Excerpt

> Getting Started with lumopt - Python API Inverse design using lumopt can be run from the CAD script editor, the command line or any python IDE. In the first sub-section, we will briefly describe how to import the lumopt and lumapi modules; although an experienced python user can likely skip this part. As a starting point, it is recommended to run the AppGallery examples and use these as templates for your own project. It may be helpful following along with these files as you read this page or you may simply reference this page when running the examples later. In the Project Init section, we outline the project inputs and necessary simulation objects that should be included. Important lumopt specific considerations are highlighted; however, a valid simulation set-up is imperative, so convergence testing should be considered a pre-requisite. Next important lumopt set-up classes, that should be updated to reflect your specifications are documented. Finally, a description of the scipy optimizer and lumopt optimization classes are presented. Shape and topology optimization primarily differ in how they handle the optimizable geometry which ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `base_sim = os.path.join(os.path.dirname(__file__), 'grating_base.fsp')`
- Code block 2: 2 line(s); first line `from lumopt.utilities.load_lumerical_scripts import load_from_lsf`
- Code block 3: 3 line(s); first line `sys.path.append(os.path.dirname(__file__))  #Add current directory to Python path`
- Code block 4: 4 line(s); first line `from lumopt.utilities.wavelengths import Wavelengths`
- Code block 5: 1 line(s); first line `wavelengths = Wavelengths(start = 1260e-9, stop = 1360e-9, points = 11)`
- Code block 6: 7 line(s); first line `from lumopt.figures_of_merit.modematch import ModeMatch`
- Code block 7: 1 line(s); first line `class ModeMatch(monitor_name = 'fom', mode_number = 3, direction = 'Backward', target_T_fwd = lambda wl: np.ones(wl.size), norm_p = 1)`
- Code block 8: 8 line(s); first line `from lumopt.figures_of_merit.PortTransmission import PortTransmission`
- Code block 9: 9 line(s); first line `from lumopt.optimizers.generic_optimizers import ScipyOptimizers`
- Code block 10: 8 line(s); first line `optimizer = ScipyOptimizers(max_iter = 200,`
- Code block 11: 14 line(s); first line `from lumopt.optimization import Optimization`
- Code block 12: 12 line(s); first line `opt_2d = Optimization(base_script = base_sim_2d,`
- Code block 13: 1 line(s); first line `opt.check_gradient(intitial_guess, dx=1e-3)`
- Code block 14: 2 line(s); first line `opt = opt_TE + opt_TM`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- Table 1: 1 column(s), 1 row(s)
  - First row sample: Note Lumerical ships with a version of Python 3, including lumapi and lumopt modules, already installed. To run any of our examples 'out of the box' simply run the scripts from the script file editor in the CAD.
- Table 2: 2 column(s), 4 row(s)
  - First row sample: Figure of Merit | Required Objects

## Official Links Found

- [Session management - Python API](https://optics.ansys.com/hc/en-us/articles/360041873053)
- [Grating coupler](https://optics.ansys.com/hc/en-us/articles/360042800573)
- [Waveguide crossing](https://optics.ansys.com/hc/en-us/articles/360042305314)
- [Y-branch.](https://optics.ansys.com/hc/en-us/articles/360042305274)
- [plane wave or gaussian beam source](https://optics.ansys.com/hc/en-us/articles/360034382854-Plane-wave-and-beam-source-Simulation-object)
- [Field Region Object](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)
- [FDE convergence](https://optics.ansys.com/hc/en-us/articles/360037172994)
- [Inverse Design of Metasurface Color Router](https://optics.ansys.com/hc/en-us/articles/33690448941587-Inverse-Design-of-Metasurface-Color-Router)
- [power coupling of guided modes](https://optics.ansys.com/hc/en-us/articles/360034902433)
- [Frequency dependent mode profile](https://optics.ansys.com/hc/en-us/articles/360034902073)
- [bounds](https://optics.ansys.com/hc/en-us/articles/360052044913)
- [project init](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01ED5A7PVZJ7MK74032HXECX4Q)
- [Wavelengths class](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01ED5A8NM7K34ZJFW16R55JXQ0)
- [ModeMatch](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01ED5ABFKDEX7R94EPTMR0Q8RQ)
- [PortTransmission](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01JH6KZ6S48CY45RM3S0ZA7TY0)
- [IntensityVolume](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01KA1Y041ZC4JF2EM0WXKV5D65)
- [ScipyOptimizer](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API#h_01ED5ACSPBP4YSB02JC9CJX8QS)

## Ansys-Related External Links Found

- None

## External Links Found

- [p-norm](https://en.wikipedia.org/wiki/Norm_(mathematics)#p-norm)
- [lambda function](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [numpy windows](https://numpy.org/doc/stable/reference/routines.window.html)
- [generalized p-norm](https://en.wikipedia.org/wiki/Norm_(mathematics))
- [SciPy optimization package](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html)
