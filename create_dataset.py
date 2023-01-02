from os import listdir
from os.path import isfile, join

mypath = "/home/orhir/CamoFormer/dataset/TestDataset/COD10K/Image"
onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]
out = ['{} {}'.format(f, f.replace("Image", "GT").replace("jpg", "png")) for f in onlyfiles]
for f in out:
    print(f)