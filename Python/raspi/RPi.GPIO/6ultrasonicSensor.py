# Libraries
import RPi.GPIO as GPIO
import time


class ultraSonicSensor:
    def __init__(self, GPIO_TRIGGER, GPIO_ECHO) -> None:
        # GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
        # set GPIO Pins
        self.GPIO_TRIGGER = GPIO_TRIGGER
        self.GPIO_ECHO = GPIO_ECHO

        # set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

    def distance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        # StartTime = time.time()
        # StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance


if __name__ == '__main__':
    try:
        ultrasonic = ultraSonicSensor(GPIO_TRIGGER=18, GPIO_ECHO=24)
        while True:
            dist = ultrasonic.distance()
            print("Distance = %.2f cm" % dist)
            time.sleep(1)

    # Reset by pressing CTRL + C
    except:
        print("stopped by User")
        GPIO.cleanup()
