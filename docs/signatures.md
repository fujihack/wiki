# RTOS Function signatures
## photo properties
```
02 00 a0 e3 00 10 a0 e1 1f 20 a0 e3 14 30
```
# Hints
## File IO Functions
- Look at `WT_LOG` and .MSG function
- For directory reading functions, look for `"*.*"`
- Calls are generally ordered as wait(), FIO call, wait(), reset()
- wait() and reset() get access to the SD card, and wait for system operations to pause

## msleep
- script WAIT and WAIT_SET code

# SQLite init function
- Look for unusual SQL code formatting, (`"FFDB"`)

# Flash reading functions
- Look for syslog `dmain` and `de`

# Multithreading
- System task function seems to be context sensitive
- Look for `"SoftTimerStart"` and `"SoftTimerStop"`

# EEPRom
- Look for most used functions, will modify a byte at an address
- `fuji_apply_eeprom()` is in "eeprom setting menu"

# Debug messages
- `fuji_screen_write()` is found in "EEPRom Setting Mode"
- `fuji_discard_text_buffer()` is found near that call
