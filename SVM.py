# ----------------------------------------------------------------
# Load Modules
# ----------------------------------------------------------------

import os
import json
import math
import numpy  as np
import pandas as pd
import random
from sklearn.svm import SVC
from sklearn.ensemble   import RandomForestClassifier
from sklearn.metrics    import f1_score
from sklearn.multiclass import OneVsRestClassifier

# ----------------------------------------------------------------
# Load Data
# ----------------------------------------------------------------

#os.chdir('/Users/felix/Documents/GSE/Term 3/14D009 Social and Economic Networks/Project Data/')
os.chdir('/Users/Nick/Desktop')
X = pd.read_csv('mod_matrix.csv', header=None)
Y = pd.read_csv('labels.csv', header=None)

# ----------------------------------------------------------------
# Run models
# ----------------------------------------------------------------
np.random.seed(123)

N    = X.shape[0]
ind  = random.sample(range(N), N)
size = 0.10

training_ind = ind[:int(math.ceil(size*N))]
test_ind     = ind[int(math.ceil(size*N)):]

X_training   = X.ix[training_ind,:]
Y_training   = Y.ix[training_ind,:]

X_test = X.ix[test_ind,:]
Y_test = Y.ix[test_ind,:]

# Train multi-label classifier
classifier = OneVsRestClassifier(SVC(kernel='linear'))
classifier.fit(X_training, Y_training)

# Predict multi labels
predictions = classifier.predict(X_test)

# Compute micro and macro F1-Score
micro = f1_score(Y_test,predictions,average='micro')
macro = f1_score(Y_test,predictions,average='macro')

# ----------------------------------------------------------------
# END CODE
# ----------------------------------------------------------------

print micro, "micro"
print macro, "macro"
