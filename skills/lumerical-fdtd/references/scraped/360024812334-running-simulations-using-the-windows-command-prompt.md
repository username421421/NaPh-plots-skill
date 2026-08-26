# Running simulations using the Windows command prompt

Source URL: https://optics.ansys.com/hc/en-us/articles/360024812334-Running-simulations-using-the-Windows-command-prompt  
Area: Discovered official source  
Topic: Discovered from Lumerical Python API Reference  
Discovery depth: 1  
Last checked: 2026-06-21  
Capture mode: citation-safe local metadata, generated summary, headings, links, code/table inventories, key terms, and bounded excerpt.

## Local Capture Summary

This local capture indexes the official page `Running simulations using the Windows command prompt` for the topic `Discovered from Lumerical Python API Reference`. It captured 13 heading(s), 7 link(s), 20 code block(s), 18 inline code term(s), and 2 table(s). Main headings: Running simulations using the Windows command prompt, Running the design environment, Examples, Running the engine, Examples, Running with an MPI, MPI Options, Solver executables. Key detected terms: command, fdtd, mode, port, script, solver, source.

## Key Terms

- command
- fdtd
- mode
- port
- script
- solver
- source

## Captured Headings

- Running simulations using the Windows command prompt
- Running the design environment
- Examples
- Running the engine
- Examples
- Running with an MPI
- MPI Options
- Solver executables
- Simple Multi-purpose Daemon (SMPD)
- Examples
- CPi - MPI test program
- Stopping your simulation (Quit and Save)
- Pipe standard output to a text file

## Official Text Excerpt

> Running simulations using the Windows command prompt This article provides details on running Lumerical simulations with command line using the Windows command prompt. From the command line, you can run simulations through the Lumerical design environment, by running the engine directly, or through an MPI. Running the design environment [[snippet||52493047561619]] [[snippet||52492316567187]] Examples Running a script while 'hiding' the CAD window and saving the log file on a different location. Running a script with a simulation file while 'hiding' the CAD window and disabling safe mode. Opening a simulation file. Running the engine [[snippet||52492560991251]] Examples Run a simulation using 12 threads (cores). Running with 4 threads (cores) and saving the log files into a specific path. Running on the local computer with the -resume flag when check point is enabled in FDTD. Running with an MPI The message passing interface (MPI) is used to run simulations at the same time on different machines or processes, or to launch a simulation on a remote machine. Lumerical supports both concurrent computing, where several simulations are run at the same time, and distributed computing, ...

## Code Block Inventory

