# pgm.py
# CSC 220, Fall 2016

from Netpbm import *

class PGM(Netpbm):
    '''Concrete Portable Gray Map file class.'''
    def __init__(self):
        super().__init__()

    def read(self, filename):
        '''Reads a Portable Gray Map file(pgm) from disk.'''
        lines = super(PGM, self).read(filename)
        if self.getMagicNumber() != 'P2':
            raise TypeError("Wrong file extension!")
        x = 0  # Width Counter
        y = 0  # Height Counter
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
                    self.setPixel(y,x,word)
                    x += 1
                    if x == self.getWidth():
                        y += 1
                        x = 0
                    if y == self.getHeight():
                        return
                    line = line.replace(word, '', 1)

    def write(self,filename):
        '''Writes a  Portable Gray Map file(pgm) to disk.'''
        outfile = super(PGM, self).write(filename)
        outfile.write(str(self.getMaxVal())+'\n')
        pixels = self.getPixels()
        for row in pixels:
            for column in row:
                outfile.write(str(column).ljust(1+len(str(self.getMaxVal()))))
            outfile.write('\n')


if __name__=='__main__':
    try:
        print('-'*80)
        print('Calling constructor...')
        test = PGM()
        print('Reading sample_images/gradients.pgm...')
        test.read('sample_images/gradients.pgm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-fungi.pgm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-fungi.pgm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/left-right-fungi.pgm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/top-bottom-fungi.pgm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
