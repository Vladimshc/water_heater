from config import time_zone

import machine
import time
import onewire
import ds18x20
from ntptime import settime
import utime

#Time
#get time from ntp
settime()
rtc = machine.RTC()
# for time convert to second
utc_time = utime.time()
# 1 hour = 3600 seconds, 2 hours = 7200 seconds
local_time = utc_time + 3600 * time_zone
tm = utime.localtime(local_time)
tm = tm[0:3] + (0,) + tm[3:6] + (0,)
rtc.datetime(tm)

# the device is on GPIO4
dat_watter = machine.Pin(4)
# create the onewire object
ds_watter = ds18x20.DS18X20(onewire.OneWire(dat_watter))

# scan for devices on the bus
roms_watter = ds_watter.scan()
print('found devices watter:', roms_watter)



pin = machine.Pin(2,machine.Pin.OUT,value=0) # set pin LOW on creation

def toggle(p):
    p.value(not p.value())

while True:
    (year, month, mday, hour, minute, second, weekday, yearday) = utime.localtime()
    world_time = rtc.datetime()
    ds_watter.convert_temp()
    time.sleep_ms(750)
    watter = ds_watter.read_temp(roms_watter[0])
    if watter < 30:
        pin(0)
        print(watter)
    else:
        pin(1)
        print("Hot = ", watter)

    print("world_time = ", world_time)
    print("hour = ", hour)
    print("minute = ", minute)

    time.sleep_ms(1000)


main()
