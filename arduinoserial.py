import time

import serial
import threading
import sys

ser = serial.Serial(

    port='/dev/ttyAMA0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
counter = 0
def odbiez():
    while True:
        if ser.in_waiting >0:
            line=ser.readline().decode('utf-8').rstrip()
            print(line)

def nadaj():
    while True:
        ser.write(str.encode("hello"))
        time.sleep(1)

t1=threading.Thread(target=odbiez)
t2=threading.Thread(target=nadaj)

t1.start()
t2.start()