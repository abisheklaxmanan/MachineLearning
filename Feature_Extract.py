pip install numpy

pip install pyopenms

import pandas as pd

from urllib.request import urlretrieve
# from urllib import urlretrieve  # use this code for Python 2.x
#gh = "https://raw.githubusercontent.com/OpenMS/OpenMS/develop"
#urlretrieve (gh +"/src/tests/topp/FeatureFinderCentroided_1_input.mzML", "feature_test.mzML")

from pyopenms import *

# Prepare data loading (save memory by only
# loading MS1 spectra into memory)
options = PeakFileOptions()
options.setMSLevels([1])
fh = MzMLFile()
fh.setOptions(options)

# Load data
input_map = MSExperiment()
fh.load("/home/user/Downloads/week11/womenRCCstage1_1617.mzML", input_map)
input_map.updateRanges()

ff = FeatureFinder()
ff.setLogType(LogType.CMD)

# Run the feature finder
name = "centroided"
features = FeatureMap()
seeds = FeatureMap()
params = FeatureFinder().getParameters(name)
ff.run(name, input_map, features, params, seeds)

features.setUniqueIds()
fh = FeatureXMLFile()
fh.store("OutputRC.featureXML", features)
print("Found", features.size(), "features")


RT=[]
MZ=[]
f0 = features[0]
for f in features:
    RT.append(f.getRT())
    MZ.append(f.getMZ())
    
print(len(RT))
print(len(MZ))
X1= list(zip(RT,MZ))
X1
