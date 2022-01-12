import cv2
import numpy as np

# Load image
bgr = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')

# Make float and divide by 255 to give BGRdash
bgrdash = bgr.astype(np.float)/255.

# Calculate K as (1 - whatever is biggest out of Rdash, Gdash, Bdash)
K = 1 - np.max(bgrdash, axis=2)

# Calculate C
C = (1-bgrdash[...,2] - K)/(1-K)

# Calculate M
M = (1-bgrdash[...,1] - K)/(1-K)

# Calculate Y
Y = (1-bgrdash[...,0] - K)/(1-K)

# Combine 4 channels into single image and re-scale back up to uint8
CMYK = (np.dstack((C,M,Y,K)) * 255).astype(np.uint8)

#print(CMYK)
print(CMYK[0,0])
print(CMYK[0,0,3])
print(CMYK.shape[0])
print(CMYK.shape[1])
print(CMYK.shape[2])

for i in range(CMYK.shape[0]):
    for j in range(CMYK.shape[1]):
        CMYK[i, j, 0] = 0
       # CMYK[i,j,1] = 0
        #CMYK[i, j, 2] = 0
        #CMYK[i, j, 3] = 0
cv2.imshow('LenaextractCrayan', CMYK)
cv2.waitKey(0)