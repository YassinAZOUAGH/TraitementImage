import numpy as np
import cv2 as cv


#img = np.ones((500,500,1),np.uint8)*255
img = np.zeros((500,500,3),dtype=np.uint8)
img[:] = 255, 255, 255

#cv.line(img,(100,80),(img.shape[1],img.shape[0]),(0,0,255),20)
#cv.rectangle(img,(0,0),(250,350),(0,0,255),2)
#cv.circle(img,(100,50),30,(0,255,0),5)

#cv.putText(img, "Texte à insérer",(50,100),cv.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

#print(img[0,0]) #l'image s'affiche en (B,G,R) dans l'index (x=3,y=3)  EX [128 136 223]


'''
for i in range(0,img.shape[0]):
    for j in range(0,img.shape[1]):
        pixel = img[i][j]
        #pixel2 = resizedImage[i][j] = [192,192,192]
        print (pixel)
        
'''

x=0
y=0
def rectangle(x,y): #Dessinez un carré rempli de couleur rouge sur fond blanc, sans utiliser la fonction rectangle
    for i in range(x, y):
        img[i][x] = [0, 0, 255]
        img[i][y] = [0, 0, 255]
        for j in range(100, 400):
            img[x][j] = [0, 0, 255]
            img[y][j] = [0, 0, 0]

rectangle(100,400)
cv.imshow('image',img)
cv.waitKey(0)


scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
hist = cv.calcHist([resizedImage],[0],None,[256],[0,256]) #Comptez le nombre de pixels de chaque niveau de gris de l’image « lena.png » ,construisez une nouvelle image dans laquelle vous allez « dessiner » l’histogramme et affichez la
cv.imshow('resizedImage',resizedImage)
cv.waitKey(0)
print(hist)

