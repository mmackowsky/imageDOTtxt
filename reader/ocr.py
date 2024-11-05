import tensorflow as tf
from keras.api.models import Sequential
from keras.api.layers import Conv2D, Flatten, MaxPooling2D, Dense
import os
import cv2
import numpy as np


images = []
labels = []

path = '/content/data/training_data'

dir_list = os.listdir(path)
for i in dir_list:
    dir = os.path.join(path, i)
    file_list = os.listdir(dir)
    for j in file_list:
        files = os.path.join(dir, j) # creates the full path to the current image file.
        img = cv2.imread(files) # reads the image using OpenCV.
        img = cv2.resize(img, (64,64)) # resizes the image to a fixed size (64×64 pixels).
        img = np.array(img, dtype=np.float32) # converts the image to a NumPy array with float32 data type.
        img = img/255 # normalizes the pixel values to the range [0, 1].
        images.append(img)
        labels.append(i)

# Converting list to NumPy arrays:

# ‘X’ is a NumPy array containing the preprocessed images. Each element of X is a 3D array representing an image.
X = np.array(images)

# ‘y’ is a NumPy array containing the corresponding labels for each image.
y = np.array(labels)
