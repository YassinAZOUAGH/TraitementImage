import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/lena.png')

scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
#cv.imshow('Lena', img)
flipVertical = cv.flip(img, 0)
flipHorizontal = cv.flip(img, 1)
flipBoth = cv.flip(img, -1)

#cv.imshow('Lena resized', img)
#cv.imshow('Flipped vertical image', flipVertical)
#cv.imshow('Flipped horizontal image', flipHorizontal)
#cv.imshow('Flipped both image', flipBoth)

img_rotate_90_clockwise = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
#cv.imshow('img_rotate_90_clockwise', img_rotate_90_clockwise)

img_rotate_90_counterclockwise = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
#cv.imshow('img_rotate_90_counterclockwise', img_rotate_90_counterclockwise)

img_rotate_180 = cv.rotate(img, cv.ROTATE_180)
#cv.imshow('img_rotate_180', img_rotate_180)

def rotate_bound(img, angle):
    # grab the dimensions of the image and then determine the
    # center
    (hauteur, largeur) = img.shape[:2] #pour detecter la hauteur et la largeur
    (cX, cY) = (largeur / 2, hauteur / 2)
    # saisir la matrice de rotation (en appliquant le négatif de la
    # angle pour faire pivoter dans le sens des aiguilles d'une montre), puis saisissez le sinus et le cosinus
    # (c'est-à-dire les composants de rotation de la matrice)
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    print("=>", cos,sin)
    # calculer les nouvelles dimensions limites de l'image
    nW = int((hauteur * sin) + (largeur * cos))
    nH = int((hauteur * cos) + (largeur * sin))
    # ajuster la matrice de rotation pour prendre en compte la translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    #effectuer la rotation réelle et renvoyer l'image
    return cv.warpAffine(img, M, (nW, nH))

img_rotate = rotate_bound(img, 60)
cv.imshow('imh_rotate', img_rotate)
cv.waitKey(1000)


M = np.float32([[1, 0, -50], [0, 1, -90]])


def Translate_image(x,y):
    M = np.float32([[1, 0, -x], [0, 1, -y]])
    Translate = cv.warpAffine(img, M, (img.shape[1], img.shape[0]))
    cv.imshow("Translate", Translate)
    cv.waitKey(0)
#Des valeurs négatives pour la valeur x déplaceront l'image vers la droite
#Des valeurs positives pour x décale l'image vers la gauche
#Des valeurs négatives pour y déplacent l'image vers le bas
#Des valeurs positives pour y déplaceront l'image vers le haut
Translate_image(-50,200)