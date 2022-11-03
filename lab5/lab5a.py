from cmath import e, pi
import math
import numpy
import cv2


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



def unsharp_mask(N):
    """Takes in N as input and retuns a list of cords of N length that process the (x,y) coordinates with negativ gaussian blur"""
    s = 4.5

    lista_x_y = [xy for xy in range(math.ceil(-N/2), math.ceil(N/2))]

    lista_cord = [[-(1/(2*pi*s**2)*e**(-(x**2+(-y)**2)/(2*s**2)))
        for x in lista_x_y ]for y in lista_x_y]

    lista_cord[math.floor(N/2)][math.floor(N/2)] = 1.5 # makes the middle 1.5

    return lista_cord

