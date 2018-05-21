# Image.py 
# CSC 220, Fall 2016

from copy import deepcopy

class Image:
    '''An "abstract" base class for generic image data.
    Not intended to be instantiated.'''

    _typeDict = {'P1':1, 'P2':1, 'P3':3}
    _channelDict = {'red':0, 'green':1, 'blue':2}

    def __init__(self):
        self.__pixels = []
        self.__dimension = [0, 0]
        self.__channels = 1

    def getWidth(self):
        return self.__dimension[0]

    def getHeight(self):
        return self.__dimension[1]

    def getPixel(self,y, x):
            return self.__pixels[y][x]

    def getPixels(self):
        return self.__pixels

    def getChannels(self):
        return self.__channels


    def setWidth(self, width):
        self.__dimension[0] = int(width)

    def setHeight(self, height):
        self.__dimension[1] = int(height)

    def setPixel(self,y, x, pixel):
        if self.getChannels() > 1:
            self.__pixels[y][x] = pixel
        else:
            self.__pixels[y][x] = int(pixel)

    def setPixels(self,pixels):
        self.__pixels = pixels

    def setChannels(self, channels):
        self.__channels = channels

    def write(self,filename):
        '''Public API for writing converted pixels to image file'''
        outfile = open(filename,'w')

    def read(self,filename):
        '''Public API for reading an image file.'''
        with open(filename, 'r') as imgfile:
            text = imgfile.read()
            lines = text.split('\n')
            newlines = []
            for i, line in enumerate(lines):
                if not "#" in line:
                    newlines.append(line)
            return newlines

    def _pixelInit(self):
        '''Protected helper function to initiate pixel with appropriate dimensions'''
        if self.__channels == 3:
            self.__pixels = [[[0] * self.getChannels()] * self.getWidth() for row in range(self.getHeight())]
        else:
            self.__pixels = [[0] * self.getWidth() for row in range(self.getHeight())]

    def flipLR(self):
        '''Flips image left-right.'''
        newpixel = deepcopy(self)
        for i in range(len(newpixel.getPixels())):
            newpixel.__pixels[i].reverse()
        return newpixel

    def flipTB(self):
        '''Flips image top-bottom.'''
        newpixel = deepcopy(self)
        newpixel.__pixels.reverse()
        return newpixel

    def invertColors(self):
        '''Inverts image colors.'''
        newpixel = deepcopy(self)
        return newpixel

    def LumaCode(self):
        '''Luma codes color image for video.'''
        newpixel = deepcopy(self)
        for i in range(newpixel.getHeight()):
            for j in range(newpixel.getWidth()):
                lumaPixel = [int(float(newpixel.getPixel(i, j)[0])*.2126+float(newpixel.getPixel(i, j)[1])*.7152+float(newpixel.getPixel(i, j)[2])*.0722)]*3
                newpixel.setPixel(i, j, lumaPixel)
        return newpixel

    def extractChannel(self, channel):
        '''Extracts a given channel from a color image.'''
        newpixel = deepcopy(self)
        return newpixel

if __name__=='__main__':
    print('Image is an abstract base class.')