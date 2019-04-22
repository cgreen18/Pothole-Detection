'''
Author: Conor Green
Description: Serves as test harness for image_manipulation.py
Version:
1.0 - April 8 2019 - General structure
1.1 - April 15 2019 - Better involves paths and current directories
1.2 -`April 22 2019 - Interacts with image_segmentation.py better`
'''

import os
import cv2
import matplotlib.pyplot as plt
import time

import renaming_files as rename
import image_manipulation as imman
import image_segmentation as imseg


def get_pics_folder():
    current_directory = os.getcwd()

    #additional_path ="/bdd100k/images/100k/test"
    #data_path = current_directory + additional_path

    #addition_path_new = "/renamed_images"
    #new_path = current_directory + addition_path_new

    path = os.path.join(current_directory + "/renamed_images/")

    return path

def path_of_pic( number):
    path = get_pics_folder()

    pic_path = os.path.join( path + "image" + str(number) + ".jpg" )

    return pic_path

def plot_orig_and_proc(orig , proc, pause):
    plt.figure()

    plt.subplot(2,1,1)
    plt.imshow(orig)

    plt.subplot(2,1,2)
    plt.imshow(proc)

    plt.show(block=False)

    time.sleep(pause)

    plt.close()

    return

def main():
    image_x_path = path_of_pic(20)

    (image_x , proc_image_x , bounds) = imseg.segment_im_file(image_x_path)

    plot_orig_and_proc(image_x , proc_image_x , 5)

    return

if __name__ == "__main__":
    main()
