import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
reader = SimpleMFRC522()

# # LED
GPIO.setup(40, GPIO.OUT)

while True:
    try:
        id, text = reader.read()
        print(f"Your ID : {id}")
        print(f'Your Text : {text}')
        if id == 944051432292:
            GPIO.output(40, True)
            sleep(1)
            GPIO.output(40, False)
            sleep(1)
    except:
        GPIO.cleanup()
