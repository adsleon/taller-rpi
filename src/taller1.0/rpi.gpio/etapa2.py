import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_ROJO = 17
LED_VERDE = 27

GPIO.setup(LED_ROJO, GPIO.OUT)
GPIO.setup(LED_VERDE, GPIO.OUT)

GPIO.output(LED_ROJO, GPIO.HIGH)
time.sleep(15)
GPIO.output(LED_ROJO, GPIO.LOW)

GPIO.output(LED_VERDE, GPIO.HIGH)
time.sleep(15)
GPIO.output(LED_VERDE, GPIO.LOW)

GPIO.cleanup()
