from src.featureExtract.feature import calFeaturesforsave
import numpy as np
import sys
from os import listdir
from os.path import isfile, join, basename

mypath = str(sys.argv[1])
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for file in onlyfiles:
    feats, names = calFeaturesforsave(mypath+'/'+file)
    np.savetxt('tedcsv/'+basename(file)+'.csv', feats, delimiter=',')
    print(file+'is successfully saved')
    
print("Done....")
