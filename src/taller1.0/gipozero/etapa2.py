from gpiozero import LED
from time import sleep

LED_ROJO = LED(17)
LED_VERDE = LED(27)

LED_ROJO.on()
sleep(15)
LED_ROJO.off()

LED_VERDE.on()
sleep(15)
LED_VERDE.off()
