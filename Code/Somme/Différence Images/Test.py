import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/lena.png')
img2 = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/shapes.png')
scale = (500, 500)
Image1 = cv.resize(img, scale, interpolation=cv.INTER_AREA)
Image2 = cv.resize(img2, scale, interpolation=cv.INTER_AREA)


SommeImg = cv.addWeighted(Image1,0.7,Image2,0.3,0)
image3 = cv.absdiff(Image1, Image2)
cv.imshow('SommeImg',image3)
cv.waitKey(0)



