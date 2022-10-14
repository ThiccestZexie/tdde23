import glob
from msilib.schema import Condition
import random
from typing import Type
import cv2
import math
from cv2 import imread
import numpy


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):

    """checks if a pixels HSV values match with a condition and if it does it returns 1 otherwise 0"""

    def is_what(hsv):
        if vlow <= hsv[2] <= vhigh and hlow <= hsv[0] <= hhigh and slow <= hsv[1] <= shigh:
            return 1
        else:
            return 0
    return is_what


def cvimg_to_list(filename):
    list_of_colors = []
    image =  filename
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
        return image_as_list[index]
    return generator

 
def combine_images(mask,  mask_function, image_generator1, image_generator2):  # just brute force it ig


    """Mask, mask_function is the conditioning to figure out if img1 or img2 is supposed to be used. 
    Creates a list with new values for each pixel from img1 and img2 based on a mask """

    list_colors = []
    conditon_image = []
    condition = gradient_condition(mask)
    img1 = [image_generator1(i) for i in range(len(mask))]
    img2 = [image_generator2(i) for i in range(len(mask))]
    for A in range(273280):
        if condition(A) == 1:
            list_colors.append(img1[A])
        elif condition(A) == 0:
            list_colors.append(img2[A])
        else:
            list_of_colors.append(img1[A] * condition(A) + img2 *condition[A])
    return list_colors


def combine_images_Original(mask,  mask_function, image_generator1, image_generator2): 
    list_colors = []
    img1 = [image_generator1(i) for i in range(len(mask))]
    img2 = [image_generator2(i) for i in range(len(mask)) ]
    for A in range(len(mask)):
        if  mask_function(mask[A]) == 1:
            list_colors.append(img1[A])            
        else:
            list_colors.append(img2[A])
    return list_colors


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
            return "Index bigger thaan len(mask)"
        except TypeError:
            return "Index must be an integer or a slice int"
    return condition
   

# Läs in en bild
plane_img = cv2.imread("plane.jpg")
flower_image = cv2.imread('flowers.jpg')
gradient_image = cv2.imread('gradient.jpg')
# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
gradient_image_list = cvimg_to_list(cv2.cvtColor(gradient_image, cv2.COLOR_BGR2HSV))
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
