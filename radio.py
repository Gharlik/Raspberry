import RPi.GPIO as GPIO
import time
import spidev
from lib_nrf24 import NRF24

GPIO.setmode(GPIO.BCM)
pipes = [[0xE0, 0xE0, 0xF1, 0xF1, 0xE0], [0xF1, 0xF1, 0xF0, 0xF0, 0xE0]]
radio1.begin(0, 25)
radio1.setPayloadSize(32)
radio1.setChannel(0x76)
radio1.setDataRate(NRF24.BR_1MBPS)
radio1.setPALevel(NRF24.PA_MIN)
radio1.openWritingPipe(pipes[0])
radio1.printDetails()
sendMessage = list("Hi..Arduino UNO")
while len(sendMessage) < 32:
    sendMessage.append(0)
    while True:
        start = time.time()
        radio.write(sendMessage)
        print("Sent the message: {}".format(sendMessage))
    send
    radio.startListening()
while not radio.available(0):
    time.sleep(1 / 100)
    if time.time() - start > 2:
        print("Timed out.")  # print error message if radio disconnected or not functioning anymore
        break
    radio.stopListening()  # close radio
    time.sleep(3)  # give delay of 3 seconds
