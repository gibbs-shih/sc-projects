"""
File: mirror_lake.py
Name: Gibbs
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    This function uses the original image to create a reflected image.
    :param filename: str, the file path of the original image
    :return: a new image with the original image and the mirrored one
    """
    img = SimpleImage(filename)
    img_new = SimpleImage.blank(img.width, img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            pixel_img = img.get_pixel(x, y)

            # divide the new blank canvas into two parts
            pixel_new1 = img_new.get_pixel(x, y)
            pixel_new2 = img_new.get_pixel(x, img_new.height-y-1)

            # fill the first empty pixel(upper part)
            pixel_new1.red = pixel_img.red
            pixel_new1.green = pixel_img.green
            pixel_new1.blue = pixel_img.blue

            # fill the second empty pixel(mirrored part)
            pixel_new2.red = pixel_img.red
            pixel_new2.green = pixel_img.green
            pixel_new2.blue = pixel_img.blue
    return img_new


def main():
    """
    This function creates a mirror lake vibe by placing the inverse image below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
