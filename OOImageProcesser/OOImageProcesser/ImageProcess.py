
from numpy import *
from pylab import *
from PIL import Image
from PIL import ImageOps
from os import listdir
from os.path import isfile, join


def grayscale(picture):
    res = Image.new(picture.mode, picture.size)
    red = '150,45,45'
    x = red.split(",")
    width, height = picture.size

    for i in range(0, width):
        for j in range(0, height):
            pixel = picture.getpixel((i, j))
            pixelStr = str(pixel)
            pixelStr = pixelStr.replace('(', '').replace(')', '')
            pixelStr.split(",")

            if not (int(pixelStr[0]) >= int(x[0]) and int(pixelStr[1]) <= int(x[1]) and int(pixelStr[2]) <= int(x[2])):
                avg = (pixel[0] + pixel[1] + pixel[2]) / 3
                res.putpixel((i, j), (int(avg), int(avg), int(avg)))
            else:
                res.putpixel(pixel)
    return res

class ImageProcess:
    """The ImageProcessing Class"""

    def __init__(self):
        self.pictures = []

    def imageProcesser(self, imPathString):
        stoppics = 0
        if "stop" in imPathString:
            try:
               im = Image.open(imPathString)

            except IOError:
                print("Could not read image" + imPathString)
                sys.exit()
            with im:
                size = 1000,1000
                im.thumbnail(size, Image.ANTIALIAS)
                im = grayscale(im)
                print("\nthe image path string is as follows: "+ imPathString)
                #new = Image.fromarray(uint8(im))
                #new.save('post/images/stop/' + 'stoppic' +str(len(self.pictures)+1))

                im.save("data/post/images/stop/newpicture"+ str(len(self.pictures)) + ".jpg")
                im = array(im)
                self.pictures.append(im)




        elif "stop" not in imPathString:
            try:
                pil_im = Image.open(imPathString).convert('L')  # trys to open said image ( long file name required /data/pre/forward/imagename.jpg ) and converts it to greyscale

            except IOError:
                print("Could not read image" + imPathString)
                sys.exit()                                               # quits cuz bad file path

            with pil_im:
                print( imPathString + " is the "+ str(len(self.pictures)) + "th image processed \n")
                # Where do we start cropping from?
                halfwidth = pil_im.size[0] / 2                 # right now I crop from the center of the image
                halfheight = pil_im.size[1] / 2                # these two lines find the location we are cropping from, as mentioned, dead center

                # How much of the image do we want to crop out?
                width = pil_im.size[0] / 2.15                  # how much for the width
                height = pil_im.size[1] / 6                    # how much for the height

                # apply the crop line one: left edge, two: top edge, three: right edge, four: bottom
                if ((width + halfwidth) > pil_im.size[0]):
                    print(" your width is out of bounds, too big the original width is " + str(
                        pil_im.size[0]) + " your proposed size is " + str((width + halfwidth)))
                    sys.exit()

                elif ((height + halfheight) > pil_im.size[1]):
                    print(" your height is out of bounds, too big the original height is " + str(
                        pil_im.size[1]) + " your proposed size is " + str((height + halfheight)))
                    sys.exit()

                else:
                    pil_im = pil_im.crop(
                        (
                            halfwidth - width,
                            halfheight - height,
                            halfwidth + width,
                            halfheight + halfheight,
                        # we want the image as close to the front of the car/ camera as possible right? so no cropping has been done for the bottom edge
                        )
                    )

                # define a maximum size for the image. 1000 x 1000 in this case, if we cropped too small do not save the image
                size = 1000, 1000

                if (pil_im.size[0] < size[0] & pil_im.size[1] < size[1]):
                    print(
                        "Your crop has made the image too small, we would like at least a 1000 width image, your width was " + str(
                            pil_im.size[0]))
                    sys.exit()               # in this instance we are going to say the image is too small if BOTH the size and the width are smaller than 1000

                pil_im = array(pil_im)  # convert the image to an array

                # these lines will adjust the contrast in the image
                pil_im = (100.0 / 255) * pil_im + 90                 # clamp the values...
                pil_im = 255.0 * (pil_im / 255.0) ** 2               # quadratic transformation

                # convert back to an image to do the equalization
                pil_im = Image.fromarray(uint8(pil_im))
                pil_im = ImageOps.equalize(pil_im)

                # resize the image
                pil_im.thumbnail(size,Image.ANTIALIAS)


                String2 = 'data/post/images/newpicture0'  # save transformed image as newpicture0
                String2 = String2 + str(len(self.pictures))
                pil_im.save(String2 + '.jpg')
                # we use thumbnail to preserve the aspect ratio during the resize, dont want to distort the image in any way, using our defined size

                # we need to "save" the images
                pil_im = array(pil_im)
                self.pictures.append(pil_im)




                ###this needs to be updateded to imPathString if i decide to use it###


                return


