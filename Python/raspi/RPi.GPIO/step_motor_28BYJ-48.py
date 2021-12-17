from time import sleep
import RPi.GPIO as GPIO
from time import sleep


class stepMotor28BJ:
    def __init__(self, *args) -> None:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.control_pins = list(args)
        # print(control_pins)
        for pin in self.control_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        self.halfstep_seq = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]
        ]

    def forward(self):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(self.control_pins[pin],
                            self.halfstep_seq[halfstep][pin])
            sleep(0.001)

    def backward(self):
        for halfstep in reversed(range(8)):
            for pin in range(4):
                GPIO.output(self.control_pins[pin],
                            self.halfstep_seq[halfstep][pin])
            sleep(0.001)


if __name__ == '__main__':
    try:
        while True:
            stepMotor = stepMotor28BJ(7, 11, 13, 15)
            # stepMotor.forward()
            stepMotor.backward()
    except:
        GPIO.cleanup()
