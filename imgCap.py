import cv2 as cv
import time
capture = cv.VideoCapture(0)
time.sleep(4)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 5000)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 5000)
local_time = time.localtime()
mon, day = local_time[1], local_time[2]

while True:
    _, frame = capture.read()
    cv.imwrite(r'/home/pi/Documents/VegetableImages/images'+'/'+'B'+str(mon)+'-'+str(day)+'.jpg', frame)
    break
                
capture.release()
cv.destroyAllWindows()
