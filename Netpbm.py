# Netbpm.py

# CSC 220, Fall 2016

from Image import *

class Netpbm(Image):
    '''An "abstract" class for the Netbpm family of image files.
    Not intended to be instantiated.'''

    def __init__(self):
        super().__init__()
        self.__magicNumber = 'XX'
        self.__maxValue = 0

    def getMagicNumber(self):
        return self.__magicNumber

    def getMaxVal(self):
        return self.__maxValue

    def setMaxVal(self, maxval):
        self.__maxValue = maxval

    def setMagicNumber(self,magicNumber):
        self.__magicNumber = magicNumber

    def read(self,filename):
        lines = super(Netpbm, self).read(filename)
        newlines = deepcopy(lines)
        for i, line in enumerate(lines):
            while line:
                line = line.strip()
                word = line.split(' ',1)[0]
                if self.getMagicNumber() == 'XX':
                    self.setMagicNumber(word)
                    line = line.replace(word, '', 1)
                    self.setChannels(self._typeDict[self.getMagicNumber()])
                elif self.getWidth() == 0:
                    if not 1 <= int(word) <= 2**16:
                        raise OverflowError("File size is not in the acceptable range!")
                    self.setWidth(word)
                    line = line.replace(word, '', 1)
                elif self.getHeight() == 0:
                    if not 1 <= int(word) <= 2**16:
                        raise OverflowError("File size is not in the acceptable range!")
                    self.setHeight(word)
                    line = line.replace(word, '', 1)
                else:
                    # newlines[i] = line
                    return newlines

                line = line.strip()

            del(newlines[0])

    def write(self, filename):
        outfile = open(filename, 'w')
        outfile.write(self.getMagicNumber()+'\n')
        outfile.write( str(self.getWidth()) + ' ' + str(self.getHeight()) +'\n')
        return outfile

    def invertColors(self):
        tempList = []
        newpixel = super(Netpbm, self).invertColors()
        for i in range(newpixel.getHeight()):
            for j in  range(newpixel.getWidth()):
                if self.getChannels() > 1:
                    for k in range(self.getChannels()):
                        tempList.append(int(newpixel.getMaxVal())- int(newpixel.getPixel(i,j)[k]))

                    newpixel.setPixel(i,j,tempList)
                    tempList = []
                else:
                    newpixel.setPixel(i,j,int(newpixel.getMaxVal())- int(newpixel.getPixel(i,j)))
        return newpixel

    def extractChannel(self, channel):
        channelIndex = self._channelDict[channel.lower()]
        newpixel = super(Netpbm, self).extractChannel(channel)

        for i in range(newpixel.getHeight()):
            for j in range(newpixel.getWidth()):
                extracted = [int(newpixel.getMaxVal()) - int(newpixel.getPixel(i,j)[channelIndex])]*self.getChannels()
                newpixel.setPixel(i, j, extracted)
        return newpixel

    def __repr__(self):
        return '<{0}X{1} image with {2} color channel(s) in range of [0,{3}]>'.format(self.getWidth(), self.getHeight(), self.getChannels(), self.getMaxVal())


if __name__=='__main__':
    print('Netpbm is an abstract class.')
