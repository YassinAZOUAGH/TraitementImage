# importing the module
import cv2

def binarize(imgGray,threshold):
    for (i,line) in enumerate(imgGray):
        for(j,pixel) in enumerate(line):
            value = imgGray[i][j]
            if value < threshold:
                imgGray[i][j] = 0
            else:
                imgGray[i][j] = 255
    return imgGray

def click_event(event, x, y, flags, params):

	# click gauche
	if event == cv2.EVENT_LBUTTONDOWN:
		# affichage des cordonnees
		print(x, ' ', y)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font,
					1, (255, 0, 0), 2)
		cv2.imshow('image', img)

def ExtractImgs():
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			Iban2 = img[263:307, 79:335]
			Date = img[122:154, 11:87]
			Nom = img[197:234, 82:289]
			Assurance = img[341:378, 87:259]
			Iban1 = img[157:195, 83:326]
			Facture = img[414:452, 88:258]
			Montant = img[118:145, 404:487]

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
	#image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExamenImg.png')
	image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExamenImg2.png')
	NewDim = (500, 500)
	resizedImage = cv2.resize(image1, NewDim, interpolation=cv2.INTER_AREA)
	imgGray = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
	cv2.imshow('imageBinarized', binarize(imgGray,150))
	cv2.imwrite('MyImg.png', binarize(imgGray,150))

	img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Code/Examen/MyImg.png')
	cv2.imshow('image', img)
	cv2.setMouseCallback('image', click_event)
	cv2.waitKey(0)
	ExtractImgs()




