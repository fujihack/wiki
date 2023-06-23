## Technical overview of Fujifilm's Firmware
(These details come from reverse-engineering the firmware of the X-A2.)

Fujifilm started working on their firmware in the early 2000s. Instead of writing their firmware directly on an RTOS,
they made a *compatibility layer* over an existing RTOS. This allowed them to easily switch from VxWorks to NORTi and
to ThreadX over the years. Each function in Fuji's compatibility layer calls a specific index of a function table, which
makes reverse engineering or using the underlying RTOS very difficult. Instead, this project aims to reverse engineer only
Fujifilm's compatibility layer instead.

## Fujifilm's compatibility layer
- See [ff_io.h](https://github.com/fujihack/fujihack/blob/master/src/ff_io.h)

## Memory management
Unlike most firmware, Fujifilm doesn't have a `malloc()` function. Each task works with fixed empty arrays. This means the developers
created *huge* global variables. This means a lot of RAM is wasted, and it makes it harder to load Fujihack. There are some allocation functions,
such as the ones from SQLite or the WiFi code, but these only offer a megabyte or two and don't take advantage of all the RAM the camera has (1GB).

This unusual memory management has both pros and cons for the Fujihack project.
- Patching data is easier - since everything is a global variable, a fixed address can be used to specify any data
- It's hard to load a large Fujihack binary - Since memory can't be easily allocated, this makes it hard to find space to load Fujihack.

Overall, it's not a deal breaker. Fujifilm managed to make it work over the years, and Fujihack can find ways around it.

## Performance
Fujifilm cameras are really slow. The CPU is underclocked to preserve battery life, which makes the camera sluggish sometimes. This doesn't
take a toll on things JPEG encoding and decoding, because it's done with hardware acceleration.

The CPU performance of the X-A2 is similar to an i386 desktop computer of the mid 90s.

## Graphics
- Vector graphics processing is handled on vglib task
- Most cameras use OpenVG with the `VG_KHR_EGL_image` plugin. Implemented into Fuji cameras by [NEC Systems Technology Ltd](https://www.nec.com/) in the 2000s.
- The rst task renders the OpenVG objects (?)
- Cameras since ~2017 use a very limited OpenGL to better render graphics and menus.
