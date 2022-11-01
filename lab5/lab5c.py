import glob
from msilib.schema import Condition
import random
from typing import Type
import cv2
import math
import numpy


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

    """checks if a pixels HSV values match with a condition and if it does it returns 1 otherwise 0"""

    def is_what(hsv):
        if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
            return 1
        else:
            return 0
    return is_what

def pixel_constrait_test(): # what should i do with negatives 
    # eftersom HSV kan endast vara mellan 0-255 blir det inte speciellt många extremfall förutom om typ high 

    condition1 = pixel_constraint(0,0,0,0,0,0)
    assert condition1((0,0,0)) == 1
    condition1 = pixel_constraint(5, -5,5,-5,5,-5)
    assert condition1((5,5,5)) == 0
    condition1 = pixel_constraint(50, 150,50,150,50,150)
    assert condition1((63,23,75)) == 0
    assert condition1((70,85,124)) == 1
    assert condition1(([123,2],50, 10)) == 0 



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
    list_of_colors = []
    image = filename
    for i in range(image.shape[0]):
        for q in range(image.shape[1]):
            list_of_colors.append(tuple(image[i,q]))

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

    """Gives the BGR value for a given pixels index"""

    def generator(index):
        try:
            if isinstance(index, int): 
                return image_as_list[index]
            else: 
                raise IndexError
        except IndexError:
            return "Given index is out of bounds"
        except TypeError:
            return "Given value is of the wrong type"
    return generator

def generator_from_image_test():
    test = generator_from_image([(0,0,0), (0,0,0)])
    assert test(0) == (0,0,0)
    test = generator_from_image([(128,128,128), (0,0,0)])
    assert test(0) == (0,0,0)

def combine_images(mask,  mask_function, image_generator1, image_generator2): 

    """Mask, mask_function is the conditioning to figure out if img1 or img2 is supposed to be used. 
    Creates a list with new values for each pixel from img1 and img2 based on a mask """

    list_colors = []
    condition = gradient_condition(mask)
    try:

            img1 = [image_generator1(i) for i in range(len(mask))] # behöver inte köra på resten av koden då om detta fungerar inte då körs inte resterande. 
            img2 = [image_generator2(i) for i in range(len(mask))] # problem när den är out of bounds 
          # what to do if a string gets put in :()
    except IndexError:
        return "Image generators index is larger than len(mask)"
    except TypeError:
        return "Image_generator has non tuples."
    else:
        if not (len(mask) == len(img1) or len(mask) == len(img2)):
            raise IndexError
        else:
            for A in range(len(mask)):
                if mask_function(A) == 1:
                    list_colors.append(img1[A])
                elif mask_function(A) == 0:
                    list_colors.append(img2[A])
                else:
                    list_colors.append(add_tuples(multiply_tuple(img1[A], condition(A)), multiply_tuple(img2[A], (1-condition(A)))))
        return list_colors


def combine_images_test(): # test base case, and then extreme 

    condition = gradient_condition([(1,3,2)])
    gen1 = generator_from_image([(23,21,52)])
    gen2 = generator_from_image([(42,32,64)])
    mask = [(1,3,2)]

    
    assert combine_images(mask, condition, gen1, gen2) == [(41.809999999999995, 31.89,63.88)]

    mask = [(255,255,255)]
    conditiona = gradient_condition([(128,128,128), (0,0,0)])
    gen1 = generator_from_image([(255,172,255), (0,0,0)])
    gen2 = generator_from_image([(0,80, 53), (0,0,0)])
    return combine_images(mask, conditiona, gen1, gen2) #== [(255,172,255), (0,0,0)]


def greyscale_list_to_cvimg(lst, height, width):
    """Return a width x height grayscale OpenCV image with specified pixels."""
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y, x] = lst[y * width + x]

    return img
 

def gradient_condition(mask):

    """Returns what conditon a pixel is on. If its BGR value is 255,255,255 it returns 1 otherwise between 1-0"""

    def condition(index):
        try:
            if isinstance(mask[index], tuple) and len(mask[index]) == 3:
                return round((sum(mask[index])/765),2) 
            else:
                raise TypeError
        except IndexError:
            return "Given index is larger than len(mask)"
        except TypeError:
            return "Given 'index' must be an integer or instance must be a tuple"
    return condition

print(combine_images_test())