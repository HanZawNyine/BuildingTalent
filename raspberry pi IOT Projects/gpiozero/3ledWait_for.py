from gpiozero import LED, Button

led = LED(19)
button = Button(26)

while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()
    led.off()
