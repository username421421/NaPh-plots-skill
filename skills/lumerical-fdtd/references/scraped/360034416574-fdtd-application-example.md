# Using the Python API in the nanowire application example

Source URL: https://optics.ansys.com/hc/en-us/articles/360034416574-FDTD-application-example  
Area: Discovered official source  
Topic: Discovered from Python API overview  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Using the Python API in the nanowire application example` for the topic `Discovered from Python API overview`. It captured 6 heading(s), 11 link(s), 8 code block(s), 0 inline code term(s), and 0 table(s). Main headings: Using the Python API in the nanowire application example, Importing modules, Setting up the geometry from Python, Analyzing simulation and theoretical results, Plotting the results, See also. Key detected terms: command, dataset, fdtd, geometry, grating, import, lumapi, mode, monitor, port, python, script.

## Key Terms

- command
- dataset
- fdtd
- geometry
- grating
- import
- lumapi
- mode
- monitor
- port
- python
- script

## Captured Headings

- Using the Python API in the nanowire application example
- Importing modules
- Setting up the geometry from Python
- Analyzing simulation and theoretical results
- Plotting the results
- See also

## Official Text Excerpt

> Using the Python API in the nanowire application example This example demonstrates the feasibility of integrating Lumerical FDTD with Python using Application Programming Interface (API). In this example, we will set the geometry based on 2D Mie scattering example and then run the simulation using Python script. Once the simulation is finished, simulation results will be imported to Python, and plots comparing simulation and theoretical results as well as a plot of Ey intensity will be provided. Requirements: Lumerical products 2018a R4 or newer Note: - Versions: The example files were created using Lumerical 2018a R4, Python 3.6 (and numpy), matplotlib 0.99.1.1, and Windows 7 - Working directory: It should be possible to store the files in any locations as desired. However, it is recommended to put the Lumerical and Python files in the same folder in order for the above script files to work properly. It is also important to check the Lumerical working directory has the correct path, see here for instructions to change the Lumerical working directory. - Linux: /opt/lumerical/interconnect/api/python/ - Windows: C:\Program Files\Lumerical\FDTD\api\python During the Lumerical ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `import lumapinw = lumapi.FDTD("nanowire_build_script.lsf") nw.save("nanowire_test")nw.run()nw.feval("nanowire_plotcs.lsf")  # run the second script for plots`
- Code block 2: 1 line(s); first line `import importlib.util#The default paths for windowsspec_win = importlib.util.spec_from_file_location('lumapi', 'C:\\Program Files\\Lumerical\\2020a\\api\\python`
- Code block 3: 1 line(s); first line `def runNanowireSimulation(profile_monitor_wavelength=1e-6):     configuration = (        ("source", (("polarization angle", 0.),                    ("injection `
- Code block 4: 1 line(s); first line `for obj, parameters in configuration:       for k, v in parameters:           fdtd.setnamed(obj, k, v)    fdtd.setnamed("profile", "wavelength center", float(pr`
- Code block 5: 1 line(s); first line `nw = runNanowireSimulation() # recalls the function to run the simulation## run the simulation once, to determine resonance wavelength## and get cross-sections `
- Code block 6: 1 line(s); first line `plt.plot(lam_sim*1e9, sigmaext*1e9,label='sigmaext')plt.plot(lam_sim*1e9, -sigmaabs*1e9)plt.plot(lam_sim*1e9, sigmascat*1e9)plt.plot(lam_sim*1e9, r25*1e9)plt.xl`
- Code block 7: 1 line(s); first line `## run the simulation again using the resonance wavelength_, _, E = runNanowireSimulation(profile_monitor_wavelength=lam_sim[np.argmax(sigmascat)])## show the f`
- Code block 8: 7 line(s); first line `plt.pcolor(np.transpose(abs(Ey)**2), vmax=5, vmin=0)`

## Inline Code Inventory

- No inline code terms detected

## Table Inventory

- No tables detected

## Official Links Found

- [here](https://optics.ansys.com/hc/en-us/articles/360034931553)
- [session management](https://optics.ansys.com/hc/en-us/articles/360041873053)
- [List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834)
- [Python API](https://optics.ansys.com/hc/en-us/articles/360034416554)
- [Lumerical Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554)

## Ansys-Related External Links Found

- None

## External Links Found

- [2D Mie scattering](https://kb.lumerical.com/particle_scattering_getting_started.html)
- [this page](https://kb.lumerical.com/installation_and_setup_python-integration.html)
- [nanowire application example](https://kb.lumerical.com/particle_scattering_getting_started.html)
- [Silver Nanowire Tutorial](https://kb.lumerical.com/particle_scattering_getting_started.html)
- [Setting up Python API](https://kb.lumerical.com/installation_and_setup_python-integration.html)
- [Matlab API](https://kb.lumerical.com/pic_passive_matlab-driven-optimization.html)
