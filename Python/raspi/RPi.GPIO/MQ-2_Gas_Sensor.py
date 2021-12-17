import time
import RPi.GPIO as GPIO

gpio.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# LED
GPIO.setup(11, GPIO.OUT)
# Buzzer
GPIO.setup(13, GPIO.OUT)

try:
    while True:
        # print(GPIO.input(7))
        if GPIO.input(7):
            # LED
            GPIO.output(11, True)
            # Buzzer
            GPIO.output(13, True)
            print("Somke")
        else:
            GPIO.output(11, False)
            GPIO.output(13, False)
        time.sleep(1)

except:
    GPIO.cleanup()
