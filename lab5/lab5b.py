import glob
import random
import cv2
import math
from cvxopt import mul
import numpy


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

<<<<<<< HEAD
    """Checks if a pixels HSV values matches with a set conditions and returns 1 or 0 depending if it does or not"""

    def pixel_condition(hsv):
=======
    def is_what(hsv):
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
        if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
            return 1
        else:
            return 0
<<<<<<< HEAD
    return pixel_condition
=======
    return is_what
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6


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
<<<<<<< HEAD

    """Returns a list of tuples of a images RGB values"""

=======
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
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
<<<<<<< HEAD
    """Gives BGR value for a pixel after it reads the list of it given a index"""
=======

>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
    def generator(index):
        return image_as_list[index]
    return generator

 
<<<<<<< HEAD
def combine_images(mask, mask_function, image_generator1, image_generator2):  
    """Combine 2 based on a mask with the help of a mask function that decides if img 1 or img 2 should be used or a blend 
    
    Returns a list of the BGR values for each pixel for the new image
    """
=======
def combine_images(mask, mask_function, image_generator1, image_generator2):  # just brute force it ig
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
    list_colors = []
    img1 = [image_generator1(i) for i in range(len(mask))]
    img2 = [image_generator2(i) for i in range(len(mask))]
    for A in range(len(mask)):
        if mask_function(mask[A]) == 1: # sends a tuple
            list_colors.append(img1[A])
        elif mask_function(mask[A]) == 0:
            list_colors.append(img2[A])
        else:
<<<<<<< HEAD
            list_colors.append(add_tuples(multiply_tuple(img1[A], condition(mask[A])), multiply_tuple(img2[A], (1-condition(mask[A])))))
=======
            list_colors.append(add_tuples(multiply_tuple(img1[A], condition(A)), multiply_tuple(img2[A], (1-condition(A)))))
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
    return list_colors


def greyscale_list_to_cvimg(lst, height, width):
    """Return a width x height grayscale OpenCV image with specified pixels."""
    img = numpy.zeros((height, width), numpy.uint8)

    for x in range(0, width):
        for y in range(0, height):
            img[y, x] = lst[y * width + x]

    return img
 

def gradient_condition(mask):
<<<<<<< HEAD
    """Retuns a value for a pixel dependent on RGB value when they all are the same."""
    def condition(index):
        if isinstance(index, tuple):
            (r,g,b) = index
            if r == g == b:
                return r/255
        else:
            return r/255
        
    return condition
=======
    
    def condition(index):
        return round((sum(mask[index])/765), 2) 
    return condition


# Läs in en bild
plane_img = cv2.imread("plane.jpg")
flower_image = cv2.imread('flowers.jpg')
gradient_image = cv2.imread('gradient.jpg')
# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
gradient_image_list = cvimg_to_list((gradient_image))
plane_img_list = cvimg_to_list(plane_img)
flower_img_list = cvimg_to_list(flower_image)
condition = gradient_condition(gradient_image_list)

# Skapa en generator för den inlästa bilden
generator1 = generator_from_image(flower_img_list)
generator2 = generator_from_image(plane_img_list)

mask = gradient_image_list

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
result = combine_images(mask, condition, generator1, generator2)

# Omvandla resultatet till en riktig bild och visa upp den
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
