import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_VERDE = 17
LED_AMBAR = 27
LED_ROJO = 22
BOTON = 5

GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_AMBAR, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)
GPIO.setup(BOTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(BOTON) == GPIO.LOW:
            print("Botón pulsado")

        GPIO.output(LED_VERDE, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(LED_VERDE, GPIO.LOW)

        GPIO.output(LED_AMBAR, GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED_AMBAR, GPIO.LOW)

        GPIO.output(LED_ROJO, GPIO.HIGH)
        time.sleep(10)
        GPIO.output(LED_ROJO, GPIO.LOW)

finally:
    GPIO.cleanup()
