import time

import serial
import threading
import sys
ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)
def odbiez():
    while True:
        if ser.in_waiting >0:
            line=ser.readline().decode('utf-8').rstrip()
            print(line)

def nadaj():
    while True:
        ser.write("hello")
        time.sleep(1)

t1=threading.Thread(target=odbiez)
t2=threading.Thread(target=nadaj)

t1.start()
t2.start()