from gpiozero import LED, Button
from time import sleep

LED_VERDE = LED(17)
LED_AMBAR = LED(27)
LED_ROJO = LED(22)
LED_ROJO_PEATON = LED(23)
LED_VERDE_PEATON = LED(24)
BOTON = Button(5)

def ciclo_normal():
    LED_ROJO_PEATON.on()
    LED_VERDE_PEATON.off()

    LED_VERDE.on()
    sleep(5)
    LED_VERDE.off()

    LED_AMBAR.on()
    sleep(2)
    LED_AMBAR.off()

    LED_ROJO.on()
    sleep(10)
    LED_ROJO.off()

def ciclo_peaton():
    LED_VERDE.off()
    LED_AMBAR.off()
    LED_ROJO.on()
    LED_VERDE_PEATON.on()
    LED_ROJO_PEATON.off()
    sleep(5)
    LED_VERDE_PEATON.off()
    LED_ROJO_PEATON.on()
    sleep(1)

peticion = False

try:
    while True:
        if BOTON.is_pressed and not peticion:
            peticion = True

        if peticion:
            ciclo_peaton()
            peticion = False
        else:
            ciclo_normal()

except KeyboardInterrupt:
    LED_VERDE.off()
    LED_AMBAR.off()
    LED_ROJO.off()
    LED_ROJO_PEATON.off()
    LED_VERDE_PEATON.off()
