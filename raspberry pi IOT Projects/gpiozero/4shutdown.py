from gpiozero import Button
import os

while True:
    Button(26).wait_for_press()
    os.system("sudo shutdown 0")
