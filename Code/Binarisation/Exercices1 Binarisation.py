import cv2
import numpy as np

# path to input image is specified and 
# image is loaded with imread command
#image1 = cv2.imread('input1.jpg')
image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY) # 150 c'est seuillage : les valeurs supérieures ou égales à 150 sont mises à 255, les autres à 0.

cv2.imshow('Binary Threshold1', thresh1)


cv2.imshow('image', image1)
cv2.waitKey(0)


