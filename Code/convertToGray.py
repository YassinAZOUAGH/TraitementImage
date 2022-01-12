import cv2 as cv
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
#img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png',0) #         pour avoir l'image Gris
Hauteur = img.shape[0]
Largeur = img.shape[1]
print("l'image est de" , "(", Hauteur,",", Largeur,")")

#convert to gray color
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
HSV_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
HLS_img = cv.cvtColor(img, cv.COLOR_BGR2HLS_FULL)

#save to new file
#cv.imwrite('LenaGris.png', gray_img)
cv.imshow('gray_img', gray_img)
cv.imshow('HSV_img', HSV_img)
cv.imshow('HLS_img', HLS_img)
#cv.imshow('Blue_img', Blue_img)
cv.waitKey(0)

#destroy window
#cv.destroyWindow()











#cv.imwrite('C:/Users/yassi/Documents/GitHub/TraitementImage/lenaCopy.png', img)
