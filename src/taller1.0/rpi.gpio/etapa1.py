import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 17
GPIO.setup(LED, GPIO.OUT)

GPIO.output(LED, GPIO.HIGH)
time.sleep(15)
GPIO.output(LED, GPIO.LOW)

GPIO.cleanup()
