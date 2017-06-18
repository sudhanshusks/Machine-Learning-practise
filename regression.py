#import linear model library from scikit learn
from sklearn import linear_model
import pandas as pd
import numpy as np

train=pd.read_csv("~/Desktop/train.csv")
test=pd.read_csv("~/Desktop/test.csv")

y_train=train['target']
del train['target']
x_train=np.array(train)

y_test=test['target']
del test['target']
x_test=test

#create linear regression object
linear=linear_model.LinearRegression()

#train the model and check score

linear.fit(x_train,y_train)
linear.score(x_train,y_train)

#Equation coefficient and intercept
print("coefficient : ",linear.coef_)
print("intercept : ",linear.intercept_)

#predict output
predicted=linear.predict(x_test)
print("predicted output : ",predicted)