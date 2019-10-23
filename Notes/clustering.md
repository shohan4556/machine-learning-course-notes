**Clustering:**
--
Clustering is the process of grouping a set of data/objects/pattern. The clustered representation of data are used in decision making. **Classification** is one of the most popular decision making paradigms. 

* Similar types of data in same clusters
* Dissimilar types of data in other clusters 
* Clustering can be used in unsupervised learning(unlabeled)
* Classification can be used in supervised learning (labeled data) 

**Difference between clustering and classification :**
>Clustering tries to group a set of objects and find whether there is _some_ relationship between the objects. 
>Classification you have a set of predefined set/group and want to know which group a new object belongs to.

*After clustering the data, we can use classification to automate the process for new data.* 

**Why Clustering is important ?**

Clustering is necessary for decision making situation like classification, prediction, finding similar pattern etc. The number of cluster representatives obtained is smaller than the number of input patterns and so there is data reduction.


**Types of Clustering**

1. Hierarchical clustering 

	a. Agglomerative (bottom up) *most popular* 
	
	b. Divisive (top down) 
	
	Typical complexity : O($n^2$ $log(n))$
	*Become very slow for large dataset*
	
	Output is a dendrogram representing hierarchical relationship among objects/data.
	
	
**Distance measure using Squared Euclidean Distance method.** 

!["Squared Euclidean Distance"](/Images/squared-euclidean.png)
