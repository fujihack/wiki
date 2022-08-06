# Auto Activated Script
`AUTO_ACT.SCR` is a script that is stored on the SD card in the `DCAA` folder. `DCAA` stands for Digital Camera Auto Act.

## Activation
The script is executed by the `mujin` task, most likely when the camera starts up.

## Rules
- Most parsing (?) is skipped when file starts with `//`
- File should start with `\r\n` (?)

## Tokens
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

## Etc
- Basic math operations are supported
- `\t` and ` ` are whitespace characters
- The script ends with `\r` (?)
