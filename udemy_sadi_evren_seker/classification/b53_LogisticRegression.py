# -*- coding: utf-8 -*-
import preprocessing
from sklearn.linear_model import LogisticRegression

pp = preprocessing.Preprocess('veriler.csv')
pp.dropCols(['ulke'])
pp.dropRows([0,1,2,3,4])
pp.scale([0,1,2])
#pp.print()
x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])

log_r = LogisticRegression(solver='lbfgs',random_state=0)
log_r.fit(x_train, y_train.values.ravel())

y_pred = log_r.predict(x_test)
print(y_pred) 
print(y_test.values.ravel())

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
print(cm)