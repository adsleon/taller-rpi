from gpiozero import LED
from time import sleep

led = LED(17)

while True: # se para con crtl + C
    led.on()
    sleep(1)
    led.off()
    sleep(1)
