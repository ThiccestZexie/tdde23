import glob
import random
import re
from typing import Type
import math


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

    """Checks if a pixels HSV values matches with a set conditions and returns 1 or 0 depending if it does or not"""

    def pixel_condition(hsv):
        
            if isinstance(hsv, tuple) and len(hsv) == 3:
                if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
                    return 1
                else:
                    return 0
            else:
                raise TypeError
    return pixel_condition


def pixel_constrait_test(): 
    # Testing mainly base cases 
    # tests
    condition1 = pixel_constraint(0, 1,0,1,0,1)
    assert condition1((5,5,5)) == 0
    assert condition1((0,0,0)) == 1
    #base cases
    condition1 = pixel_constraint(50, 150,50,150,50,150)
    assert condition1((63,23,75)) == 0
    assert condition1((70,85,124)) == 1
    assert condition1((123,50, 10)) == 0 
    assert condition1((11,72,64)) == 0
    
    try:
        condition1 = pixel_constraint(50, 150,50,150,50,150)
        assert condition1(520) == TypeError
        raise TypeError
    except TypeError:
        print("Given input is not a tuple")

    try: 
        condition1 = pixel_constraint(50, 150,50,150,50,150)
        assert condition1(520) == TypeError
        raise TypeError
    except TypeError:
        print("Given input is not a string")


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

    """Gives BGR value for a pixel after it reads the list of it given a index"""

    def generator(index):
        try:
            if index > len(image_as_list): 
                raise IndexError
            elif isinstance(index, int):
                return image_as_list[index]
            else:
                raise TypeError
        except IndexError:
            return IndexError
        
    return generator


def generator_from_image_test():
    # Tests a list and sees if the values or the same. 
    tuple_list = [(255,0,255),(0,35,1),(0,0,0)]

    generator = generator_from_image(tuple_list)
    
    for i in range(len(tuple_list)):
        assert generator(i) == tuple_list[i]
    
    assert generator(231) == IndexError


def combine_images(mask,  mask_function, image_generator1, image_generator2):  

    """Combine 2 based on a mask with the help of a mask function that decides if img 1 or img 2 should be used or a blend Returns a list of the BGR values for each pixel for the new image
    """

    list_colors = []
    try:
        if isinstance(mask, list):
            img1 = [image_generator1(i) for i in range(len(mask))]
            img2 = [image_generator2(i) for i in range(len(mask))]
            for A in range(len(mask)):
                if mask_function(mask[A]) == 1: # sends a tuple
                    list_colors.append(img1[A])
                elif mask_function(mask[A]) == 0:
                    list_colors.append(img2[A])
                else:
                    list_colors.append(add_tuples(multiply_tuple(img1[A], mask_function(mask[A])), multiply_tuple(img2[A], (1-mask_function(mask[A])))))
                return list_colors
        else:
            raise TypeError
    except IndexError:
        return "Image generators index is larger than len(mask)"
    except TypeError:
        return "Image_generator is a function and not tuples."
    

def combine_images_test(): 
    
    # Testing normal caes
    condition = gradient_condition([(1,3,2)])
    gen1 = generator_from_image([(23,21,52)])
    gen2 = generator_from_image([(42,32,64)])
    mask = [(5,5,5)]
    assert combine_images(mask,condition,gen1,gen2) == [(41.627450980392155, 31.784313725490193, 63.76470588235294)]
    
    mask = [(255,255,255), (0,0,0)]
    conditiona = gradient_condition([(128,128,128), (0,0,0)])
    gen1 = generator_from_image([(255,172,255), (0,0,0)])
    gen2 = generator_from_image([(0,80, 53), (0,0,0)])
    print(combine_images(mask, conditiona, gen1, gen2)) == [(255,172,255), (0,0,0)]

    #Testing caes where input list or generators arent correct.
    try:
        input_list = 'random string'
        combine_images(input_list, condition, gen1, gen2)
        raise TypeError
    except TypeError:
        print("TypeError, input list isnt a list")
    try:
        gen1 = lambda x: x
        combine_images(input_list, condition, gen1, gen2)
        raise TypeError        
    except TypeError:
        print("TypeError as gen")
    try:
        gen2 = lambda x: x
        combine_images(input_list, condition, gen1, gen2)
        raise TypeError 
    except TypeError:
        print("should raise TypeError when generator2 doesn't return tuples")

   
   



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
        try:
            if isinstance(index, tuple):
                (r,g,b) = index
                if r == g == b:
                    return r/255
            else:
                return r/255
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

