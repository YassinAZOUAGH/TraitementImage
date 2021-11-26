




import cv2
import numpy as np

image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')


img = cv2.split(image1)[0]
newImg1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
#fait un threshold adaptatif en utilisant des voisinages de 9 (doit être impair) et
# en mettant les valeurs au-dessus de la moyenne locale moins 10 à la valeur 255


cv2.imshow('seuillage adaptatif1', newImg1)

cv2.waitKey(0)
