import numpy as np
import cv2 as cv
img = np.zeros((500,500,3),dtype=np.uint8)
img[:] = 255, 255, 255 # color blanc
x=0
y=0
def carre(x,y): #Dessinez un carré rempli de couleur rouge sur fond blanc, sans utiliser la fonction rectangle
    for i in range(x, y):
        img[i][x] = [0, 0, 255]
        img[i][y] = [0, 0, 255]
        for j in range(100, 400):
            img[x][j] = [0, 0, 255]
            img[y][j] = [0, 0, 255]
carre(100,400)

img[100:400,100:400]=[0,0,255] # carré rempli de couleur rouge
cv.imshow('image',img)
cv.waitKey(0)
