**What is Linear Regression?** 

>Regression searches for relationships among variables.

For example, you can observe several employees of some company and try to understand how their **salaries** (*response / dependent variable / outputs*) depend on the features, such as **experience**, **level of education**, **role**, **city** *(predictor / independent variable / inputs)* they work in, and so on.


**Why we need Regression ?**
> Regression typically used to check how several variables are related.

**Regression formula :**

!["least square method"](/Images/regression.png)

We will learn to use Linear Regression by using **Least Square Method**

**What is Least Square Method ?**
>The least squares method is a statistical procedure to find the best fit for a set of data points by minimizing the sum of the offsets or residuals of points from the plotted curve. Least squares regression is used to predict the behavior of dependent variables

**Formula for Multiple Linear Regression**

!["Multiple Linear Regression"](/Images/linear-regression.png)

**Formula for Simple Linear Regression**

!["Simple Linear Regression"](/Images/simple-linear-regression.png)


**What is residuals point ?**
> Residuals points is the difference between predicted response and actual response. Regression is about determining the smallest residuals.


!["Residual"](/Images/residual.png)


**K-Fold Cross Validation:** K-Fold CV is a resampling method used to calculate accuracy of a model more confidently.

> By using Cross-Validation, we are able to get more metrics and draw important conclusion both about our model and our data.


!["Residual"](/Images/k-fold-cv.png)

**Regularized Regression:** Regularized regression is the way of preventing model's overfitting or underfitting which may result from simple linear regression.

* **Ridge Regression:** Ridge regression is a technique that is implemented by adding bias to a **linear regression** model to expect a much accurate regression with tested data at a cost of losing accuracy for the training data.

> model evaluation should be based on new data (testing set), not given data (training set)


* **Lasso Regression:** Lasso regression is similar to ridge regression, except it also helps to select most important feature by shrinking the cooefficient of less important features to exactly 0.

```
from sklearn.linear_model import Lasso
lasso = Lasso(alpha=0.4, normalize=True)

lasso.fit(X,y)
lasso_coef = lasso.fit(X, y).coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
```

*[Important Link](https://www.mathsisfun.com/data/least-squares-regression.html)*
