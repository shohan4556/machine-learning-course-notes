import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('Codes/Algo Implement/gm_2008_region.csv', index_col=0)

# life expectancy vs Region 
# since scikit learn dont accept non-numeric variable we have to convert it to numeric variable 
df_region = pd.get_dummies(df)
df_region = pd.get_dummies(df, drop_first=True)
print(df_region.columns)

df.boxplot('life', 'Region', rot=60)
plt.show()


# drop row of missing value 
voteDF = pd.read_csv('Codes/Algo Implement/house-votes-84.csv', index_col=0)
# replace missing value by Nan
voteDF[voteDF == '?'] = np.nan

print(voteDF.isnull().sum())
# drop all the rows of missing value 
voteDF = voteDF.dropna()

print(voteDF.head())

