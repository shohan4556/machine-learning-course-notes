import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set()

pd.set_option('display.max_columns', None)

nobel  = pd.read_csv('nobel.csv')

print(nobel.shape)
print(nobel.columns)
print(nobel.head(10))


ax = sns.countplot(x='Sex', hue='Sex',data=nobel)
ax.set_title('Nobel prize won by Male and Female from 1901 to 2016')