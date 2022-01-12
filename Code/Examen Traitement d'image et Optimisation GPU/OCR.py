import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread("./image2/Nom.png")

cv2.imshow("Image", img)
text = pytesseract.image_to_string(img)
print(text)

file_object = open('OCRTest.txt', 'a')
file_object.write(text)
file_object.close()

