from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

while True: # En python los booleanos van en mayuscula la primera
  button.wait_for_press()
  led.on()
  sleep(3)
  led.off()
