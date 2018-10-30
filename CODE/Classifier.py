# -*- coding: utf-8 -*-
import sklearn
import pandas as pd
import nltk as nltk
from nltk.corpus import stopwords
import re
import scipy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score, StratifiedShuffleSplit, cross_validate
from sklearn import svm
from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.pipeline import Pipeline, FeatureUnion
from scipy.sparse import vstack, csr_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt

#Read file:
path = "data.csv"

x=[]
messages =[]
data = pd.read_csv(path)
clean_data = data.iloc[:,1:-1]
print clean_data


'''
vectorizer = TfidfVectorizer(ngram_range=(1,2))
ngrams = vectorizer.fit_transform(clean_data, data['y'])

ngrams2=vectorizer.fit_transform(clean_data[2:3], data['y'][2:3])
print ngrams
print clean_data[2]
'''
classifier = Pipeline([

       ('clf', RandomForestClassifier())
])
'''
length_data = scipy.sparse.csr_matrix(length_data)
length_data = length_data.transpose()
print ngrams.shape, length_data.shape
ngrams = scipy.sparse.hstack((ngrams,length_data)).tocsr()
 '''
# separate out training and testing data
trainX, testX, trainY, testY = train_test_split(
    clean_data,
    data['y'],
    test_size=0.2
)
print len(clean_data)

classifier.fit(trainX,trainY)
predY = classifier.predict(testX)
print metrics.f1_score(testY, predY)*100
print metrics.precision_score(testY, predY)*100
print metrics.recall_score(testY, predY)*100
print metrics.accuracy_score(testY, predY)*100

scores = cross_validate(classifier,
                         np.concatenate((trainX.values, testX.values), axis=0),
                         np.concatenate((trainY.values, testY.values), axis=0),
                         cv=StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=0),
                         scoring={'accuracy': 'accuracy',
                                  'f1' : 'f1'}
                         )
print scores
print scores['train_accuracy'].mean()
print scores['train_f1'].mean()
print scores['test_accuracy'].mean()
print scores['test_f1'].mean()

'''
plt.plot([i for i in range(1,11)], scores['train_accuracy'])
plt.show()


plt.plot([i for i in range(1,11)], scores['train_f1'])
plt.show()


plt.plot([i for i in range(1,11)], scores['test_accuracy'])
plt.show()


plt.plot([i for i in range(1,11)], scores['test_f1'])
plt.show()
'''