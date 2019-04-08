'''
Author: Conor Green
Description:
Version:
1.0 - April 7 2019 - Basic functionality to learn libraries
1.1 - April 8 2019 - Added better code structure
1.2 - April 8 2019 - Works as intended. Still requires paramter tuning
1.3 - April 8 2019 - Added daylight or not classification
1.4 - April 8 2019 - Added slideshow functionality
1.5 - April 8 2019 - Fixed bugs, tuned daylight, better coding style
'''
##colorizer.org

import cv2
import matplotlib.pyplot as plt
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

def get_avg_val(hsv_image):
    sum = 0
    h , w , d = hsv_image.shape

    for i in range(0,h):
        for j in range(0,w):
            sum += hsv_image[i,j,2]

    avg_value = sum/(w*h)

    return avg_value

def is_daytime(hsv_image):
    #paramter
    threshold = 120 #/255

    is_day = True

    avg_val = get_avg_val(hsv_image)

    if avg_val < threshold:
        is_day = False

    return is_day

def classify_hsv_image(hsv_image, verbose):
    classification = "not daylight"

    if is_daytime(hsv_image) == True:
        classification = "daylight"


    if verbose == True:
        print classification

    return classification

def get_mask(im_class , im_hsv ):
    if im_class == "daylight":
        return cv2.inRange(im_hsv,(0,0,80),(255,60,150))

    #default
    #elif im_class == "not daylight":
    return cv2.inRange(im_hsv,(0,0,100),(255,150,230))

def clean_noise_(image, (kernel_h , kernel_w) ):
    kernel = np.ones(( kernel_h , kernel_w ));

    image = cv2.erode(image, kernel , iterations=1)

    image = cv2.dilate(image, kernel , iterations =1)

    return image

'''
    Set h = 640 and w = 380
'''
def resize_(image , desired_h , desired_w ):
    im_h , im_w , im_d = image.shape()

    image = cv2.resize(image, () , interpolation = cv2.INTER_AREA)

    return


def process_image(image_path , verbose):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    #hue saturation value
    im_hsv = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    im_class = classify_hsv_image(im_hsv , verbose)

    mask = get_mask(im_class , im_hsv )

    im = cv2.bitwise_and(orig_image,orig_image,mask = mask)

    kernel_dim = ( 100 , 100 )

    filter = clean_noise_(im , kernel_dim)

    filter[filter>0] = 1

    proc_image = orig_image*filter

    return (orig_image , proc_image)

def slideshow_images(path , number , pause_length , verbose):
    for i in range(0,number):
        file_number = i

        image_path = os.path.join(path, "image" + str(file_number) + ".jpg")


        (orig_image, proc_image) = process_image(image_path , verbose = verbose)

        plt.figure()

        plt.subplot(2,1,1)
        plt.imshow(orig_image)

        plt.subplot(2,1,2)
        plt.imshow(proc_image)

        plt.show(block=False)

        time.sleep(pause_length)

        plt.close()

    return

def main():
    additional_path ="bdd100k/images/10k/test"
    current_directory = ""
    data_path = additional_path + current_directory

    new_path = "bdd100k/images/10k/renamed_images"
    #"~/Documents/University/Junior Year/Pothole Detection/bdd100k/images/10k/test"

    count = 20
    verbose = True

    rename_this_many_(data_path , new_path , count)

    slideshow_images(new_path , count , 10 , verbose)

    '''
    Crop image into small rectangle
    cv2.resize()
    '''

    return

if __name__ == "__main__":
    main()
