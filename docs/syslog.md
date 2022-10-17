# Syslog
- Syslog is a logging mechanism that records important system info and errors to RAM
- Typically, `syslog Ver 2.3     ` is printed on startup.
- Log start addr typically is saved at addr `0x400a0400`
- Each log is `16` bytes
- The log string has no null terminator (easy to confuse with compressed ROM)

## First log / info struct
```
struct Initial {
  char msg[0x14]; // only this is null terminated
  uint16_t of_0x14;
  uint8_t of_0x16;
  uint8_t of_0x17;
  uint16_t of_0x18;
  uint16_t of_0x1a;
  uint16_t of_0x1c_curr_msg;
  // ...
  uint32_t of_30;
  // end
};
```

## Each log
struct log {
  // addressed in uint32_t and uint8_t form
  uint8_t type; (0xf == signal, 0x72 == string msg  )
  uint8_t of_1_ret_from_thread;
  uint8_t of_2; // val @ fffa9c08
  uint8_t of_3; // 0
  
  uint32_t id; // magic number??
  
  char msg[8];
}
