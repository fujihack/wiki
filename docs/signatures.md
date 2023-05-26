# RTOS Function signatures
## photo properties
```
02 00 a0 e3 00 10 a0 e1 1f 20 a0 e3
```
Typical Layout:
```
int show_photo_properties(void) {
  char cVar1;
  byte bVar2;
  ushort uVar3;
  undefined4 uVar4;
  short sVar5;
  uint uVar6;
  int iVar7;
  int iVar8;
  undefined auStack60 [32];
  
  uVar4 = DAT_X;
  iVar8 = *DAT_XX;
  cVar1 = *(char *)(DAT_XXX + 0xe754);
  if (cVar1 == 2) {
    fuji_rst_config1(0xf);
    fuji_rst_config2(10);
lbl1:
    if (DAT_007b21ec[0x34b] != 0) {
      FUN_1(1,(DAT_007b21ec[0x34e] & 0xffffU) - 0x11 & 0xffff,
                   (DAT_007b21ec[0x34f] & 0xffffU) - 0x11 & 0xffff,
                   (DAT_007b21ec[0x34e] & 0xffffU) + 0x11 & 0xffff,
                   (DAT_007b21ec[0x34f] & 0xffffU) + 0x11 & 0xffff,2,0x47);
      goto lbl3;
    }
lbl2:
    if (cVar1 == 2) goto lbl3;
  }
  else {
    FUN_2(2, 2, 0x1f, 0x14, 0x12, 0, 0xcc);
    fuji_rst_config1(0xf);
    fuji_rst_config2(10);
    if (cVar1 == 1) {
      FUN_3(0x10, 2, 0xff000684);
      fuji_rst_write(2, 3, &DAT_STR_X);
      fuji_rst_write(0x10, 3, &DAT_STR_XX);
```
## usb plugged-in screen
Function checks if a global integer is 0, 2, or 3. (signature will match more than 1 function)
```
eb 05 00 a0 e3 01 10 a0 e3
```
Typical Layout:
```
void usb_menu(void) {
  undefined4 uVar1;
  
  uVar1 = DAT_XXX;
  if (DAT_USB_MODE == '\0') {
    FUN_1();
    FUN_2();
    DAT_USB_MODE = '\x01';
  }
  else {
    if (DAT_USB_MODE == '\x02') {
      FUN_3();
    }
    if (DAT_USB_MODE == '\x03') {
      FUN_4();
      fuji_rst_config1(0xd);
      fuji_rst_config2(10);
      FUN_5(2,1,0xff0008a6);
      FUN_6(5,1,0x7c0);
      FUN_7();
      FUN_8(1,1,0x20,0x14,0x12,0,0xff);
      goto lbl;
    }
  }
  fuji_rst_config1(0xd);
  FUN_9(0x7c0,0,0xff0008a6,7,2,0x6d);
  FUN_10(1,1,0x20,0x14,0x12,0,0xff);
lbl:
  fuji_rst_config1(uVar1);
  return;
}
```


# Hints
## File IO Functions
- Look at `WT_LOG` and .MSG function
- For directory reading functions, look for `"*.*"`
- Calls are generally ordered as wait(), FIO call, wait(), reset()
- wait() and reset() get access to the SD card, and wait for system operations to pause

## msleep
- script WAIT and WAIT_SET code

# SQLite init function
- Look for unusual SQL code formatting, (`"FFDB"`)

# Flash reading functions
- Look for syslog `dmain` and `de`

# Multithreading
- System task function seems to be context sensitive
- Look for `"SoftTimerStart"` and `"SoftTimerStop"`

# EEPRom
- Look for most used functions, will modify a byte at an address
- `fuji_apply_eeprom()` is in "eeprom setting menu"

# Debug messages
- `fuji_screen_write()` is found in "EEPRom Setting Mode"
- `fuji_discard_text_buffer()` is found near that call
