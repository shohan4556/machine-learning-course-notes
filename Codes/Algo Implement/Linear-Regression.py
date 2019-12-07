from sklearn.linear_model import LinearRegression
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

# Create the regressor: reg
reg = LinearRegression()
df = pd.read_csv('Codes/Algo Implement/gm_2008_region.csv', index_col=0)
#print(df.head)

X_fertility = df['fertility'].values
y_life = df['life'].values

X_fertility = X_fertility.reshape(-1, 1)
y_life = y_life.reshape(-1,1)

#print(X_fertility.shape)

#Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

# Fit the model to the data
# X = feature -> fertility 
# y = target -> life

reg.fit(X_fertility, y_life)

# feature -> prediction space 
# target -> y_pred
y_pred = reg.predict(prediction_space)
print(y_pred)

# Print R^2 
print(reg.score(X_fertility, y_life))

# Plot regression line
plt.scatter(df['fertility'].values, df['life'].values)
plt.xlabel('Fertility')
plt.ylabel("Life Expectancy")

plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
