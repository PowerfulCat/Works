#pragma once
#include"UnifiedAtType.h"

class FirmwareInfo{
public:
    String atVersion;
    String sdkVersion;
    String compileTime;
    String binVersion;
};

class AtUartConfig {
public:
    int32_t  rate;
    int32_t  databits;
    int32_t  stopbits;
    int32_t  parity;
    int32_t  flowControl;
};

class RfPower{
public:
    int32_t wifiPower;
    int32_t bleAdvPower;
    int32_t bleScanPower;
    int32_t bleConnPower;
};

bool atReset(actionMode mode = actionMode::waitReady);
bool atFirmwareInfo(FirmwareInfo * result);
bool atDeepSleep(int32_t ms);
bool atUartTemp(AtUartConfig const & config);
bool atUartNovolatile(AtUartConfig const & config);
bool atSleepMode(bool enable);
bool atSleepMode(bool * result);
bool atRfPower(int32_t wifi);
bool atRfPower(RfPower const & config);
bool atRfPower(RfPower * config);
