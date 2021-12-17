from gpiozero import LED, Button

led = LED(19)
button = Button(26)

while True:
    button.when_pressed = led.on
    button.when_released = led.off
