#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and 
        that creates and returns a new 2-D list of pixels for an image 
        that is a grayscale version of the original image.
    """
    height = len(pixels)
    width = len(pixels[0])
    
    new_pixels = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            pixel = pixels[r][c]
            gray = brightness(pixel)
            new_pixels[r][c] = [gray, gray, gray]
    return new_pixels

def  mirror_vert(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and 
        that creates and returns a new 2-D list of pixels for an image in 
        which the original image is “mirrored” vertically.
    """
    height = len(pixels)
    width = len(pixels[0])
    
    new_pixels = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            if r < height // 2:
                new_pixels[r][c] = pixels[r][c]
            else:
                new_pixels[r][c] = pixels[-r - 1][c]
    return new_pixels

def flip_horiz(pixels):
    """  takes the 2-D list pixels containing pixels for an image, and 
         that creates and returns a new 2-D list of pixels for an image in 
         which the original image is “flipped” horizontally.
    """
    height = len(pixels)
    width = len(pixels[0])
    
    new_pixels = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            n = width // 2
            if width % 2 == 1:
                if c < n:
                    new_pixels[r][c] = pixels[r][n + (n - c)]
                else:
                    new_pixels[r][c] = pixels[r][n - (c - n)]
            else:
                if c < n:
                    new_pixels[r][c] = pixels[r][n + (n - c) - 1]
                else:
                    new_pixels[r][c] = pixels[r][n - (c - n) - 1]                    
    return new_pixels

def reduce(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and 
        that creates and returns a new 2-D list that represents an image 
        that is half the size of the original image.
    """
    height = len(pixels) // 2
    width = len(pixels[0]) // 2
    
    new_pixels = blank_image(height, width)
    for r in range(height):
        for c in range(width):
            new_pixels[r][c] = pixels[2 * r][2 * c]
    return new_pixels

def transpose(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and that 
        creates and returns a new 2-D list that is the transpose of pixels.
    """
    height = len(pixels[0])
    width = len(pixels)
    
    new_pixels = blank_image(height, width)
    for r in range(height):
        for c in range(width):
           new_pixels[r][c] = pixels[c][r]
    return new_pixels
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    