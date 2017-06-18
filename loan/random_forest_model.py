from sklearn.model_selection import train_test_split
#import random forest classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
train=pd.read_csv("~/Desktop/train.csv")
test=pd.read_csv("~/Desktop/test.csv")
y=train['target']
del train['target']

x=train
x_train,x_test,y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=1,stratify=y)

#create random forest classifier object
clf=RandomForestClassifier(n_estimators=500, max_depth=6)
#train the RF classifier
clf.fit(x_train,y_train)

#predict the output of random forest on test data
clf.predict(x_test)	

#make prediction and check model's accuracy
prediction=clf.predict(x_test)
acc=accuracy_score(np.array(y_test),prediction)
#new print format where {} is used with .format(number) 
print('The accuracy of Random Forest is {}'.format(acc))

