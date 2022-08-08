# Auto Activated Script
`AUTO_ACT.SCR` is a script that is stored on the SD card in the `DCAA` folder. `DCAA` stands for Digital Camera Auto Act.

## Activation
The script is executed by the `mujin` task, most likely when the camera starts up. See [tasks](tasks.md).
Currently the only way to activate the script is by manually calling the function.

## Rules
- Files absolutely *must* use Windows style line breaks (`\n\r`). Else, the parser will hang.
- Comments start with `//`
- Each token can be no more than `20` characters long.
- Each line can have up to 10 tokens

## Keywords
```
WAITSET
func
LABEL
key
calc
set
jump
random
END
tp
WT_LOG
EXE_M
```

## Functions
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

## Operations
- `&`, `-`, `*`, `+`, and `/` are supported math operations

# Comparisons
- `!=`, `<=`, `>=`, and `==`.
