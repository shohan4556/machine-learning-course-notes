**Confusion Matrix or Error Matrix:** A confusion matrix is a summery of prediction result on a classification model.The number of correct and incorrect predictions are summarized with count values and broken down by each class. This is the key to the confusion matrix. The confusion matrix shows the ways in which your classification model is confused when it makes predictions.

> It gives us insight not only into the errors being made by a classifier but more importantly the types of errors that are being made.


!["Confusion Matrix"](/Images/cofusion-matrix-1.png)


**Precision:** To get precision we divide the *total number of correctly* classified positive examples by *the total number of predcited positive* examples.

**Recall** Recall can be defined as the ratio of the *total number of correctly classified positive* examples divide to the *total number of positive examples*. 


**F1Score/F-Measure:** F1 score is the harmonic mean of recall and precision.

!["Confusion Matrix"](/Images/cofusion-matrix-2.png)

> **High recall, low precision:** This means that most of the positive examples are correctly recognized (low FN) but there are a lot of false positives.


> **Low recall, high precision:** This shows that we miss a lot of positive examples (high FN) but those we predict as positive are indeed positive (low FP)

```
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.40, random_state = 42)

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```


**ROC Curve:** The ROC curve is created by plotting the true positive rate aganist the false positive rate for various threshold. ROC curve used to determine the best threshold for a logistic regression. True positive rate is also know as 
Recall.

> Larger area under the ROC curve is better model  