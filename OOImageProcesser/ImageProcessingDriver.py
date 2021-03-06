from ImageTesting import imageProcesser
from ImageTesting import processedImagesToArray
from ImageTesting import buildCSV


#image testing has 3 methods meant to be called elsewhere in the project
#buildCSV looks at the /images directory and builds a comma seperated value file with all the image names
#imageProcessingDriver uses that CSV to manipulate the images, convert to B&W, crop, resize, equalize ect
    #ImageProcessingDriver calls #imageProcess to do a lot of this work
#processedImagesToArray will convert the images in images/post/ to image arrays to be manipulated by the nerual net


images = buildCSV()                                      # commenting out this line will cause the program to not process old or new images


convertedImages = imageProcesser(images)                         # does most of the work


list = processedImagesToArray(convertedImages)                 # returns a list of image arrays



print(list)             # shows us that the processed images have successfully been converted to array form
