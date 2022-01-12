import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png',0)

hist = cv.calcHist([img],[0],None,[256],[0,256])
#plt.hist(img.ravel(),256,[0,256]);
plt.plot(hist)


plt.xlabel("niveau de gris")
plt.ylabel('Nombre de pixels')
plt.title('Histogramme')
plt.show()












