import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')


scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
#cv.imshow('new Lena gray', resizedImage)
#cv.waitKey(1000)


for i in range(0,resizedImage.shape[0]):
    for j in range(0,resizedImage.shape[1]):
        pixel = resizedImage[i][j]
        #pixel2 = resizedImage[i][j] = [192,192,192]
        print (pixel)

cv.imwrite('pixel.png', pixel)
cv.imshow('pixel', pixel)
cv.waitKey(10000)

"""
image_data = np.asarray(resizedImage)
for i in range(len(image_data)):
 for j in range(len(image_data[0])):
     print(image_data[i][j])  # this row prints an array of RGB color for each pixel in the image



Extraction = img[0:1000,0:200]
cv.imshow('Extraction', Extraction)
cv.waitKey(1000)



Inversion = cv.flip(img,-1)
cv.imshow('Inversion', Inversion)
cv.waitKey(1000)
"""

