import cv2 as cv

def SinCityEffect(filename):
    bgr = cv.imread(filename)
    B = bgr[:, :, 0]
    G = bgr[:, :, 1]
    R = bgr[:, :, 2]
    H = 0
    for x in range(bgr.shape[0]):
        for y in range(bgr.shape[1]):
            Cmax = max(R[x][y], G[x][y], B[x][y])
            Cmin = min(R[x][y], G[x][y], B[x][y])
            Delta = (float)(Cmax - Cmin)
            if Delta == 0:  # Hue
                H = 0
            elif Cmax == R[x][y]:
                tmp = ((G[x][y] - B[x][y]) / Delta)
                if tmp < 0:
                    H = 60 * (tmp + 6)
                else:
                    H = 60 * tmp
            elif Cmax == G[x][y]:
                H = 60 * (((B[x][y] - R[x][y]) / Delta) + 2.0)
            elif Cmax == B[x][y]:
                H = 60 * ((R[x][y] - G[x][y] / Delta) + 4.0)
            print(H)
            if 3 <= H <= 344:
                R[x][y] = Cmin
                G[x][y] = Cmin
                B[x][y] = Cmin

    return bgr

img = SinCityEffect('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/SinCity.jpg')
cv.imshow("SinCity",img)
cv.waitKey(0)