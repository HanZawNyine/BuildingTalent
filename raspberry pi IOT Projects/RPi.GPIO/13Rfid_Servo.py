import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# servo
from Servo_13_2 import servo
servo = servo(servo=7, frequency=50)

GPIO.setwarnings(False)
reader = SimpleMFRC522()

# LED
GPIO.setup(40, GPIO.OUT)

# buzzer
GPIO.setup(38, GPIO.OUT)

# # initialize
# GPIO.output(40, False)
# GPIO.output(38, False)

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
            time.sleep(1)
            GPIO.output(38, False)
            GPIO.output(40, False)

            # servo
            servo.dutyCycle(90)
            servo.dutyCycle(0)
        GPIO.output(38, True)
        time.sleep(1)
        GPIO.output(38, False)

    except:
        GPIO.cleanup()
