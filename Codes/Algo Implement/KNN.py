from sklearn.neighbors import KNeighborsClassifier
import numpy as pd 

# import dataset from csv as dataframe  
# each column is a features and each rows are observation or data points 
# target needs to a single column with the same number of observation as feature data 

"""
#target/response variable 
y = df['party'].values

#features array 
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit/train the classifier to the data
knn.fit(X,y)

# then predict for new data

"""



