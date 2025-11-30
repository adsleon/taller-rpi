import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_VERDE = 17
LED_AMBAR = 27
LED_ROJO = 22

GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_AMBAR, GPIO.OUT)
GPIO.setup(LED_ROJO, GPIO.OUT)

try:
    while True:
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
