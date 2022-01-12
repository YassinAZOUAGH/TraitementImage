import cv2

from numba import vectorize
import numpy as np
import timeit

from numba import jit, cuda
import time

#Binarisation GPU simple
@jit(nopython=True)  # forcer le "mode nopython"
def binarizeGPU(imgGray,threshold):
    for (i,line) in enumerate(imgGray):
        for(j,pixel) in enumerate(line):
            value = imgGray[i][j]

            if value < threshold:
                imgGray[i][j] = 0
            else:
                imgGray[i][j] = 255

    return imgGray

def binarize(imgGray,threshold):
    for (i,line) in enumerate(imgGray):
        for(j,pixel) in enumerate(line):
            value = imgGray[i][j]
            if value < threshold:
                imgGray[i][j] = 0
            else:
                imgGray[i][j] = 255
    return imgGray

def rotate_bound(img, angle):
    # grab the dimensions of the image and then determine the
    # center
    (hauteur, largeur) = img.shape[:2] #pour detecter la hauteur et la largeur
    (cX, cY) = (largeur / 2, hauteur / 2)
    # saisir la matrice de rotation (en appliquant le négatif de la
    # angle pour faire pivoter dans le sens des aiguilles d'une montre), puis saisissez le sinus et le cosinus
    # (c'est-à-dire les composants de rotation de la matrice)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # calculer les nouvelles dimensions limites de l'image
    nW = int((hauteur * sin) + (largeur * cos))
    nH = int((hauteur * cos) + (largeur * sin))
    # ajuster la matrice de rotation pour prendre en compte la translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    #effectuer la rotation réelle et renvoyer l'image
    return cv2.warpAffine(img, M, (nW, nH))





def click_event(event, x, y, flags, params):

	if event == cv2.EVENT_LBUTTONDOWN:

		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)


def ExtractImgs():

	if 'ExamenImg1' in path:
		print('traitement image 1')
		Iban2 = img[263:307, 79:335]
		Date = img[122:154, 11:87]
		Nom = img[197:234, 82:289]
		Assurance = img[341:378, 87:259]
		Iban1 = img[157:195, 83:326]
		Facture = img[414:452, 88:258]
		Montant = img[118:145, 404:487]

		cv2.imwrite('../Examen2/Image1/Iban2.png', Iban2)
		cv2.imwrite('../Examen2/Image1/Date.png', Date)
		cv2.imwrite('../Examen2/Image1/Iban1.png', Iban1)
		cv2.imwrite('../Examen2/Image1/Nom.png', Nom)
		cv2.imwrite('../Examen2/Image1/Assurance.png', Assurance)
		cv2.imwrite('../Examen2/Image1/Facture.png', Facture)
		cv2.imwrite('../Examen2/Image1/Montant.png', Montant)

		cv2.imshow('IBAN', Iban2)
		cv2.imshow('Date', Date)
		cv2.imshow('Nom', Nom)
		cv2.imshow('Iban1', Iban1)
		cv2.imshow('Assurance', Assurance)
		cv2.imshow('Facture', Facture)
		cv2.imshow('Montant', Montant)
		cv2.waitKey(0)

	if 'ExamenImg2' in path:
		print('traitement image 1')
		Date = img[154:185, 31:106]
		Nom = img[221:261, 104:343]
		Iban2 = img[292:323, 112:350]
		Impot = img[364:395, 113:287]
		Tva = img[431:463, 121:280]
		Iban1 = img[188:221, 104:336]
		Montant = img[147:182, 416:490]

		cv2.imwrite('../Examen2/Image2/Iban2.png', Iban2)
		cv2.imwrite('../Examen2/Image2/Date.png', Date)
		cv2.imwrite('../Examen2/Image2/Iban1.png', Iban1)
		cv2.imwrite('../Examen2/Image2/Nom.png', Nom)
		cv2.imwrite('../Examen2/Image2/Impot.png', Impot)
		cv2.imwrite('../Examen2/Image2/TVA.png', Tva)
		cv2.imwrite('../Examen2/Image2/Montant.png', Montant)

		cv2.imshow('IBAN2', Iban2)
		cv2.imshow('Date', Date)
		cv2.imshow('Nom', Nom)
		cv2.imshow('IBAN1', Iban1)
		cv2.imshow('Impot', Impot)
		cv2.imshow('TVA', Tva)
		cv2.imshow('Montant', Montant)
		cv2.waitKey(0)

	if 'ExamenImg3' in path:
		print('traitement image 3')
		Iban2 = img[263:307, 79:335]
		Date = img[108:154, 7:79]
		Nom = img[194:233, 79:228]
		Assurance = img[350:396, 79:189]
		Iban1 = img[157:195, 83:326]
		Facture = img[434:473, 78:271]
		Montant = img[118:145, 397:452]

		cv2.imwrite('../Examen2/Image3/Iban2.png', Iban2)
		cv2.imwrite('../Examen2/Image3/Date.png', Date)
		cv2.imwrite('../Examen2/Image3/Iban1.png', Iban1)
		cv2.imwrite('../Examen2/Image3/Nom.png', Nom)
		cv2.imwrite('../Examen2/Image3/Proximus.png', Assurance)
		cv2.imwrite('../Examen2/Image3/Facture.png', Facture)
		cv2.imwrite('../Examen2/Image3/Montant.png', Montant)

		cv2.imshow('IBAN', Iban2)
		cv2.imshow('Date', Date)
		cv2.imshow('Nom', Nom)
		cv2.imshow('Iban1', Iban1)
		cv2.imshow('Assurance', Assurance)
		cv2.imshow('Facture', Facture)
		cv2.imshow('Montant', Montant)
		cv2.waitKey(0)

# driver function
if __name__=="__main__":
    path = 'ExamenImg1.png'
    #path = 'ExamenImg2.png'
    #path = 'ExamenImg3.png'
    image1 = cv2.imread(path)
    NewDim = (500, 500)
    resizedImage = cv2.resize(image1, NewDim, interpolation=cv2.INTER_AREA)


    img_rotate = rotate_bound(resizedImage, -6)
    if 'ExamenImg2' in path:
        imgGray = cv2.cvtColor(img_rotate, cv2.COLOR_BGR2GRAY)
    else:
        imgGray = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)

    start = time.time()
    # cv2.imshow('imageBinarized', binarize(imgGray, 150))
    # cv2.imwrite('MyImg.png', binarize(imgGray, 150))

    cv2.imshow('imageBinarized', binarizeGPU(imgGray, 150))
    cv2.imwrite('MyImg.png', binarizeGPU(imgGray, 150))
    end = time.time()
    print('temps excution', end - start)

    img = cv2.imread('MyImg.png')
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)
    ExtractImgs()


