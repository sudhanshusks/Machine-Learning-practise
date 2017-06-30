import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

mapping={'Front':0 , 'Right': 1, 'Left': 2, 'Rear': 3}
train=train.replace({'DetectedCamera':mapping})
test=test.replace({'DetectedCamera':mapping})
train.rename(columns={'SignFacing (Target)': 'Target'}, inplace=True)
mapping = {'Front':0, 'Left':1, 'Rear':2, 'Right':3}
train=train.replace({'Target':mapping})

y_train=train['Target']
test_id=test['Id']
train.drop(['Target', 'Id'], inplace=True, axis=1)
test.drop('Id', inplace=True, axis=1)
clf=RandomForestClassifier(n_estimators=500, max_features=3, min_samples_split=5, oob_score=True)

clf.fit(train,y_train)

pred=clf.predict_proba(test)
columns = ['Front','Left','Rear','Right']
sub = pd.DataFrame(data=pred, columns=columns)
sub['Id'] = test_id
sub = sub[['Id','Front','Left','Rear','Right']]
sub.to_csv("solution.csv", index=False)
