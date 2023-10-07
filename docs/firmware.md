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
