from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(4)
camera.capture('/home/pi/Documents/VegetableImages/images/x.jpg')
camera.stop_preview()
