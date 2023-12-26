import time
import w1thermsensor
import datetime
from time import strftime

wynik = []
while True:
    sensor = w1thermsensor.W1ThermSensor()
    temp = str(sensor.get_temperature())
    x = str(datetime.datetime.now())
    wynik.append(f"{temp}      {x}\n")
    time.sleep(1)
    with open("temperatury.txt", "a") as writer:
        writer.writelines(wynik)
