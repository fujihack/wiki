# Auto Activated Script
`AUTO_ACT.SCR` is a script that is stored on the SD card in the `DCAA` folder. `DCAA` stands for Digital Camera Auto Act.
This script has been with the Fujifilm cameras [since 2004](https://en.wikipedia.org/wiki/FinePix_S3_Pro), and is still included on modern cameras.

## Activation
The script is executed by the `mujin` task, most likely when the camera starts up. See [tasks](tasks.md).
Currently the only way to activate the script is by manually calling the function.

## Rules
- Files absolutely *must* use Windows style line breaks (`\n\r`). Else, the lexer will hang.
- Comments start with `//`
- Each token can be no more than `20` characters long.
- Each line can have up to 10 tokens
- Keywords are case sensitive.
- ' ', '\r', and '\t' are whitespace characters.

## Keywords
```
if
func
key
calc
set
jump
random
tp
LABEL
END
WAITSET
WT_LOG
EXE_M
```
## if
- The 5th parameter is purely for decoration. The interpreter never checks it. It could be any valid token.
- Supported operations: `!=`, `<=`, `>=`, and `==`.
```
if x == 10 jump label
```
## calc
- The `=` or 3rd parameter is again, purely for decoration.
- `&`, `-`, `*`, `+`, and `/` are supported math operations.
```
calc x = x + 1
calc x = 123 & 6
```
## jump
- Jump to a label.
```
jump label
```
## LABEL
- Won't work if lowercase.
```
LABEL top
```
## WT_LOG
- Creates a function that makes DSCFXXXX.MSG log file in DCIM
- I've already known about this function, and it doesn't appear to be anything useful.
- Accepts a parameter, but seems to never be used.
```
WT_LOG
```

## Functions
TODO: more research
```
ON
OFF
MOVE
SWEEP
2ON
2OFF
2MOVE
2SWEEP
MULTI
```

## Examples
### Count to 10
```
set x = 1
LABEL lab
  if x >= 10 goto end
  calc x = x + 1
  jump lab
LABEL end
```
