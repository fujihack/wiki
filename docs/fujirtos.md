# Fujifilm's Tech History

## History
- In 1988, Fujifilm released their first 0.4mp digital camera, the Fujix DS-1P (first commercial digital camera)
- Fuji released the $3500 Fujifilm S1 Pro in 2000, which accepted firmware updates
- In 2003, Fujifilm first released a firmware update and [hackers on DPReview started to tinker with it](https://www.dpreview.com/forums/thread/430068)
- Fujifilm started out using VxWorks, then later switched to MiSPO [iTRON/NORTi](https://en.wikipedia.org/wiki/ITRON_project)
- More modern cameras use ThreadX, an open source RTOS. Many pieces of the original 2003 Fujifilm code is still present.
- SQLite was introduced in ~2012 to manage special settings in the camera. SQLite starts up about 10 minutes after powering on.
- In 2016-2017, a web server and networking drivers were introduced into the firmware, for WiFi connectivity (wpa_supplicant)
- In 2022, Linux is booted on the X-H2S for WiFi and processing functionality.
- To this day, Fujifilm continues to use most of the original firmware code from the early 2000s.

## CPUs
- Early Fujifilm cameras started out with 64 bit TX49 MIPS III CPUs but switched to 32 bit ARM later on
- Smaller cameras have the FF4224 SoC, but there is also a FF4226. These appear to be ARM v6 CPUs.
- Recently, Fujifilm started compiling their firmware in thumb bytecode.
- The SoC has no internal memory and must be paired with external RAM chips (1gb is common)
- Flash chips tend to be under the SD card reader (and tend to be 64mb)

## Graphics
- Vector graphics processing is handled on vglib task
- Most cameras use OpenVG with the `VG_KHR_EGL_image` plugin. Implemented into Fuji cameras by [NEC Systems Technology Ltd](https://www.nec.com/) in the 2000s.
- The rst task renders the OpenVG objects (?)
- Cameras since ~2017 use a very limited OpenGL to better render graphics and menus.

## Memory Management
- Each task tends to have a custom method of allocating memory
- Each task tends to have it's own memset/memcpy/strcpy set of functions
- Once SQLite is initialized manually, memory can be allocated from `sqlite_mallocAlarm`
- Memory starts at `0x00000000` and a read/write only mirror of the same region starts at `0x400000000`
- IO regions start at `0xf0000000`
