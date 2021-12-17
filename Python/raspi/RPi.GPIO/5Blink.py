import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)  # gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT)

while True:
    gpio.output(24, True)
    sleep(1)
    gpio.output(24, False)
    sleep(1)
