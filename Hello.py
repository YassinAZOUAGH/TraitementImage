import cv2 as cv
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')

cv.imshow('Lena', img)
cv.waitKey(5000)


cv.imwrite('C:/Users/yassi/Documents/GitHub/TraitementImage/lenaCopy.png', img)
