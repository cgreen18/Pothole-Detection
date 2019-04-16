'''
Author: Conor Green
Description: Provides functions to rename files
Usage: Call through another script
Version:
1.0 - April 7 2019 - Final. Copy and pasted from image_manipulation.py v1.6
'''

import os

def rename_all_(path , new_path):
    i = highest_num_image(new_path) + 1

    for filename in os.listdir(path):
        old_file = os.path.join(path,filename)
        new_file = os.path.join(new_path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
        i +=1
    return

def rename_this_many_(path , new_path , count):
    start_pt = highest_num_image(new_path) + 1

    for i in range(start_pt, start_pt + count):
        filename = os.listdir(path)[i]
        old_file = os.path.join(path,filename)
        new_file = os.path.join(new_path, "image" + str(i) + ".jpg")
        os.rename(old_file , new_file)
    return

def highest_num_image(path):
    highest = 0
    for filename in os.listdir(path):
        radix = filename.find(".")
        temp = filename[5:radix]
        if int(temp) > highest:
            highest = int(temp)

    return highest

def main():
    print "error"
    return

if __name__ == "__main__":
    pass
