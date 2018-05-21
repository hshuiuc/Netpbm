# ppm.py 
# CSC 220, Fall 2016

from Netpbm import *

class PPM(Netpbm):
    '''Concrete Portable Pixel Map file class.'''

    def __init__(self):
        super().__init__()

    def read(self, filename):
        '''Reads a Portable Pixel Map file(ppm) from disk.'''
        lines = super(PPM, self).read(filename)
        if self.getMagicNumber() != 'P3':
            raise TypeError("Wrong file extension!")
        x = 0 # Width Counter
        y = 0 # Height Counter
        z = 0 # Component Counter
        tempList = []
        for i, line in enumerate(lines):
            while line:
                line = line.strip()
                word = line.split(' ', 1)[0]
                if self.getMaxVal() == 0:
                    if not 1 <= int(word) <= 255:
                        raise ValueError("Maximum Value of each pixel is not in acceptable range!")
                    self.setMaxVal(word)
                    line = line.replace(word, '', 1)
                    self._pixelInit()
                else:
                    tempList.append(int(word))
                    z += 1
                    if z == self.getChannels():
                        self.setPixel(y, x, tempList)
                        x += 1
                        z = 0
                        tempList = []
                    if x == self.getWidth():
                        y += 1
                        x = 0
                    if y == self.getHeight():
                        return
                    line = line.replace(word, '', 1)

    def write(self,filename):
        '''Writes a  Portable Pixel Map file(ppm) to disk.'''
        outfile = super(PPM, self).write(filename)
        outfile.write(str(self.getMaxVal())+'\n')
        pixels = self.getPixels()
        for row in pixels:
            for column in row:
                for subcolumn in column:
                    outfile.write(str(subcolumn).ljust(1+len(str(self.getMaxVal()))))
            outfile.write('\n')


        
if __name__=='__main__':
    # Assumes this is called from directory containing
    # sample_images sub-folder.
    try:
        print('-'*80)
        print('Calling constructor...')
        test = PPM()
        print('Reading sample_images/example.ppm...')
        test.read('sample_images/test_pattern.ppm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-cropped-purple_coneflowers.ppm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-cropped-purple_coneflowers.ppm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/' \
                'left-right-cropped_purple_coneflowers.ppm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/' \
                'top-bottom-cropped-purple_coneflowers.ppm')
        print('Luma coding image...')
        luma = test.LumaCode()
        luma.write('sample_images/' \
                'luma-cropped-purple_coneflowers.ppm')
        print('Extracting red channel...')
        red = test.extractChannel('red')
        red.write('sample_images/' \
                'red-cropped-purple_coneflowers.pgm')
        print('Extracting green channel...')
        green = test.extractChannel('green')
        green.write('sample_images/' \
                'green-cropped-purple_coneflowers.pgm')
        print('Extracting red channel...')
        blue = test.extractChannel('blue')
        blue.write('sample_images/' \
                'blue-cropped-purple_coneflowers.pgm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
