'''
Author: Conor Green
Description: Provides functionality for segmenting images
Usage: Call functions through other script
Version:
1.0 - April 15 2019 - Created structure
1.1 - April 21 2019 - Added many functions. Compiles and nearly operates as intended
1.2 - April 22 2019 - Further modified the segmentation and filtering
'''

import cv2

def get_avg_val(hsv_image):
    sum = 0
    h , w , d = hsv_image.shape

    for i in range(0,h):
        for j in range(0,w):
            sum += hsv_image[i,j,2]

    avg_value = sum/(w*h)

    return avg_value

def perform_average_on_image(hsv_image):
    avg = get_avg_val(hsv_image)

    h , w , d = hsv_image.shape

    for i in range(0,h):
        for j in range(0,w):
            hsv_image[i,j,2] = int(hsv_image[i,j,2] / avg)

    return hsv_image

def extract_road(hsv_image):

    averaged_hsv_image = hsv_image # perform_average_on_image(hsv_image)

    mask = cv2.inRange(averaged_hsv_image,(0,0,0),(255,60,150))

    filter = cv2.bitwise_and(hsv_image,hsv_image,mask = mask)

    filter[filter > 0] = 1

    proc_image = hsv_image*filter

    return (proc_image , filter )

def segment_filter(filter):
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

def segment_im_file(image_path):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    hsv_image = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)

    (proc_hsv_image , im_filter ) = extract_road(hsv_image)
    proc_image = cv2.cvtColor(proc_hsv_image , cv2.COLOR_HSV2RGB)

    bounds = segment_filter(im_filter)


    return (orig_image , proc_image , bounds)


def main():

    return

if __name__ == "__main__":
    pass
