import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')

histogram = np.zeros(256)

print("G",img[0,0,0])
print("B",img[0,0,1])
print("R",img[0,0,2])

def grayScale(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            k=(int(img[i,j,0]) + int(img[i,j,1]) + int(img[i,j,2]))/3.0
            img[i, j, :] = k
            #print(k)
            #histogram[int(k)] = histogram[int(k)]+1
            #print(histogram[int(k)])



grayScale(img)
cv.imshow('Lena gray', img)
cv.waitKey(0)