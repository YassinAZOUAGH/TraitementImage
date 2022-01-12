import cv2 as cv
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/pool.png')
# Pour obtenir la taille de l'image (largeur, hauteur, nombre de composantes couleur)
print(img.shape)
# Pour obtenir les composantes RGB du pixel de coordonnées (200, 200)
print(img[200,200,1])


for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        img[i,j,0] = 0
        img[i,j,1] = 0
cv.imshow('Red Cat', img)
cv.waitKey(0)