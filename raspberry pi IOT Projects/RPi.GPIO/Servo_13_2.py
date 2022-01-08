import RPi.GPIO as GPIO
from time import sleep


class servo:
    def __init__(self, servo, frequency) -> None:
        self.servo = servo
        self.frequency = frequency

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo, GPIO.OUT)
        self.servoObj = GPIO.PWM(servo, frequency)  # 50Hz
        self.servoObj.start(0)

    def dutyCycle(self, angle):
        duty = angle / 18 + 2
        self.servoObj.ChangeDutyCycle(duty)
        sleep(1)


if __name__ == '__main__':
    servo = servo(servo=7, frequency=50)
    while True:
        try:
            servo.dutyCycle(90)
            print("Change to 90 degree ...")
            servo.dutyCycle(180)
            print("Change to 180 degree ...")
            servo.dutyCycle(90)
            print("Change to 90 degree ...")
            servo.dutyCycle(0)
            print("Change to 0 degree ...")
        except:
            GPIO.cleanup()
