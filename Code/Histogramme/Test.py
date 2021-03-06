import cv2
import numpy as np
from matplotlib import pyplot as plt

#gray_img = cv2.imread('images/GoldenGateSunset.png', cv2.IMREAD_GRAYSCALE)
#gray_img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png' , cv2.IMREAD_GRAYSCALE)
img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png',0)
#img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/cat.jpg')

hist = cv2.calcHist([img], [0], None, [256], [0, 256])# hist = cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogramme pour image en niveaux de gris')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.ylabel('Nomre de pixels')

plt.show()
