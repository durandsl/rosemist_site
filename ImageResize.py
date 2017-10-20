import PIL
import os
from PIL import Image


def resizeBasedOnHeight(fileName, height, newFileName):
    img = Image.open(fileName)
    hpercent = (height/ float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, height), PIL.Image.ANTIALIAS)
    img.save(newFileName)

def main():
    dir = "/home/stephanie/rosemist_goldens/rosemist_site/pages/img"
    height = 720
    outdir = "/home/stephanie/rosemist_goldens/rosemist_site/pages/img/smaller"
    for fileName in os.listdir(dir):
        if(fileName.endswith('.jpg') or fileName.endswith('.jpeg')):
            absfile = os.path.join(dir, fileName)
            resizeBasedOnHeight(absfile, height, os.path.join(outdir, fileName))

if __name__ == '__main__':
    main()