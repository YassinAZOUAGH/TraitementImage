import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
import copy
import time

def pixel_neighborhood(image,mask_dimension,actual_pixel_x,actual_pixel_y):
    actual_pixel = image[actual_pixel_x][actual_pixel_y]
    new_matrix = [[None for i in range(mask_dimension)]
                    for j in range(mask_dimension)]

    matrix_index = int((mask_dimension-1)/2)    
    line = 2*matrix_index
    column = 0
    for i in range(-matrix_index,2*matrix_index,1):
        for j in reversed(range(-matrix_index,2*matrix_index,1)):
            try:
                if actual_pixel_x+i < 0 or actual_pixel_y+j < 0:
                    pass
                else:
                    new_matrix[line][column] = image[actual_pixel_x+i][actual_pixel_y+j]
                    line-=1
                    if line < 0 :
                        line = 2*matrix_index
            except Exception as e:
                new_matrix[line][column] = None
        column += 1 
        if  column > 2*matrix_index:
            column = 0

    return new_matrix

def erosion_image(binarized_image):
    eros_image = np.copy(binarized_image)
    option = 'cross'
    for (i,row) in enumerate(binarized_image):
        for (j,pixel) in enumerate(row):
            if pixel == 0:
                try:
                    neighborhood_matrix = pixel_neighborhood(binarized_image, 3, i, j)
                    if option == 'cross':
                        neighborhood_matrix[0][0] = None
                        neighborhood_matrix[0][2] = None
                        neighborhood_matrix[2][0] = None
                        neighborhood_matrix[2][2] = None
                    
                    values = neighborhood_matrix[0] + neighborhood_matrix[1] + neighborhood_matrix[2]
                    if all(((element == 0) or (element == None) for element in values)):
                        pass
                    else:
                        eros_image[i][j] = 255
                except Exception as e :
                    input(e)
    return eros_image

#image = cv.imread("Exercices\\testImages\\Planimeter.png")
image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/Planimeter.png')
#image = cv.imread('C:/Users/yassi/Documents/GitHub/TraitementImage/testImages/ExemenImg.png')
scale_percent = 10
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dsize = (width, height)
output = cv.resize(image, dsize)

grayed_image = cv.cvtColor(output, cv.COLOR_BGR2GRAY)

ret, binarized_image = cv.threshold(grayed_image, 180, 255, 
                                   cv.THRESH_BINARY)    

cv.imshow("binarized_image",binarized_image)

# Création d'une matrice qui va contenir tous les labels
rows_length = binarized_image.shape[0]
columns_length = binarized_image.shape[1]

l = [ [ None for i in range(columns_length) ] for j in range(rows_length) ]

labelized_image= np.array([np.array(xi) for xi in l])

# Creating kernel
kernel = np.ones((3, 3), np.uint8)


square_ref_image = output[int(rows_length/1.19):,:int(columns_length/4)]
cv.imshow("square_ref_image", square_ref_image)
cv.waitKey(0)
square_ref_image_binarized = binarized_image[int(rows_length/1.19):,:int(columns_length/4)]
cv.imshow("square_ref_image_binarized", square_ref_image_binarized)
cv.waitKey(0)

pixel_counter = 0
pixel_counter_tmp = 0
# On determine longueur du côté du carré
for (i,row) in enumerate(square_ref_image_binarized):
    for (j,pixel) in enumerate(row):
        if pixel == 0:
            pixel_counter_tmp += 1
    if pixel_counter_tmp > pixel_counter :
        pixel_counter = pixel_counter_tmp
        kept_row_index = i
    pixel_counter_tmp = 0


print("Un côté de 2 cm vaut : ",pixel_counter,"pixels")
pixel_cote = 2/pixel_counter


# On labelise les objets
same_labels = []
objects_counter = 0

