import RPi.GPIO as gpio
from time import sleep

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)  # gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
gpio.setup(16, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(12, gpio.OUT)

# gpio.output(21, True)
# gpio.output(12, True)
# gpio.output(16, True)
# gpio.output(20, True)

gpio.output(12, False)
gpio.output(21, False)
gpio.output(16, False)
gpio.output(20, False)
