from typing import Text
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

reader = SimpleMFRC522()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, True)

while True:
    try:
        id, text = reader.read()
        print(f'ID : {id}')
        print(text)

        GPIO.output(37, False)
        sleep(1)

    except:
        GPIO.cleanup()

    finally:
        GPIO.output(37, True)
