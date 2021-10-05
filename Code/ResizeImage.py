import cv2 as cv
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/cat.bmp)')
scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
cv.imshow('Lena', img)
cv.imshow('Lena resized', resizedImage)
cv.waitKey(0)


Hauteur = img.shape[0]
Largeur = img.shape[1]

print(Hauteur,Largeur)

