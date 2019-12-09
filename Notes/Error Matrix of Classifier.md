**Confusion Matrix or Error Matrix:** A confusion matrix is a summery of prediction result on a classification model.The number of correct and incorrect predictions are summarized with count values and broken down by each class. This is the key to the confusion matrix. The confusion matrix shows the ways in which your classification model is confused when it makes predictions.

> It gives us insight not only into the errors being made by a classifier but more importantly the types of errors that are being made.


!["Confusion Matrix"](/Images/confusion-matrix-1.png)


**Precision:** To get precision we divide the *total number of correctly* classified positive examples by *the total number of predcited positive* examples.

**Recall** Recall can be defined as the ratio of the *total number of correctly classified positive* examples divide to the *total number of positive examples*. 


**F1Score/F-Measure:** F1 score is the harmonic mean of recall and precision.

!["Confusion Matrix"](/Images/confusion-matrix-2.png)

> **High recall, low precision:** This means that most of the positive examples are correctly recognized (low FN) but there are a lot of false positives.


> **Low recall, high precision:** This shows that we miss a lot of positive examples (high FN) but those we predict as positive are indeed positive (low FP)