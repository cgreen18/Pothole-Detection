'''
Author: Conor Green
Description: Provides functionality for segmenting images
Usage: Call functions through other script
Version:
1.0 - April 15 2019 - Created structure
'''


def segment_image(image_path):
    im = cv2.imread(image_path)

    orig_image = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

    im_hsv = cv2.cvtColor(orig_image,cv2.COLOR_BGR2HSV)


    '''
    im_class = classify_hsv_image(im_hsv)

    mask = get_mask(im_class , im_hsv )

    im = cv2.bitwise_and(orig_image,orig_image,mask = mask)

    kernel_dim = ( 20 , 20 )

    filter = clean_noise(im , kernel_dim)

    filter[filter>0] = 1

    proc_image = orig_image*filter
    '''
    #temp
    proc_image = orig_image

    return (orig_image , proc_image)



def main():

    return

if __name__ == "__main__"
