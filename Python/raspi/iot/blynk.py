import BlynkLib
from datetime import datetime
from blinking.blink.views import on
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # gpio.setmode(gpio.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# Initialize Blynk
BLYNK_AUTH = 'QrJChxsQa7qvsRr8-lwgb4PW7nuzR8mp'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.VIRTUAL_WRITE(1)
def v1_write_handler(value):
    led1State = int(value[0])
    
    #print("V0: {}".format(led1State))
    if led1State == 1:
       GPIO.output(14, True)
       GPIO.output(15, True)
       #print("on")
       blynk.virtual_write(0, 255)
       blynk.virtual_write(3, 255)
    else:
       GPIO.output(14, False)
       GPIO.output(15, False)
       #print("off")
       blynk.virtual_write(0, 0)
       blynk.virtual_write(3, 0)
    
@blynk.VIRTUAL_READ(2)
def v2_read_handler():
    currentTime = datetime.now()
    blynk.virtual_write(2, currentTime.strftime("%d/%m/%Y %H:%M:%S"))

print("started!")
while True:
    blynk.run()
