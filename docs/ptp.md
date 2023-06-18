## List of PTP Optcodes
See [ptp.h](https://raw.githubusercontent.com/petabyt/sequoia-ptpy/master/ptp.h)  
Also see  @malc0mn's [pip-ip library in Go](https://github.com/malc0mn/ptp-ip).
[camlib](https://github.com/petabyt/camlib) attempts to have a complete implementation of Fujifilm's PTP/IP protocol

0x1001-0x100B, 0x100F, 0x1014, 0x1015, 0x1016, 0x101B  
Fujifilm commands: 0x900C, 0x900D, 0x901D  
Microsoft commands: 0x9801, 0x9802, 0x9803, 0x9805  

Vendor specific commands can be used to upload firmware files to the camera

## 0x900C
- Create file
## 0x900D
- Possibly for sending file info
## 0x901D
- Write to file

These might be sligtly modified versions of 0x100C, 0x100D, and 100B (?)  
Either way, they are very similar.
