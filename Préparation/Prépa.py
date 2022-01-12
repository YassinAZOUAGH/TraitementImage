import cv2 as cv
img = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
#cv.imshow('Lena', img)
#cv.waitKey(0)

#cv.imwrite('path/testImages/lenaCopy.png', img) # souvegarde l'image
# CMYK colors is a combination of CYAN, MAGENTA, YELLOW , and BLACK.  =CYAN, MAGENTA, JAUNE et NOIR.==  أزرق وأرجواني وأصفر وأسود.
# HCL (hue, saturation, lightness)
# RGB (red, green, blue). == (rouge, vert, bleu).

print("valeurs de BGR de pixel [0,0]",img[200,200]) #Pour accéder aux valeurs de chacun des pixels, ([ 71  52 160])  ==> les  données dans l’ordre BGR

largeur = img.shape[0]
hauteur =  img.shape[1]
nbrOctetParpixel = img.shape[2]
tailleImg = img.shape
#print("largeur et hauteur et nbrOctetParpixel",largeur,hauteur, nbrOctetParpixel)

print("Taille de l'image: largeur et hauteur et nbrOctetParpixel ",tailleImg)
print("-->",img[200,200])
print(img[200,200,0])
print(img[200,200,1])
print(img[200,200,2])

tst = img[200,200,0] = 0
tst = img[200,200,1] = 0
print("tst",tst)
print(img[200,200])



#region Extract Red
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j,0] = 0
        img[i,j,1] = 0
cv.imshow('LenaRed', img)
cv.waitKey(500)
#endregion


imgGray = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png',0)
#cv.imshow('imgLenaGray', imgGray)
#cv.waitKey(0)


HLS_img = cv.cvtColor(img, cv.COLOR_BGR2HLS_FULL)
#cv.imshow('HLS_img', HLS_img)
#cv.waitKey(0)

print("HLS Values in [10,10]: ",HLS_img[10,10])
print(HLS_img.shape[0])
print(HLS_img.shape[1])

#region Extract Saturation from HSL Image
for i in range(HLS_img.shape[0]):
    for j in range(HLS_img.shape[1]):
        HLS_img[i,j,0] = 0
        HLS_img[i,j,2] = 0
cv.imshow('Extract saturation S', HLS_img)
cv.waitKey(500)


#region rezize Image
scale = (200, 200)
resizedImage = cv.resize(img, scale, interpolation=cv.INTER_AREA)
cv.imshow('resizedImage', resizedImage)
cv.waitKey(500)
#endregion


ExtractionImg = img[0:200,0:200]

cv.imshow('ExtractionImg', ExtractionImg)
cv.waitKey(0)
