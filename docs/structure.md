#FujiHack Repository Structure and Coding Rules
- There is no official code standard. Immitate the the style of the code you see in the project already.

## src/
This is the main program that is sent over via USB into the camera.

## firm.c
The firmware utility that unpacks, repacks, injects, and unravels the Fujifilm firmware files.
Will most likely be replaced by the [web patcher](https://github.com/fujihack/patcher) in the near future.

## main.S, jump.S,
This is custom ARM32 assembly code that is carefully injected into the firmware file. `main.S` allows code execution via USB.

## ptp/
Folder for reverse engineering Fujifilm's PTP/USB commands, using Python3 and the ptpy library.

## model/
Each camera model that is reverse engineered has it's own C header file, or information file.
It holds information on the camera, including important addreses in memory, functions, and other
details.

Each file is named with the model code "xf1", "xt4", etc. Then an underscore, and the version code of the
firmware that was analyzed. For example, if the version is "1.01", then the version code would be "101".

See `template.h` for a basic example. Memory addresses start with `MEM_`, firmware addresses start with `FIRM_`,
and functions are defined with the `NSTUB` macro.

## emulator/
A basic emulator for running small bits of Fujifilm code. It won't display any screen or open any windows. Very basic.
