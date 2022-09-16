# FujiFilm's RTOS

## Quick Facts:  
- Fujifilm started out using VxWorks, then later switched to [iTRON](https://en.wikipedia.org/wiki/ITRON_project)
- Early Fujifilm cameras started out with M32R CPUs but switched to ARM later on
- Modern cameras use SQLite to store some settings. SQLite starts up about 10 minutes after powering on the camera.
- More modern cameras use ThreadX.

## Memory Management
- Each task seems to have a custom method of allocating memory
- Once SQLite is initialized manually, memory can be allocated from `sqlite_mallocAlarm`
- Memory starts at `0x00000000` and a mirror of the same region starts at `0x400000000`
- Main memory seems to be 256 megabytes, and each other region (0x1*, 0x2*, 0x3*...) seems to be 256kb
