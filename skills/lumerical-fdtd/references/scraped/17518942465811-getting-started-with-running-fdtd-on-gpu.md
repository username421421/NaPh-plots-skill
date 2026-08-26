# Getting started with running FDTD on GPU

Source URL: https://optics.ansys.com/hc/en-us/articles/17518942465811-Getting-started-with-running-FDTD-on-GPU  
Area: Discovered official source  
Topic: Discovered from Optimization session in lumopt2  
Discovery depth: 1  
Last checked: 2026-06-23  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Getting started with running FDTD on GPU` for the topic `Discovered from Optimization session in lumopt2`. It captured 10 heading(s), 24 link(s), 1 code block(s), 2 inline code term(s), and 0 table(s). Main headings: Getting started with running FDTD on GPU, Hardware requirements, Licensing, Supported simulation objects and limitations, Sources, Monitors, Materials, Other. Key detected terms: analysis, bfast, command, fdtd, geometry, import, material, mesh, mode, monitor, pml, port, script, solver, source, sweep.

## Key Terms

- analysis
- bfast
- command
- fdtd
- geometry
- import
- material
- mesh
- mode
- monitor
- pml
- port
- script
- solver
- source
- sweep
- tfsf

## Captured Headings

- Getting started with running FDTD on GPU
- Hardware requirements
- Licensing
- Supported simulation objects and limitations
- Sources
- Monitors
- Materials
- Other
- GPU simulation types and limitations
- GPU resource pages

## Official Text Excerpt

> Getting started with running FDTD on GPU The FDTD solver in Ansys Lumerical FDTD™ supports running 3D FDTD simulations on GPU starting in the 2023 R2 release. Calculations using the GPU can significantly speed up simulations. The FDTD solver supports single GPU, multi-GPU, as well as multi-node Multi GPU calculations. This page summarizes requirements and limitations of the current FDTD GPU solver, and points to various pages on specific setup instructions for different GPU applications. Note: Operations other than solver, such as meshing and script commands, still use the CPU. Hardware requirements GPU calculations with FDTD leverage CUDA 12, which in turn requires specific versions of the Nvidia CUDA driver, as well as a specific Compute Capability version. The driver and Compute Capability requirements are as follows: - Driver version: - 525.60.13 or later for Linux - 527.41 or later for Windows - Compute Capability: Compute Capability 5.0 or higher (Maxwell microarchitecture or newer). Please consult your GPU specifications to find the Compute Capability suitable for your GPU. Drivers of older devices were discontinued in January 2023. All GPU cards ...

## Code Block Inventory

- Code block 1: 5 line(s); first line `setnamed("time monitor", "spatial interpolation", "nearest cell");`

## Inline Code Inventory

- `CliqueId`
- `nvidia-smi -q`

## Table Inventory

- No tables detected

## Official Links Found

- [Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [License consumption calculation tools section](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption#toc_3)
- [GPU memory check feature](https://optics.ansys.com/hc/en-us/articles/360046368573-Running-FDTD-simulations-from-the-design-environment#toc_3)
- [2D standard optical conductivity models](https://optics.ansys.com/hc/en-us/articles/360034915113-Standard-optical-conductivity-material-models-in-FDTD-and-MODE)
- [np density index perturbation:](https://optics.ansys.com/hc/en-us/articles/360034901753-np-Density-and-Temperature-Index-Perturbation-Simulation-object)
- [Other advanced permittivity models](https://optics.ansys.com/hc/en-us/articles/360034394734-Advanced-and-custom-optical-material-models-in-FDTD-and-MODE)
- [Flexible Material Plugin Framework](https://optics.ansys.com/hc/en-us/articles/360034915213-Flexible-Material-Plugin-Framework)
- [FDTD Solver simulation object](https://optics.ansys.com/hc/en-us/articles/360034382534-FDTD-solver-Simulation-Object)
- [with a job scheduler](https://optics.ansys.com/hc/en-us/articles/360034620113-Lumerical-job-scheduler-integration-Slurm-Torque-LSF-SGE)
- [Ansys Cloud Burst Compute™.](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical)
- [concurrent parametric computing](https://optics.ansys.com/hc/en-us/articles/360026162414-Concurrent-Parametric-Computing)
- [distributed computing](https://optics.ansys.com/hc/en-us/articles/360026321353-Distributed-computing)
- [GPU resource pages](https://optics.ansys.com/hc/en-us/articles/17518942465811#toc5)
- [Check GPU streaming multiprocessor count page](https://optics.ansys.com/hc/en-us/articles/49707776311571-Checking-GPU-streaming-multiprocessor-count)
- [FDTD benchmark on CPU](https://optics.ansys.com/hc/en-us/articles/4403780894355)
- [resource configuration](https://optics.ansys.com/hc/en-us/articles/49707848532243-Resource-configuration-for-single-node-GPU-simulations)
- [Resource configuration for multi-node multi-GPU simulations article](https://optics.ansys.com/hc/en-us/articles/49708133627667-Resource-configuration-for-multi-node-multi-GPU-simulations)
- [license estimation utility](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)
- [Checking GPU streaming multiprocessor count](https://optics.ansys.com/hc/en-us/articles/49707776311571-Checking-GPU-streaming-multiprocessor-count)
- [Resource configuration for single node GPU simulations](https://optics.ansys.com/hc/en-us/articles/49707848532243-Resource-configuration-for-single-node-GPU-simulations)
- [Resource configuration for multi-node multi-GPU simulations](https://optics.ansys.com/hc/en-us/articles/49708133627667-Resource-configuration-for-multi-node-multi-GPU-simulations)
- [Running GPU simulations](https://optics.ansys.com/hc/en-us/articles/49708199997971-Running-GPU-simulations)
- [Accessing GPU results](https://optics.ansys.com/hc/en-us/articles/49708268223251-Accessing-GPU-results)

## Ansys-Related External Links Found

- [this document](https://www.ansys.com/content/dam/it-solutions/platform-support/2026-r1/ansys-2026-r1-gpu-compute-capabilities.pdf)

## External Links Found

- None
