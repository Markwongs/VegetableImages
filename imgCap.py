import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import time

videoCaptureObject = cv.VideoCapture(0)
result = True
local_time = time.localtime()
mon, day = local_time[1], local_time[2]
while result:
        ret, frame = videoCaptureObject.read()
        cv.imwrite(r'/home/pi/Documents/VegetableImages/images'+'//'+'B'+str(mon)+'-'+str(day)+'.jpg', frame)
        result = False
videoCaptureObject.release()
cv.destroyAllWindows()
