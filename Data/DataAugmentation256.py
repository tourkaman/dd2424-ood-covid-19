import PIL
from PIL import Image
from os import listdir
from os.path import isfile, join
from matplotlib import image
from matplotlib import pyplot as plt
from numpy import asarray
from PIL import ImageOps
import numpy as np
import csv
import pickle

#files = [ 'data/images/'+f for f in listdir('data/images') if isfile(join('data/images', f))]
dictFromFile = {}
classList = []
files = []

dictSampletoLabel = {}


with open('data/sample_labels.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not( '|'in row[1] or 'Finding'in row[1]):
            if not(row[1] in classList):
                classList.append(row[1])
            dictFromFile['data/images/'+row[0]] = row[1]
            files.append('data/images/'+row[0])

for f in files:
    try:
        print(f)
        pic = Image.open(f)
        im = ImageOps.fit(pic,(256,256),method=3, bleed=0.0, centering=(0.5, 0.5))
        imArray1 = np.array(im)

        im = ImageOps.mirror(im)
        imArray2 = np.array(im)

        im = ImageOps.fit(pic,(256,256),method=3, bleed=0.0, centering=(0.5, 0.5))
        im = ImageOps.solarize(im,threshold=128)

        imArray3 = np.array(im)

        im = ImageOps.mirror(im)
        imArray4 = np.array(im)
        print('done ' + f)

    except Exception:
        print('error image')
        pass
    else:
        dictSampletoLabel[f.replace('images/','256_256/Normal/').replace('.png', 'Normal_256_256.png')] = dictFromFile[f]
        dictSampletoLabel[f.replace('images/','256_256/Mirror/').replace('.png', 'Mirror_256_256.png')] = dictFromFile[f]
        dictSampletoLabel[f.replace('images/','256_256/Solarize/').replace('.png', 'Solarize_256_256.png')] = dictFromFile[f]
        dictSampletoLabel[f.replace('images/','256_256/Solarize_Mirror/').replace('.png', 'Solarize_Mirror_256_256.png')] = dictFromFile[f]
        Image.fromarray(imArray1).save(f.replace('images/','256_256/Normal/').replace('.png', 'Normal_256_256.png'))
        Image.fromarray(imArray2).save(f.replace('images/','256_256/Mirror/').replace('.png', 'Mirror_256_256.png'))
        Image.fromarray(imArray3).save(f.replace('images/','256_256/Solarize/').replace('.png', 'Solarize_256_256.png'))
        Image.fromarray(imArray4).save(f.replace('images/','256_256/Solarize_Mirror/').replace('.png', 'Solarize_Mirror_256_256.png'))

pickle.dump(dictSampletoLabel,open("dictSampletoLabel_256.p","wb"))
print(dictSampletoLabel)
