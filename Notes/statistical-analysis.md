**Exploratory Data Analysis :**
======
The process of organizing, ploting and summerizing in a dataset. 
> **Data Talks**

*Exploratory data analysis can never be the whole story but nothing else can serve as a foundation stone*

EDA may time consuming but you should do it at first then jump into hypothesis.  

**Empirical cumulative distribution function(ECDF)** : ECDF is a step function that jumps up by 1/n at each of the n data points. Its value at any specified value of the measured variable is the fraction of observations of the measured variable that are less than or equal to the specified value.

*xlabel = sort(n)*

*ylabel = (0,1)/n*

> The ECDF essentially allows you to plot a feature of your data in order from least to greatest and see the whole feature as if is distributed across the data set. It gives a overview of data.

**Mean** : Average of data **[(x1+x2+......xn) / n]**

**Outlier** : Data points whose value is much greater or lesser than the most of the rest of the data. Outlier effects significanly on mean not median. 

**Meidan** : The middile point of the data/dataset

**Variance** : Variance means a measurement of the spread of the data. Variance is the *average* of the *squared distance* from the *mean*. To calculate variance, for each data point **xi** we square the distacne from the **mean** then take the average of the all of these values. 

![Variance](/Images/variance.png)

**Standard Deviation :** Standard deviation is the squared root of the **variance**. 

> It used to get an idea about the spread of the data


**Covariance**: A measure how two quantities vary togeather. If **x** and **y** both below their 
respective means then the covariance is positive (positively correlated) otherwise negative.


![Covariance](/Images/covariance.png)

**Pearson Correlation Coefficient :** It measures the strength between variables and relationships. It is dimensionless and range from **-1 (complete anticorrelation) to 1 (complete correlation)**. Value **0** means there are no correlation at all.


![Pearson Correlation](/Images/pearson-correlation.png)


![Pearson Correlation](/Images/pearson-correlation_1.png)



**Binomial Distribution/Probability:** Binomial distribution can be thought of as simply the probability of a SUCCESS or FAILURE outcome in an experiment or survey that is repeated multiple times. for example,
*A coin is tossed 10 times. What is the probability of getting exactly 6 heads?*

> A real world example. *A company drills 9 wild-cat oil exploration wells, each with an estimated probability of success of 0.1. All nine wells fail. What is the probability of that happening?*


```
Let’s do 20,000 trials of the model, and count the number that generate zero positive results.

sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.

answer = 0.38885, or 38%.

```


![Binomial Distribution](/Images/binomial-probability.jpg)

**Poisson Distribution :** Poisson distribution is a statistical distribution that shows how many times an event is likely to occur within a specified period of time. It is used for independent events which occur at a constant rate within a given interval of time. 

> Poisson distribution is used to describe the distribution of **rare** events in a large dataset. 

`numpy.random.poisson(mean number of success, range)`


**Probability Density Function (PDF):** PDF defines a probability distribution for a **continuous** random variable as opposed to a discrete random variable.

