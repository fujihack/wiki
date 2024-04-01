## Low Hanging Fruit
Things needed as of April 2024
# Fork Qemu and create an emulator for Fuji firmware
This would be a huge task, and would involve setting up Qemu for emulating an ARM11 SoC, setting up the memory regions, CPU configuration, and also IO such as the LCD, GPIO, SD MMC,
and any other hardware that the camera has and firmware expects.
# Data hoarding
It might be useful to compile a list of all Fuji cameras, and hoard as much information as possible for each camera. It would be great to have a database of information and a definite list of what cameras
run Fuji's main firmware system (what cameras are relevant to the Fujihack project) and what cameras don't (XP series, S series + a few others)

# Fudge
If you have experience with PTP/USB, Bluetooth, Android, or iOS, the [Fudge](https://github.com/petabyt/fudge) project may be interesting to you.
