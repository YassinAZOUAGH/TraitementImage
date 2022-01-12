

import cv2 as cv
#img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/cat.bmp')
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Code/Examen/MyImage.png')


Iban2 = img[263:307,79:335]
Date = img[122:154,11:87]
Nom = img[197:234,82:289]
Assurance = img[341:378,87:259]
Iban1 = img[157:195,83:326]
Facture = img[414:452,88:258]
Montant = img[118:145,404:487]

cv.imshow('img', img)
cv.imshow('IBAN', Iban2)
cv.imshow('Date', Date)
cv.imshow('Nom', Nom)
cv.imshow('Iban1', Iban1)
cv.imshow('Assurance', Assurance)
cv.imshow('Facture', Facture)
cv.imshow('Montant', Montant)
cv.waitKey(0)


