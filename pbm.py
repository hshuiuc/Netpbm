# pbm.py 
# CSC 220, Fall 2016

from Netpbm import *

class PBM(Netpbm):
    '''Concrete Portable Bit Map file class.'''
    def __init__(self):
       super().__init__()

    def read(self,filename):
        '''Reads a Portable Bit Map file(pbm) from disk.'''
        with open(filename,'r') as infile:
            lines = super(PBM, self).read(filename)
            if self.getMagicNumber() != 'P1':
                raise TypeError("Wrong file extension!")
            x = 0  # Width Counter
            y = 0  # Height Counter
            self._pixelInit()
            self.setMaxVal(1)
            for i, line in enumerate(lines):
                while line:
                    line = line.strip()
                    if line.find(' ') < 0:
                        word = line[0]
                    else:
                        word = line.split(' ', 1)[0]
                    if not word in '01':
                        raise ValueError('Pixel('+str(x)+', '+str(y)+') value is not in the acceptable range for PBM files!')
                    self.setPixel(y, x, word)
                    x += 1
                    if x == self.getWidth():
                        y += 1
                        x = 0
                    if y == self.getHeight():
                        return
                    line = line.replace(word, '', 1)

    def write(self, filename):
        '''Writes a  Portable Bit Map file(pbm) to disk.'''
        outfile = super(PBM, self).write(filename)
        pixels = self.getPixels()
        for row in pixels:
            for column in row:
                outfile.write(str(column))
            outfile.write('\n')

if __name__=='__main__':
    # Assumes this is called from directory containing
    # sample_images sub-folder.
    try:
        print('-'*80)
        print('Calling constructor...')
        test = PBM()
        print('Reading sample_images/G.pbm...')
        test.read('sample_images/G.pbm')
        print('Writing a duplicate...')
        test.write('sample_images/copy-G.pbm')
        print('Inverting colors and writing copy...')
        inverted = test.invertColors()
        inverted.write('sample_images/inverted-G.pbm')
        print('Flipping left-right and writing copy...')
        leftRight = test.flipLR()
        leftRight.write('sample_images/left-right-G.pbm')
        print('Flipping top-bottom and writing copy...')
        topBottom = test.flipTB()
        topBottom.write('sample_images/top-bottom-G.pbm')
        print('Finished __main__, exiting.')
        print('-'*80)
    except Exception as e:
        print('Exception raised:')
        print(e)
