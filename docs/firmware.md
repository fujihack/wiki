# Firmware Patching

The firmware payload is bit-flipped (`~`). The checksum is a simple case of "add up all the bytes and make sure it equals X"

## Header
```
struct FujiFirmHeader {
	// Type of the firmware layout - shows parser how big MODEL_CODE_SIZE is
	unsigned int type;

	// Proprietary model ID code
	unsigned char code[MODEL_CODE_SIZE];

	// Printed as hex in the camera. X.X
	unsigned int version1;
	unsigned int version2;

	// File checksum
	unsigned int checksum;

	// Whether device is a lens or camera
	unsigned int device_type;
};
```

## Dangerous?
Firmware patching is always dangerous no matter what. A small typo can brick the entire camera.

When I first started the project, I bought the cheapest camera I could find, to test if patching was possible,  
and what if it were possible to run custom code on it. Somewhere in my experiments I accidentally deleted a number  
off an address, and the camera no longer showed any signs of life. It was a bummer, but I had prepared for it.

That was with a few janky Makefiles and C scripts. The new Javascript patcher has sanity checks that verify checksums and  
instructions around the injection point. It's much safer, and I've probably tested it around 100 times or so. But it's still  
very dangerous.

My personal advice is that you don't try custom firmware on any piece of technology worth more than $1000. However, sometimes  
the rewards outweight the risks.

It is most likely possible to recover a bricked camera, through the boot ROM, burned into the SoC. Reverse engineering this takes  
a lot of time, skill, and money, so it hasn't been figured out as of mid 2023.
