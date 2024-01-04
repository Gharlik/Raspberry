from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

for i in range(3*60):
    camera.capture(f'image_x{i:03d}.jpg')  # Take a ppicture every minute for 3 hours
    sleep(5)