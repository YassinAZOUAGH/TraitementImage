
import cv2
import numpy as np
from numba import cuda
import time


def binarize(imgGray,threshold):
    for (i,line) in enumerate(imgGray):
        for(j,pixel) in enumerate(line):
            value = imgGray[i][j]
            if value < threshold:
                imgGray[i][j] = 0
            else:
                imgGray[i][j] = 255
    return imgGray

NewDim = (500, 500)
image1 = cv2.imread('/testImages/ExemenImg.png')
image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExamenImg.png')
resizedImage = cv2.resize(image1, NewDim, interpolation=cv2.INTER_AREA)

img = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image binarized', binarize(img , 150))
cv2.imwrite('MyImage.png', img)
cv2.waitKey(0)

