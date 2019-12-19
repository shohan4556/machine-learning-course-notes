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

plt.figure()
sns.countplot(x='Sex', hue='Sex',data=nobel)
plt.title('Nobel prize won by Male and Female from 1901 to 2016')
plt.savefig('male-vs-female.png')

category = nobel['Category'].value_counts()
#print(category)

plt.figure()
sns.barplot(x=category.index, y=category.values)
plt.title('Nobel Prize Category')
plt.savefig('category.png')

country = nobel['Birth Country'].value_counts().head(10)
plt.figure()
sns.barplot(x=country.index, y=country.values)
plt.title('Top 10 Nobel Prize Winner Country')
plt.xticks(rotation=90)
plt.savefig('country.pdf',  bbox_inches = "tight")

