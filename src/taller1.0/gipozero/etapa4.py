from gpiozero import LED, Button
from time import sleep

LED_VERDE = LED(17)
LED_AMBAR = LED(27)
LED_ROJO = LED(22)
BOTON = Button(5)

try:
    while True:
        if BOTON.is_pressed:
            print("Botón pulsado")

        LED_VERDE.on()
        sleep(5)
        LED_VERDE.off()

        LED_AMBAR.on()
        sleep(2)
        LED_AMBAR.off()

        LED_ROJO.on()
        sleep(10)
        LED_ROJO.off()

except KeyboardInterrupt:
    LED_VERDE.off()
    LED_AMBAR.off()
    LED_ROJO.off()
