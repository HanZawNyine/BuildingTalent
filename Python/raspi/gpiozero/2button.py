from gpiozero import Button
from time import sleep

button = Button(26)

while True:
    # print(button.is_pressed)
    if button.is_pressed:
        print("Pressed")
    else:
        print("Released")
    sleep(1)
