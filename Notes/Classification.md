**Classification**
----

classifier takes a **unlabeled** data as input and outputs as **labeled** data. 

> we need labeled data as training set. 

we will use **K-Nearest Neighbor** algorithm for classification. 

 **KNN :** It takes a bunch of labelled data and uses them to learn how to label new data. To label a new point, it looks at the labelled points closest to the new point (those are its *nearest neighbors*), and has those neighbors votes. Which unlabeled point has majority vote it will clasify the unlabled point to that labeled point
  (the “k” is the number of neighbors it checks).


  ![KNN](/Images/knn.jpg)