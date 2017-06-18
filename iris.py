import numpy as np
import matplotlib as plt
#sklearn has datasets module which contains many toy datas to play with
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
#Load and return iris dataset from web without downloading
dataset=datasets.load_iris()
model=LogisticRegression()

model.fit(dataset.data, dataset.target)

predicted=model.predict(dataset.data)
expected=dataset.target
#classification report returns precision, recall and F1-score of the classification problem
print(metrics.classification_report(expected,predicted))
#confusion matrix has rows as actual/expected values and columns as predicted values
print(metrics.confusion_matrix(expected,predicted))
