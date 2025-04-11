# Is it possible to bring a newer film simulation to an older camera?

Nobody knows yet. Exactly how film simulations work in the image processing pipeline and if/how they depend
on the image processor is not understood.

# Is it possible to downgrade the firmware on a body/lens?

Yes, it's as simple as modifying a few bytes in the firmware header.
There's some risk involved in downgrading because the data non-volatile memory is not
gauranteed to be backwards-compatible, but so far nobody has reported any issues.

You can use the web-based firmware patcher to modify the version of firmware files: https://fujihack.org/patcher/

# Is it possible to run firmware for X camera on Y camera?

This is probably impossible between any two Fuji cameras. Slight differences like button mapping and minor hardware
differences would likely cause major issues if not brick the camera.

# Liveview overlays?

Probably easy to implement.
