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
kernel trick converts non-separable data into separable data by **adding more dimensions to it**. It makes SVM more powerful, flexible and accurate. 

**Before Kernel Trick:**
!["SVM"](/Images/SVM_Kernal.png)

**After Kernel Trick:**
!["SVM"](/Images/SVM_Kernel2.png)


The following are some of the types of kernels used by SVM: 

1. Linear Kernel : It can be used as a dot product between any two observations. The formula of linear kernel is as below −

    > K(x,xi)=sum(x∗xi)

    From the above formula, we can see that the product between two vectors say 𝑥 & 𝑥𝑖 is the sum of the multiplication of each pair of input values

2. Polynomial Kernel : It is more generalized form of linear kernel and distinguish curved or nonlinear input space. Following is the formula for polynomial kernel −

    >k(X,Xi)=1+sum(X∗Xi)^d

    Here d is the degree of polynomial, which we need to specify manually in the learning algorithm.

3. Radial Basis Function (RBF) Kernel : RBF kernel, mostly used in SVM classification, maps input space in indefinite dimensional space. Following formula explains it mathematically −

    >K(x,xi)=exp(−gamma∗sum(x−xi^2))   

Here, gamma ranges from 0 to 1. We need to manually specify it in the learning algorithm. A good default value of gamma is 0.1

**Pros & Cons of SVM:**
---

The pros to SVM's:

1. Effective in classifying higher dimensional space
2. Saves space on memory because it only uses the support vectors to create the optimal line.
3. Best classifier when data points are separable

The cons to SVM's:

1. Performs poorly when there is a large data set, the training times are longer.
2. Performs badly when the classes are overlapping, i.e. non-separable data points.





[reference - 1](https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_classification_algorithms_support_vector_machine.htm)

[reference - 2](https://github.com/machinelearningmindset/machine-learning-course/blob/master/docs/source/content/supervised/linear_SVM.rst)