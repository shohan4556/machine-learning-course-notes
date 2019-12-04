**Classification**
----

classifier takes a **unlabeled** data as input and outputs as **labeled** data. 

> we need labeled data as training set. 

we will use **K-Nearest Neighbor** algorithm for classification. 

 **KNN :** It takes a bunch of labelled data and uses them to learn how to label new data. To label a new point, it looks at the labelled points closest to the new point (those are its *nearest neighbors*), and has those neighbors votes. Which unlabeled point has majority vote it will clasify the unlabled point to that labeled point
  (the “k” is the number of neighbors it checks).


<img src="/Images/knn.jpg" alt="drawing" width="500"/>

Depends on *K* the model could be **overfit** or **underfit**.

<img src="/Images/K-NN.png" alt="drawing" width="500"/>


**Overfitting :** Overfitting is the case where the overall cost is really small, but the generalization of the model is unreliable. This is due to the model learning **“too much”** from the training data set.

**Underfitting :** Underfitting is the case where the model has **“not learned enough”** from the training data, resulting in low generalization and unreliable predictions.
 
