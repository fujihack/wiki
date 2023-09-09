# Fujihack project structure

Quick overview of Fujihack's code structure:

![flowchart](img/flow.png)

## src/
- POSIX/Frontier compliant compatibility layer over Fujifilm's proprietary OS
- Header files defining Fujifilm's proprietary OS API (`ff_`)

## frontier/
Submodule to Frontier. You can learn more about the project [here](https://github.com/petabyt/frontier).

## patch/
- ARM32 assembly patches inserted directly into firmware. The patcher pulls files from this directory.

## ptp/
- PTP/USB utility for running code with the code execution patch. Can also quickly load the fujihack binary.

## model/
- Each camera model that has been reverse-engineered has its own C header file.
It holds information on the camera, including important addreses (stubs) in memory, firmware, and other
important model-specific information.

- Each file is named with the model code "xf1", "xt4", etc. Then an underscore, and the version code of the
firmware that was analyzed. For example, if the version is "1.01", then the version code would be "101".

- See `template.h` for a basic example. Memory addresses start with `MEM_`, firmware addresses start with `FIRM_`,
and functions are defined with the `NSTUB` macro.
