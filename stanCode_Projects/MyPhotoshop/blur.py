"""
File: blur.py
Name: Gibbs
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Get a blurred image using the average RGB values of a pixel's nearest neighbors. (9 different conditions)
    :param img: the image used to be blurred
    :return: the image after blurred
    """
    blurred_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            blur_p = blurred_img.get_pixel(x, y)
            if x == 0:
                if y == 0:  # the upper left corner
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x+1, y)
                    p3 = img.get_pixel(x, y+1)
                    p4 = img.get_pixel(x+1, y+1)
                    blur_p.red = (p1.red+p2.red+p3.red+p4.red)//4
                    blur_p.green = (p1.green+p2.green+p3.green+p4.green)//4
                    blur_p.blue = (p1.blue+p2.blue+p3.blue+p4.blue)//4
                elif y == img.height-1:  # the lower left corner
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x+1, y)
                    p3 = img.get_pixel(x, y-1)
                    p4 = img.get_pixel(x+1, y-1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red) // 4
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green) // 4
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                else:  # the left edge
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x + 1, y)
                    p3 = img.get_pixel(x, y - 1)
                    p4 = img.get_pixel(x + 1, y - 1)
                    p5 = img.get_pixel(x, y+1)
                    p6 = img.get_pixel(x+1, y+1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red+p5.red+p6.red)//6
                    blur_p.green = (p1.green+p2.green+p3.green+p4.green+p5.green+p6.green)//6
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue+p5.blue+p6.blue)//6
            elif x == img.width-1:
                if y == 0:  # the upper right corner
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x, y + 1)
                    p4 = img.get_pixel(x - 1, y + 1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red) // 4
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green) // 4
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                elif y == img.height-1:  # the lower right corner
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x, y - 1)
                    p4 = img.get_pixel(x - 1, y - 1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red) // 4
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green) // 4
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4
                else:  # the right edge
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x, y - 1)
                    p4 = img.get_pixel(x - 1, y - 1)
                    p5 = img.get_pixel(x, y + 1)
                    p6 = img.get_pixel(x - 1, y + 1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
            else:
                if y == 0:  # the up edge
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x+1, y)
                    p4 = img.get_pixel(x + 1, y + 1)
                    p5 = img.get_pixel(x, y + 1)
                    p6 = img.get_pixel(x - 1, y + 1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                elif y == img.height-1:  # the bottom edge
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x + 1, y)
                    p4 = img.get_pixel(x - 1, y - 1)
                    p5 = img.get_pixel(x, y - 1)
                    p6 = img.get_pixel(x + 1, y - 1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red) // 6
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green) // 6
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue) // 6
                else:  # the rest parts
                    p1 = img.get_pixel(x, y)
                    p2 = img.get_pixel(x - 1, y)
                    p3 = img.get_pixel(x + 1, y)
                    p4 = img.get_pixel(x - 1, y - 1)
                    p5 = img.get_pixel(x, y - 1)
                    p6 = img.get_pixel(x + 1, y - 1)
                    p7 = img.get_pixel(x, y+1)
                    p8 = img.get_pixel(x-1, y+1)
                    p9 = img.get_pixel(x+1, y+1)
                    blur_p.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red + p7.red + p8.red + p9.red) // 9
                    blur_p.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green + p7.green + p8.green + p9.green) // 9
                    blur_p.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue + p7.blue + p8.blue + p9.blue) // 9
    return blurred_img


def main():
    """
    This function will get a blurred image. You can decide to blur how many times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
