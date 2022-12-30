# FujiFilm's RTOS

## History
- Fujifilm started out using VxWorks, then later switched to MiSPO [iTRON/NORTi](https://en.wikipedia.org/wiki/ITRON_project)
- Modern cameras use SQLite to store some settings. SQLite starts up about 10 minutes after powering on the camera.
- More modern cameras use ThreadX, an open source RTOS. Most of the Fujifilm code is still used.
- SQLite was introduced in ~2012 to manage special settings in the camera
- In 2016-2017, a web server was introduced, with WiFi (wpa_supplicant)
- In 2022, Linux is dual booted on the X-H2S

## CPUs
- Early Fujifilm cameras started out with TX49 MIPS III CPUs but switched to ARM later on (64 bit, Little endian)
- Smaller cameras have the FF4224, Arm v5 Little Endian 32 bit
- Later cameras have Arm v7

## Graphics
- Vector graphics processing is handled on vglib task
- Most cameras use OpenVG with the `VG_KHR_EGL_image` plugin. Implemented into Fuji cameras by [NEC Systems Technology Ltd](https://www.nec.com/) in the 2000s.
- The rst task renders the OpenVG objects (?)

## Memory Management
- Each task tends to have a custom method of allocating memory
- Each task tends to have it's own memset/memcpy/strcpy set of functions
- Once SQLite is initialized manually, memory can be allocated from `sqlite_mallocAlarm`
- Memory starts at `0x00000000` and a mirror of the same region starts at `0x400000000`
- Main memory seems to be 256 megabytes, and each other region (0x1*, 0x2*, 0x3*...) seems to be 256kb
- IO regions start at `0xf0000000` (?)
