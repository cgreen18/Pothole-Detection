'''
Author: Conor Green
Description: Provides functionality for segmenting images
Usage: Call functions through other script
Version:
1.0 - April 15 2019 - Created structure
1.1 - April 21 2019 - Added many functions. Compiles and nearly operates as intended
1.2 - April 22 2019 - Further modified the segmentation and filtering
1.3 - April 22 2019 - Added averaging and better file manipulation.
'''

import cv2
import os
import numpy
#import matplotlib.pyplot as plt

def perform_average_on_image(hsv_image):
    h , w , d = hsv_image.shape

    mod_hsv_image = numpy.copy(hsv_image)

    mean , std = cv2.meanStdDev(hsv_image)

    for i in range(0,h):
        for j in range(0,w):
            for k in range (0,d):
                mod_hsv_image[i,j,k] = int((hsv_image[i,j,k] - mean[k]) / std[k])

    return mod_hsv_image

def extract_road(hsv_image):

    averaged_hsv_image = perform_average_on_image(hsv_image)

    mask = cv2.inRange(averaged_hsv_image,(0,0,0),(255,60,150))

    filter = cv2.bitwise_and(hsv_image,hsv_image,mask = mask)

    filter[filter > 0] = 1

    proc_image = hsv_image*filter

    return (proc_image , filter )

def segment_filter(filter):
    #cv2.countNonZero(filter[:,i,1])


    threshold = .5  #50%

    h , w , d = filter.shape

    x_low = 0
    x_high = w
    y_low = 0
    y_high = h

    search_left = True

    for i in range( 0 , w):
        run_sum = 0
        limit = h*3*threshold

        run_sum = sum(sum(filter[:,i,:]))

        if run_sum > limit and search_left == True:
            x_low = i

        if run_sum < limit and search_left == False:
            x_high = i

    for j in range( 0 , h):
        run_sum = 0
        limit = w*3*threshold

        run_sum = sum(sum(filter[j,:,:]))

        if run_sum > limit and search_left == True:
            y_low = j

        if run_sum < limit and search_left == False:
            y_high = j


    bounds = (x_low , y_low , x_high , y_high)

    return bounds

def get_connected_pts():


    return

def segment_im_file(image_path):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    hsv_image = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    (proc_hsv_image , im_filter ) = extract_road(hsv_image)
    proc_image = cv2.cvtColor(proc_hsv_image , cv2.COLOR_HSV2RGB)

    bounds = segment_filter(im_filter)

    return (orig_image , proc_image , bounds)

def get_pics_folder():
    current_directory = os.getcwd()

    #additional_path ="/bdd100k/images/100k/test"
    #data_path = current_directory + additional_path

    #addition_path_new = "/renamed_images"
    #new_path = current_directory + addition_path_new

    path = os.path.join(current_directory + "/renamed_images/")

    return path

def path_of_pic(number):
    path = get_pics_folder()

    pic_path = os.path.join( path + "image" + str(number) + ".jpg" )

    return pic_path

def get_rgb_from_path(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    return image

def get_hsv_from_path(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)

    return image

def main():

    return

if __name__ == "__main__":
    pass
