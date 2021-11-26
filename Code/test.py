import numpy as np
import cv2 as cv
#img = np.ones((300,400,1),np.uint8)*200
img = np.zeros((255,300,3),dtype=np.uint8)
img[:] = 255, 0, 0
print(img)

hist = cv.calcHist([img],[0],None,[256],[0,256]) # le nombre de pixel x*y
#print(hist)
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),10)
cv.imshow('image',img)
cv.waitKey(0)