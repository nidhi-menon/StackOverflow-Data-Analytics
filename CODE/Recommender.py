import pandas as pd
import scipy as sc
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

path = "./update.csv"
data = pd.read_csv(path)
#print data
tags = []
for i in range(0, 1500):
    tags.append(data.iloc[i]['tags'])
data.ffill(inplace=True)
uniquetags = list(set(tags))
#print uniquetags
#print len(uniquetags)
'''
blah = {}
for i in range(0,len(uniquetags)):
    blah[uniquetags[i]] = i
print blah

data['tags'] = data['tags'].map(blah)
data.to_csv("update.csv")
'''
'''for i in range(0,10):
    key=data.iloc[i]['tags']
    #print blah[key]
    data.iloc[i]['tags'] = blah[key]'''
trainRows = 20020
testRows = 20150
trainData = data.iloc[:trainRows]
testData = data.iloc[trainRows:testRows]
print trainData

################################
def bench_k_means(estimator, name, data):
    estimator.fit(data)
'''
bench_k_means(KMeans(init='k-means++', n_clusters=len(uniquetags), n_init=10),
              name="k-means++", data=trainData)

bench_k_means(KMeans(init='random', n_clusters=len(uniquetags), n_init=10),
              name="random", data=trainData)
'''
kmeans = KMeans(n_clusters=len(uniquetags))
kmeans.fit(trainData) #Training stage
predict = kmeans.predict(testData) #Testing stage
centroids = kmeans.cluster_centers_
print {i: np.where(kmeans.labels_ == i) for i in range(kmeans.n_clusters)} #Prints all the users in each cluster
j=0
for prediction in predict:
    print "Question ID:", testData.iloc[j], "Predict: ",np.where(kmeans.labels_ == prediction)   #Gives us the list of users who are in the cluster K-means predicted the question to be in
    j+=1