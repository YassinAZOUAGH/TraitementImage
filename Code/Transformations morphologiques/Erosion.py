
import cv2
import numpy

img = cv2.imread("C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/OCR.PNG")
newImg = cv2.split(img)[0]
(retVal, newImg) = cv2.threshold(newImg, 130, 255, cv2.THRESH_BINARY)
kernel = numpy.ones((3, 3), numpy.uint8)
newImg = cv2.erode(newImg, kernel, iterations = 1)

cv2.imshow('new image',newImg)
cv2.waitKey(0)