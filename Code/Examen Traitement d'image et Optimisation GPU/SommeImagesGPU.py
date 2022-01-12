from numba import jit, cuda
import numpy as np
import cv2 as cv
import time

# Somme de deux images
def cuda_sum_images(imgA,imgB):
    # On récupère les dimensions des deux images
    hauteurA,largeurA,dimA = imgA.shape
    hauteurB,largeurB,dimB = imgB.shape
    
    # On garde les dimensions minimum
    min_w = min(largeurA,largeurB)
    min_h = min(hauteurA,hauteurB)
    print(min_w,min_h) # 481 512 --> 480 512 

    min_w -= 1 # On supprime une ligne de pixel pour obtenir 480 divisible pour que ça soit divisble par 32
    # 512 divisible par 32

    # Création d'une matrice résultat
    result = np.empty((min_h,min_w,dimA)).astype(dtype=np.uint8)
    
    tpbx = None #thread per block x
    tpby = None #thread per block x

    threads_per_block_dimensions = [32]  # 32 thread par block
    # ça dépend de la dimension de l'image qu'on a
    for d in (threads_per_block_dimensions): # determiner les dimensions de threads
        if result.shape[0] % d == 0:
            tpbx = d

        if result.shape[1] % d == 0:
            tpby = d

    threads_per_block = (tpbx, tpby)
    # Combien de blocks dans le grid ? 
    bpgx = int(np.ceil(result.shape[0])/threads_per_block[0])
    bpgy = int(np.ceil(result.shape[1])/threads_per_block[1])
    blocks_per_grid = (bpgx, bpgy)
    
    # On envoie la matrice resultat au GPU
    d_result = cuda.to_device(result)


    # Copie des matrice images du Host vers le Device ( gpu )
    d_imgA = cuda.to_device(imgA)
    d_imgB = cuda.to_device(imgB)
    
    # On applique la fonction optimisé sur chaque pixel
    cuda_sum_images_pixel[blocks_per_grid, threads_per_block](d_imgA,d_imgB,d_result)
    
    # On retourne le résultat du gpu vers le host
    result = d_result.copy_to_host()
    # On retourne le résultat final
    return result

# Fonction qui va s'appliquer sur chaque pixel
@cuda.jit
def cuda_sum_images_pixel(imgA,imgB,result):
    i, j = cuda.grid(2)
    if i < result.shape[0] and j < result.shape[1]:        
        b = int(imgA[i,j][0]/2+imgB[i,j][0]/2)
        g = int(imgA[i,j][1]/2+imgB[i,j][1]/2)
        r = int(imgA[i,j][2]/2+imgB[i,j][2]/2)
        result[i, j][0] = b
        result[i, j][1] = g
        result[i, j][2] = r


imgA = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExamenImg0.png')
imgB = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExamenImg1.png')

NewDim = (481, 512)
resizedImageA = cv.resize(imgA, NewDim, interpolation=cv.INTER_AREA)
resizedImageB = cv.resize(imgB, NewDim, interpolation=cv.INTER_AREA)

start = time.time()
imgR = cuda_sum_images(resizedImageA,resizedImageB)
end = time.time()
print('temps excution' ,end - start)
cv.imshow("Somme", imgR)
cv.waitKey(0)