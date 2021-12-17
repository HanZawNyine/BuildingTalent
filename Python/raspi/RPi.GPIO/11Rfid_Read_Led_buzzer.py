import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)
reader = SimpleMFRC522()

# LED
GPIO.setup(40, GPIO.OUT)

# buzzer
GPIO.setup(38, GPIO.OUT)

# initialize
GPIO.output(40, False)
GPIO.output(38, False)

print("RFID Reader is Starting ...")
while True:
    try:
        id, text = reader.read()
        print(f"Your ID : {id}")
        print(f'Your Text : {text}')
        if id == 944051432292:
            GPIO.output(40, True)
            # buzzer
            GPIO.output(38, True)
            GPIO.output(38, False)

            GPIO.output(40, False)
    except:
        GPIO.cleanup()
