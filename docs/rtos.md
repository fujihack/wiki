## Technical overview of Fujifilm's Firmware
(These details come from reverse-engineering the firmware of the X-A2.)

Fujifilm started working on their firmware in the early 2000s. Instead of writing their firmware directly on an RTOS,
they made a *compatibility layer* over an existing RTOS. This allowed them to easily switch from VxWorks to NORTi and
to ThreadX over the years. This project is more concerned with reversing Fuji's compatibility layer than reversing ThreadX.

## Fujifilm's I/O API
- See [ff_io.h](https://github.com/fujihack/fujihack/blob/master/src/ff_io.h)

## Memory management
Unlike most firmware, Fujifilm doesn't have a `malloc()` function. Each task works with fixed empty arrays. The developers
created *huge* global variables. This means a lot of RAM is "wasted", and it makes it harder to allocate arbritrary space. There are some allocation functions,
such as the ones from SQLite or the WiFi code, but these only offer a megabyte or two and don't take advantage of all the RAM the camera has (1GB).

This unusual memory management has both pros and cons for the Fujihack project.
- Patching data is easier - since everything is a global variable, a fixed address can be used to specify any data
- It's hard to load a large Fujihack binary - Since memory can't be easily allocated, this makes it hard to find space to load Fujihack.

Overall, it's not a deal breaker. Fujifilm managed to make it work over the years, and Fujihack can find ways around it.

## Performance
Fujifilm cameras up to 2016 are really slow. About 100 tasks are running, which takes a toll on UI performance. This doesn't
take a toll on things like JPEG/MOV encoding/decoding because it's done through hardware.

After 2016, Fujifilm switched to ThreadX as their RTOS, which improved performance and the responsiveness of the menus.

## Graphics
- Vector graphics processing is handled on vglib task
- Most cameras use OpenVG with the `VG_KHR_EGL_image` plugin. Implemented into Fuji cameras by [NEC Systems Technology Ltd](https://www.nec.com/) in the 2000s.
- The rst task renders the OpenVG objects (?)
- Cameras since ~2017 use a very limited OpenGL to better render graphics and menus.
