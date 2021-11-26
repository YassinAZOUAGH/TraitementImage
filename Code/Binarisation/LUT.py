import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/TestLUT.jpg')
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/lena.png')

cv.imshow('new Lena gray', img)
cv.waitKey(1000)

lut = np.array([256-i for i in range(256)])
#lut = np.arange(256)//128
plt.figure();
plt.plot(range(256),lut,'b+-')
plt.show()

img_out = lut[img]
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img_out[y,x] = lut[img[y,x]]

plt.figure();
plt.imshow(img_out, cmap=plt.cm.gray)
plt.show()