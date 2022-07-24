# FujiFilm's RTOS
Quick Facts:  
- Fujifilm has an operating system for cameras that appears to be unique.
- Modern cameras use SQLite to store some settings.

# Screen
- The display on Fujifilm cameras is made of of several layers.
- The display has a seperate text layer, and text can be drawn on the screen with a function.
- The display buffer is made of 32 bit integers, and seems to simply be hex colors.

# Tasks
- The RTOS runs around 20-30 tasks at once. Some of these tasks are "ui", "flash", "imgstabi", "hdmi", etc
