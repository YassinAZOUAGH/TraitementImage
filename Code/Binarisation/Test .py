import os
import numpy as np
import cv2 as cv

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')



LUT= np.arange(256)//32
print (LUT)