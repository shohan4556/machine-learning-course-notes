import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('Codes/Algo Implement/gm_2008_region.csv', index_col=0)

# life expectancy vs Region 
# since scikit learn dont accept non-numeric variable we have to convert it to numeric variable 
df_region = pd.get_dummies(df)
df_region = pd.get_dummies(df, drop_first=True)
print(df_region.columns)

df.boxplot('life', 'Region', rot=60)
plt.show()

