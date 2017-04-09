
import os
from PIL import *
from PIL import Image
from numpy import *
from pylab import *
from PIL import ImageOps
from os import listdir
from os.path import isfile, join
import glob
from ImageProcess import ImageProcess

#buildCSV
    #reads in a directory and builds a csv file of all the images in the directory
    #calling this sets the integer at the head of the file to zero causing all images to be reprocessed

def buildCSV():

    #if not(os.path.isdir("/data/images/")):                                                              #WORK ON THIS MIKEEEEEEE DO IT TODO WOOOO
    #    print("\n the provided path in the function BUILD CSV doesnt exist")
    #    sys.exit()


    images = glob.glob('data/images/**/*.jpg')
    return images


#imageProcessingDriver
    #designed to be called from elsewhere in the project
    #calles imageProcess for each image, where the image is manipulated

def imageProcesser(images):
    processer = ImageProcess()
    for item in images:
        processer.imageProcesser(item)
        print(item + " was the " + str(len(processer.pictures)))
    return processer.pictures

#processedImagesToArray
    #converts images in the /post directory to a list of image arrays
    #returns the list of image arrays

def processedImagesToArray(images):

    listOfImageArrays = []
    x = []
    for p in images:
        print(p)
        listOfImageArrays.append(p)

#    return listOfImageArrays



# open images
    # no open imagess method as of now since in the first open images we combine with the convert to black and white
    # this might be changed in the future as this is converted to OO


#readLineSplit
    #helper function, reccommended to only be called from within this file
    #reads a single line from open file and split it on comma
    #returns the split array

def readLineSplit(openedfile):
    splitarray = openedfile.readline()
    splitarray = splitarray.split(",")
    return splitarray


#csvOpen
    # should only be called by other methods in this file
    # returns an opened file for read and write
    # if the file location is "bad" then we exit the program saying what file we tried to open

def csvOpen(locationstring):
    try:
        openedfile = open(locationstring, "r+")
    except IOError:
        print("\n\n could not open CSV file located at: " + locationstring)
        sys.exit()
    return openedfile
