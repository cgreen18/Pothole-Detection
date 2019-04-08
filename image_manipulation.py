'''
Author: Conor Green
Description:
Version:
1.0 - April 7 2019 - Basic functionality to learn libraries
1.1 - April 8 2019 - Added better code structure

'''

##colorizer.org

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


#Renames file number num in path
def rename_file( path , num , new_name ):
    file = os.listdir(folder)[file_number]
    return

def rename_all_(path):
    i = 0
    for filename in os.listdir(path):
        os.rename(filename,"image" + str(i) )
        i += 1
    return

def rename_this_many_(path , count):
    for i in range(0, count):
        filename = os.listdir(path)[i]
        old_file = os.path.join(path,filename)
        new_file = os.path.join(path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
        #os.rename(filename,"image" + str(i))
    return

def process_image(image_path):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    #hue saturation value
    im_hsv = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    #allow values of hue 0-14 , saturation 100-255 and value 100-255
    mask = cv2.inRange(im_hsv,(0,0,100),(255,60,180))

    im = cv2.bitwise_and(orig_image,orig_image,mask = mask)

    kernel = np.ones((12,12));
    im = cv2.erode(im, kernel, iterations=1)

    filter = cv2.dilate(im,kernel,iterations =1)

    filter[filter>0] = 1

    proc_image = orig_image*im

    return (orig_image , proc_image)

def main():
    current_directory = ""
    additional_path = current_directory + "bdd100k/images/10k/test"
    #"~/Documents/University/Junior Year/Pothole Detection/bdd100k/images/10k/test"

    count = 5

    rename_this_many_(additional_path , count)

    file_number = 0
    image_path = "image" + str(file_number) + ".jpg"

    (orig_image, proc_image) = process_image(image_path)

    plt.figure()
    plt.subplot(2,1,1)
    imshow(orig_image)

    plt.subplot(2,1,2)
    imshow(proc_image)


    #cv2.imwrite("image1_modified",target)
    #cv2.imwrite("processed_image.jpg",image2)

    return

if __name__ == "__main__":
    main()
