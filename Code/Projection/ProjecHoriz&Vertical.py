import os
import numpy as np
import cv2


def getVProjection(image):
    #  The image image is converted to a black and white two-value map, and the RET receives the current threshold, the two-value chart of the output of the output
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    (h, w) = thresh1.shape  # Return high and wide
    a = [0 for z in range(0,
                          w)]  # A = [0, 0, 0, ..., 0, 0] initializes an array of length W for recording the number of black points of each column

    # Record the peak of each column
    for j in range(0, w):  # Traverse one column
        for i in range(0, h):  # Traverse
            if thresh1[i, j] == 0:  # If this point is black
                a[j] += 1  # The column's counter adds a count
                print(a[j])
                thresh1[i, j] = 255  # After the record is finished, it will be white.

    for j in range(0, w):  # Traverse each column
        for i in range((h - a[j]),
                       h):  # From the top of this column, the top of the black is started to be blacked to the bottom
            thresh1[i, j] = 0  # Black

    cv2.imshow('Vimage', thresh1)


def getHProjection(image):
    # The image image is converted to a black and white two-value map, and the RET receives the current threshold, the two-value chart of the output of the output
    ret, thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    (h, w) = thresh1.shape  # Return high and wide
    a = [0 for z in range(0,
                          h)]  # A = [0, 0, 0, ..., 0, 0] initializes an array of length h, used to record the number of black spots of each line

    # Record the peak of each line
    for j in range(0, h):  # Traverse
        for i in range(0, w):  # Traverse one column
            if thresh1[j, i] == 0:  # If this point is black
                a[j] += 1  # The column's counter adds a count
                thresh1[j, i] = 255  # After the record is finished, it will be white.

    for j in range(0, h):  # Traverse every line
        for i in range(a[j]):  # From the top of this line, the number of black dots were burned to the right.
            thresh1[j, i] = 0  # Black

    cv2.imshow('Himage', thresh1)


if __name__ == '__main__':

    #img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
    img = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/Sudoko.PNG')
    cv2.imshow("image",img)
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #Convert IMG images to grayscale, output to grayimage
    getVProjection(GrayImage)  #Call the getvprojection function to perform vertical projection
    getHProjection(GrayImage)  #Call the gethprojection function to make a horizontal projection
    cv2.waitKey(0)
    cv2.destroyAllWindows()
