# FujiFilm's RTOS

## Quick Facts:  
- Fujifilm started out using VxWorks, then later switched to [iTRON](https://en.wikipedia.org/wiki/ITRON_project)
- Modern cameras use SQLite to store some settings. SQLite starts up every 10 minutes or so.
- More modern cameras use ThreadX.

## Screen
- The display on Fujifilm cameras is made of of several layers.
- The display has a seperate text layer, and text can be drawn on the screen with a function.
- The display buffer is made of 32 bit integers, and seems to simply be hex colors.

## Task List

| ID | Name | Desc |
| - | - | - |
| 0x2a | zoom | ... |
| 0x37 | rplib | ... |
| 0x23 | saclac | ... |
| 0x32 | initcont | ... |
| 0x1b | mujin | "unpopulated" in Japanese. Responsible for [AUTO_ACT.SCR](autoactscr.md) |
| 0x17 | soundio | ... |
| 0x16 | voicecont | ... |
| 0x14 | comp | ... |
| 0x57 | root | ... |
| 0x55 | idle0 | ... |
| 0x56 | idle1 | ... |
| 0x52 | standby1 | ... |
| 0x44 | pm_dsp | ... |
| 0x3b | book | ... |
| 0x29 | lensdc | ... |
| 0x3d | iwayagrelease | ... |
| 0x2f | redeye | ... |
| 0x38 | chase | ... |
| 0x3a | hdmi | ... |
| 0x35 | facerecog | ... |
| 0x26 | calcsub | ... |
| 0x3e | vglib | ... |
| 0x20 | graphic | ... |
| 0x5 | beep | ... |
| 0x54 | elfloader | ... |
| 0x39 | mdetect | ... |
| 0x2b | focus | ... |
| 0x15 | media | ... |
| 0x30 | imgstabi | ... |
| 0x3f | pm_snd | ... |
| 0x24 | calc | ... |
| 0x40 | pm_frm | ... |
| 0x36 | searchTbl | ... |
| 0x19 | uilib | ... |
| 0x6 | delay | ... |
| 0x8 | calendar | ... |
| 0x1d | keytimer | ... |
| 0x4 | playcont | ... |
| 0x21 | audio | ... |
| 0x9 | timer | ... |
| 0x42 | pm_dcn | ... |
| 0x3c | iwagdispatch | ... |
| 0x3 | reccont | ... |
| 0x1c | usb | ... |
| 0x33 | flashloader | ... |
| 0x7 | usbcont | ... |
| 0x1 | execcpu | Task ID is loaded from memory |
| 0x13 | dpof | ... |
| 0x2c | iris | ... |
| 0xa | flash | ... |
| 0x18 | playsub | ... |
| 0x28 | movdc | ... |
| 0x43 | pm_rsz | ... |
| 0x41 | pm_dec | ... |
| 0x2 | syscont | ... |
| 0x25 | calc1 | ... |
| 0x27 | imgdc | ... |
| 0x7 | face | ... |
| 0x1f | levelsens | ... |
| 0x1a | lcdevf | ... |
| 0x1 | ui | ... |
