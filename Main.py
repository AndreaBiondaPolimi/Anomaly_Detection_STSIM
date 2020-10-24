from ModelCreator import Model
from DataLoader import load_patches, load_patches_from_file
import cv2
import numpy as np
import matplotlib.pyplot as plt

train_patch_size = 24

valid_patch_size = 24
stride = 8

"""
for i in range (1,400):
    if (696 % i == 0):
        print (i)
"""


if __name__ == "__main__":

    train_patches = load_patches('Dataset\\SEM_Data\\Normal', patch_size=train_patch_size, random=True, n_patches=50)

    valid_patches = load_patches_from_file('Dataset\\SEM_Data\\Anomalous\\images\\ITIA1108.tif', patch_size=valid_patch_size, 
        random=False, stride=stride) 

    model = Model('stsim')
    model.model_create(train_patches)
    train = model.database

    density = model.get_distance_density_from_model (valid_patches, density_shape=(640,1024), stride=stride, patch_size=valid_patch_size)
    plt.imshow(density)
    plt.show()
    

