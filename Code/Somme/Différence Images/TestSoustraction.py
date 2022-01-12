import cv2
import collections
cap = cv2.VideoCapture(0)
import numpy as np

ret, first_frame = cap.read()


while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_AREA)
    difference =  cv2.absdiff(first_frame,frame)
    cv2.imshow('Input', frame)
    #cv2.imshow('Input2', first_frame)
    cv2.imshow('difference', difference)


    Key = cv2.waitKey(1)
    if Key == 27:
        break


cap.release()
cv2.destroyAllWindows()