for (i,row) in enumerate(binarized_image):
    for(j,pixel) in enumerate(row):
        if pixel == 0 :
            # Check voisinage 
            neighborhood_labelized_matrix = pixel_neighborhood(labelized_image,3,i,j)
            neighborhood_labelized_matrix = neighborhood_labelized_matrix[:-1] # On enlève la dernière ligne
            neighborhood_labelized_matrix[0][0] = None # Haut gauche
            neighborhood_labelized_matrix[0][2] = None # Haut droite
            neighborhood_labelized_matrix[1][1] = None # Milieu
            neighborhood_labelized_matrix[1][2] = None # Droit
            
            neighborhood_values = [] 
            for r in neighborhood_labelized_matrix :
                neighborhood_values += r
            
            # On supprime les None
            neighborhood_values = [ i for i in neighborhood_values if i!=None ]
            
            if len(neighborhood_values) > 0:
                neighborhood_values = list(set(neighborhood_values))
                
                labelized_image[i][j] = min(neighborhood_values)

                # On fait le lien entre les labels dans la liste, puisqu'ils sont équivalents
                found_sublist = False
                for val in neighborhood_values:
                    for (k,subList) in enumerate(same_labels):
                        if val in subList:
                            found_sublist = True
                            same_labels[k] = list(set(same_labels[k] + neighborhood_values))
                            for (l,subList) in enumerate(same_labels):
                                if l != k and any(i in same_labels[k] for i in subList) :       
                                    same_labels[k] = list(set(same_labels[k] + same_labels[l])) 
                                    same_labels[l].clear()
                            break
                    else:
                        continue
                    break
            
            else:             
                objects_counter += 1
                labelized_image[i][j] = objects_counter
                same_labels.append([objects_counter])

class Label: 
    def __init__(self,label):
        self.label = label
        self.from_row = None
        self.from_column = None
        self.to_row = None
        self.to_column = None
        self.pixels_count_inside = 0
        self.color = None


indices_labels  = [] # Va contenir les labels minium de chaque liste de labels communs
labels = [] # Va contenir les classes Label qui contiendront les cadres de délimitations
colors = [] # Va contenir des couleurs aléatoires attribuées à chaque objet

for (i,row) in enumerate(labelized_image):
    for(j,label) in enumerate(row):
        if label != None:
            for same_label in same_labels:
                if len(same_label) > 0 :
                    if label in same_label:
                        labelized_image[i][j] = min(same_label)

for same_label in same_labels:
    if len(same_label) > 0 :
        kept_min_label = min(same_label)
        new_label = Label(kept_min_label)
        labels.append(new_label)
        indices_labels.append(kept_min_label)
        color1 = (list(np.random.choice(range(256), size=3)))  
        color =[int(color1[0]), int(color1[1]), int(color1[2])] 
        colors.append(color)
        new_label.color = color

for (i,row) in enumerate(labelized_image):
    for(j,label) in enumerate(row):
        if label != None:
            count = np.count_nonzero(labelized_image == label)
            ok = indices_labels.index(label)
            color = colors[indices_labels.index(label)]
            output[i][j] = color

cv.imshow("Image", output)    
cv.waitKey(0)

for (i,row) in enumerate(labelized_image):
    for(j,label) in enumerate(row):
        if label != None:
            index = indices_labels.index(label)
            if labels[index].from_row == None or i < labels[index].from_row  : 
                labels[index].from_row = i
            
            elif labels[index].to_row == None or i > labels[index].to_row :
                labels[index].to_row = i
            
            if labels[index].from_column == None or j < labels[index].from_column:
                labels[index].from_column = j            
            elif labels[index].to_column == None or j > labels[index].to_column :
                labels[index].to_column = j
            
kept_labels = []

# Calcul des surfaces en croppant ( carré, on ne suit pas exactement la forme)
start = time.time()
for (i,label) in enumerate(labels):
    if None not in [label.from_row,label.to_row,label.from_column,label.to_column] :
        if label.to_row-label.from_row > 40 and label.to_column-label.from_column > 40:  
            height = label.to_row-label.from_row
            width = label.to_column-label.from_column
            labels[i].pixels_count_inside = width * height  
            surface = (width * height) * (pixel_cote * pixel_cote)
            image_label = output[label.from_row:label.to_row,label.from_column:label.to_column]
            cv.imshow("Label : "+ str(surface)+" cm^2", image_label)    
            cv.waitKey(0)
    else:
        labels[i] = None

cv.imshow("Image", output)    
cv.waitKey(0)
end = time.time()
elapsed = end - start
print(f'Temps d\'exécution : {elapsed:.2}ms')