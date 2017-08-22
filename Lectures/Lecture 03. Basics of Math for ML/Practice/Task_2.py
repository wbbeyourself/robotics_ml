# -*- coding: utf-8 -*-

import numpy as np
from sklearn.tree import DecisionTreeClassifier

# TITANIC TASK 7
# What factors were the most important for salvation?

def replacer(row):
    if(row['Sex']=='male'):
        row['Sex']=1.0
    else:
        row['Sex']=2.0

    return row




import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

target_column = data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']]

# drop all rows which contain uncertainty or skipped data (cell)
fill_target_column = target_column.dropna().reset_index()

samples = fill_target_column[['Pclass', 'Fare', 'Age', 'Sex']]
target = fill_target_column[['Survived']]

X = samples.apply(replacer, axis=1).values
y = target.values

# print X
# print len(X)

clf = DecisionTreeClassifier(random_state=241)
clf.fit(X, y)

importances = clf.feature_importances_

print list(samples)
print importances
