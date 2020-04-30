# Yasir Hassan
# CS 4332 AI
# Project 2 - Face Detection
# This program builds video from
# frame-images, in a processed “P2E_S5_C1” file.
# The program utilizes the python programming
# language, opencv, and numpy libraries.
# I run this program with python 3.7 version

# import the libraries
import cv2         # for opencv
import numpy as np # for numpy
import glob        # for fetching the image-file
 
img_array = [] # an array to store the images

# use for-loop to loop over all the images
# in the .jpg file.
# glob.glob(Pathname) fetches all the filenames
# present in the file path...*jpg’ means all the jpg images.
for filename in glob.glob('C:/Users/NeverGiveUp/Desktop/AI Out/P2E_S5_C1.1/*.jpg'):
    
    #Read each image using cv2.imread()              
    img = cv2.imread(filename)

    # get the shape of the image
    height, width, layers = img.shape
    size = (width,height)

    # Store the image into the list
    img_array.append(img)
 
# initialize a video writer
out = cv2.VideoWriter('project2.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

# read each image and then display it. 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

