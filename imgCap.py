import cv2 as cv
import time

print("-"*50)
print("Image Capturing")
capture = cv.VideoCapture(0)
time.sleep(4)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 5000)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 5000)
local_time = time.localtime()
mon, day, hour, min = [local_time[i] for i in range(1, 5)]
<<<<<<< HEAD


while True:
    _, frame = capture.read()
    cv.imwrite(r"/home/pi/Documents/VegetableImages/images"+'/'+'B'+str(mon)+'-'+str(day) + '-' + str(hour) + ':' + str(min) + '.jpg', frame)
=======

while True:
    _, frame = capture.read()
    cv.imwrite(r"/home/pi/Documents/VegetableImages/images"+'/'+'B'+str(mon)+'-'+str(day) + '-' + str(hour) + ':' + str(min) + '.jpg', frame)
>>>>>>> d4de339613b03e72d0e2d332ffca243ab7b40afe
    break
                
capture.release()
cv.destroyAllWindows()
print("Image Captured")
print("-"*50)
