import os
from imutils import paths
import random
import cv2
from keras.preprocessing.image import img_to_array
import numpy as np
data = []
labels = []
imagePaths = sorted(list(paths.list_images("images")))
#print (imagePaths)


# loop over the input images
for imagePath in imagePaths:
	# load the image, pre-process it, and store it in the data list
    

    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)


print (labels)