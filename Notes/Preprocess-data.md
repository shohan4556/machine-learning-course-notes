**preprocessing data**
---

**Missing Value:** Since scikit learn dont accept non-numeric variable we have to convert it to numeric variable. 

```
df_region = pd.get_dummies(df)
df_region = pd.get_dummies(df, drop_first=True)

```

**Imputing:** Replace missing value with educative guess or drop the row of missing value.   


**Normalize Data:** Data should be normalized before train. 

* Standardization : subtract the mean and devide by the variance so that all fratures are centered around 0 and variance 1.

