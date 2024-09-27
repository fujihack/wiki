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

## CPU History
## TX49 MIPS III CPU
- X-Pro 1, X-Pro 2
## EXR Processor (2012)
- X-F1
- AkA FF4224?
## EXR Processor II (2015?)
- X-T1, X-T20, X-A2
- AkA FF4226?
## EXR Processor III (2018)
- X-Pro 3, X-T30, X-H1
## X-Processor 4
- X100V, Fujifilm X-S10
## X-Processor 5
- X-H2S, X-T5
- Quad-core Aarch64 CPU
- Most of these cams dual-boot Linux for frame.io functionality.
