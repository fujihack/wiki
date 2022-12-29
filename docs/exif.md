# IMFIDX10
`IMxxxxxxxxxx` directories are described in the 1998 JEIDA (Japan Electronic Industry Development Association) [patent](http://www.awm.jp/~yoya/cache/www.clavis.ne.jp/~hre/files/Exifj.pdf)
`IMxxxxxxxxxx` are referred to as an 'Exif directory'.

Exif directories can store Exif files. It's difficult to understand exactly what the paper says, but it's clear that this folder
is used for general purpose file (image, sound, video) manipulation.

In Fujifilm cameras, an S3 file can be stored in the `IMFIDX10` directory. For the XF1, it is `C:\IMFIDX10\XF10RS.S3`.
In the JEIDA paper, `IMFIDX10` is described as a 'self-recorded Exif directory'.

S3 files are standard Motorola [S-record files](https://en.wikipedia.org/wiki/SREC_(file_format)). Fujifilm has a long history of using these files.
On cameras from the early 2000s, they were used to [apply early firmware updates](https://www.dpreview.com/forums/thread/430068).

These files appear on Fujifilm cameras as far back as the S3 Pro to the XH2S (`C:\IMFIDX10\LX46.S`).

See [/etc/s3](https://github.com/fujihack/fujihack/tree/master/etc/s3) for a lousy attempt to understand S3 files.

Nobody knows how to trigger this file, although it's clear that it is ran in a very similar way to firmware updates. It might not be possible to trigger it at all.