- Code block 1: 1 line(s); first line `"C:\Program Files\Lumerical\[[verpath]]\bin\interconnect.exe" -hide -run scriptfile.lsf -logall -o "C:\temp\logfiles\"`
- Code block 2: 1 line(s); first line `"C:\Program Files\Lumerical\[[verpath]]\bin\fdtd-solutions" -nw -trust-script -run scriptfile.lsf simulationfile.fsp`
- Code block 3: 2 line(s); first line `"C:\Program Files\Lumerical\[[verpath]]\bin\mode-solutions.exe" simulationfile.lms`
- Code block 4: 1 line(s); first line `"C:\Program Files\Lumerical\[[verpath]]\bin\fdtd-engine.exe" -t 12 "C:\temp\example.fsp"`
- Code block 5: 1 line(s); first line `"C:\Program Files\Lumerical\v261\[[verpath]]\varfdtd-engine.exe" -t 4 "C:\temp\example.lms" -o "C:\temp\logfiles\"`
- Code block 6: 1 line(s); first line `"C:\Program Files\Lumerical\v261\[[verpath]]\varfdtd-engine.exe" -t 4 -resume "\path\simulationfile`
- Code block 7: 1 line(s); first line `mpiexec [mpi_options] solver [solver_options]`
- Code block 8: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\mpiexec.exe" -help`
- Code block 9: 1 line(s); first line `"C:\Program Files\Lumerical\v261\intel_mpi\bin\mpiexec.exe" -help`
- Code block 10: 1 line(s); first line `-hosts n host1 n1 host2 n2…`
- Code block 11: 1 line(s); first line `-hosts host1,host2…`
- Code block 12: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\smpd.exe" -debug`
- Code block 13: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\mpiexec.exe" -n 32 "C:\Program Files\Lumerical\v261\bin\fdtd-engine-msmpi.exe" -t 1 -resume "\path\simulationfile.fsp"`
- Code block 14: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\mpiexec.exe" -n 12 "C:\Program Files\Lumerical\v261\bin\fdtd-engine-msmpi.exe" -t 1 "C:\temp\simulation.fsp"`
- Code block 15: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\mpiexec.exe" -n 8 -priority 1 "C:\Program Files\Lumerical\v261\bin\fdtd-engine-msmpi.exe" "C:\temp\example.fsp"`
- Code block 16: 1 line(s); first line `"C:\Program Files (x86)\IntelSWToolsMPI\mpi\2018.4.274\intel64\bin\mpiexec.exe" -n 4 "C:\Program Files\Lumerical\v261\bin\fdtd-engine-impi.exe" -t 1 "C:\temp\si`
- Code block 17: 1 line(s); first line `"C:\Program Files (x86)\IntelSWToolsMPI\mpi\2018.4.274\intel64\bin\mpiexec.exe" -n 16 -hosts 2 node1 node2 "C:\Program Files\Lumerical\v261\bin\fdtd-engine-impi`
- Code block 18: 1 line(s); first line `"C:\Program Files\Microsoft MPI\Bin\mpiexec.exe" -n 4 "C:\Program Files\Lumerical\[[verpath]]\mpitest\cpi-msmpi.exe"`
- Code block 19: 6 line(s); first line `Process 2 on localhost`
- Code block 20: 2 line(s); first line `"C:\Program Files\Lumerical\v261\bin\fdtd-engine.exe" -v > "C:\temp\engine_version.txt"`

## Inline Code Inventory

- `-affinity`
- `-help`
- `-hosts n <hostlist>`
- `-machinefile <file>`
- `-n <#>`
- `CTRL+C`
- `device-engine`
- `dgtd-engine`
- `eme-engine-impi`
- `eme-engine-msmpi`
- `fd-engine`
- `fdtd-engine-impi`
- `fdtd-engine-msmpi`
- `feem-engine`
- `mqw-engine`
- `thermal-engine`
- `varfdtd-engine-impi`
- `varfdtd-engine-msmpi`

## Table Inventory

- Table 1: 2 column(s), 4 row(s)
  - Headers: Option Flag, Description
  - First row sample: -n <#> | Only for the FDTD solver, varFDTD solver, and EME solver. Specifies the number of MPI processes.
- Table 2: 4 column(s), 12 row(s)
  - Headers: Product, Solver, MPI, Command
  - First row sample: Ansys Lumerical FDTD™ | FDTD | Microsoft MPI | fdtd-engine-msmpi

## Official Links Found

- [concurrent computing](https://optics.ansys.com/hc/en-us/articles/360026162414-Concurrent-Parametric-Computing)
- [distributed computing](https://optics.ansys.com/hc/en-us/articles/360026321353-Distributed-computing)
- [Register your user credentials](https://optics.ansys.com/hc/en-us/articles/5615899829907-Intel-MPI-Configuration-for-Remote-Simulations#toc_3)
- [distributed across 2 computers](https://optics.ansys.com/hc/en-us/articles/360026321353)
- [Resource Configuration](https://optics.ansys.com/hc/en-us/articles/360025161033)
- [Resource configuration elements and controls](https://optics.ansys.com/hc/en-us/articles/360058790674)
- [FDTD GPU Solver Information](https://optics.ansys.com/hc/en-us/articles/17518942465811)

## Ansys-Related External Links Found

- None

## External Links Found

- None
