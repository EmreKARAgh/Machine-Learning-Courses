# -*- coding: utf-8 -*-
from sklearn.tree import DecisionTreeClassifier
from preprocessing import Preprocess
from sklearn.metrics import confusion_matrix

pp = Preprocess('src/veriler.csv')
pp.dropCols(['ulke'])
data = pp.getData()

x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])
y_train = y_train.values.ravel()

dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
y_pred = dtc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)
