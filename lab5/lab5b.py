import glob
import random
import cv2
import math
from cvxopt import mul
import numpy


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """Checks if a pixels HSV values matches with a set conditions and returns 1 or 0 depending if it does or not"""

    def pixel_condition(hsv):
        if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
            return 1
        else:
            return 0
    return pixel_condition


def multiply_tuple(tpl, mult):
    """Return a tuple where all elements are scaled by factor 'mult'.

    (a,b,c) * k = (a*k, b*k, c*k)
    """
    return tuple(map(lambda x: x*mult, tpl))


def add_tuples(tpl1, tpl2):
    """
    Return a the element-wise sum of tpl1 and tpl2.

    (a,b,c) + (d,e,f) = (a+d, b+e, c+f)
    """
    return tuple(map(lambda t1, t2: t1+t2, tpl1, tpl2))



def cvimg_to_list(filename):
    """Returns a list of tuples of a images RGB values"""

    list_of_colors = []
    image =  filename
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            list_of_colors.append(tuple(image[x,y]))

    return list_of_colors
    

def rgblist_to_cvimg(lst, height, width):
    """Return a width x height OpenCV image with specified pixels."""
    # A 3d array that will contain the image data
    img = numpy.zeros((height, width, 3), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            pixel = lst[y * width + x]
            img[y, x, 0] = pixel[0]
            img[y, x, 1] = pixel[1]
            img[y, x, 2] = pixel[2]

    return img


def generator_from_image(image_as_list):
    """Gives BGR value for a pixel after it reads the list of it given a index"""
    def generator(index):
        return image_as_list[index]
    return generator

 
def combine_images(mask, mask_function, image_generator1, image_generator2):  
    """Combine 2 based on a mask with the help of a mask function that decides if img 1 or img 2 should be used or a blend 
    
    Returns a list of the BGR values for each pixel for the new image
    """
    list_colors = []
    img1 = [image_generator1(i) for i in range(len(mask))]
    img2 = [image_generator2(i) for i in range(len(mask))]
    for index in range(len(mask)):
        if mask_function(mask[index]) == 1: # sends a tuple
            list_colors.append(img1[index])
        elif mask_function(mask[index]) == 0:
            list_colors.append(img2[index])
        else:
            list_colors.append(add_tuples(multiply_tuple(img1[index], mask_function(mask[index])), multiply_tuple(img2[index], (1-mask_function(mask[index])))))
    return list_colors


def greyscale_list_to_cvimg(lst, height, width):
    """Return a width x height grayscale OpenCV image with specified pixels."""
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y, x] = lst[y * width + x]

    return img
 

def gradient_condition(mask):
    """Retuns a value for a pixel dependent on RGB value when they all are the same."""
    def condition(index):
        if isinstance(index, tuple):
            (r,g,b) = index
            if r == g == b:
                return r/255
        else:
            return index/255
        
    return condition
