'''
Author: Conor Green
Description:
Version:
1.0 - April 7 2019 - Basic functionality to learn libraries
1.1 - April 8 2019 - Added better code structure
1.2 - April 8 2019 - Works as intended. Still requires paramter tuning
1.3 - April 8 2019 - Added daylight or not classification
'''
##colorizer.org

import cv2
import matplotlib.pyplot as plt
#from plt import plot, subplot, draw,
import numpy as np
import os
import time

def rename_all_(path):
    i = 0
    for filename in os.listdir(path):
        filename = os.listdir(path)[i]
        old_file = os.path.join(path,filename)
        new_file = os.path.join(path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
    return

def rename_this_many_(path , new_path , count):
    for i in range(0, count):
        filename = os.listdir(path)[i]
        old_file = os.path.join(path,filename)
        new_file = os.path.join(new_path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
    return

def is_daytime(hsv_image):
    is_day = True

    h , w , d = hsv_image.shape

    sum = 0
    avg_sum = h*w*50

    for i in range(0,h):
        for j in range(0,w):
            sum += hsv_image[:,:,2][i,j]

    if sum < avg_sum:
        is_day = False

    return is_day

def classify_hsv_image(hsv_image):
    if is_daytime(hsv_image) == True:
        return "daylight"

    return "not daylight"

def process_image(image_path):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    #hue saturation value
    im_hsv = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    if classify_hsv_image(im_hsv) == "daylight":
        mask = cv2.inRange(im_hsv,(0,0,100),(255,60,180))
        print "daylight detected"
    elif classify_hsv_image(im_hsv) == "not daylight":
        mask = cv2.inRange(im_hsv,(0,0,100),(255,150,230))
        print "not daylight detected"

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

    additional_path ="bdd100k/images/10k/test"
    current_directory = ""
    data_path = additional_path + current_directory

    new_path = "bdd100k/images/10k/renamed_images"
    #"~/Documents/University/Junior Year/Pothole Detection/bdd100k/images/10k/test"

    count = 20

    rename_this_many_(data_path , new_path , count)


    #plt.ion()

    for i in range(0,20):
        file_number = i

        image_path = os.path.join(data_path, "image" + str(file_number) + ".jpg")


        (orig_image, proc_image) = process_image(image_path)

        plt.figure()

        plt.subplot(2,1,1)
        plt.imshow(orig_image)

        plt.subplot(2,1,2)
        plt.imshow(proc_image)

        plt.show(block=False)

        time.sleep(4)

        plt.close()

        #cv2.destroyAllWindows()
    return
    #file_number = 0

    image_path = os.path.join(data_path, "image" + str(file_number) + ".jpg")


    (orig_image, proc_image) = process_image(image_path)

    plt.figure()
    plt.subplot(2,1,1)
    plt.imshow(orig_image)

    plt.subplot(2,1,2)
    plt.imshow(proc_image)

    plt.show()

    #cv2.imwrite("image1_modified",target)
    #cv2.imwrite("processed_image.jpg",image2)

    return

if __name__ == "__main__":
    main()
