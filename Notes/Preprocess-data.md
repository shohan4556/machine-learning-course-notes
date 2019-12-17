**preprocessing data**
---

**Missing Value:** Since scikit learn dont accept non-numeric variable we have to convert it to numeric variable. 

```
df_region = pd.get_dummies(df)
df_region = pd.get_dummies(df, drop_first=True)

```

**Imputing:** Replace missing value with educative guess or drop the row of missing value.   


**Normalize Data:** Data should be normalied before training. Normalized data could increase accuracy.

* Standardization : subtract the mean and devide by the variance so that all features are centered around 0 and variance 1.

```
steps = [('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier())]
        
pipeline = Pipeline(steps)
knn_scaled = pipeline.fit(X_train, y_train)
knn_scaled.score(X_test, y_test)
```