from machine import ADC, Pin
from time import sleep

adc = ADC(Pin(26))

while True:
    Bit = adc.read_u16()
    Volt = bit*(3.3/65535)  
    Temp = Volt*(1/0.01)
    print(Temp)
    sleep(5)