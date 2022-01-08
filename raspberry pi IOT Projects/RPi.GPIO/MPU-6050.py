import board
import adafruit_mpu6050
import time

i2c = board.I2C()
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    print("Temperature : %.2f C" % mpu.temperature)
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    # print(mpu.gyro)
    print("*"*100)
    time.sleep(1)

    # print(mpu.temperature)
    # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    # print("Temperature: %.2f C" % mpu.temperature)
    # print("")
