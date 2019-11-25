**Exploratory Data Analysis :**
======
The process of organizing, ploting and summerizing in a dataset. 
> **Data Talks**

*Exploratory data analysis can never be the whole story but nothing else can serve as a foundation stone*

EDA may time consuming but you should do it at first then jump into hypothesis.  

**ECDF** :  *This empirical cumulative distribution function* is a step function that jumps up by 1/n at each of the n data points. Its value at any specified value of the measured variable is the fraction of observations of the measured variable that are less than or equal to the specified value.

*xlabel = sort(n)*

*ylabel = (0,1)/n*

> The ECDF essentially allows you to plot a feature of your data in order from least to greatest and see the whole feature as if is distributed across the data set. It gives a overview of data.

**Mean** : Average of data **[(x1+x2+......xn) / n]**

**Outlier** : Data points whose value is much greater or lesser than the most of the rest of the data. Outlier effects significanly on mean not median. 

**Meidan** : The middile point of the data/dataset

**Variance** : Variance means a measurement of the spread of the data. Variance is the *average* of the *squared distance* from the *mean*. To calculate variance, for each data point **xi** we squre the distacne from the **mean** then take the average of the all of these values. 

![Variance](/Images/variance.png)

**Standard Deviation :** Standard deviation is the squared root of the **variance**. 

> It used to get an idea about the spread of the data

