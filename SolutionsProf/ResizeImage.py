import cv2 as cv
img = cv.imread('/Users/RudiGiot 1/Dropbox/Programmes/Python/ImageProcessing/testImages/lena.png')
scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
cv.imshow('Lena', img)
cv.imshow('Lena resized', resizedImage)
cv.waitKey(0)

