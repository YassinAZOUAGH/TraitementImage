import cv2 as cv


img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/lena.png')

NewDim = (200, 200)
resizedImage = cv.resize(img, NewDim, interpolation=cv.INTER_AREA)
cv.imshow('Lena', img)
cv.imshow('Lena resized', resizedImage)
cv.waitKey(0)



