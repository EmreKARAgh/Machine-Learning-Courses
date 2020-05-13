# -*- coding: utf-8 -*-
import preprocessing
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

pp = preprocessing.Preprocess('src/veriler.csv')
pp.dropCols(['ulke'])
pp.dropRows([0,1,2,3,4])
data = pp.getData()
pp.scale([0,1,2])

x_train, x_test, y_train, y_test = pp.trainTestSplitting(['cinsiyet'])

svc = SVC(kernel='linear')
svc.fit(x_train,y_train)

y_pred = svc.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print(cm)

