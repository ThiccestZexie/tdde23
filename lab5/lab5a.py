from cmath import e, pi
import math
<<<<<<< HEAD
=======
from operator import sub
>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
import numpy
import cv2


def cvimg_to_list(filename):
<<<<<<< HEAD
    """Returns a list of tuples of a images RGB values"""

    list_of_colors = []
    image =  filename
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            list_of_colors.append(tuple(image[x,y]))

    return list_of_colors


=======

    """Takes in a cv2 img that has been read and loops through every coordinate on it and takes out the BGR value of each pixel and appends it to a list and returns that list"""

    list_of_colors = []
    image =  filename
    for i in range(image.shape[0]):
        for q in range(image.shape[1]):
            list_of_colors.append(tuple(image[i,q]))

    return list_of_colors

>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6
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
<<<<<<< HEAD
    """Takes in N as input and retuns a list of cords of N length that process the (x,y) coordinates with negativ gaussian blur"""
    s = 4.5

    lista_x_y = [xy for xy in range(math.ceil(-N/2), math.ceil(N/2))]

    lista_cord = [[-(1/(2*pi*s**2)*e**(-(x**2+(-y)**2)/(2*s**2)))
        for x in lista_x_y ]for y in lista_x_y]

    lista_cord[math.floor(N/2)][math.floor(N/2)] = 1.5 # mitten blir = 1.5

    return lista_cord
=======

    """returns a negativ gauss blur filter based from a argument N. The lists length equals to N and expands from 0 to both positive and negative integers."""
 
    s = 4.5

    lista_x_y = [xy for xy in range(math.ceil(-N/2), math. ceil(N/2))]

    lista_cord = [-(1/(2*pi*s**2)*e**(-(x**2+(-y)**2)/(2*s**2)))
        for x in lista_x_y for y in lista_x_y]
    
    sublistlength = len(lista_cord) // N
    lista_blur = [lista_cord[i:i + sublistlength] for i in range(0, len(lista_cord), sublistlength)] 

    lista_blur[math.floor(N/2)][math.floor(N/2)] = 1.5 # mitten blir = 1.5

    return lista_blur

img = cv2.imread('460613.jpg')
print(cvimg_to_list(img))
#img = cv2.imread('460613.jpg')      
#list_img = cvimg_to_list(img)
#converted_img = rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])    # Bildens dimensioner
#cv.imshow("converted", converted_img)
#cv.waitKey(0)

>>>>>>> f3c81ce51741594f46e31b82a03932d9b2cfc1d6

