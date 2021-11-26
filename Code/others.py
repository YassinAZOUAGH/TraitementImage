import cv as cv
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt # utile pour les graphiques

# Convertit l'image en niveaux de gris Y
#image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/Sudoko.png')
#image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/cat.jpg')
b,v,r = cv.split(image)         # récupère 3 matrices d'octets séparées
y = 0.299*r + 0.587*v + 0.114*b # opération matricielle
y = y.astype(np.uint8)          # convertit les réels en octets

# Calcule l'histogramme de l'image
hist = np.zeros(256, int)       # prépare un vecteur de 256 zéros (pour chaque gris)

histo = cv.calcHist([image],[0],None,[256],[0,256]) # le nombre de pixel x*y
print("-->",histo)
for i in range(0,image.shape[0]):      # énumère les lignes
    for j in range(0,image.shape[1]):  # énumère les colonnes
        hist[y[i,j]] = hist[y[i,j]] + 1
        #print(hist[y[i,j]])
plt.ylabel('Nombre de pixel')
plt.xlabel('Valeur');
#print(hist)
plt.plot(hist)
plt.show()