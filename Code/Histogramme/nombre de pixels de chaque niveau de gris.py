import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
hist = cv.calcHist([img],[0],None,[256],[0,256])

cv.imshow('Lena img', img)
cv.waitKey(0)