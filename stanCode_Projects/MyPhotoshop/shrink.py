"""
File: shrink.py
Name: Gibbs
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    This function will get a new shrunk image by keeping parts of the pixels in the original image.
    :param filename: str, the file path of the original image
    :return img: SimpleImage, the width and the height is half of the original image
    """
    img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(img.width//2, img.height//2)  # half the width and the height
    for y in range(img.height):
        for x in range(img.width):
            pixel_img = img.get_pixel(x, y)
            pixel_shrink = shrink_img.get_pixel(x//2, y//2)
            if x % 2 == 0 and y % 2 == 0:  # keep parts of the pixels in the original image
                pixel_shrink.red = pixel_img.red
                pixel_shrink.green = pixel_img.green
                pixel_shrink.blue = pixel_img.blue
    return shrink_img


def main():
    """
    This function will get a new shrunk image, the width and the height is half of the original image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
