from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# load data 
df = pd.read_csv('Codes/Algo Implement/gm_2008_region.csv', index_col=0)

X_fertility = df['fertility'].values
y_life = df['life'].values

# reshape for scikit learn 
X_fertility = X_fertility.reshape(-1, 1)
y_life = y_life.reshape(-1,1)

# create regressor 
reg = LinearRegression()

# test and train split 
X_train, X_test, y_train, y_test = train_test_split(X_fertility, y_life, test_size = 0.3, random_state = 42)

# Fit the model to the data
# X = feature -> fertility 
# y = target -> life

reg.fit(X_train, y_train)

# predict with test data 
y_pred = reg.predict(X_test)

# Print R^2 
print('Score :',reg.score(X_fertility, y_life))

# print root mean square error of cost function 
# average squared difference between the estimated values and the actual value
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error : ', rmse)

# K-Fold Cross Validation 
cv_scores = cross_val_score(reg, X_fertility, y_life, cv=5)
print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

# Plot regression line
plt.scatter(df['fertility'].values, df['life'].values)
plt.xlabel('Fertility')
plt.ylabel("Life Expectancy")
plt.plot(X_test, y_pred, color='black', linewidth=3)
plt.show()


