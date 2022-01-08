import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)  # gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

while True:
    try:
        gpio.output(14, True)
        sleep(1)
        gpio.output(14, False)
        sleep(1)
    except:
        gpio.cleanup()
