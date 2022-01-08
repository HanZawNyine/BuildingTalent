import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(33, GPIO.OUT)

def buzz_now(iterations):
    for x in range(iterations):
        GPIO.output(33, True)
        sleep(0.1)
        GPIO.output(33, False)
        sleep(0.1)

# buzz_now(1)

try:
    while True:
        # print(GPIO.input(8))
        if GPIO.input(12) == 0:  # 1
            buzz_now(5)
            print("Rain Dtected")
        time.sleep(1)
except:
    GPIO.cleanup()
