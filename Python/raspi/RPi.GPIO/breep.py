import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)  # gpio.setmode(gpio.BCM)

gpio.setup(38, gpio.OUT)
gpio.setup(40, gpio.OUT)
while True:
    gpio.output(38, True)
    gpio.output(40, True)
    sleep(1)
    gpio.output(38, False)
    gpio.output(40, False)
    sleep(1)
