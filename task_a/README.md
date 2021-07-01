# Download of Dataset

We manually downloaded the [GSE68086_TEP_data_matrix.txt ](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE68086) dataset.

# Conversion of file

We unzipped the file and loaded it into our jupyternotebook using the pandas module.
`pd.read_csv(GSE68086_TEP_data_matrix.txt, sep='\t')`

# Preparation of dataset

The dataset had RNA-Seq information for wildtype (WT) and cancerous Brest tissue samples (others). 
Therefore we seperated our samples into two (2) groups, Group (1) referring to cancerous sample and group (0) referring to WT samples.
The given Gene identifiers and their given RNA Seq values were used as feautures. 

# Implementation of KNN 
``` # imports
import itertools
import numpy as np
import gzip
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
%matplotlib inline

# reading in dataset
training_data = pd.read_csv('GSE68086_TEP_data_matrix.txt', sep='\t').dropna()
training_data.head(57736)

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)

# features
params = training_data['Gene Id']
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
params_encoded=le.fit_transform(params)
# zip our feautures to our training data
zipped_features = list(list(zip(training_data[col].to_list(), params_encoded)) for col in training_data if col !='Unnamed: 0')
# assign data to labels  0 = cancer not present, 1 = cancer present 
labels = [(training_data[col].to_list(), 0) if 'WT' in col else  (training_data[col].to_list(), 1) for col in training_data.columns if col!= 'Unnamed: 0']

X = [label[0] for label in labels]
Y = [label[1] for label in labels]
```