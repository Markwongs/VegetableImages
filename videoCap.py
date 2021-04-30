import cv2 as cv
import numpy

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    resize = cv.resize(frame, (1920,1080))
    cv.imshow('frame', resize)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

