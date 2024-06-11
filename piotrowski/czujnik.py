import smbus2
import bme280
# biblioteki odpowiedzialne za czujnik BME280

import time
import w1thermsensor
import datetime

# część kodu odpowiedzialna za czujnik BME280
port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)
while True:
    # the sample method will take a single reading and return a
    # compensated_reading object
    data = bme280.sample(bus, address, calibration_params)

    # the compensated_reading class has the following attributes
    x = str(datetime.datetime.now())
    temp = str(round(data.temperature, 1))
    pres = round(data.pressure, 1)
    wilg = round(data.humidity, 1)
    wynik=[]
    wynik.append(
        f"\"{x}\":{chr(123)}\"temperatura\":\"{temp}\"  , \"cisnienie\":\"{pres}\" ,\"wilgotnosc\":\"{wilg}\" , \"data\":\"{x}\" {chr(125)},\n")
    with open("temperatury.json", "a") as writer:
        writer.writelines(wynik)
    time.sleep(1)