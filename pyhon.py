# ----------------------------------------------------------------
# Load Modules
# ----------------------------------------------------------------

import os
import json
import math
import random
import numpy  as np
import pandas as pd
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble   import RandomForestClassifier
from sklearn.metrics    import f1_score

# ----------------------------------------------------------------
# Load Data
# ----------------------------------------------------------------

os.chdir('/Users/felix/Documents/GSE/Term 3/14D009 Social and Economic Networks/Project Data/')

X = pd.read_csv('mod_matrix.csv')
Y = pd.read_csv('labels.csv')

# ----------------------------------------------------------------
# Run models
# ----------------------------------------------------------------

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
classifier = OneVsRestClassifier(RandomForestClassifier(n_estimators = 10))
classifier.fit(X_training, Y_training)

# Predict multi labels
predictions = classif.predict(X_test)

# Compute micro and macro F1-Score
micro = f1_score(true_labels,predictions,average='micro')
macro = f1_score(true_labels,predictions,average='macro')

# ----------------------------------------------------------------
# END CODE
# ----------------------------------------------------------------
