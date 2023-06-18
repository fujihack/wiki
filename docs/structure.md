# FujiHack Repository Structure and Coding Rules
- Immitate the the style of the code you see in the project already.

## src/
This is the main program that is sent over via USB into the camera.

## patch/
ARM32 assembly patches inserted directly into firmware. The patcher pulls files from this directory.

## ptp/
PTP/USB utility for running code with the code execution patch. Can also quickly load the fujihack binary.

## model/
Each camera model that is reverse engineered has it's own C header file, or information file.
It holds information on the camera, including important addreses in memory, functions, and other
details.

Each file is named with the model code "xf1", "xt4", etc. Then an underscore, and the version code of the
firmware that was analyzed. For example, if the version is "1.01", then the version code would be "101".

See `template.h` for a basic example. Memory addresses start with `MEM_`, firmware addresses start with `FIRM_`,
and functions are defined with the `NSTUB` macro.
