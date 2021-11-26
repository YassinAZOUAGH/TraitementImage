import matplotlib.pyplot as plt
import cv2 as cv
import matplotlib.pyplot as plt # utile pour les graphiques
import numpy as np


#image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
#image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/Lena.bmp')
image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/cat.jpg')
#x = [1, 2, 2, 3, 4, 4, 4, 4, 4, 5, 5]
y=cv.calcHist([image],[0],None,[256],[0,256])
plt.hist(y, range = (0, 255), bins = 255, color = 'yellow', edgecolor = 'blue')
plt.xlabel('valeurs')
plt.ylabel('nombres')
plt.title('Exemple d\' histogramme simple')
plt.ylabel('Nomre de pixels')

plt.show()