

import cv2 as cv
img = cv.imread('/testImages/cat.bmp')

print(type(img))

Hauteur = img.shape[0]
Largeur = img.shape[1]

print(Hauteur,Largeur)

imgCropped = img[50:400,100:550]


cv.imshow('imgCropped', imgCropped)
cv.waitKey(0)


cv.flip(img, 1)
