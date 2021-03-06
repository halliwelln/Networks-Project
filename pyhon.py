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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics    import f1_score

# ----------------------------------------------------------------
# Functions
# ----------------------------------------------------------------

def rep(item, n ):
    new = []
    for i in range(n):
        new.append(item)
    return new  

# ----------------------------------------------------------------
# Load Data
# ----------------------------------------------------------------

#os.chdir('/Users/felix/Documents/GSE/Term 3/14D009 Social and Economic Networks/Project Data/')
os.chdir('/Users/Nick/Desktop')

comm = pd.read_csv("new_communities.csv", header=None)
mod = pd.read_csv('mod_matrix_new.csv',header=None)

X = pd.concat([mod, comm], axis=1)
Y = pd.read_csv('new_labels.csv',header=None)

# ----------------------------------------------------------------
# Run models
# ----------------------------------------------------------------

# Init storage
rolling_micro  = []
rolling_macro  = []
size_training  = []
size_test      = []
step_wise_size = range(50,500,50)
# Run rolling model 20,5
for j,i in enumerate(rep(75,5)):

	print '# ------------------------'
	print 'Started iteration ' + str(j)
	print '# ------------------------'

	N    = X.shape[0]
	ind  = random.sample(range(N), N)
	size = i/float(100)
	
	training_ind = ind[:int(math.ceil(size*N))]
	test_ind     = ind[int(math.ceil(size*N)):]#int(math.ceil(size*N))+step_wise_size[j]]

	size_training.append(len(training_ind))
	size_test.append(len(test_ind))

	X_training   = X.ix[training_ind,:]
	Y_training   = Y.ix[training_ind,:]

	X_test = X.ix[test_ind,:]
	Y_test = Y.ix[test_ind,:]

	# Train multi-label classifier
	classifier = OneVsRestClassifier(RandomForestClassifier(n_estimators=100))
	classifier.fit(X_training, Y_training)

	# Predict multi labels
	predictions = classifier.predict(X_test)

	# Compute micro and macro F1-Score
	micro = f1_score(Y_test,predictions,average='micro')
	macro = f1_score(Y_test,predictions,average='macro')

	print '# ------------------------'
	print 'Finished iteration ' + str(j)
	print '# ------------------------'
	print 'Results:' 
	print 'Micro: ' + str(micro)
	print 'Macro: ' + str(macro)

	rolling_micro.append(micro)
	rolling_macro.append(macro)


# ----------------------------------------------------------------
# END CODE
# ----------------------------------------------------------------
