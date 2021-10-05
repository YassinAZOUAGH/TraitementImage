import cv2 as cv
import numpy as np


img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
lower=np.array([169,100,100])
upper=np.array([189,255,255])
mask=cv.inRange(hsv,lower,upper)
cv.imshow('new Lena gray', mask)
cv.waitKey(1000)
