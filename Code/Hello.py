import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
#img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png',0) #         pour avoir l'image Gris

# print(img[3,3]) #l'image s'affiche en (B,G,R) dans l'index (x=3,y=3)  EX [128 136 223]
Hauteur = img.shape[0]
Largeur = img.shape[1]
print("=>",img.shape[:2])
print("l'image est de" , "(", Hauteur,",", Largeur,")")


(hauteur, largeur) = img.shape[:2] #pour detecter la hauteur et la largeur
(cX, cY) = (largeur / 2, hauteur / 2)
print("---->",cX,cY)


#convert to gray color
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#save to new file
cv.imwrite('LenaGris.png', gray_img)
cv.imshow('new Lena gray', gray_img)
cv.waitKey(1000)

#destroy window
#cv.destroyWindow()


'''
start = time.time()
#**********************#
end = time.time()
print('temps excution' ,end - start)
'''








#cv.imwrite('C:/Users/yassi/Documents/GitHub/TraitementImage/lenaCopy.png', img)
