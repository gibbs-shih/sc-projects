"""
File: best_photoshop_award.py
Names: Gibbs
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# a threshold used better to recognize the green screens
THRESHOLD = 1.3

# r + g + b < BLACK, the color is close to black
BLACK = 150


def main():
    """
    This function will combine two images into a new image.
    I'm thinking about keeping a dog.
    However, it's too difficult to choose between Shiba-Inu(the left one) and Corgi(the right one).
    They are so adorable.
    If you were me, what's the decision would you make?
    By the way, the color, classic blue(15,76,129), is Pantone Color of the Year 2020!
    """
    me = SimpleImage('image_contest/me.jpg')
    bg = SimpleImage('image_contest/cute.jpg')
    result = combine(me, bg)
    result.show()


def combine(figure, background):
    """
    :param figure: a image with green screens
    :param background: a image used to replace the green screens of the figure image
    :return: figure image after replaced the green screens by background_img
    """
    background.make_as_big_as(figure)
    for y in range(figure.height):
        for x in range(figure.width):
            pixel_fg = figure.get_pixel(x, y)
            pixel_bg = background.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.green + pixel_fg.blue) // 3
            total = pixel_fg.red + pixel_fg.green + pixel_fg.blue
            if pixel_fg.green > avg*THRESHOLD and total > BLACK:  # find green screens and avoid 'hair' area
                pixel_fg.red = pixel_bg.red
                pixel_fg.green = pixel_bg.green
                pixel_fg.blue = pixel_bg.blue
            elif y >= figure.height // 10 * 7.5:  # divide remained figure into 3 colors
                pixel_fg.red = 15
                pixel_fg.green = 76  # color of 2020: classic blue
                pixel_fg.blue = 129
            elif y >= figure.height // 10 * 4.5:
                pixel_fg.red = 24
                pixel_fg.green = 121
                pixel_fg.blue = 205
            elif y >= figure.height // 10 * 2:
                pixel_fg.red = 95
                pixel_fg.green = 170
                pixel_fg.blue = 236
    return figure


if __name__ == '__main__':
    main()
