import re

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

files = [ 'data/imagesTesting/others/'+f for f in listdir('data/imagesTesting/others') if isfile(join('data/imagesTesting/others', f))]
dictFromFile = {}
classList = []

dictSampletoLabel = {}

list = []
with open('data/sample_labels.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if ('No'in row[1]):
            if not(row[1] in classList):
                classList.append(row[1])
                list.append('data/images/'+row[0])



i = 0
files2 = [ 'data/imagesTesting/covid/'+f for f in listdir('data/imagesTesting/covid') if isfile(join('data/imagesTesting/covid', f))]
files3 = [ 'data/imagesTesting/normal/'+f for f in listdir('data/imagesTesting/normal') if isfile(join('data/imagesTesting/normal', f))]
j = 0
k = 0


for f in files:
    try:
        pic = Image.open(f)
        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        imArray1 = np.array(im)

        im = ImageOps.mirror(im)
        imArray2 = np.array(im)

        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        im = ImageOps.solarize(im,threshold=128)

        imArray3 = np.array(im)

        im = ImageOps.mirror(im)
        imArray4 = np.array(im)

    except Exception:
        print('error image')
        pass
    else:
        if not(f in list):
            print('done '+f)

            i = i+1
            s = 'data/128_128_test/Normal/' + str(i) + '_xxxx_128.png'
            s1 = s.replace('xxxx','Normal')
            s2 = s.replace('xxxx','Mirror')
            s3 = s.replace('xxxx','Solarize')
            s4 = s.replace('xxxx','Solarize_Mirror')

            dictSampletoLabel[s1] = 'non'
            dictSampletoLabel[s2] = 'non'
            dictSampletoLabel[s3] = 'non'
            dictSampletoLabel[s4] = 'non'

            Image.fromarray(imArray1).save(s1)
            Image.fromarray(imArray2).save(s2)
            Image.fromarray(imArray3).save(s3)
            Image.fromarray(imArray4).save(s4)



for f in files3:
    try:
        pic = Image.open(f)

        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        imArray1 = np.array(im)

        im = ImageOps.mirror(im)
        imArray2 = np.array(im)

        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        im = ImageOps.solarize(im,threshold=128)

        imArray3 = np.array(im)

        im = ImageOps.mirror(im)
        imArray4 = np.array(im)
        print('done ' + f)

    except Exception:
        print('error image')
        pass
    else:
        i = i+1
        k= k+1
        s = 'data/128_128_test/Normal/' + str(i) + '_healthy_xxxx_128.png'
        s1 = s.replace('xxxx','Normal')
        s2 = s.replace('xxxx','Mirror')
        s3 = s.replace('xxxx','Solarize')
        s4 = s.replace('xxxx','Solarize_Mirror')

        dictSampletoLabel[s1] = 'healthy'
        dictSampletoLabel[s2] = 'healthy'
        dictSampletoLabel[s3] = 'healthy'
        dictSampletoLabel[s4] = 'healthy'
        Image.fromarray(imArray1).save(s1)
        Image.fromarray(imArray2).save(s2)
        Image.fromarray(imArray3).save(s3)
        Image.fromarray(imArray4).save(s4)




for f in files2:
    try:
        pic = Image.open(f)

        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        imArray1 = np.array(im)

        im = ImageOps.mirror(im)
        imArray2 = np.array(im)

        im = ImageOps.fit(pic,(128,128),method=3, bleed=0.0, centering=(0.5, 0.5))
        im = ImageOps.solarize(im,threshold=128)

        imArray3 = np.array(im)

        im = ImageOps.mirror(im)
        imArray4 = np.array(im)

        im = ImageOps.crop(pic,20)
        imArray5 = np.array(im)

        im = PIL.ImageOps.crop(pic,15)
        imArray6 = np.array(im)

        im = ImageOps.crop(pic,10)
        imArray7 = np.array(im)

        im = ImageOps.posterize(pic,7)
        imArray8 = np.array(im)

        print('done ' + f)
    except Exception:
        print('error image')
        pass
    else:
        i = i+1
        j = j+1
        s = 'data/128_128_test/Normal/' + str(i) + '_covid_xxxx_128.png'
        s1 = s.replace('xxxx','Normal')
        s2 = s.replace('xxxx','Mirror')
        s3 = s.replace('xxxx','Solarize')
        s4 = s.replace('xxxx','Solarize_Mirror')
        s5 = s.replace('xxxx','Crop20')
        s6 = s.replace('xxxx','Crop15')
        s7 = s.replace('xxxx','Crop10')
        s8 = s.replace('xxxx','posterize')
        dictSampletoLabel[s1] = 'covid'
        dictSampletoLabel[s2] = 'covid'
        dictSampletoLabel[s3] = 'covid'
        dictSampletoLabel[s4] = 'covid'
        dictSampletoLabel[s5] = 'covid'
        dictSampletoLabel[s6] = 'covid'
        dictSampletoLabel[s7] = 'covid'
        dictSampletoLabel[s8] = 'covid'
        Image.fromarray(imArray1).save(s1)
        Image.fromarray(imArray2).save(s2)
        Image.fromarray(imArray3).save(s3)
        Image.fromarray(imArray4).save(s4)
        Image.fromarray(imArray1).save(s5)
        Image.fromarray(imArray2).save(s6)
        Image.fromarray(imArray3).save(s7)
        Image.fromarray(imArray4).save(s8)

print(i-j-k)
print(j)
print(k)

pickle.dump(dictSampletoLabel,open("dictSampletoLabel_128_Testing.p","wb"))
print(dictSampletoLabel)
