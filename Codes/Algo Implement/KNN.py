from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 

# import dataset from csv as dataframe  
# each column is a features and each rows are observation or data points 
# target needs to a single column with the same number of observation as feature data 


df = pd.read_csv('Codes/Algo Implement/gm_2008_region.csv', index_col=0)
# rename columns
print(df.head())



"""
# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values
#print(X)

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))

"""



