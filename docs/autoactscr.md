# Auto Activated Script
`AUTO_ACT.SCR` is a script that is stored on the SD card in the `DCAA` folder. `DCAA` stands for Digital Camera Auto Act.
This script has been with the Fujifilm cameras [since 2004](https://en.wikipedia.org/wiki/FinePix_S3_Pro), and is still included on modern cameras.

## Activation
- The script is executed by the `mujin` task. See [tasks](tasks.md).
- The script is only activated when byte `0xa2` in EEPROM is set to `2`.

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
```
### if
- The 5th parameter is only for decoration. The interpreter never checks it. It could be any valid token.
- Supported operations: `!=`, `<=`, `>=`, and `==`.
```
if x == 10 jump label
```
### calc
- The `=` or 3rd parameter is again, only for decoration.
- `&`, `-`, `*`, `+`, and `/` are supported math operations.
```
calc x = x + 1
calc x = 123 & 6
```
### jump
- Jump to a label.
```
jump label
```
### LABEL
- Won't work if lowercase.
```
LABEL top
```
### WT_LOG
- Creates a function that makes DSCFXXXX.MSG log file in DCIM
- Nothing significant, writes some UI logs in a binary format. Maybe Syslog format?
- Accepts a parameter, but seems to never be used.
```
WT_LOG
```
### END
- Ends the script
### key
- Triggers a key press
- First parameter can be `MODE` or a [button key](keys.md) name.
- Second parameter can be `ON` or `OFF`
```
// Disconnect USB
key USB OFF

// Press UP key
key UP ON
```
### random
- Random between two numbers
```
random x 0 10
```
### wait
- wait x miliseconds
```
wait 2000
```
### WAITSET
- Creates a delay between each command in the script, in miliseconds.
```
WAITSET 0x1234
```

## Types:
### EEPROM type
- Starts with `E_`, and follows is 4 hexadecimal numbers
- Can be used to either set or get a byte from EEPROM.
```
set x = E_a2
set E_9999 = 123
```
### Integer
- Can be 5 bytes long
```
123
```
### Hexadecimal
- Must be lower case
- Can only be 4 bytes long
```
0x123
0xa1
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
  if x >= 10 jump end
  calc x = x + 1
  jump lab
LABEL end
```
