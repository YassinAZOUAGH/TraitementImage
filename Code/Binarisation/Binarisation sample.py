import cv2
import numpy as np
from numba import cuda
import time
from numba import jit



# image input with applied parameters
# to convert the image in grayscale


#@cuda.jit(device=True)
def binarize(imgGray,threshold):
    for (i,line) in enumerate(imgGray):
        for(j,pixel) in enumerate(line):
            value = imgGray[i][j]
            if value < threshold:
                imgGray[i][j] = 0
            else:
                imgGray[i][j] = 255
    return imgGray



def convert_binary(image_matrix, thresh_val):
    white = 255
    black = 0

    initial_conv = np.where((image_matrix <= thresh_val), image_matrix, white)
    final_conv = np.where((initial_conv > thresh_val), initial_conv, black)

    return final_conv


image1 = cv2.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/Lena.png')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

start = time.time()
binarize(img , 150)
end = time.time()
print('temps excution' ,end - start)

'''
start = time.time()
binarize_GPU(img , 150)
end = time.time()
print('temps excution' ,end - start)
'''


#cv2.imshow('new Lena gray', convert_binary(img , 150))
#cv2.imshow('new Lena gray convert_binary', convert_binary(img , 150))
#cv2.waitKey(0)