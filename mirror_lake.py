"""
File: mirror_lake.py
Name:
----------------------------------
This program reads the image “mt-rainier.jpg” and generates a 
new image that creates a mirror-lake effect by placing an 
inverted copy of the original image beneath it.
"""


from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for y in range(img.height):
        for x in range(img.width):
            imgp=img.get_pixel(x, y)
            bp1=b_img.get_pixel(x, y)
            bp1.red = imgp.red # b_img.set_rgb(x,y,imgp.red, imgp.green, imgp.blue)
            bp1.green = imgp.green
            bp1.blue = imgp.blue
            bp2=b_img.get_pixel(x, b_img.height - 1 - y) # b_img.set_rgb(x,b_img.height - 1 - y,imgp.red, imgp.green, imgp.blue)
            bp2.red = imgp.red
            bp2.green = imgp.green
            bp2.blue = imgp.blue
    b_img.show()

def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
