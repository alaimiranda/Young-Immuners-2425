import machine 
import utime

buzzer = machine.Pin(12, machine.Pin.OUT)

for i in range(10): 
    buzzer.value(1)
    utime.sleep(0.2) 
    buzzer.value(0) 
    utime.sleep(0.2)