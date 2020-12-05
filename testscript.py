from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1944, 1944)
camera.start_preview()
for i in range(5):
    sleep(0.5)
    camera.capture('/home/pi/Desktop/testimage%s.jpg' % i)
    print("success: pic " + str(i))
camera.stop_preview()
