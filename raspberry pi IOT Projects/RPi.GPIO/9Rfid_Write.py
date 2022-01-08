import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()

writeText = input("Enter Your RFID Tag :")
reader.write(writeText)

while True:
    try:
        id, text = reader.read()
        print(f"Your ID : {id}")
        print(f'Your Text : {text}')
        #print(type(id), type(text))
    except:
        GPIO.cleanup()
