"""
File: green_screen.py
Name: Gibbs
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    background_img is used as background and replaces the green pixels in figure_img.
    :param background_img: the image used to replace the green pixels of the figure_img
    :param figure_img: the image with green pixels
    :return: figure_img after replaced the green pixels by background_img
    """
    background_img.make_as_big_as(figure_img)
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)  # return the one that is bigger
            if pixel.green > 2*bigger:  # find green screens
                background_pixel = background_img.get_pixel(x, y)
                pixel.red = background_pixel.red
                pixel.green = background_pixel.green
                pixel.blue = background_pixel.blue
    return figure_img


def main():
    """
    This function will combine two images into a new image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
