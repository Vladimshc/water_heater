# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import config
import gc
import webrepl
webrepl.start()
gc.collect()


def connect():
    import network
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        return
    station.active(True)
    station.connect(config.ssid, config.ap_password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
    print(station.ifconfig())

connect()