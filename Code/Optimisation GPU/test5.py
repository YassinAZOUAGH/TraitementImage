import  cv2

img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png', cv2.IMREAD_GRAYSCALE)
src = cv2.cuda_GpuMat()
src.upload(img)

clahe = cv2.cuda.createCLAHE(clipLimit=5.0, tileGridSize=(8, 8))
dst = clahe.apply(src, cv2.cuda_Stream.Null())

result = dst.download()

cv2.imshow("result", result)
cv2.waitKey(0)