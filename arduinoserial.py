import time
import struct
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
size=struct.calcsize('f')
def odbiez():
    while True:
        if ser.in_waiting >0:
            line=ser.read(size)
            data=struct.unpack('f',line)
            print("odebrano")
            print(data[0])

def nadaj():
    a=1
    while True:
        ser.write(str.encode("%d\n"%(a)))
        print("nadano")
        print(a)
        a=a+1
        time.sleep(1)

t1=threading.Thread(target=odbiez)
t2=threading.Thread(target=nadaj)

t1.start()
t2.start()