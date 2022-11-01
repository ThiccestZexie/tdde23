import glob
import random
from typing import Type
import cv2
import math
import numpy


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

    """checks if a pixels HSV values match with a condition and if it does it returns 1 otherwise 0"""

    def is_what(hsv):
        try:
            if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
                return 1
            else:
                return 0
        except TypeError:
            return "Given datatype is not a tuple"
    return is_what

def pixel_constrait_test(): # what should i do with negatives 
    # eftersom HSV kan endast vara mellan 0-255 blir det inte speciellt många extremfall förutom om typ high 

    # tests
    condition1 = pixel_constraint(0, 1,0,1,0,1)
    assert condition1((5,5,5)) == 0
    assert condition1((0,0,0)) == 1
    #base cases
    condition1 = pixel_constraint(50, 150,50,150,50,150)
    assert condition1((63,23,75)) == 0
    assert condition1((70,85,124)) == 1
    assert condition1((123,50, 10)) == 0 



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

    """Gives the BGR value for a pixel after it reads the list of it"""


    def generator(index):
        try:
            if isinstance(index, int):
                return image_as_list[index]
            elif index > len(image_as_list): 
                raise IndexError
        except IndexError:
            return "Given index is out of bounds"
        except TypeError:
            return "Given value is of the wrong type"
    return generator


def generator_from_image_test():
    tuple_list = [(255,0,255),(0,35,1),(0,0,0)]

    generator = generator_from_image(tuple_list)
    for i in range(len(tuple_list)):
        assert generator(i) == tuple_list[i]

def combine_images(mask,  mask_function, image_generator1, image_generator2):  

    """Mask, mask_function is the conditioning to figure out if img1 or img2 is supposed to be used. 
    Creates a list with new values for each pixel from img1 and img2 based on a mask """

    list_colors = []
    try:
        if isinstance(mask, list):
            img1 = [image_generator1(i) for i in range(len(mask))]
            img2 = [image_generator2(i) for i in range(len(mask))]
            condition = pixel_constraint(100, 150, 50, 200, 100, 255) # Should give their own errors has they have their own exceptions
            condition = gradient_condition(mask) # Same
            for A in range(len(mask)):
                if mask_function(A) == 1:
                    list_colors.append(img1[A])
                elif mask_function(A) == 0:
                    list_colors.append(img2[A])
                else:
                    list_colors.append(add_tuples(multiply_tuple(img1[A], condition(A)), multiply_tuple(img2[A], (1-condition(A)))))
            return list_colors
        else:
            raise TypeError
    except IndexError:
        return "Image generators index is larger than len(mask)"
    except TypeError:
        return "Image_generator is a function and not tuples."
    
       

def combine_images_test(): # test base case, and then extreme 
    
    condition = gradient_condition([(1,3,2)])
    gen1 = generator_from_image([(23,21,52)])
    gen2 = generator_from_image([(42,32,64)])
    mask = [(1,3,2)]
    assert combine_images(mask, condition, gen1, gen2) == [(41.809999999999995, 31.89,63.88)]

    try:
        input_list = 'random string'
        combine_images(input_list, condition, gen1, gen2)
    except TypeError:
        return "TypeError"

    mask = [(255,255,255), (0,0,0)]
    conditiona = gradient_condition([(128,128,128), (0,0,0)])
    gen1 = generator_from_image([(255,172,255), (0,0,0)])
    gen2 = generator_from_image([(0,80, 53), (0,0,0)])
    assert combine_images(mask, conditiona, gen1, gen2) == [(255,172,255), (0,0,0)]

   



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
            return "Given index is begger than len(mask)"
        except TypeError:
            return "Given index must be an integer"
    return condition
if __name__ == "__main__":
    generator_from_image_test()
    combine_images_test()
    pixel_constrait_test()
    print("Code passed all the test")

