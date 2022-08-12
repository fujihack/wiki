# FujiFilm's RTOS

## Quick Facts:  
- Fujifilm started out using VxWorks, then later switched to [iTRON](https://en.wikipedia.org/wiki/ITRON_project)
- Early Fujifilm cameras started out with M32R CPUs but switched to ARM later on
- Modern cameras use SQLite to store some settings. SQLite starts up every 10 minutes or so.
- More modern cameras use ThreadX.

## Screen
- The display on Fujifilm cameras is made of of several layers.
- The display has a seperate text layer, and text can be drawn on the screen with a function.
- The display buffer is made of 32 bit integers, and seems to simply be hex colors.
