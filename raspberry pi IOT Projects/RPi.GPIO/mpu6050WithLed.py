import board
import adafruit_mpu6050
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

gpio.setup(16, gpio.OUT)
gpio.setup(12, gpio.OUT)

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

# print(mpu.acceleration)
# print(type(mpu.acceleration))
xAxis = mpu.acceleration[0]
yAxis = mpu.gyro[1]
zAxis = mpu.acceleration[2]

while True:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    if mpu.acceleration[0] > xAxis+1:
        # print(mpu.acceleration[0] - xAxis, mpu.acceleration[2] - zAxis)
        gpio.output(21, True)
        print("Left")
    else:
        gpio.output(21, False)

    if mpu.acceleration[0] < xAxis-1:
        #print(mpu.acceleration[0] - xAxis, mpu.acceleration[2] - zAxis)
        print("Right")
        gpio.output(20, True)
    else:
        gpio.output(20, False)

    if mpu.acceleration[1] > yAxis+1:
        #print(mpu.acceleration[1] - yAxis)
        gpio.output(16, True)
        print("back")
    else:
        gpio.output(16, False)

    if mpu.acceleration[1] < yAxis-1:
        #print(mpu.acceleration[1] - yAxis)
        print("front")
        gpio.output(12, True)
    else:
        gpio.output(12, False)

    # if mpu.acceleration[2] > zAxis+1:
    #     print(mpu.acceleration[2] - zAxis+1)
    #     print("Up")
    # else:
    #     pass
    # if mpu.acceleration[2] < zAxis-1:
    #     print(mpu.acceleration[2] - zAxis-1)
    #     print("Down")
    # else:
    #     pass
    time.sleep(1)
