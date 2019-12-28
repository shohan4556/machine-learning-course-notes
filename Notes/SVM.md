**Support Vector Machine**
---

**Support Vector Machine :** SVM is a binary classifer algorithm to classify data. 
SVM try to find a line or hyperplane to divide a dimensional space which best classifies the data points and also maintain the 
**maximum margin** between the data points. 
> Sometimes data classes will have **outlier**, SVM ignore the outlier and create a best line to separate the two classes. 



!["SVM"](/Images/optimal_hyperplane.png)


**Hyperplane:** Hyperplane divides the space into two or multiple disconnected part, A hyperplane depends on which space it is. for example in 1-dimensional space hyperplane would be a point, in 2-dimensional space would be a line, in 3-dimensional space would be a plane and so on. 

**Support Vector:**  Datapoints that are closest to the hyperplane is called support vectors. Separating line will be defined with the help of these data points.


**Kernel Trick :** SVM can classify **non linearly seprable** data using a trick called **kernel trick** 

**Pros & Cons of SVM:**
---

The pros to SVM's:

1. Effective in classifying higher dimensional space
2. Saves space on memory because it only uses the support vectors to create the optimal line.
3. Best classifier when data points are separable

The cons to SVM's:

1. Performs poorly when there is a large data set, the training times are longer.
2. Performs badly when the classes are overlapping, i.e. non-separable data points.
