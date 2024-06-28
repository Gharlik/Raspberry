import smbus2
import bme280
# biblioteki odpowiedzialne za czujnik BME280

import time

import datetime

#//////////////////////////////////////////
#biblioteki do mpu6050
import mpu6050
import time



# część kodu odpowiedzialna za moduł mpu6050
mpu6050 = mpu6050.mpu6050(0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    global accelerometer_data
    accelerometer_data = mpu6050.get_accel_data()

    # Read the gyroscope values
    global gyroscope_data
    gyroscope_data = mpu6050.get_gyro_data()

    # Read temp
    global temperature
    temperature = mpu6050.get_temp()

    return accelerometer_data, gyroscope_data, temperature



# część kodu odpowiedzialna za czujnik BME280
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)
while True:
    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)
    accelerometer_data, gyroscope_data, temperature = read_sensor_data()
    # the compensated_reading class has the following attributes
    x = str(datetime.datetime.now())
    temp = str(round(data.temperature, 1))
    pres = round(data.pressure, 1)
    wilg = round(data.humidity, 1)
    wynik = []
    wynik.append(
        f"\"{x}\":{chr(123)}\"temperatura\":\"{temp}\"  , \"cisnienie\":\"{pres}\" ,\"wilgotnosc\":\"{wilg}\" , \"data\":\"{x}\" {chr(125)},\"Accelerometer\":\"{accelerometer_data}\,"
        f"\"Gyroscope\":\"{gyroscope_data}\"\n")
    with open("temperatury.json", "a") as writer:
        writer.writelines(wynik)
    time.sleep(1)